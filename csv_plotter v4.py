from turtle import color, width
import matplotlib.pyplot as plt
import csv
from matplotlib.patches import Ellipse, Rectangle
import numpy as np
def readCSV (path):
  data = []
  header = [] # removes first line of file
  filename = path
  with open(filename) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)  # removes first line of file
    for datapoint in csvreader:
        values = [float(value) for value in datapoint]
        data.append(values)
  return data

def magnitudeBode(dataList, dataLabel,col, col2=-1):
  #Figure size (x,y) in inches. Move Legend if changed drasticly to avoid clipping
  fig = plt.figure(1, figsize=(14.5, 6.5))
  
  #number of rows/cols of subplots 
  ax = fig.add_subplot(1, 1, 1)
  #plt.minorticks_on()
  #max num ticks in axis
  max_yticks = 15
  max_xticks = 10 #irrelevant due to log scale
  yloc = plt.MaxNLocator(max_yticks)
  xloc = plt.MaxNLocator(max_xticks)
  ax.yaxis.set_major_locator(yloc)
  ax.xaxis.set_major_locator(xloc)
  ax.tick_params(which='major', length=8)
  ax.tick_params(which='minor', length=6)
  ax.tick_params(which='both', width=1)
  #ax.yaxis.set_minor_locator(AutoMinorLocator())
  #Use log scale  
  #ax.set_xscale('log')
  # ax.set_yscale('log')

  #plt.title('Bode diagram demping')
  plt.grid(True)
  
  #ax.xaxis.minorTicks()
  ax.xaxis.grid(b=True, which='minor', linestyle=(0, (1,3)))


  #plot data
  for i in range (0,len(dataList)):
    time = [p[0] for p in dataList[i]]
    if col2!=-1:
      trace1 = [p[col2] for p in dataList[i]]
      plt.plot(time, trace1, "-")
    
    trace1 = [p[col] for p in dataList[i]]
    plt.plot(time, trace1, "-", alpha=0.8,label = dataLabel[i])
    

  #labels  
  plt.xlabel("Frekvens [Hz]")
  plt.ylabel("Demping [dB]")
  
  
  
  #Final touch
  # ellipse = Ellipse(xy=(580, -24), width=900, height=10, 
  #                       edgecolor='r', fc='None', lw=2)
  # ax.add_patch(ellipse)
  
  #ypoints = [(0,580),(-44,580)]

  #plt.plot(ypoints, linestyle = 'dotted')
  plt.axvline(x=3750, ymin=-0.95, ymax=0.95, linestyle = (0,(5,1)), color = 'tab:orange',label='$f_1 = 3750$ Hz')
  plt.axvline(x=7500, ymin=-0.95, ymax=0.95, linestyle = (0,(5,1)), color = 'tab:green',label='$f_2 = 7500$ Hz')
  plt.axvline(x=11250, ymin=-0.95, ymax=0.95, linestyle = (0,(5,1)), color = 'tab:red',label='$f_3  = 11250$ Hz')
  #legend. Source: https://stackoverflow.com/questions/4700614/how-to-put-the-legend-outside-the-plot-in-matplotlib
  plt.legend(bbox_to_anchor=(0.5, -0.15), loc="upper center",fancybox=True, ncol=8, borderaxespad=0)
  plt.tight_layout(rect=[0,0,1,0.98])

  plt.show()

