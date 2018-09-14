import sqlite3
import xlsxwriter
import csv

workbook = xlsxwriter.Workbook('statsChart.xlsx')
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': 1})

# Add the worksheet data that the charts will refer to.
headings = ['Date', 'On HIX', 'Off HIX']
worksheet.set_column(0, 0, 14)
formatA = workbook.add_format()
formatA.set_align('center')
formatA.set_bold()
worksheet.write_row('A1', headings, formatA)
format = workbook.add_format()
format.set_align('right')
format.set_bold()
worksheet.write(0,1,"OnHIX",format)
worksheet.write(0,2,"OffHIX",format)
db = sqlite3.connect('./recordsProcessed.db')
# Get a cursor object
cursor = db.cursor()

cursor.execute("""select * from (select * from stats order by date DESC limit 7) order by date ASC""")
#cursor.execute("""select * from stats """)
row=1
col=0
for results in cursor.fetchall():
#    print("  {0} -- {1} --- {2} ".format(results[0], results[1], results[2]))
        col=0
        for item in results:
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
    'categories': '=Sheet1!$A$2:$A$8',
    'values':     '=Sheet1!$B$2:$B$8',
})
chart1.add_series({
    'name':       '=Sheet1!$C$1',
    'categories': '=Sheet1!$A$2:$A$8',
    'values':     '=Sheet1!$C$2:$C$8',
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