import requests
from bs4 import BeautifulSoup
import re

DEBATE_TOPICS_URL = 'https://www.debatedrills.com/past-topics'

def get_soup():
    response = requests.get(DEBATE_TOPICS_URL)
    if response.ok:
        soup = BeautifulSoup(response.text, "html.parser")#"lxml")

        TOPICS = []
        for i in soup.find_all("li", class_="padding-bottom-10-px"):
            mystring=i.contents[-1].get_text().split(':')[-1]
            #print(re.sub('[^A-Za-z0-9]+',' ', mystring))
            TOPICS.append(re.sub('[^A-Za-z0-9]+', ' ', mystring))
        TOPICS = [x.lstrip().rstrip() for x in TOPICS]
        TOPICS = TOPICS[:-1]
        topic_dict = dict(zip(range(1,len(TOPICS)+1), TOPICS))
        return topic_dict
    else:
        return {'Response':f'{response.status_code}'}

if __name__ == "__main__":
    topic_dict = get_soup()
    #print(topic_dict)