import os
import unittest
from csv_reconciler.imports import Imports

class TestImports(unittest.TestCase):

  def create_test_csv(self):
    with open('test.csv', 'w') as f:
      f.write('ID,Name,Date,Amount\n')
      f.write('1,John Doe,2020-01-01,100\n')
      f.write('2,Jane Doe,2020-01-02,200\n')
      f.write('3,John Smith,2020-01-03,300\n')
      f.write('4,Jane Smith,2020-01-04,400\n')
      f.write('5,John Doe,2020-01-05,500\n')

  def remove_test_csv(self):
    os.remove('test.csv')

  @classmethod
  def setUpClass(self):
    self.create_test_csv(self)

  @classmethod
  def tearDownClass(self):
    self.remove_test_csv(self)


  def test_imports(self):
    sampleImport = Imports('source','test.csv', ['amount'])
    self.assertEqual(sampleImport.validate_extension(), 'test.csv')
    
    try :
      sampleImport = Imports('source', 'test.txt', ['amount'])
    except TypeError as e:
      self.assertEqual(str(e), 'File must have one of the following extensions: [\'csv\']')

  def test_get_recordids(self):
    sampleImport = Imports('source', 'test.csv', ['amount'])
    sampleImport.import_file()
    assert sampleImport.get_recordids() == ['1', '2', '3', '4', '5']

  def test_get_record(self):
    sampleImport = Imports('source', 'test.csv', [])
    sampleImport.import_file()
    assert sampleImport.get_record('1') == {'ID': '1', 'Name': 'John Doe', 'Date': '2020-01-01', 'Amount': '100'}

  