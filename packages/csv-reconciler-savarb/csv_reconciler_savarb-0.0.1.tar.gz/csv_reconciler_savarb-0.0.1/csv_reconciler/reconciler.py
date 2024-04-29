from datetime import datetime
from rapidfuzz import fuzz
from jinja2 import Template
from csv_reconciler.imports import Imports
from csv_reconciler.report import Report, Details

class Reconciler():
  def __init__(self, source, target, ignore):
    for id, value  in enumerate(ignore):
      ignore[id] = value.lower()
    self.ignore = ignore

    if "id" in self.ignore:
      raise ValueError('ID column cannot be ignored')

    self.source = Imports('Source', source, self.ignore)
    self.target = Imports('Target', target, self.ignore)
    
    self.source_recordids, self.target_recordids = [], []
    self.matched_recordids, self.duplicate_recordids = [], []

    self.report = Report(self.source.fname, self.target.fname)

    self.report.summary.source_file_rows = len(self.source.details)
    self.report.summary.target_file_rows = len(self.target.details)
    self.report.summary.missing_in_target = 0
    self.report.summary.duplicates_in_target = 0
    self.report.summary.missing_in_source = 0
    self.report.summary.duplicates_in_source = 0
    self.report.summary.field_discrepancies = 0
    self.report.summary.successful_matches = 0

  def import_files(self):
    errors = []
    try:
      self.source.import_file()
    except Exception as e1:
      errors.append(e1)
    
    try:
      self.target.import_file()
    except Exception as e2:
      errors.append(e2)

    if len(errors) > 0:
      raise ExceptionGroup("Reconciler Errors",errors)

  def compare_headers(self):
    #check if headers match
    if self.source.headers != self.target.headers:
      raise ValueError('Headers do not match: {} vs {}'.format(self.source.headers, self.target.headers))
    
    #check if headers contain ID, 
    if "ID" not in self.source.headers or "ID" not in self.target.headers:
      raise ValueError('ID column is required for matching in both \'{}\' and \'{}\' files'.format(self.source.fname, self.target.fname))

  def compare_details(self):
    #identify the recordids in source and target
    self.source_recordids = self.source.get_recordids()
    self.target_recordids = self.target.get_recordids()

    #check for records present in source but missing or duplicated in target
    self.identify_missing_in_target()

    #check for records present in target but missing or duplicated in source 
    self.identify_missing_in_source()

    #remove duplicates recordids from the matched recordids in previous steps
    self.remove_duplicates()

    #identify discrepancies in the matched recordids
    self.identify_discrepancies()

  def remove_duplicates(self):
    for recordid in self.duplicate_recordids:
      self.matched_recordids.remove(recordid)

  def identify_missing_in_target(self):
    for recordid in sorted(list(set(self.source_recordids))):
      occurence = self.target_recordids.count(recordid)
      if occurence == 0:
        self.report.details.append(Details('Missing in Target', recordid, '', '', '', occurence))
        self.report.summary.missing_in_target += 1
      elif occurence > 1:
        self.report.details.append(Details('Duplicates in Target', recordid, '', '', '', occurence))
        self.report.summary.duplicates_in_target += occurence
        self.duplicate_recordids.append(recordid)
      else:
        self.matched_recordids.append(recordid)  
    self.matched_recordids = sorted(list(set(self.matched_recordids)))
    self.duplicate_recordids = sorted(list(set(self.duplicate_recordids)))

  def identify_missing_in_source(self):
    for recordid in sorted(list(set(self.target_recordids))):
      occurence = self.source_recordids.count(recordid)
      if occurence == 0:
        self.report.details.append(Details('Missing in Source', recordid, '', '', '', occurence))
        self.report.summary.missing_in_source += 1
      elif occurence > 1:
        self.report.details.append(Details('Duplicates in Source', recordid, '', '', '', occurence))
        self.report.summary.duplicates_in_source += occurence
        self.duplicate_recordids.append(recordid)
      else:
        self.matched_recordids.append(recordid)
    self.matched_recordids = sorted(list(set(self.matched_recordids)))
    self.duplicate_recordids = sorted(list(set(self.duplicate_recordids)))

  def identify_discrepancies(self):
    for recordid in self.matched_recordids:
      source_record = self.source.get_record(recordid)
      target_record = self.target.get_record(recordid)
      
      no_discrepancy = True
      for header in self.source.headers:
        if header.lower() == 'id':
          continue
        if header.lower() == 'name':
          if source_record[header].lower() != target_record[header].lower():
            if fuzz.token_sort_ratio(source_record[header].lower(), target_record[header].lower()) < 90:
              self.report.details.append(Details('Field Discrepancy', recordid, header, source_record[header], target_record[header], '0'))
              self.report.summary.field_discrepancies += 1
              no_discrepancy = False
        if header.lower() == 'amount':
          if source_record[header] != target_record[header]:
            self.report.details.append(Details('Field Discrepancy', recordid, header, source_record[header], target_record[header], '0'))
            self.report.summary.field_discrepancies += 1
            no_discrepancy = False
        if header.lower() == 'date':
          if self.check_and_transform_date_format(source_record[header]) != self.check_and_transform_date_format(target_record[header]):
            self.report.details.append(Details('Field Discrepancy', recordid, header, source_record[header], target_record[header], '0'))
            self.report.summary.field_discrepancies += 1
            no_discrepancy = False

      if no_discrepancy:
        self.report.summary.successful_matches += 1

  # check for multiple date formats and transform to %Y-%m-%d for comparisons
  def check_and_transform_date_format(self, date):
    format_matches = ['%Y-%m-%d', '%m-%d-%Y', '%d-%m-%Y', '%Y-%d-%m', '%m-%d-%y', '%d-%m-%y', '%y-%d-%m', '%m/%d/%Y', '%d/%m/%Y', '%Y/%d/%m', '%m/%d/%y', '%d/%m/%y', '%y/%d/%m']
    formated_date = ""
  
    for format in format_matches:
      try:
        formated_date = datetime.strptime(date, format).strftime('%Y-%m-%d')
        break
      except ValueError:
        continue
    return formated_date

  def generate_html_report(self):
    template_string = self.report.html_template()
    template = Template(template_string)
    return template.render(report=self.report)