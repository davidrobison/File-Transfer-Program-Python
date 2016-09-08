# Import necessary libraries***********************************************************************************
import time
import random
import sqlite3
from sqlite3 import *
import os
import datetime
import shutil
from Tkinter import *
import os
from tkFileDialog import askdirectory
import Tkinter, tkFileDialog, Tkconstants


content = ''
folderPath = ''


# Functions****************************************************************************************************


# Associate a directory with first browse entry button
def browseFolder():

    global folderName
    folderName = tkFileDialog.askdirectory()
    foldersPath = os.path.dirname(folderName)
    folderPath.set(folderName)


# Associate a second directory with second browse entry button
def browseFolderTwo():

    global folderNameTwo
    folderNameTwo = tkFileDialog.askdirectory()
    foldersPathTwo = os.path.dirname(folderNameTwo)
    folderPathTwo.set(folderNameTwo)


# Importing 58of33.py file into #Functions section*********************************

def clicking():   
    
    # Set source(src), destination(dst), current time(now) and files_list variables
    src = folderName+'/'
    dst = folderNameTwo+'/'
    now = datetime.datetime.now()
    files_list = os.listdir(src)


    # Loop through the files to process
    for documents in files_list:


        # Use statinfo to get info about the file
        statinfo = os.stat(os.path.join(src, documents))


        # Extract only the info on modification time (st_mtime)
        timestamp = statinfo.st_mtime


        # Convert the timestamp to date
        date = datetime.datetime.fromtimestamp(timestamp)
        

        # Use strftime to compare day variables
        now_now = int(now.strftime('%d'))
        last_mod_time = int(date.strftime('%d'))


        if (now_now - last_mod_time) <= 1:
            if documents.endswith(".txt"):
                shutil.copy2(src + documents, dst)
    transferredFiles = str(os.listdir(dst.encode('utf-8')))
    print ('Files that have transfered:\n'+transferredFiles)


    #SQL portion*******************************
    
    conn = sqlite3.connect('transfer.files.db')
    c = conn.cursor()


    #Create a table
    def create_table():

        c.execute('CREATE TABLE IF NOT EXISTS fileCheckRegister(fileCheckDate TEXT, fileCheckTime REAL)')


    #Manually input data    
    #def data_entry():
    #    c.execute("INSERT INTO fileCheckRegister VALUES( , )")
    #    conn.commit()
    #    c.close()
    #    conn.close()
    

    #Get date/time info
    def dynamic_data_entry():

        global fileCheckDate
        fileCheckTime = time.time()
        fileCheckDate = str(datetime.datetime.fromtimestamp(fileCheckTime).strftime('%m-%d-%Y   %I:%M:%S %p'))
        c.execute("INSERT INTO fileCheckRegister(fileCheckTime, fileCheckDate) VALUES(?,?)",
                    (fileCheckTime, fileCheckDate))            
        conn.commit()
        
    
    # Retrieve data for "Current file check date/time"
    def read_from_db():

        c.execute('SELECT fileCheckDate FROM fileCheckRegister ORDER BY ROWID DESC LIMIT 1')
        data = c.fetchone()[0]
        fileCheckDateTime.set(str(data)) 

    #Retrieve data for "Last file check date/time"
    def read_from_dbtwo():

        c.execute('SELECT fileCheckDate FROM fileCheckRegister ORDER BY ROWID DESC LIMIT 1 OFFSET 1')
        data = c.fetchone()[0]
        fileCheckDateTimetwo.set(str(data)) 

    # Commands
    create_table()
    dynamic_data_entry()
    read_from_db()
    read_from_dbtwo()
    
     
# GUI Interface************************************************************************************************

root = Tk()
root.title('File Transfer')
root.geometry("598x200+350+270")

mf = Frame(root)
mf.pack()


# Frames for buttons and entries
f1 = Frame(mf, width=600, height=250)
f1.pack(fill=X)
f2 = Frame(mf, width=600, height=250)
f2.pack(fill=X)
f3 = Frame(mf, width=300, height=300)
f3.pack()
f4 = Frame(mf, width=600, height=250)
f4.pack(fill=X)
f5 = Frame(mf, width=600, height=250)
f5.pack(fill=X)


#Entry references to functions
folderPath = StringVar(None)
folderPathTwo = StringVar(None)
fileCheckDateTime = StringVar(None)
fileCheckDateTimetwo = StringVar(None)


#First browse button and entry
Label(f1,text="Select Source Folder (Only txt files):        ").grid(row=0, column=0, sticky='e')
Entry(f1, width=50, textvariable = folderPath).grid(row=0,column=1,padx=2,pady=2,sticky='we',columnspan=25)
Button(f1, text="Browse...", command=browseFolder).grid(row=0, column=27, sticky='ew', padx=8, pady=4)

#Second browse button and entry
Label(f2,text="Select Destination Folder (Only txt files):").grid(row=0, column=0, sticky='e')
Entry(f2, width=50, textvariable = folderPathTwo).grid(row=0,column=1,padx=2,pady=2,sticky='we',columnspan=25)
Button(f2, text="Browse...", command=browseFolderTwo).grid(row=0, column=27, sticky='ew', padx=8, pady=4)

#Transfer files button
Button(f3, text="Transfer files", width=22, command=lambda: clicking()).grid(sticky='ew', padx=10, pady=10)

#Current file check entry
Label(f4,text="Current file check date/time:                 ").grid(row=0, column=0, sticky='e')
Entry(f4, width=30, textvariable = fileCheckDateTime).grid(row=0,column=1,padx=8,pady=8,sticky='we',columnspan=25)

#Last file check entry
Label(f5,text="Last file check date/time:                       ").grid(row=0, column=0, sticky='e')
Entry(f5, width=30, textvariable = fileCheckDateTimetwo).grid(row=0,column=1,padx=8,pady=8,sticky='we',columnspan=25)

root.mainloop()