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

#הפונקציה מעתיקה ודורסת את התוכן הקודם של הקובץ השני במידה והיה קיים
def copy_file(source_path,destination_path ):
    shutil.copyfile(source_path, destination_path)


def find_last_created_folder(path):
     # קבל את כל התיקיות בתיקיה הנתונה
    folders = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
    # מיין את התיקיות לפי זמן יצירתן (מהחדש לישן)
    last_created_folder = max(folders, key=lambda folder: os.path.getctime(os.path.join(path, folder)))
    return last_created_folder


def copy_folder(source_path,destination_path):
    shutil.copytree(source_path, destination_path)


#פונקציה שמקבלת ניתובים ומילה ומעתיקה מהמקור ליעד את הכל ורק משאירה לה גם את המילה
def copy_folder_without_param(source_path,destination_path, param ):
    for item in os.listdir(destination_path):
        if item != param:
            path = os.path.join(destination_path, item)
            os.remove(path)
    for item in os.listdir(source_path):
        path = os.path.join(source_path, item)
        new_path = os.path.join(destination_path, item)
        copy_file(path, new_path)


def copy_files_and_overwrite(source_dir, destination_dir):
    # מעבר על כל הקבצים והתיקיות בתיקיית המקור
    for item in os.listdir(source_dir):
        source_item = os.path.join(source_dir, item)
        destination_item = os.path.join(destination_dir, item)

        # אם זה תיקיה,  קריאה חוזרת לפונקציה להעתיק גם את תוכן התיקיה
        if os.path.isdir(source_item):
            if not os.path.exists(destination_item):
                os.makedirs(destination_item)  # יצירת את התיקיה אם היא לא קיימת
            copy_files_and_overwrite(source_item, destination_item)
        else:
            # אם זה קובץ, תמיד  העתקה מחדש (החלפה אוטומטית של קובץ ישן)
            shutil.copy2(source_item, destination_item)  # העתקת הקובץ עם זמן יצירה ומידע נוסף



# copy_files_and_overwrite(r"C:\Users\user1\Documents\תיכנות\שנה ב\סמסטר א\Pyton\test\1", r"C:\Users\user1\Documents\תיכנות\שנה ב\סמסטר א\Pyton\test\2")
# print("ההעברה הושלמה.")

def emptying_folder (path):
    for item in os.listdir(path):
        try:
            current_file=os.path.join(path,item)
            os.remove(current_file)
        except:
            print("Folder doesn't exist")


def folder_is_empty(path):
    if not os.listdir(path):
        return True
    return False


def read_names_file_in_folder (path):
    all_names = []
    try:
        for item in os.listdir(path):
            # print(item)
            all_names.append(item)
        return all_names
    except:
        print("Folder doesn't exist")

#בדיקת פונקציהcopy_file
# copy_folder(r"C:\Users\user1\Documents\תיכנות\שנה ב\סמסטר א\Pyton\test\1", r"C:\Users\user1\Documents\תיכנות\שנה ב\סמסטר א\Pyton\test\2")
# print(folder_is_empty(r"C:\Users\user1\Documents\תיכנות\שנה ב\סמסטר א\Pyton\test\1"))
# print(read_names_file_in_folder(r"C:\Users\user1\Documents\תיכנות\שנה ב\סמסטר א\Pyton\test\1"))

#מקבלת שתי ניתובים ובודקת האם שתי הקבצים נוצרו בזמן שונה
def is_file_modified_after(path1, path2):
    date_path1 = os.path.getmtime(path1)
    date_path2 = os.path.getmtime(path2)
    #מחזירה נכון כשהניתוב הראשון נעשה אחרי הניתוב השני
    if date_path1 > date_path2:
        return True
    return False

#print(is_file_modified_after(r"C:\Users\user1\Documents\תיכנות\שנה ב\סמסטר א\Pyton\test\2", r"C:\Users\user1\Documents\תיכנות\שנה ב\סמסטר א\Pyton\test\1"))
