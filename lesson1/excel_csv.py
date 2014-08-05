# -*- coding: utf-8 -*-
# Find the time and value of max load for each of the regions
# COAST, EAST, FAR_WEST, NORTH, NORTH_C, SOUTHERN, SOUTH_C, WEST
# and write the result out in a csv file, using pipe character | as the delimiter.
# An example output can be seen in the "example.csv" file.
import xlrd
import os
import csv
from zipfile import ZipFile
datafile = "2013_ERCOT_Hourly_Load_Data.xls"
outfile = "2013_Max_Loads.csv"


def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    data = []
    # YOUR CODE HERE
    # Remember that you can use xlrd.xldate_as_tuple(sometime, 0) to convert
    # Excel date to Python tuple of (year, month, day, hour, minute, second)
    regions = ["COAST", "EAST", "FAR_WEST", "NORTH", "NORTH_C", "SOUTHERN", "SOUTH_C", "WEST"]
    for i, region in enumerate(regions):
        col = sheet.col_values(i + 1)
        del col[0]
        maxvalue = max(col)
        maxvalue_row = col.index(maxvalue) + 1	    		
        maxvalue_exceltime = sheet.cell_value(maxvalue_row, 0)
        maxvalue_tupletime = xlrd.xldate_as_tuple(maxvalue_exceltime, 0)		
        line = [region, maxvalue_tupletime[0], maxvalue_tupletime[1], maxvalue_tupletime[2], maxvalue_tupletime[3], maxvalue]
        data.append(line) 

    return data

def save_file(data, filename):
    # YOUR CODE HERE
    with open("2013_Max_Loads.csv", 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter='|')
        writer.writerow(["Station", "Year", "Month", "Day", "Hour", "Max Load"])
        for row in data:
            writer.writerow(row)

def test():
    open_zip(datafile)
    data = parse_file(datafile)
    save_file(data, outfile)

    ans = {'FAR_WEST': {'Max Load': "2281.2722140000024", 'Year': "2013", "Month": "6", "Day": "26", "Hour": "17"}}
    
    fields = ["Year", "Month", "Day", "Hour", "Max Load"]
    with open(outfile) as of:
        csvfile = csv.DictReader(of, delimiter="|")
        for line in csvfile:
            s = line["Station"]
            if s == 'FAR_WEST':
                for field in fields:
                    
                    assert ans[s][field] == line[field]

        
test()