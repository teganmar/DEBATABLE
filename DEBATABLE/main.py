import uvicorn
from fastapi import FastAPI
import requests
from pydantic import BaseModel
from typing import Optional
from scraper import get_soup, DEBATE_TOPICS_URL
import random as rd

app = FastAPI()

# class topics(BaseModel):
#     topic_num:float
#     topic:str

@app.get("/welcome/{name}")
def welcome(name:str):
    return {'Welcome!':f'Hi {name} thanks for using DEBATABLE',
        'message':'A critical thought a day keeps the stupid away!'}

@app.get("/topics/{num}")
def get_topic(num:int):
    topic_dict = get_soup()
    return topic_dict[num]

@app.get("/raondomized-topics")
def get_rand_topic():
    topic_dict = get_soup()
    return topic_dict[rd.randrange(len(topic_dict))]

if __name__ == "__main__":
    uvicorn.run("main:app", host='127.0.0.1', port=8200,reload=True)