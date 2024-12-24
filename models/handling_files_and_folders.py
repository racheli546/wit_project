import os
from os.path import exists, isdir

import shutil



def create_folder(folder_name, path):
    if not exists(path):
        raise FileNotFoundError ("path not found")
    new_path =  os.path.join(path,folder_name)
    if isdir(new_path):
        raise FileExistsError( "folder already exists")
    os.mkdir(new_path)

#בדיקה לפעולה create_folder
# create_folder("1",r"C:\Users\user1\Documents\תיכנות\שנה ב\סמסטר א\Pyton\test")

#דורס את התקייה במידה וקיימת תקיה בשם זה
def create_file(file_name, path):
    if not exists(path):
        raise FileNotFoundError("path not found")
    new_path = os.path.join(path,file_name)
    file = open(new_path,"w").close()


#בדיקה לפעולה create_file
#create_file("index.html",r"C:\Users\user1\Documents\תיכנות\שנה ב\סמסטר א\Pyton\test\1")

#מוסיפה כתיבה לקובץ קיים ולא דורסת את התוכן הקודם
def write_file(path, text):
    if not exists(path):
        print("path not found")
        raise FileNotFoundError("path not found")
    with open(path, "a") as file:
        file.write(text)

#בדיקת פעולה write_file
#write_file(r"C:\Users\user1\Documents\תיכנות\שנה ב\סמסטר א\Pyton\test\1\index.html", "<h1> racheli</h1>")

#ייתכן שלא נצטרך להשתמש בה
def read_file(path):
    if not exists(path):
        print("path not found")
        raise FileNotFoundError("path not found")
    with open(path, "r") as file:
        return file.read()


#print(read_file(r"C:\Users\user1\Documents\תיכנות\שנה ב\סמסטר א\Pyton\test\1\index.html"))

#הפונקציה מעתיקה ודורסת את התוכן הקודם של הקובץ השני
def copy_file(source_path,destination_path ):
    shutil.copyfile(source_path, destination_path)


#בדיקת פונקציהcopy_file
#copy_file(r"C:\Users\user1\Documents\תיכנות\שנה ב\סמסטר א\Pyton\test\1\index.html", r"C:\Users\user1\Documents\תיכנות\שנה ב\סמסטר א\Pyton\test\1\try1.html")

