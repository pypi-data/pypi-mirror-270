import os
import unittest

from csv_reconciler.reconciler import Reconciler

class TestReconciler(unittest.TestCase):
    
  def create_source_and_target_csv(self):
    with open('test-source.csv', 'w') as f:
      f.write('ID,Name,Date,Amount\n')
      f.write('1,John Doe,2020-01-01,100\n')
      f.write('2,Jane Doe,2020-01-02,200\n')
      f.write('3,John Smith,2020-01-03,300\n')
      f.write('4,Jane Smith,2020-01-04,400\n')
      f.write('5,John Doe,2020-01-05,500\n')
    with open('test-target.csv', 'w') as f:
      f.write('ID,Name,Date,Amount\n')
      f.write('1,John Doe,2020-01-01,100\n')
      f.write('2,Jane Doe,2020-01-02,200\n')
      f.write('3,John Smith,2020-01-03,300\n')
      f.write('4,Jane Smith,2020-01-04,400\n')
      f.write('5,John Doe,2020-01-05,500\n')

  def remove_source_and_target_csv(self):
    os.remove('test-source.csv')
    os.remove('test-target.csv')
  
  @classmethod
  def setUpClass(self):
    self.create_source_and_target_csv(self)

  @classmethod
  def tearDownClass(self):
    self.remove_source_and_target_csv(self)
          
  def test_compare_headers_and_details_and_generate_report(self):
    csvreconciler = Reconciler('test-source.csv', 'test-target.csv', [])
    csvreconciler.import_files()
    csvreconciler.compare_headers()
    csvreconciler.compare_details()
    csvreconciler.generate_html_report()
    