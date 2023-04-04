from datetime import datetime


class my_date:

    def __init__(self):
        print(self)

    def date_to_db(self):
        try:
            form_date_to_db = datetime.datetime.strptime(self, "%Y-%m-%d %H:%M")
        except:
            form_date_to_db = None
        return form_date_to_db

    def composite_date(*self):
        print("my_date.composite_date: ", self)
        if not self[0]:
            print("my_date.composite_date: ", "is none")
            form_date_to_db = None
        else:
            print("my_date.composite_date: ", "is not none")
            try:
                #form_date_to_db = datetime.datetime.strptime(self[0] + 'T' + self[1], "%Y-%m-%dT%H:%M")
                form_date_to_db = str(self[0] + 'T' + self[1])
            except:
                form_date_to_db = None

        return form_date_to_db
