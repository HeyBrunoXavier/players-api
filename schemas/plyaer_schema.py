def playerEntity(db_item) -> dict:
  return {
    "id": str(db_item['_id']),
    "name": db_item['name'],
    "age": db_item['age'],
    "time": db_item['time']
  }

def listPlayersEntity(db_item_list) -> list:
  list_players = []
  for item in db_item_list:
    list_players.append(playerEntity(item))
  return list_players