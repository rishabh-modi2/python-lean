import os
import datetime
import time
import requests
import logging, time
# coding: utf-8
import sys
from datetime import datetime
import leancloud
from flask import Flask, jsonify, request, send_file
from flask import render_template
from flask_sockets import Sockets
from leancloud import LeanCloudError
# log_file = open("log.txt", "a+")
http_base_url = "https://bakchodi.org/api/v3"
interval_post_per_second = 600

logging.basicConfig(filename="log.txt", 
                    format='%(asctime)s %(message)s', 
                    filemode='w') 
logger=logging.getLogger() 
logger.setLevel(logging.DEBUG) 

# while True:
#     logger.debug("This is just a harmless debug message") 
#     time.sleep(2)

auth_placebot01 = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjEzMzYsImlzcyI6ImJha2Nob2RpLm9yZyIsImlhdCI6MTY1MDI2MjY2M30.JgxIvbZX_uT-TziDu4rj1oEhsnA_m-qa_Nsu0JZxTLc'

def send_post_request(location, json_data):
    r = requests.post(f"{http_base_url}{location}", json=json_data)
    return r


def send_get_request(location, json_data):
    r = requests.get(f"{http_base_url}{location}", json=json_data)
    return r


app = Flask(__name__)


@app.route('/log')
def log():
    return send_file('log.txt')


@app.route('/createaccount')
def createaccount():
    postData1 = {"username": request.args.get('username'), "password_verify": request.args.get('password'),
                 "password": request.args.get('password'), "show_nsfw": True, "answer": 'Allow Me'}
    postData = {k: v for k, v in postData1.items() if v}
    CreateAccountResponse = send_post_request("/user/register", json_data=postData)
    logger.debug(CreateAccountResponse.text)
    logger.debug(CreateAccountResponse.status_code)


@app.route('/createpost')
def createPost(community_id, name, body=None, url=None, nsfw=False, auth=None, **kwarg):
    postData1 = {"name": name, "url": url, "body": body,
                 "nsfw": nsfw, "community_id": int(community_id), "auth": auth}
    postData = {k: v for k, v in postData1.items() if v}
    createPostResponse = send_post_request("/post", json_data=postData)
    logger.debug(createPostResponse.text)


@app.route('/createcomment')
def CreateComment(content, post_id):
    postData1 = {"content": content, "post_id": int(post_id), "auth": auth}
    postData = {k: v for k, v in postData1.items() if v}
    createCommentResponse = send_post_request("/comment", json_data=postData)
    logger.debug(createCommentResponse.text)


@app.route('/like')
def like(score, post_id, auth):
    #   global auth
    postData1 = {"score": int(1), "post_id": int(post_id), "auth": auth}
    postData = {k: v for k, v in postData1.items() if v}
    createCommentResponse = send_post_request("/post/like", json_data=postData)
    logger.debug(createCommentResponse.text)


@app.route('/deletepost')
def DeletePost(post_id, auth):
    #   global auth
    postData1 = {"deleted": True, "post_id": int(post_id), "auth": auth}
    postData = {k: v for k, v in postData1.items() if v}
    createCommentResponse = send_post_request("/post/delete", json_data=postData)
    logger.debug(createCommentResponse.text)




class BadGateway(Exception):
    status_code = 502

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_json(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return jsonify(rv)


class BadRequest(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_json(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return jsonify(rv)


@app.errorhandler(BadGateway)
def handle_bad_gateway(error):
    response = error.to_json()
    response.status_code = error.status_code
    return response


@app.errorhandler(BadRequest)
def handle_bad_request(error):
    response = error.to_json()
    response.status_code = error.status_code
    return response


@app.route('/api/python-version', methods=['GET'])
def python_version():
    return jsonify({"python-version": sys.version})
