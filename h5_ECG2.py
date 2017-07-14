# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright © 2016, Continuum Analytics, Inc. All rights reserved.
#
# The full license is in the file LICENSE.txt, distributed with this software.
# ----------------------------------------------------------------------------

import pylab
import numpy as np
ecg = [0] * 10000
count = 3
count2 = 0
count3 = 0
count4 = 0
value = [0] * 1000
HRate = 60 / (np.average(t2[count4]) / 1000
              
file = open("opensignals_file_YYYY-MM-DD_hh-mm-ss.format_extension_2017-07-11_09-57-14.txt", "r")
#print file.readline()
t = [0] * 10000
t2 = [0] * 10000

array = []    
with open("opensignals_file_YYYY-MM-DD_hh-mm-ss.format_extension_2017-07-11_09-57-14.txt","r") as ins:
    for line in ins:
        array.append(line)

while(count != 10000):
    t = count-3 
    string = array[count]
    mystring = string.replace('\t', '-')
    mystring2 = mystring.split("-")
    #print mystring2
    ecg[count-3] = mystring2[5]
    count = count +1
    
while(count2 != 10000):
    if int(ecg[count2]) > 650:
        #print ecg[count2]
        #print " index value: "
        #print count2
        #print "-------------"
        value[count3] = count2
        #print value[count3]
        count3 = count3 + 1
    count2 = count2 + 1
    #print count3

while(count4 != 108):
    t2[count4] = value[count4+1]-value[count4]
    #print value[count4+1]
    #print t2[count4]
    count4 = count4 + 1
    #print t2[count4]
    #if 60 <= count4 <= 100:
      #print count4
    #count4 = count4 + 1
t2[count4] = range(400,1000)
print np.average(t2[count4])
print np.average(t2[count4]) / 1000
print 60 / (np.average(t2[count4]) / 1000
#print " t is: beats per millisecond"
#print t
#print array[100]    
#string = array[3]
#print string
#print string[13]

#mystring = string.replace('\t', '-')
#mystring2 = mystring.split("-")
#print mystring2[5]
t = np.linspace(0,10000,10000)
print t
#ecg = np.sin(t)
#print ecg
pylab.xlabel('Time(ms)')
pylab.ylabel('Milivolt')
pylab.axhspan(0, 200, alpha=0.5, color='red')
pylab.axhspan(750, 800, alpha=0.5, color='red')
pylab.axvspan(600,1000,alpha=0.5, color='green')
pylab.text(1,800,"Heart Rate" = HRate)
#BPMverticalalignment='bottom', horizontalalignment='right',
#transform = pylab.transAxes,color='black', fontsize=15):
pylab.plot(t, ecg)
pylab.show()
