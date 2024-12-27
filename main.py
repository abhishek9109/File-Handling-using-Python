from pathlib import Path
import os
import shutil

def creatingfolder():
   try:
      name = input("tell your folder name")
      path = Path(name)
      path.mkdir()
      print(f"folder name {name} has been created successfully")
   except Exception as err:
      print("folder already exist")

def readingfileandfolder():
   path=Path("")
   items=list(path.rglob("*"))
   for i ,v in enumerate(items):
      print(f"{i+1}) {v}") 

def updatingfolder():
   try:
      readingfileandfolder()
      oldname=input("tell which folder you want to update")
      path=Path(oldname)
      if path.exists()and path.is_dir():
         newname=input("tell your new name") 
         newpath=Path(newname)
         path.rename(newpath)
         print(f"folder name{oldname} update to {newname}seccussfully")
      else:
         print("Error folder does not exists")
   except Exception as err:
    print(f"An error occured as {err}") 

def deletingfolder():
   try:
      readingfileandfolder()
      name=input("tell your folder name that you want to delete")
      path=Path(name)
      if path.exists() and path.is_dir():
         shutil.rmtree(path)
         print("seccussfully deleted")
      else:
         print("Error folder does not exists")
   except Exception as err:
    print(f"Error as {err}")

def creatingfile():
   try:
      readingfileandfolder()
      name=input("tell file name with extension")
      path=Path(name)
      if not path.exists():
         with open(name,"w")as file:
            data=input("please tell your data you wnat to input")
            file.write(data)
            print("file created seccussfully ")
      else:
         print("file name already exists")
   except Exception as err:
     print(f"An Error occured as {err}") 

def updatingfile():
   try:
      readingfileandfolder()
      name=input("which file you want to update")
      path=Path(name)
      if path.exists () and path.is_file():
        print("operations")
        print("press 1 for rename the file")
        print("press 2 overwritting the file")
        print("press 3 appending the contant in the file")
        choice=input("please tell your choice")

      if choice =="1":
         newname=input("tell your new file name")
         newpath=Path(newname)
         if not newpath.exists():
           path.rename(newpath)
           print(f"file name{name} changed to {newname} successfully")
         else:
            print(f"Error filename{newname} already exists")

      if choice=="2":
         with open (name,"w") as file:
            data=input("tell your data you want to overwrite")
            file.write(data)
            print("overwritting successfully")

      if choice =="3":
         with open (name,"a")as file:
            data=input("please tell your data you wanr to append")
            file.write("  " + data)
            print("appeneded successfully")
      else:
        print("file does not exists")
   except Exception as err:
     print(f"An Error occured as {err}") 

def readingfile():
   try:
      readingfileandfolder() 
      name=input("tell your file name you want to read")
      path=Path(name)
      if path.exists():
         with open(name,"r") as file:
            print(file.read())
      else:
       print("file does not exists")
   except Exception as err:
     print(f"An error occured to {err}") 

def deletingfile():
   try:
      readingfileandfolder()
      name=input("tell which file you want to delete")
      path=Path(name)
      if path.exists():
         path.unlink()
         print("tell deleted successfully")
      else:
         print("file does not exists")
   except Exception as err:
    print(f"An error occuerd as {err}")             

print("press 1 for creating a folder")
print("press 2 for reading a folder")    
print("press 3 for updating a folder")
print("press 4 for deleding a folder")
print("press 5 for creating a file")
print("press 6 for updating a file")
print("press 7 for reading a file")
print("press 8 for deleting a file")
a= input("tell your input")
if a=="1":
   creatingfolder()
if a=="2": 
    readingfileandfolder()
if a=="3":
     updatingfolder()
if a=="4":
     deletingfolder()
if a=="5":
       creatingfile()
if a=="6":
   updatingfile()
if a=="7":
   readingfile()
if a=="8":
   deletingfile()          


