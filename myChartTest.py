#######################################################################
#
# An example of creating Excel Column charts with data tables using
# Python and XlsxWriter.

import xlsxwriter
import csv

workbook = xlsxwriter.Workbook('myChart.xlsx')
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': 1})

# Add the worksheet data that the charts will refer to.
headings = ['Date', 'On HIX', 'Off HIX']

worksheet.write_row('A1', headings, bold)
inFile="./inputData.csv"
row=1
col=0

with open(inFile) as ifile:
    csvfile = csv.reader(ifile)
    for line in csvfile:
        col=0
        for item in line:
            try:
                worksheet.write(row,col , int(item))
            except:
                worksheet.write(row,col , item)
            col += 1
        row += 1

#######################################################################
#
# Create a column chart with a data table.
#
chart1 = workbook.add_chart({'type': 'column'})

# Configure the first series.

chart1.add_series({
    'name':       '=Sheet1!$B$1',
    'categories': '=Sheet1!$A$2:$A$7',
    'values':     '=Sheet1!$B$2:$B$7',
})
chart1.add_series({
    'name':       '=Sheet1!$C$1',
    'categories': '=Sheet1!$A$2:$A$7',
    'values':     '=Sheet1!$C$2:$C$7',
})

# Add a chart title and some axis labels.
chart1.set_title({'name': 'Chart with Data Table'})
chart1.set_x_axis({'name': 'Date Totals'})
chart1.set_y_axis({'name': 'Records'})

# Set a default data table on the X-Axis.
chart1.set_table()

# Insert the chart into the worksheet (with an offset).
worksheet.insert_chart('D2', chart1, {'x_offset': 25, 'y_offset': 10})

workbook.close()