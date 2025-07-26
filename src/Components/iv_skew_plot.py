# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 15:51:47 2023

@author: EMCLABUSER
"""

# Import modules
'''from nptdms import TdmsFil

# Save the PDF file
pdf.output('output.pdf', 'F')
'''


from nptdms import TdmsFile
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm
import pandas as pd
import matplotlib.pyplot as plt
from reportlab.pdfgen import canvas
from reportlab.platypus import Image
from matplotlib.backends.backend_pdf import PdfPages
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfbase.ttfonts import TTFont
from  datetime import date
import datetime
import glob
import os


import sys
sys.argv = ['report generation','Alice','123','aliice@mail.com','DUT_val','standard_val']

if len(sys.argv) < 6:
    print("Usage: python script.py <name> <aid> <mail> <DUT> <standard>")
    sys.exit(1)
name = sys.argv[1]
aid= sys.argv[2]
mail = sys.argv[3]
DUT = sys.argv[4]
standard = sys.argv[5]

pdf_file = canvas.Canvas("output.pdf")

pdf_file.setFillColor(colors.black)
dt = date.today().strftime('%d-%b-%Y')
pdf_file.drawString(520,820,dt)
dt_1=datetime.datetime.now().strftime("%Hhrs:%Mmins ") 
pdf_file.drawString(520,805,dt_1)
pdf_file.drawCentredString(297, 8, "Page 1 of 4")
pdf_file.drawCentredString(70, 810, "Location: Bangalore,India")
  
pdf_file.setFont("Times-Roman", 20)
pdf_file.setFillColor(colors.blue)
pdf_file.drawString(100, 600, "Operator Detail")

pdf_file.setFont("Times-Roman", 15)
pdf_file.setFillColor(colors.black)
pdf_file.drawString(100, 570, f"Name: {name}")
pdf_file.drawString(100, 550, f"Aid/Xid: {aid}")
pdf_file.drawString(100, 530, f"Mail-ID: {mail}")
pdf_file.drawString(100, 510, f"DUT Name: {DUT}")
pdf_file.drawString(100, 490, f"Standard: {standard}")



pdf_file.setFont("Times-Roman", 12)
pdf_file.setFillColor(colors.red)
pdf_file.drawCentredString(500,23, "TI Confidential-NDA Restrictions")
pdf_file.drawImage(r"C:\Users\sweet\Downloads\NITA.png",372,801)

pdf_file.setStrokeColorRGB(0,0,1) # red colour of line
pdf_file.setLineWidth(2) #width of the line 
pdf_file.line(0,798,600,798) # draw line

pdf_file.setPageSize((595, 842))
pdf_file.setFont("Times-Roman", 36)
pdf_file.setFillColor(colors.red)
pdf_file.drawCentredString(280, 700, "IC Level Emission IEC-61967-8")

pdf_file.setStrokeColorRGB(0,0,0) # red colour of line
pdf_file.setLineWidth(2) #width of the line 
pdf_file.line(57,692,510,692) # draw line


# Get the list of files in the directory
list_of_files = glob.glob(r'C:\Users\EMCLABUSER\Desktop\tdmsfile\*.tdms')

# Create a list of tuples with file name and modification time
files_modified_list = [(f, os.path.getmtime(f)) for f in list_of_files]

# Sort the list by the second element (modification time)
sorted_files_modified_list = sorted(files_modified_list, key=lambda x: x[1])

# Get the last 5 elements of the sorted list
top_4_latest_files = [f[0] for f in sorted_files_modified_list[-5:]]


pdf_file.showPage()
pdf_file.setFillColor(colors.black)
dt = date.today().strftime('%d-%b-%Y')
pdf_file.drawString(520,820,dt)
dt_1=datetime.datetime.now().strftime("%Hhrs:%Mmins ") 
pdf_file.drawString(520,805,dt_1)
pdf_file.drawCentredString(297, 8, "Page 2 of 4")
pdf_file.drawCentredString(70, 810, "Location: Bangalore,India")
pdf_file.setFont("Times-Roman", 12)
pdf_file.setFillColor(colors.red)
pdf_file.drawImage(r"C:\Users\sweet\Downloads\NITA.png",372,801)

pdf_file.setStrokeColorRGB(0,0,1) # red colour of line
pdf_file.setLineWidth(2) #width of the line 
pdf_file.line(0,798,600,798) # draw line

pdf_file.setFont("Times-Roman", 16)
pdf_file.setFillColor(colors.black)
pdf_file.drawString(100, 600, "Test Location and Equipment Used:")
pdf_file.setFont("Times-Roman", 12)
pdf_file.setFillColor(colors.black)
pdf_file.drawString(100, 580, "This test was carried out in the Semi-Anechoic Chamber")


pdf_file.setFont("Times-Roman", 14)
pdf_file.setFillColor(colors.blue)
pdf_file.drawString(100, 540, "Description")

pdf_file.setFont("Times-Roman", 14)
pdf_file.setFillColor(colors.blue)
pdf_file.drawString(400, 540, "Model#")

pdf_file.setFont("Times-Roman", 12)
pdf_file.setFillColor(colors.black)
pdf_file.drawString(100, 520, "IC Stripline TEM Cell")

pdf_file.setFont("Times-Roman", 12)
pdf_file.setFillColor(colors.black)
pdf_file.drawString(400, 520, "EM601-6A")

pdf_file.setFont("Times-Roman", 12)
pdf_file.setFillColor(colors.black)
pdf_file.drawString(100, 500, "ESA-E Series Spectrum Analyzer")

pdf_file.setFont("Times-Roman", 12)
pdf_file.setFillColor(colors.black)
pdf_file.drawString(400, 500, "E4402B")


pdf_file.setFont("Times-Roman", 12)
pdf_file.setFillColor(colors.black)
pdf_file.drawString(100, 480, "RF Cable")

pdf_file.setFont("Times-Roman", 12)
pdf_file.setFillColor(colors.black)
pdf_file.drawString(400, 480, "MWX221")

pdf_file.setFont("Times-Roman", 12)
pdf_file.setFillColor(colors.black)
pdf_file.drawString(100, 460, "50 Ohm Terminator")

pdf_file.setFont("Times-Roman", 12)
pdf_file.setFillColor(colors.black)
pdf_file.drawString(400, 460, "RFT50-NM")

pdf_file.drawImage(r"C:\Users\EMCLABUSER\Desktop\IMG20231127172128.jpg",100,150,width=400, height=250)

pdf_file.showPage()
pdf_file.setFillColor(colors.black)
dt = date.today().strftime('%d-%b-%Y')
pdf_file.drawString(520,820,dt)
dt_1=datetime.datetime.now().strftime("%Hhrs:%Mmins ") 
pdf_file.drawString(520,805,dt_1)
pdf_file.drawCentredString(297, 8, "Page 3 of 4")
pdf_file.drawCentredString(70, 810, "Location: Bangalore,India")
pdf_file.setFont("Times-Roman", 12)
pdf_file.setFillColor(colors.red)
pdf_file.drawCentredString(500,23, "TI Confidential-NDA Restrictions")
pdf_file.drawImage(r"C:\Users\EMCLABUSER\Desktop\ti_logo.png",372,801)

pdf_file.setStrokeColorRGB(0,0,1) # red colour of line
pdf_file.setLineWidth(2) #width of the line 
pdf_file.line(0,798,600,798) # draw line

pdf_file.setFont("Times-Roman", 14)
pdf_file.setFillColor(colors.black)
pdf_file.drawString(130, 770, "Ambient Noise Measurement:")
pdf_file.setFont("Times-Roman", 12)
pdf_file.drawString(130, 755, "DUT: Not Connected")
pdf_file.drawString(130, 740, "Start Frequency: 2.5 GHz")
pdf_file.drawString(130, 725, "Stop Frequency: 3 GHz")
pdf_file.drawString(130, 710, "Resolution Bandwidth: 9 KHz - 3 GHz")
pdf_file.drawString(130, 695, "Mode: Ambient (DUT Powered-OFF) ")


tdms_file_1 = TdmsFile(str(top_4_latest_files[0]))
df_1 = tdms_file_1.as_dataframe()
# Plot the dataframe using matplotlib
plt.figure()
print(df_1.columns)
df_1.plot(x='/Ambient Noise Data/Frequency',y='Ambient Noise Data/Amplitude',logx=True)

plt.title("Ambient Noise data",color="orange",fontsize=16)
plt.xlabel("Frequency (logHz)",color="green")
plt.ylabel("Amplitude (dbµvolt)",color="green")
plt.axhline(y=54, color="red", linestyle="--", label="Limit Class I")
plt.axhline(y=42, color="green", linestyle="--", label="Limit Class II")
plt.axhline(y=30, color="black", linestyle="--", label="Limit Class III")
plt.legend()
# Save the plot as a PNG image
plt.savefig("plot1.png") 
pdf_file.drawImage("plot1.png", 80, 420, width=400, height=260)

tdms_file_3 = TdmsFile(str(top_4_latest_files[2]))
df_3 = tdms_file_3.as_dataframe()
#print(df_2)
plt.figure()
df_3.plot(x="/'Limit Class I'/'Frequency'",y="/'Limit Class I'/'Amplitude'",logx=True)
plt.title("Limit Class I",color="orange",fontsize=16)
plt.xlabel("Frequency (logHz)",color="green")
plt.ylabel("Amplitude (dbµvolt)",color="green")

# Save the plot as a PNG image
plt.savefig("plot2.png")
pdf_file.drawImage("plot2.png", 150, 290, width=270, height=120)
  
tdms_file_4 = TdmsFile(str(top_4_latest_files[3]))
df_4 = tdms_file_4.as_dataframe()
plt.figure()
df_4.plot(x="/'Limit Class II'/'Frequency'",y="/'Limit Class II'/'Amplitude'",logx=True)
plt.title("Limit Class II",color="orange",fontsize=16)
plt.xlabel("Frequency (logHz)",color="green")
plt.ylabel("Amplitude (dbµvolt)",color="green")

# Save the plot as a PNG image
plt.savefig("plot3.png")
pdf_file.drawImage("plot3.png", 150, 170, width=270, height=120)

tdms_file_5 = TdmsFile(str(top_4_latest_files[4]))
df_5 = tdms_file_5.as_dataframe()
plt.figure()
df_5.plot(x="/'Limit Class III'/'Frequency'",y="/'Limit Class III'/'Amplitude'",logx=True)
plt.title("Limit Class III",color="orange",fontsize=16)
plt.xlabel("Frequency (logHz)",color="green")
plt.ylabel("Amplitude (dbµvolt)",color="green")


# Save the plot as a PNG image
plt.savefig("plot4.png")
pdf_file.drawImage("plot4.png", 150, 50, width=270, height=120)

pdf_file.showPage()
pdf_file.setFillColor(colors.black)
dt = date.today().strftime('%d-%b-%Y')
pdf_file.drawString(520,820,dt)
dt_1=datetime.datetime.now().strftime("%Hhrs:%Mmins ") 
pdf_file.drawString(520,805,dt_1)
pdf_file.drawCentredString(297, 8, "Page 4 of 4")
pdf_file.drawCentredString(70, 810, "Location: Bangalore,India")
pdf_file.setFont("Times-Roman", 12)
pdf_file.setFillColor(colors.red)
pdf_file.drawCentredString(500,23, "TI Confidential-NDA Restrictions")
pdf_file.drawImage(r"C:\Users\EMCLABUSER\Desktop\ti_logo.png",372,801)

pdf_file.setStrokeColorRGB(0,0,1) # red colour of line
pdf_file.setLineWidth(2) #width of the line 
pdf_file.line(0,798,600,798) # draw line

pdf_file.setFont("Times-Roman", 14)
pdf_file.setFillColor(colors.black)
pdf_file.drawString(130, 770, "DUT Emission Measurement:")
pdf_file.setFont("Times-Roman", 12)
pdf_file.drawString(130, 755, "DUT: Samsung LM301B")
pdf_file.drawString(130, 740, "Start Frequency: 2.5 GHz")
pdf_file.drawString(130, 725, "Stop Frequency: 3 GHz")
pdf_file.drawString(130, 710, "Resolution Bandwidth: 9 KHz - 3 GHz")
pdf_file.drawString(130, 695, "Mode: Run mode (DUT Powered-ON) ")



tdms_file_2 = TdmsFile(str(top_4_latest_files[1]))
df_2 = tdms_file_2.as_dataframe()

# Plot the dataframe using matplotlib
plt.figure()
df_2.plot(x="/'IC level DUT Emission'/'Frequency'",y="/'IC level DUT Emission'/'Amplitude'",logx=True)
plt.title("DUT Emission data",color="orange",fontsize=16)
plt.xlabel("Frequency (logHz)",color="green")
plt.ylabel("Amplitude (dbµvolt)",color="green")
plt.axhline(y=54, color="red", linestyle="--", label="Limit Class I")
plt.axhline(y=42, color="green", linestyle="--", label="Limit Class II")
plt.axhline(y=30, color="black", linestyle="--", label="Limit Class III")
plt.legend()

# Save the plot as a PNG image
plt.savefig("plot5.png")

# Draw the image on the PDF document
pdf_file.drawImage("plot5.png", 80, 420, width=400, height=260)

tdms_file_3 = TdmsFile(str(top_4_latest_files[2]))
df_3 = tdms_file_3.as_dataframe()
#print(df_2)
plt.figure()
df_3.plot(x="/'Limit Class I'/'Frequency'",y="/'Limit Class I'/'Amplitude'",logx=True)
plt.title("Limit Class I",color="orange",fontsize=16)
plt.xlabel("Frequency (logHz)",color="green")
plt.ylabel("Amplitude (dbµvolt)",color="green")

# Save the plot as a PNG image
plt.savefig("plot2.png")
pdf_file.drawImage("plot2.png", 150, 290, width=270, height=120)
  
tdms_file_4 = TdmsFile(str(top_4_latest_files[3]))
df_4 = tdms_file_4.as_dataframe()
plt.figure()
df_4.plot(x="/'Limit Class II'/'Frequency'",y="/'Limit Class II'/'Amplitude'",logx=True)
plt.title("Limit Class II",color="orange",fontsize=16)
plt.xlabel("Frequency (logHz)",color="green")
plt.ylabel("Amplitude (dbµvolt)",color="green")

# Save the plot as a PNG image
plt.savefig("plot3.png")
pdf_file.drawImage("plot3.png", 150, 170, width=270, height=120)

tdms_file_5 = TdmsFile(str(top_4_latest_files[4]))
df_5 = tdms_file_5.as_dataframe()
plt.figure()
df_5.plot(x="/'Limit Class III'/'Frequency'",y="/'Limit Class III'/'Amplitude'",logx=True)
plt.title("Limit Class III",color="orange",fontsize=16)
plt.xlabel("Frequency (logHz)",color="green")
plt.ylabel("Amplitude (dbµvolt)",color="green")

# Save the plot as a PNG image
plt.savefig("plot4.png")
pdf_file.drawImage("plot4.png", 150, 50, width=270, height=120)



pdf_file.save()
