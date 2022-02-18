from utilities.db.db_manager import dbManager

class Players:
    def __init__(self):
        pass

    def get_players(self):
        query = 'select id, concat(first_name," ", last_name) AS name, level, age, school from Players;'
        return dbManager.fetch(query)

    def get_players_id(self):
        query = 'select id from Players;'
        return dbManager.fetch(query)

    def insert_player(self,id, first_name, last_name, level, age, school):
        query = "insert into Players(id, first_name, last_name, level, age, school) values (%s,%s,%s,%s,%s,%s);"
        return dbManager.commit(query,(id, first_name, last_name, level, age, school))

    def delete_player(self,Players_id):
        query = "delete from Players where id='%s';" % Players_id
        return dbManager.commit(query,(Players_id))

    def update_player(self,field, result,id):
        query = "UPDATE Players SET %s='%s' WHERE id ='%s';" % (field, result, id)
        return dbManager.commit(query, (id))

Players = Players()
