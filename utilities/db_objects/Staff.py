from utilities.db.db_manager import dbManager

class Staff:
    def __init__(self):
        pass

    def get_staff(self):
        query = 'select email, concat(first_name," ", last_name) AS name, phone, role, password from staff;'
        return dbManager.fetch(query)

    def get_staff_email(self):
        query = 'select email from Staff;'
        return dbManager.fetch(query)

    def get_staff_password(self,user_email):
        query = "select password from staff where email='%s';" % user_email
        return dbManager.fetch(query, (user_email))

    def get_staff_name(self, user_email):
        query = "select first_name from staff where email='%s';" % user_email
        return dbManager.fetch(query, (user_email))

    def insert_staff(self, email, first_name, last_name, phone, role, password):
        query = "insert into Staff(email, first_name, last_name, phone, role, password) values (%s,%s,%s,%s,%s,%s); "
        return dbManager.commit(query,(email, first_name, last_name, phone, role, password))


    def delete_staff(self, email):
        query = "delete from staff where email='%s';" % email
        return dbManager.commit(query, (email))

Staff = Staff()
