#FTP using python 
#Author: Ankit Patel

#import ftp lib 
import sys
from ftplib import FTP
import time

ftp=FTP()
#function to connect
start_time=0
execution_time=time.clock()

def connect():
	
	start_time=time.clock()	
	ip=input("Enter a valid ftp domain.")
	username=input("Enter valid username.[For Anonymous login press enter]")
	password=input("Enter valid password.[For Anonymous login press enter]")
	ftp.connect(ip)
	ftp.login(username,password)
	ftp.getwelcome()	       
	print("Connected!")
	print("-----------------------------")

#function to download file

def download():

	download_time=time.clock()
	filename=input("Enter filename to download")
	ftp.retrbinary("RETR %s" %filename,open(filename,"wb").write)
	print("File downloaded successfully at %s seconds"%(time.clock()-download_time))
	print("------------------------------------")

#function to upload file

				
def upload():

	choice=input("Do you want to create a new file? Y|N")
	if(choice=="Y" or choice=="y"):
		filename=input("Enter filename.")
		file=open(filename,"w")
		contents=input("Enter the contents of the file..")
		file.write(contents)
		print("Contents added successfully.")
		ftp.storlines("STOR "+"/"+filename,file)
		print("Contents stored successfully at %s"%(ip))
		file.close()
	else:
		filename=input("Enter filename to upload.")
		file=open(filename,"rb")
		ftp.storlines("STOR "+"/"+filename,file)
		print("Contents stored successfully at %s"%(ip))
		file.close()

#function to change directory

def show():

	ftp.retrlines('LIST')
	print("Files content displayed successfully")
	print("------------------------------")

def size(filename):
	s=ftp.size(filename)
	print("Size of file is %d"%(s))

#function to change directory

def cd(dir):

	ftp.cwd(dir)

try:
	while True:
	#	print("Time %s"%(time.time())
		print("\tFTP using python ")
		print("1. Connect to ftpserver.")
		print("2. List the contents.")
		print("3. Download a file.")
		print("4. Upload a file.")
		print("5. Change directory")
		print("6. Display size of file")
		print("7. Close FTP connection")
		print("8. Exit")
		choice=int(input("Enter your choice"))
		if(choice!=0):
			if(choice==1):
				connect()

			if(choice==2):
				show()			
					     
			if(choice==3):
				download()

			if(choice==4):
				upload()	
				
			if(choice==5):
				dir=input("Enter directory to change.")
				cd(dir)

			if(choice==6):
				filename=input("Enter the filename.")
				size(filename)

			if(choice==7):
				print("Connection active for %s seconds"%(time.clock()-start_time))
				ftp.close()
				print("Connection closed.")

		
			if(choice==8):
				print("Execution time ---%s seconds"%(time.clock()-execution_time))
				exit()

		else:
			print("Enter a choice greater than zero")

except ValueError:
	print("No value entered. Exiting.")

except Exception:
	print("Error encountered.Exiting")


				       


		
			
	
