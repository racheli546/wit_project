import json
from os import listdir

from models.handling_files_and_folders import*
import os
from datetime import datetime
from  classes.Commit import Commit

class Repository:
    def __init__(self, repository_path, user_name):
        self.dict_commits = {}
        self.repository_path = repository_path
        self.user_name = user_name
        self.count_commit = 0
        self.load_commits()
        self.wit_path = os.path.join(self.repository_path, ".wit")
        self.commits_path = os.path.join(self.wit_path, "commits")
        self.staging_area_path = os.path.join(self.wit_path, "Staging Area")
        self.commits_json_path = os.path.join(self.wit_path, "commits.json")


    def __str__(self):
        commits_str = "\n".join(
            f"{key}: {str(commit)}" for key, commit in self.dict_commits.items()
        )
        return (
            f"Repository:\n"
            f"  Path: {self.repository_path}\n"
            f"  User: {self.user_name}\n"
            f"  Commits:\n{commits_str if commits_str else '  No commits yet.'}"
        )




    def load_commits(self):
        """טוען את הקומיטים הקיימים מתוך הקובץ ומעדכן את המונה"""
        new_path = os.path.join(self.repository_path, ".wit", "commits.json")
        if os.path.exists(new_path):
            try:
                with open(new_path, "r", encoding="utf-8") as json_file:
                    existing_data = json.load(json_file)
                if isinstance(existing_data, dict):
                    self.count_commit = len(existing_data)  # מספר הקומיטים הקיימים
                    self.dict_commits = existing_data  # טוען את הקומיטים למילון
            except Exception as e:
                print(f"Error loading commits: {e}")

    def add_commit(self, message):
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d%H:%M:%S")
        c = Commit(formatted_time, self.user_name, message)
        new_path = os.path.join(self.repository_path, ".wit", "commits.json")
        try:
            if os.path.exists(new_path):
                with open(new_path, "r", encoding="utf-8") as json_file:
                    existing_data = json.load(json_file)
                    print(existing_data)
            else:
                existing_data = {}
            existing_data[self.count_commit] = c.to_dict()
            self.count_commit += 1
            with open(new_path, "w", encoding="utf-8") as json_file:
                json.dump(existing_data, json_file, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Error updating JSON file: {e}")

        # מוסיפה לרשימה את כל הקבצים שנעשה עליהם שינוי אחרי הcommit
        def append_changing_file(self):
            list_change = []  # מערך שמכיל את רשימת הקבצים ששונו
            path_commit = os.path.join(self.repository_path, ".wit", "commits")
            last_commit = find_last_created_folder(path_commit)
            path_last_commit = os.path.join(path_commit, last_commit)
            for item in os.listdir(self.repository_path):
                path = os.path.join(self.repository_path, item)
                if item != ".wit" and is_file_modified_after(path, path_last_commit):
                    list_change.append(item)
            return list_change

    def wit_init(self):
        try:
            create_folder(".wit", self.repository_path)
            new_path = self.wit_path
            create_folder("Staging Area", new_path)
            create_folder("commits", new_path)
            create_file("commits.json", new_path)
            new_path = os.path.join(new_path, "commits.json")
            write_file(new_path,"{}")
        except FileExistsError as e:
            print(e)
        except FileNotFoundError as e:
            print(e)


    def wit_add(self, file_name):
        try:
            new_path = self.wit_path
            new_path = os.path.join(new_path, "Staging Area")
            create_file(file_name, new_path)
            new_path = os.path.join(new_path, file_name)
            source_path = os.path.join(self.repository_path, file_name)
            copy_file(source_path, new_path)
        except FileNotFoundError as e:
            print(e)



    def wit_commit(self, message):
        message += "("+str(self.count_commit) +")"
        self.add_commit(message)
        path_commit= os.path.join(self.repository_path, ".wit", "commits")
        path_new_folder = os.path.join(path_commit, message)
        #בדיקה אם הcommit שנוצר הוא הגרסה הראשונה
        if not os.listdir(path_commit):
            create_folder(message,path_commit)
            #יצירת גרסה חדשה של commit שמועתקת מהגרסה הקודמת
        else:
            last_folder = find_last_created_folder(path_commit)
            path_last_folder = os.path.join(path_commit, last_folder)
            copy_folder(path_last_folder, path_new_folder)

        #יצירת שינויים לגירסה החדשה - השינויים מהStaging Area
        path_staging_area = os.path.join(self.repository_path, ".wit", "Staging Area")
        copy_files_and_overwrite(path_staging_area, path_new_folder)
        emptying_folder(path_staging_area)


    def wit_log(self):
        path_commits_json = os.path.join(self.repository_path, ".wit", "commits.json")
        try:
            with open(path_commits_json, "r", encoding="utf-8") as json_file:
                all_commits = json.load(json_file)
                for key, value in all_commits.items():
                    print(json.dumps({key: value}, indent=4, ensure_ascii=False))
                    print("\n")  # הורדת שורה
            return all_commits
        except FileNotFoundError as e:
            print(e)


    def wit_status(self):
        list_name_file_in_staging_area = []
        path = os.path.join(self.repository_path, ".wit", "Staging Area")
        if folder_is_empty(path):
            print("No changes added to commit")
        else:
            list_name_file_in_staging_area = read_names_file_in_folder(path)
        list_files_changing = self.append_changing_file()
        #יצירת רשימה חדשה של מה שלא נמצא בadd
        list_files_changing =  [item for item in list_files_changing if item not in list_name_file_in_staging_area]
        return list_name_file_in_staging_area, list_files_changing


    def wit_checkout(self, commit_id):
        path_commits_json = os.path.join(self.repository_path, ".wit", "commits.json")
        message_commit = ""
        try:
            with open(path_commits_json, "r", encoding="utf-8") as json_file:
                all_commits = json.load(json_file)
                for key, value in all_commits.items():
                    if key == commit_id:
                        message_commit = value["message"]
                if message_commit == "":
                    return "id not valid"
        except FileNotFoundError as e:
            print(e)
        commit_path = os.path.join(self.repository_path, ".wit", "commits")
        for item in listdir(commit_path):
            if item == message_commit:
                commit_path = os.path.join(commit_path, item)
                copy_folder_without_param(commit_path, self.repository_path, ".wit")
                return





    #בדיקה לפונקציה init
repo = Repository(r"C:\Users\user1\Documents\תיכנות\שנה ב\סמסטר א\Pyton\test", "racheli")
#יצירת תקייה wit ובתוכה תקייה Staging Areaו תקייה commits וקובץ commits.json
# repo.wit_init()

#מוסיף לStaging Area קובץ שנעשה בו שינוי ורוצים להעלות אותו ל wit
# repo.wit_add("in.html")
# יצירת commit חדש - הכנסה שלו לקובץ הjson והוספת תקייה בשם שנשלח לתוך תקיית הcommits בתקייה יש את הפרוייקט עם הדפים שהועלו
# repo.wit_commit("add in.html ")
#מציג את רשימת הcommits למשתמש
# repo.wit_log()
# מחזיר למשתמש באילו קבצים הוא עשה שינויים ולא עשה add וכן באילו קבצים הוא עשה add אבל לא העלה לgit עם commit
# print(repo.wit_status())
# מחזיר את הפרוייקט שיהיה כמו הcommit בעל הid שהתקבל
# print(repo.wit_checkout("1"))