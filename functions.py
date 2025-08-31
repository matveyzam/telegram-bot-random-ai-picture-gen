import random
import requests

def numgen():
  number = random.randint(1,10)
  return number

def rewrite(user_id, user_text):
  with open(f"user_{user_id}_text.txt", "a", encoding="utf-8") as file:
    file.write(user_text + "\n")
  return user_id
