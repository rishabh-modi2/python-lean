import time, praw, _thread, requests, logging, time, sys, datetime, os, random
from datetime import datetime
from flask import Flask, jsonify, request, send_file
from flask import render_template
from flask_sockets import Sockets
# from leancloud import LeanCloudError
# log_file = open("log.txt", "a+")
http_base_url = "https://bakchodi.org/api/v3"
interval_post_per_second = 600

logging.basicConfig(filename="log.txt", 
                    format='%(asctime)s %(message)s', 
                    filemode='w') 
logger=logging.getLogger() 
logger.setLevel(logging.DEBUG) 
reddit = praw.Reddit(
    client_id="sjAd1LOtxmlJWNZ7cuMGWg",
    client_secret="izHyy-ynwCppgsHFJTrkdlLWaJ9TVw",
    user_agent="ris",
    username="Dank_ka_choda-",
    password="rishabh2003",
    ratelimit_seconds=900,
)   

# while True:
#     logger.debug("This is just a harmless debug message") 
#     time.sleep(2)
auth_manushya = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjEzMTQsImlzcyI6ImJha2Nob2RpLm9yZyIsImlhdCI6MTY1MDI2MTYzNn0.M7V0oQ9vdZv86ryXqLDmmqw16A3SS8M5jaM8R055yiU'
auth_placebot01 = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjEzMzYsImlzcyI6ImJha2Nob2RpLm9yZyIsImlhdCI6MTY1MDI2MjY2M30.JgxIvbZX_uT-TziDu4rj1oEhsnA_m-qa_Nsu0JZxTLc'
auth_Baaphutera = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjEzMzcsImlzcyI6ImJha2Nob2RpLm9yZyIsImlhdCI6MTY1MDI3Mjg4M30.YXBPXLQZkv1kZDQ_yLiJEJavISKJEN1MBTMxmFY9NUs'
auth_Comedy_cex = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjEzMzgsImlzcyI6ImJha2Nob2RpLm9yZyIsImlhdCI6MTY1MDI3Mjk1M30.YLoOws55w6HXaeJps9t4Y9OG1bA_oPn1UPshlr3saVw'
auth_Dangerous_bhaiya = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjEzMzksImlzcyI6ImJha2Nob2RpLm9yZyIsImlhdCI6MTY1MDI3MzAzOH0.vzOa9zlOxFzTqh2KlG_As3tZdjHuvqNsPr0SJ_zTP6Q'
auth_Buddhu = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjE3ODEsImlzcyI6ImJha2Nob2RpLm9yZyIsImlhdCI6MTY1MzIzMDM2NH0.VqZbZMvJJjd2bdiBp9RZ6sdwTCSPGjNF2Fp0uHQKXNk'
auth_Gaddarmusalman = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjE3ODIsImlzcyI6ImJha2Nob2RpLm9yZyIsImlhdCI6MTY1NTQ0ODY2N30.rjCg7o7QyKWd_9Jbez5yPiPsF6-ZWBjhYYbQyft69v0'
auth_Csk_raja = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjE5MTAsImlzcyI6ImJha2Nob2RpLm9yZyIsImlhdCI6MTY1NTQ0ODcwNH0.Tu9hcp2-spjQu13Wn3UEqLyCgf2GjCheatC0bIcB6Ec'
auth_MaiKyuBatau='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjE5MzksImlzcyI6ImJha2Nob2RpLm9yZyIsImlhdCI6MTY1Njc0MDc1N30.lRqPYOrKhoeeL5vnw0QHOt_D2DR8v81glIsaMGb0X1w'
auth_terabaaphu='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjE5NDAsImlzcyI6ImJha2Nob2RpLm9yZyIsImlhdCI6MTY1Njc0Nzg4NH0.cd3TND5IK7IVOED8ZZBTl47mIz3BOO97UeQvtgmcg9Y'
auth_tujhekya='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjE5NDEsImlzcyI6ImJha2Nob2RpLm9yZyIsImlhdCI6MTY1Njc0NzkyOX0.P9pivfipk6ee4Vbmt07U_rRvfATRJnQwQACN5SMR_HQ'
authid = [auth_terabaaphu, auth_tujhekya, auth_manushya, auth_Gaddarmusalman, auth_Buddhu, auth_Csk_raja, auth_Dangerous_bhaiya, auth_Comedy_cex, auth_Baaphutera, auth_MaiKyuBatau]


def send_post_request(location, json_data):
    r = requests.post(f"{http_base_url}{location}", json=json_data)
    return r


