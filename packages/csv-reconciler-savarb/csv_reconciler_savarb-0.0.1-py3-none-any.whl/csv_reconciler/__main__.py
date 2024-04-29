import os
import argparse
import webbrowser
from csv_reconciler.reconciler import Reconciler

from tkinter import *
from tkinter import filedialog as fd 

def select_file(filetype):
  filepath = fd.askopenfilename(filetypes = [("CSV files", "*.csv")])
  if filepath == '':
    print('{} file is required'.format(filetype))
    return select_file(filetype)
  else:
    return filepath

def save_to_file(content):
  filename = fd.asksaveasfilename(defaultextension=".html", filetypes = [("HTML files", "*.html")], initialfile='reconciler_report.html', initialdir='.')
  with open(filename, 'w') as f:
    f.write(content)
  return filename

def main():
  # sys.tracebacklimit = 0
  parser = argparse.ArgumentParser()
  parser.add_argument('-s', dest='source', help='Source CSV file , omit the -s flag to select the file using a file dialog')
  parser.add_argument('-t', dest='target', help='Target CSV file, omit the -t flag to select the file using a file dialog')
  parser.add_argument('-i', '--list', nargs='*', dest='ignore', help='Columns to ignore')
  args = parser.parse_args()
  
  source_file = args.source
  target_file = args.target
  
  if source_file is None:
    print('Select Source File')
    source_file = select_file('Source')

  if target_file is None:
    print('Select Target File')
    target_file = select_file('Target')
  
  print('CSV Reconciler will compare the following files:')
  print('Source: {}'.format(source_file))
  print('Target: {}'.format(target_file))
  if args.ignore is not None:
    print('Ignoring columns: {}'.format(args.ignore))

  csvreconciler = Reconciler(args.source, args.target, args.ignore)
  csvreconciler.import_files()
  csvreconciler.compare_headers()
  csvreconciler.compare_details()

  htmlreport = csvreconciler.generate_html_report()

  filename = save_to_file(htmlreport)
  webbrowser.open('file://' + os.path.realpath(filename))

if __name__ == '__main__':
    main()
