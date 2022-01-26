from utilities.db.db_manager import dbManager

class Tournaments:
    def __init__(self):
        pass

    def get_tournament(self,id):
        query = 'select * from tournaments where id=%s;' % tournament_id
        return dbManager.fetch(query,(id))

Tournaments = Tournaments()