def send_get_request(location, json_data):
    r = requests.get(f"{http_base_url}{location}", json=json_data)
    return r

def retrypost(endpoint, json_data, p1):
    postresponse=send_post_request(endpoint, json_data=json_data)
    if postresponse.status_code!=200:
        p1=p1+1
        retrypost(endpoint, json_data, p1=p1)



def createPost(name, url, body, nsfw, community_id, auth, sleep):
    if sleep==None:
        print('no sleep')
    else:
        time.sleep(int(sleep))
    if community_id==None:
        community_id=18
    postData1 = {"name": name, "url": url, "body": body,
                 "nsfw": nsfw, "community_id": int(community_id), "auth": auth}
    postData = {k: v for k, v in postData1.items() if v}
    createPostResponse = send_post_request("/post", json_data=postData)
    logger.debug(createPostResponse.text)
    logger.debug(createPostResponse.status_code)
    if createPostResponse.status_code!=200:
        time.sleep(600)
        createPostResponse = send_post_request("/post", json_data=postData)
        if createPostResponse.status_code!=200:
            time.sleep(600)
            createPostResponse = send_post_request("/post", json_data=postData)
            if createPostResponse.status_code!=200:
                time.sleep(600)
                createPostResponse = send_post_request("/post", json_data=postData)
            else:
                logger.debug(createPostResponse.text)
                # logger.debug(createPostResponse.status_code)
                return createPostResponse.json()
        else:
            logger.debug(createPostResponse.text)
            # logger.debug(createPostResponse.status_code)
            return createPostResponse.json()
    else:
        logger.debug(createPostResponse.text)
        # logger.debug(createPostResponse.status_code)
        return createPostResponse.json()



def CreateComment(content, post_id, auth, sleep):
    if sleep==None:
        print('no sleep')
    else:
        time.sleep(int(sleep))
    postData1 = {"content":content, "post_id":int(post_id), "auth": auth}
    postData = {k: v for k, v in postData1.items() if v}
    createCommentResponse = send_post_request("/comment", json_data=postData)
    logger.debug(createCommentResponse.text)
    logger.debug(createCommentResponse.status_code)
    if createCommentResponse.status_code!=200:
        time.sleep(600)
        createCommentResponse = send_post_request("/comment", json_data=postData)
        if createCommentResponse.status_code!=200:
            time.sleep(600)
            createCommentResponse = send_post_request("/comment", json_data=postData)
            if createCommentResponse.status_code!=200:
                time.sleep(600)
                createCommentResponse = send_post_request("/comment", json_data=postData)
            else:
                logger.debug(createCommentResponse.text)
                # logger.debug(createCommentResponse.status_code)
                return createCommentResponse.text
        else:
            logger.debug(createCommentResponse.text)
            # logger.debug(createCommentResponse.status_code)
            return createCommentResponse.text
    else:
        logger.debug(createCommentResponse.text)
        # logger.debug(createCommentResponse.status_code)
        return createCommentResponse.text

def PostResponse():
    postData1 = {"username": username, "password_verify": password,
                 "password": password, "show_nsfw": True, "answer": 'Allow Me'}
    postData = {k: v for k, v in postData1.items() if v}
    CreateAccountResponse = send_post_request("/user/register", json_data=postData)
    

def createaccount(username, password, sleep):
    if request.args.get('sleep')==None:
        print('no sleep')
    else:
        time.sleep(int(request.args.get('sleep')))
    postData1 = {"username": username, "password_verify": password,
                 "password": password, "show_nsfw": True, "answer": 'Allow Me'}
    postData = {k: v for k, v in postData1.items() if v}
    CreateAccountResponse = send_post_request("/user/register", json_data=postData)
    if CreateAccountResponse.status_code!=200:
        time.sleep(600)
        CreateAccountResponse = send_post_request("/user/register", json_data=postData)
        if CreateAccountResponse.status_code!=200:
            time.sleep(600)
            CreateAccountResponse = send_post_request("/user/register", json_data=postData)
        else:
            logger.debug(CreateAccountResponse.text)
            logger.debug(CreateAccountResponse.status_code)
            return CreateAccountResponse.text
    else:
        logger.debug(CreateAccountResponse.text)
        logger.debug(CreateAccountResponse.status_code)
        return CreateAccountResponse.text



app = Flask(__name__)

    # if request.args.get('sleep')==None:
    #     print('no sleep')
    # else:
    #     time.sleep(int(request.args.get('sleep')))


@app.route('/')
def index():
    return 'running'

