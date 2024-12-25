class Commit:
    def __init__(self, date, user_name, message):
        self.date = date
        self.user_name = user_name
        # self.file_name = file_name
        self.message = message


    def __str__(self):
        return f" {self.date} date, {self.user_name} user_name, {self.message} message"

    def to_dict(self):
        return {
            "date": self.date,
            "user_name": self.user_name,
            "message": self.message
        }