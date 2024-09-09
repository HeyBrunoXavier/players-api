from fastapi import APIRouter
from config.database import connection
from models.player import Player
from schemas.plyaer_schema import playerEntity, listPlayersEntity
from bson import ObjectId

player_router = APIRouter()

@player_router.get("/")
async def init():
  return "Welcome FullStack FARM"

@player_router.get('/players')
async def list_players():
  return listPlayersEntity(connection.local.player.find())

@player_router.get('/players/{id}')
async def get_player_by_id(id: str):
  return playerEntity(connection.local.player.find_one(
      {"_id": ObjectId(id)}
    )
  )

@player_router.post('/players')
async def insert_player(player: Player):
  connection.local.player.insert_one(dict(player))
  return listPlayersEntity(connection.local.player.find())

@player_router.put('/players/{id}')
async def update_player(id: str, player: Player):
  connection.local.player.find_one_and_update(
    {
      "_id": ObjectId(id)
    },
    {
      "$set": dict(player)
    }
  )
  return playerEntity(connection.local.player.find_one(
      {
        "_id": ObjectId(id)
      }
    )
  )

@player_router.delete('/players/{id}')
async def delete_player_by_id(id: str):
  return playerEntity(connection.local.player.find_one_and_delete(
      {
        "_id": ObjectId(id)
      }
    )
  )