import requests
import uuid
import os
import sys
import json

TOPIC      = os.getenv("TOPIC", "authorizations")
BASE_URL   = os.getenv("URL")
print(BASE_URL)
CREATE_URL = "{}/kafka/topic/create".format(BASE_URL)
SEND_URL   = "{}/kafka/topic/{}/send".format(BASE_URL, TOPIC)
API_KEY    = os.getenv("API_KEY")

## Status Codes
TOPIC_ALREADY_EXISTS = 409

def create_session():
    session = requests.Session()
    session.headers.update({
        "Authorization" : "Bearer " + API_KEY,
        "Content-Type": "application/json"
    })
    return session

def create_topic(session):
    try:
        response = session.post(CREATE_URL, json = {
            "topic" : TOPIC,
            "partitions": 1,
            "replicas": 1
        })
        response.raise_for_status()
        return response
    except requests.exceptions.HTTPError as e:
        status_code = e.response.status_code
        if status_code == TOPIC_ALREADY_EXISTS:
            print("{}-topic already exists, continuing normally".format(status_code))
        else:
            print("{}-an unknown error occured".format(status_code))

def produce(session, data):
    try:
        response    = session.post(SEND_URL, json = data)
        response.raise_for_status()
        print("{}-{}\n{}".format(response.status_code, json.dumps(data), response.json()))
    except Exception as e:
        print(e)
