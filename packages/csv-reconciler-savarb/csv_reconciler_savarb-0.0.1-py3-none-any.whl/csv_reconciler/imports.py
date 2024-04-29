import os
import csv

class Imports():
  def __init__(self, type, fname, ignore):
    self.type = type
    self.fname = fname
    self.ignore = ignore
    self.extensions = ['csv']
    self.headers = []
    self.details = []
    
  def import_file(self):
    self.validate_extension()
    
    if os.path.exists(self.fname) == False:
      raise FileNotFoundError('{} file \'{}\' not found'.format(self.type, self.fname))

    with open(self.fname, 'r') as csvfile:
      csvreader = csv.reader(csvfile, delimiter=',')
      headers = next(csvreader)
      
      for header in headers:
        if header.strip().lower() not in self.ignore:
          self.headers.append(header.strip())
        else:
          self.headers.append('IGNORED')

      for row in csvreader:
        jsonrow = {}
        for id, col in enumerate(row):
          if self.headers[id].lower() not in self.ignore:
            jsonrow[self.headers[id]] = col.strip()
        self.details.append(jsonrow)    

  def validate_extension(self):
    ext = os.path.splitext(self.fname)[1][1:]
    if ext not in self.extensions:
      raise TypeError('{} file must have one of the following extensions: {}'.format(self.type, self.extensions))
    return self.fname
    
  def get_recordids(self):
    recordids = []
    for row in self.details:
      recordids.append(row['ID'])
    return sorted(recordids)
  
  def get_record(self, recordid):
    for record in self.details:
      if record['ID'] == recordid:
        return record