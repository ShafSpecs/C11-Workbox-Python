import json
from pathlib import Path
from typing import Optional

current_dir = Path(__file__).parent.absolute()

if not Path.exists(current_dir / "db.json"):
  Path.touch(current_dir / 'db.json')

db = Path(__file__).parent.absolute() / 'db.json'


def read_db() -> list:
  with db.open(mode="r", encoding="utf-8") as file:
    return json.load(file)


def write_to_db(new_db: list):
  with db.open(mode="w", encoding="utf-8") as file:
    json.dump(new_db, file, indent=2)
    
  
def add_to_db(new_db: dict):
    db_data: list = read_db()
    db_data.append(new_db)
    db_data.sort(key=lambda x: x["username"])
    write_to_db(db_data)
    
  
def get_user(username: str) -> Optional[dict]:
  db_data: list = read_db()
  for user in db_data:
    if user["username"] == username:
      return user
  return None


def get_usernames() -> list:
  db_data: list = read_db()
  usernames: list = []
  if len(db_data) > 0:
    for user in db_data:
      usernames.append(user["username"])
  return usernames


def get_user_tweets(username: str) -> Exception or list:
  user: dict = get_user(username)
  if user is None:
    return Exception("User not found!")
  return user["tweets"]


def create_tweet(username: str, tweet: dict):
  user: dict = get_user(username)
  if user is None:
    return Exception("User not found!")
  user["tweets"].append(tweet)
  user["tweets"].sort(key=lambda x: x["date"])
  
  db_data = read_db()
  for i in range(len(db_data)):
    if db_data[i]["username"] == username:
      db_data[i] = user
      break
      
  write_to_db(db_data)


def delete_tweet(username: str, tweet: dict):
  db_data: list = read_db()
  user: dict = get_user(username)
  if user is None:
    return Exception("User not found!")

  user["tweets"].remove(tweet)
  user["tweets"].sort(key=lambda x: x["date"])

  for i in range(len(db_data)):
    if db_data[i]["username"] == username:
      db_data[i] = user
      break

  write_to_db(db_data)
  