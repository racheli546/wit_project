from models.handling_files_and_folders import*
import os
from datetime import datetime
from  classes.Commit import Commit

class Repository:
    def __init__(self, repositary_path, user_name):
        self.dict_commits = {}
        self.repositary_path = repositary_path
        self.user_name = user_name
        self.count_commit = 0


    def add_commit(self, message):
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        c = Commit(formatted_time, self.user_name, message)
        self.dict_commits[self.count_commit] = c
        self.count_commit += 1
        print(self)


    def __str__(self):
        commits_str = "\n".join(
            f"{key}: {str(commit)}" for key, commit in self.dict_commits.items()
        )
        return (
            f"Repository:\n"
            f"  Path: {self.repositary_path}\n"
            f"  User: {self.user_name}\n"
            f"  Commits:\n{commits_str if commits_str else '  No commits yet.'}"
        )


    def wit_init(self):
        try:
            create_folder(".wit", self.repositary_path)
            new_path = os.path.join(self.repositary_path, ".wit")
            create_folder("Staging Area", new_path)
        except FileExistsError as e:
            print(e)
        except FileNotFoundError as e:
            print(e)


    def wit_add(self, file_name):
        try:
            new_path = os.path.join(self.repositary_path, ".wit")
            new_path = os.path.join(new_path, "Staging Area")
            create_file(file_name, new_path)
            new_path = os.path.join(new_path, file_name)
            source_path = os.path.join(self.repositary_path, file_name)
            copy_file(source_path, new_path)
        except FileNotFoundError as e:
            print(e)



    # def wit_commit(self):




#בדיקה לפונקציה init
repo = Repository(r"C:\Users\user1\Documents\תיכנות\שנה ב\סמסטר א\Pyton\test", "racheli")
# repo.wit_init()

# repo.wit_add("try.html")

# print(datetime.now())

# repo.add_commit("racheli")
# repo.add_commit("jhgxz")