@app.route('/rping')
def rping():
    while True:
        requests.get('https://bakchodi.avosapps.us')
        time.sleep(1500)


@app.route('/log')
def log():
    if request.args.get('sleep')==None:
        print('no sleep')
    else:
        time.sleep(int(request.args.get('sleep')))
    print(request.args.get('sleep'))
    return send_file('log.txt')

@app.route('/getauth')
def getauth():
    if request.args.get('sleep')==None:
        print('no sleep')
    else:
        time.sleep(int(request.args.get('sleep')))
    login_data = {"username_or_email": request.args.get('username'), "password": request.args.get('password')}
    login_data_response = send_post_request("/user/login", json_data=login_data)
    auth = login_data_response.json()["jwt"]
    logger.debug(login_data_response.text)
    return auth


@app.route('/createaccount')
def responseCreateAccount():
    createaccount(username=request.args.get('username'), password=request.args.get('password'), sleep=request.args.get('sleep'))


@app.route('/createpost')
def responsecreatePost():
    #createPost(name, url, body, nsfw, community_id, auth, sleep)
    _thread.start_new_thread(createPost, (request.args.get('name'), request.args.get('url'),request.args.get('body'), request.args.get('nsfw'), request.args.get('community_id'), request.args.get('auth'), request.args.get('sleep'),)) #createPost(name=request.args.get('name'), url=request.args.get('url'), body=request.args.get('body'), nsfw=request.args.get('nsfw'), community_id=request.args.get('community_id'), auth=request.args.get('auth'), sleep=request.args.get('sleep'))


@app.route('/createcomment')
def responseCreateComment():
    _thread.start_new_thread(CreateComment, (request.args.get('content'), request.args.get('post_id'), request.args.get('auth'), request.args.get('sleep'),))    #CreateComment(content=request.args.get('content'), post_id=request.args.get('post_id'), auth=request.args.get('auth'), sleep=request.args.get('sleep'))
    return 'success'

@app.route('/createpostcomment')
#requires id community_id sleep
#createPostResponse.json()['post_view']['post']['id']
def CreatePostComment():
    if request.args.get('sleep')==None:
        print('no sleep')
    else:
        time.sleep(int(request.args.get('sleep')))
    submission=reddit.submission(request.args.get('id'))
    Postresponse=createPost(name=submission.title, url=submission.url, body=request.args.get('body'), nsfw=request.args.get('nsfw'), community_id=request.args.get('community_id'), auth='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjE2OTgsImlzcyI6ImJha2Nob2RpLm9yZyIsImlhdCI6MTY1Njc4MTQzMn0.23iwHhUiE6XQsrNWoi1AqbIJ4lFKbiGprORyE0tEDQs', sleep=1)
    commentsleep=300
    icomment=-1
    try:
      for comment in submission.comments:
        if comment.author=='QualityVote' or comment.author=='AutoModerator' or 'savevideo' in comment.author:
            pass
        else:
            icomment+=1
            old_sleep=commentsleep
            commentsleep=old_sleep + random.randint(300, 500)
            _thread.start_new_thread(CreateComment, (comment.body, Postresponse['post_view']['post']['id'], authid[icomment], commentsleep)) #CreateComment(content=comment.body, post_id=Postresponse, auth=authid[icomment], sleep=commentsleep)
            if icomment == len(authid)-1:
                break
    except Exception as e:
        return e
    return 'succes'


@app.route('/like')
def like(score, post_id, auth):
    if request.args.get('sleep')==None:
        print('no sleep')
    else:
        time.sleep(int(request.args.get('sleep')))
    #   global auth
    postData1 = {"score": int(1), "post_id": int(request.args.get('post_id')), "auth": request.args.get('auth')}
    postData = {k: v for k, v in postData1.items() if v}
    createCommentResponse = send_post_request("/post/like", json_data=postData)
    logger.debug(createCommentResponse.text)
    return createCommentResponse.text    


@app.route('/deletepost')
def DeletePost(post_id, auth):
    if request.args.get('sleep')==None:
        print('no sleep')
    else:
        time.sleep(int(request.args.get('sleep')))
    #   global auth
    postData1 = {"deleted": True, "post_id": int(request.args.get('post_id')), "auth": request.args.get('auth')}
    postData = {k: v for k, v in postData1.items() if v}
    createCommentResponse = send_post_request("/post/delete", json_data=postData)
    logger.debug(createCommentResponse.text)
    return createCommentResponse.text



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


if __name__ == '__main__':
  app.run(debug=True, port=os.getenv("PORT", default=5000))
