from flaskr.database import db


def query_games():
    sql = "SELECT name, id FROM games"
    result = db.session.execute(sql).fetchall()
    return result


def query_game_by_name(game_name: str):
    sql = "SELECT id FROM games WHERE games.name=:game_name"
    result = db.session.execute(sql, {"game_name": game_name}).fetchone()
    if result:
        return result[0]
    else:
        raise ValueError(f"No game with name {game_name} found")


def get_game_name(id: int):
    sql = f"SELECT name FROM games WHERE id=:id"
    result = db.session.execute(sql, {"id": id}).fetchone()
    if result:
        return result[0]
    else:
        raise ValueError("No game with id found")


def get_all_times_in_game(id: int):
    sql = "SELECT courses.name, times.course_id, users.username FROM times JOIN courses ON courses.id=times.course_id JOIN users ON users.id=times.user_id WHERE times.course_id=:id"
    results = db.session.execute(sql, {"id": id}).fetchall()
    return results