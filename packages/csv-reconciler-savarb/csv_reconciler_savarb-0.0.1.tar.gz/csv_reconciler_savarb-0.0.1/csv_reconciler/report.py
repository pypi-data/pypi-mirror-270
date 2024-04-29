from datetime import datetime

class Details():
  def __init__(self, type, recordid, field, source_value, target_value, duplicates):
    self.type = type
    self.recordid = recordid
    self.field = field
    self.source_value = source_value
    self.target_value = target_value
    self.duplicate_count = duplicates

class Summary():
  def __init__(self):
    self.source_file_rows = 0
    self.target_file_rows = 0
    self.missing_in_target = 0
    self.duplicates_in_target = 0
    self.missing_in_source = 0
    self.duplicates_in_source = 0
    self.field_discrepancies = 0
    self.successful_matches = 0


class Report():
  def __init__(self, source, target):
    self.source_file = source
    self.target_file = target
    self.report_date = datetime.now().strftime('%Y-%m-%d')
    self.report_time = datetime.now().strftime('%H:%M:%S')
    self.summary = Summary()
    self.details = []

  def html_template(self):
    return """
  <!DOCTYPE html>
  <html lang="en">

    <head>
      <meta charset="utf-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1" />
      <meta name="theme-color" content="#000000" />
      <title>CSV Reconciler - Report</title>
    </head>

    <style >
      .text-center{text-align: center};
      td{padding: 5px};
    </style>

    <body>
      <div>
        <h1>CSV Reconciler</h1>
        Report Date: {{ report.report_date }} {{ report.report_time }} <br/>
        
        <table border=1>
          <tr>
            <th>Type</th>
            <th>Name</th>
            <th>Records </th>
          </tr>
          <tr>
            <td> Source File </td>
            <td>{{report.source_file}}</td>
            <td class='text-center'>{{ report.summary.source_file_rows }}</td>
          </tr>
          <tr>
            <td>Target File:</td>
            <td>{{ report.target_file }}</td>
            <td class='text-center'> {{ report.summary.target_file_rows }}</td>
          </tr>
        </table>
      </div>

      <h2>Summary</h2>
      <table border=1>
        <tr>
          <th>Type</td>
          <th>Records</td>
        </tr>
        
        <tr>
          <td>Missing in Target:</td>
          <td class='text-center'>{{ report.summary.missing_in_target }}</td>
        </tr>
        <tr>
          <td>Missing in Source:</td>
          <td class='text-center'>{{ report.summary.missing_in_source }}</td>
        </tr>

        <tr>
          <td>Duplicates in Target:</td>
          <td class='text-center'>{{ report.summary.duplicates_in_target }}</td>
        </tr>
        <tr>
          <td>Duplicates in Source:</td>
          <td class='text-center'>{{ report.summary.duplicates_in_source }}</td>
        </tr>

        <tr>
          <td>Field Discrepancies:</td>
          <td class='text-center'>{{ report.summary.field_discrepancies }}</td>
        </tr>

        <tr>
          <td>Successful Matches:</td>
          <td class='text-center'>{{ report.summary.successful_matches }}</td>
        </tr>
      </table>


      <h2>Details</h2>
      <table border=1>
        <tr>
          <th>Number</th>
          <th>Type</th>
          <th>Record Identifier</th>
          <th>Field</th>
          <th>Source Value</th>
          <th>Target Value</th>
          <th>Duplicate Count</th>
        </tr>
        {% for row in report.details %}
          <tr>
            <td class='text-center'>{{ loop.index }}</td>
            <td>{{ row.type }}</td>
            <td class='text-center'>{{ row.recordid }}</td>
            <td>{{ row.field }}</td>
            <td>{{ row.source_value }}</td>
            <td>{{ row.target_value }}</td>
            <td class='text-center'>{{ row.duplicate_count }}</td>
          </tr>
        {% endfor %}
        
      </table>

    </body>
  </html>
  """