def magnitudeSpektrum(dataList, dataLabel,col, col2=-1):
  #Figure size (x,y) in inches. Move Legend if changed drasticly to avoid clipping
  fig = plt.figure(1, figsize=(14.5, 6.5))
  
  #number of rows/cols of subplots 
  ax = fig.add_subplot(1, 1, 1)
  
  #max num ticks in axis
  max_yticks = 20
  max_xticks = 10 #irrelevant due to log scale
  yloc = plt.MaxNLocator(max_yticks)
  xloc = plt.MaxNLocator(max_xticks)
  ax.yaxis.set_major_locator(yloc)
  ax.xaxis.set_major_locator(xloc)

  #Use log scale  
  #ax.set_xscale('log')
  #ax.set_yscale('log')

  #plot data
  time = [p[0] for p in dataList[0]]
  trace1 = [p[col] for p in dataList[0]]
  plt.plot(time, trace1, "-", alpha=1)
  #plt.plot(time, trace1, "-", alpha=0.8)
    
  for i in range (0,len(dataList)):
    
    
    
    if col2!=-1:
      trace1 = [p[col2] for p in dataList[i]]
      plt.plot(time, trace1, "-", alpha=1)
      #plt.plot(time, trace1, "-")
    
    

  #labels  
  plt.xlabel("Frekvens [Hz]")
  plt.ylabel("Magnitude (Peak Hold Cont.) [dB]")
  
  #legend. Source: https://stackoverflow.com/questions/4700614/how-to-put-the-legend-outside-the-plot-in-matplotlib
  plt.legend(dataLabel, bbox_to_anchor=(0.5, -0.15), loc="upper center",fancybox=True, ncol=8, borderaxespad=0)
  plt.tight_layout(rect=[0,0,1,0.98])

  #ellipse = Ellipse(xy=(580, -24), width=900, height=10, edgecolor='r', fc='None', lw=2)
  #ax.add_patch(ellipse)
  #add rectangle
  # plt.gca().add_patch(Rectangle((250,-100),1000,80,edgecolor='red',facecolor='none',lw=2))
  
  #Final touch
  #plt.title('Spektrum diagram')
  plt.grid(True)
  plt.show()

def phase(dataList, dataLabel,col):
  #Figure size (x,y) in inches. Move Legend if changed drasticly
  fig = plt.figure(1, figsize=(14.5, 6.5))
  
  #number of rows/cols of subplots 
  ax = fig.add_subplot(1, 1, 1)
  
  #max num ticks in axis
  max_yticks = 20
  max_xticks = 20 #irrelevant due to log scale
  yloc = plt.MaxNLocator(max_yticks)
  xloc = plt.MaxNLocator(max_xticks)
  ax.yaxis.set_major_locator(yloc)
  ax.xaxis.set_major_locator(xloc)

  #Use log scale  
  ax.set_xscale('log')
  # ax.set_yscale('log')

  #plot data
  for i in range (0,len(dataList)):
    time = [p[0] for p in dataList[i]]
    measurement = [p[col] for p in dataList[i]]
    plt.plot(time, measurement, "-")

  #labels  
  plt.xlabel("Frekvens [Hz]")
  plt.ylabel("Fase [grader]")
  
  #Legend
  plt.legend(dataLabel, bbox_to_anchor=(0.5, -0.1), loc="upper center",fancybox=True, ncol=8, borderaxespad=0)
  plt.tight_layout(rect=[0,0,1,0.98])
  
  #Final touch
  plt.grid(True)
  plt.title('Bode diagram fase')
  plt.show()

def bodeDiagram(fileList,dataLabel):
  if len(fileList)!=len(dataLabel):
    print("\n\nMissing labels for grafs\n\n")
  dataList= []
  for i in range (0,len(fileList)):
    dataList.append(readCSV(fileList[i]))
  magnitudeBode(dataList, dataLabel,2)
  phase(dataList, dataLabel,3)

def spektrumDiagram(fileList,dataLabel):
  if len(fileList)!=len(dataLabel):
    print("\n\nMissing labels for grafs\n\n")
  dataList= []
  for i in range (0,len(fileList)):
    dataList.append(readCSV(fileList[i]))
  magnitudeSpektrum(dataList, dataLabel,1,3)
  #phase(dataList, dataLabel,2)
plt.rcParams.update({'font.size': 16})



dataLabel = ["Demping ved $R_5 = 54$ $\Omega$","$R_2 = 470$ $\Omega$","$R_2 = 2,76$ k$\Omega$","$R_2 = 10,14$ k$\Omega$","$f_1$"]
bodefiles = ["D3 bode.csv"]
# bodeDiagram(bodefiles, dataLabel)



spektrumFiles = ["D3 spektrum 5.csv","D3 spektrum 6.csv"]

dataLabel = ["$x_1(t)$","$y(t)$","$\hat{x}_2(t)$"]

spektrumDiagram(spektrumFiles,dataLabel)