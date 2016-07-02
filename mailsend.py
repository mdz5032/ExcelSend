import smtplib, ssl
import openpyxl
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

#Load thk Workbookd in the script 
wb = openpyxl.load_workbook('Work.xlsx')

sheet = wb.active

#Set cell Reference for the chatr
values = openpyxl.chart.Reference(sheet, min_col=1, min_row=2, max_col=2, max_row =7)
sports = openpyxl.chart.Reference(sheet, min_col=1, min_row=2, max_col=2, max_row =7)

#Create Chart and edit chart things
chart = openpyxl.chart.BarChart()
chart.y_axis.title = "Sales"
chart.x_axis.title = "Produce"
chart.height = 10
chart.width = 20

#add the values to the chart 
chart.add_data(values)
chart.set_categories(sports)

#add chart to workbook and save as a new file
sheet.add_chart(chart)
wb.save('UpdatedWork.xlsx')


# Set addresses 
fromaddr = 'bdz5032@gmail.com'
sendto = 'bdz5032@gmail.com'


#prepare Message
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = sendto
msg['Subject'] = 'Analysis of Todays Farmers Market'

body = "Here is a bar chart of of the sales today"


msg.attach(MIMEText(body, 'plain'))

filename = 'UpdatedWork.xlsx'
attachment = open('UpdatedWork.xlsx', 'rb')

part = MIMEBase('application', "octet-stream")
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename= %s' % filename)


#add attachment
msg.attach(part)

#open up the http and log into email
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('bdz5032@gmail.com', 'Dogdog11')

#send email and close the http
text = msg.as_string()
smtpObj.sendmail(fromaddr, sendto , text)
smtpObj.quit()
