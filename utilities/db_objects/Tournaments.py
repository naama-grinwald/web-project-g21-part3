from utilities.db.db_manager import dbManager

class Tournaments:
    def __init__(self):
        pass

    def get_all_tournaments(self):
        query = 'select * from tournaments;'
        return dbManager.fetch(query)

    def get_tournament(self,id_tournament):
        query = 'select * from tournaments where id=%s;' % id_tournament
        return dbManager.fetch(query,(id_tournament))

    def create_tournament(self,name,date,location,type,Season,details):
        query = "insert into tournaments(name,date,location,type,Season,details) values (%s,%s,%s,%s,%s,%s);"
        return dbManager.commit(query,(name,date,location,type,Season,details))

    def update_tournament(self, field, result,tournament_id):
        query = "UPDATE tournaments SET %s='%s' WHERE id ='%s';" % (field, result,tournament_id)
        return dbManager.commit(query, (tournament_id))

    def get_results(self, id_tournament):
        query = 'select id_player, concat(P.first_name," ", P.last_name) AS name, score, ROW_NUMBER() OVER(ORDER BY score desc) RowNumber from(select id_player1 as id_player, sum(score_player1) as score from((select id_player1,score_player1 from gamescores where id_tournament=%s) union all (select id_player2,score_player2 from gamescores where id_tournament=%s)) as scores group by id_player1) as S join Players AS P ON S.id_player = P.id  order by Score desc;' % (id_tournament, id_tournament)
        return dbManager.fetch(query,(id_tournament))

    def get_scores(self, id_tournament):
        query = 'select * from GameScores where id_tournament=%s;' % id_tournament
        return dbManager.fetch(query,(id_tournament))

    def insert_scores(self,id_tournament,Round,desk,id_player1,id_player2,score_player1,score_player2):
        query = "INSERT INTO GameScores(id_tournament,Round,desk,id_player1,id_player2,score_player1,score_player2) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        return dbManager.commit(query,(id_tournament,Round,desk,id_player1,id_player2,score_player1,score_player2))

    def delete_scores(self,id_tournament,Round,desk):
        query = 'DELETE FROM GameScores WHERE id_tournament=%s and Round=%s and desk=%s;'
        return dbManager.commit(query,(id_tournament,Round,desk))

    def get_ranked_tables(self, id_tournament):
        query = 'select count(*) as tables from GameScores where id_tournament=%s;' % id_tournament
        return dbManager.fetch(query,(id_tournament))

    def get_num_of_rounds(self, id_tournament):
        query = 'select count(distinct round) as rounds from GameScores where id_tournament=%s;' % id_tournament
        return dbManager.fetch(query,(id_tournament))

    def get_num_of_players(self,id_tournament):
        query = 'select count(distinct player) as players from ((select id_player1 as player from GameScores where id_tournament=%s) union (select id_player2 as player from GameScores where id_tournament=%s)) as a;' % (id_tournament, id_tournament)
        return dbManager.fetch(query, (id_tournament))

Tournaments = Tournaments()
