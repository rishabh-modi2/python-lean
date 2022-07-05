import time, praw, _thread, requests, logging, time, sys, datetime, os, random, re
from datetime import datetime
from flask import Flask, jsonify, request, send_file
from flask import render_template
# from flask_sockets import Sockets
# from leancloud import LeanCloudError
# log_file = open("log.txt", "a+")
http_base_url = "https://bakchodi.org/api/v3"
#http_base_url = "https://lemmy.rishabh.gq/api/v3"
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
auth_terimaaka='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjE5NDgsImlzcyI6ImJha2Nob2RpLm9yZyIsImlhdCI6MTY1Njg1OTE1Mn0.jfBfP4zHjhKGLM0T2e7czL6kNtiJgCWwT8_73yDNt4o'
auth_Khalif='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjE5NDUsImlzcyI6ImJha2Nob2RpLm9yZyIsImlhdCI6MTY1Njg1OTE1NH0.Ij6q6ATblltOj43gshmCO7ZX9eXLNZTfh5e9XjHAsKM'
auth_RamKhan='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjE5NDYsImlzcyI6ImJha2Nob2RpLm9yZyIsImlhdCI6MTY1Njg1OTE1N30.Kmb28kZcVMlP0MF-AffsJMYz0H5b2KEaT10MUa0-N8c'
auth_LibranduHuMAI=  'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjE5NDcsImlzcyI6ImJha2Nob2RpLm9yZyIsImlhdCI6MTY1Njg1OTE1OX0.AgFQIoDIgoj246pDdgyBZaNRinaHj--kIbvEjTDN_I0'
auth_BhenchodBUlla='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjE5NDksImlzcyI6ImJha2Nob2RpLm9yZyIsImlhdCI6MTY1Njg1OTE2MX0.poGc2K2sa_zg0JxrWoaJHCvif3irop3GUwBkbulMpEE'
raw_authid = [auth_Khalif, auth_RamKhan, auth_LibranduHuMAI, auth_BhenchodBUlla, auth_terabaaphu, auth_tujhekya, auth_manushya, auth_Gaddarmusalman, auth_Buddhu, auth_Csk_raja, auth_Dangerous_bhaiya, auth_Comedy_cex, auth_Baaphutera, auth_MaiKyuBatau]
raw_auth1id = [auth_Khalif, auth_RamKhan, auth_LibranduHuMAI, auth_BhenchodBUlla, auth_terabaaphu, auth_tujhekya, auth_manushya, auth_Gaddarmusalman, auth_Buddhu, auth_Csk_raja, auth_Dangerous_bhaiya, auth_Comedy_cex, auth_Baaphutera, auth_MaiKyuBatau]
raw_auth2id = [auth_Khalif, auth_RamKhan, auth_LibranduHuMAI, auth_BhenchodBUlla, auth_terabaaphu, auth_tujhekya, auth_manushya, auth_Gaddarmusalman, auth_Buddhu, auth_Csk_raja, auth_Dangerous_bhaiya, auth_Comedy_cex, auth_Baaphutera, auth_MaiKyuBatau]
raw_auth3id = [auth_Khalif, auth_RamKhan, auth_LibranduHuMAI, auth_BhenchodBUlla, auth_terabaaphu, auth_tujhekya, auth_manushya, auth_Gaddarmusalman, auth_Buddhu, auth_Csk_raja, auth_Dangerous_bhaiya, auth_Comedy_cex, auth_Baaphutera, auth_MaiKyuBatau]
raw_auth4id = [auth_Khalif, auth_RamKhan, auth_LibranduHuMAI, auth_BhenchodBUlla, auth_terabaaphu, auth_tujhekya, auth_manushya, auth_Gaddarmusalman, auth_Buddhu, auth_Csk_raja, auth_Dangerous_bhaiya, auth_Comedy_cex, auth_Baaphutera, auth_MaiKyuBatau]
raw_auth5id = [auth_Khalif, auth_RamKhan, auth_LibranduHuMAI, auth_BhenchodBUlla, auth_terabaaphu, auth_tujhekya, auth_manushya, auth_Gaddarmusalman, auth_Buddhu, auth_Csk_raja, auth_Dangerous_bhaiya, auth_Comedy_cex, auth_Baaphutera, auth_MaiKyuBatau]
raw_auth6id = [auth_Khalif, auth_RamKhan, auth_LibranduHuMAI, auth_BhenchodBUlla, auth_terabaaphu, auth_tujhekya, auth_manushya, auth_Gaddarmusalman, auth_Buddhu, auth_Csk_raja, auth_Dangerous_bhaiya, auth_Comedy_cex, auth_Baaphutera, auth_MaiKyuBatau]
aa1id='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjgsImlzcyI6Im15ZG9tYWluLm1sIiwiaWF0IjoxNjU2OTAxNzA4fQ.ngO4BI9Wl6wUlBBzCgJ3DsD5dtouRnpARkSYJgas2zU'
aa2id='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjksImlzcyI6Im15ZG9tYWluLm1sIiwiaWF0IjoxNjU2OTAxNzEwfQ.M_mXudrZ9mLrVJMZYapaEnXKD90NK-56l0RdXrQpn9k'
aa3id='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjEwLCJpc3MiOiJteWRvbWFpbi5tbCIsImlhdCI6MTY1NjkwMTcxMX0.l61Es2MKAm36WNjnN1cY2Zm6OukYAKGqeR3MJ-ecKlY'
aa4id='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjExLCJpc3MiOiJteWRvbWFpbi5tbCIsImlhdCI6MTY1NjkwMTcxM30.2hJVQ91rFoPwCwQ6KMylsaouvp3ThtloTpb-ksNPkOU'
aa5id='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjEyLCJpc3MiOiJteWRvbWFpbi5tbCIsImlhdCI6MTY1NjkwMTcxNH0.pydvSbuC5b97aeaLB4dBbRHRDLyW0GX_9QvW7U4_7YU'
aa6id='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjEzLCJpc3MiOiJteWRvbWFpbi5tbCIsImlhdCI6MTY1NjkwMTcxNn0.d0itC5eZheJj6wpvzwKPXFn9Jye7gEJ4APJnQ899KlU'
aa7id='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjE0LCJpc3MiOiJteWRvbWFpbi5tbCIsImlhdCI6MTY1NjkwMTcxN30.xBB-HMCt4kmVRHd4t18q6ZfHlZOr0FKeP3eNAR3i1pY'
a8id='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjE1LCJpc3MiOiJteWRvbWFpbi5tbCIsImlhdCI6MTY1NjkwMTc2M30.hpj_FbHvDKAufWZNa2Kh5SVhMNUBemBfkmmDDS6qH0M'
a9id='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjE2LCJpc3MiOiJteWRvbWFpbi5tbCIsImlhdCI6MTY1NjkwMTc2NX0.NoAdAkvr53LZn2G2hroqjjQIpzObpi0oMkhVhjHBPUI'
a10id='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjI3LCJpc3MiOiJteWRvbWFpbi5tbCIsImlhdCI6MTY1NjkwMjA1M30.7JWzNdY-JJBJw4oKZCabYEENYOn-Nmjdn6Nq7hczeY4'
a11id='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjI4LCJpc3MiOiJteWRvbWFpbi5tbCIsImlhdCI6MTY1NjkwMjA1NX0.A7L6IrrzzmlV7Po-HUuzd7WcbcLr0K2iGz_PYlxlhM0'
a12id='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjI5LCJpc3MiOiJteWRvbWFpbi5tbCIsImlhdCI6MTY1NjkwMjA1Nn0.E94qb9v8dQHj34spg_GPcaPFl0C8uKvKOwv09JSevU4'
a13id='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjMwLCJpc3MiOiJteWRvbWFpbi5tbCIsImlhdCI6MTY1NjkwMjA1OH0.qMlsRr6oDR9FrCZjVJ5V1NkO2uR6pYdhKQNTsfAYGbI'
a14id='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjMxLCJpc3MiOiJteWRvbWFpbi5tbCIsImlhdCI6MTY1NjkwMjA2MH0.ow2DMS6WF_4SLF8Ibti-TkYiU6mwi6i7dcsBYn35qR4'
a15id='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjMyLCJpc3MiOiJteWRvbWFpbi5tbCIsImlhdCI6MTY1NjkwMjA2MX0.D9kKUEV0hR5JNiChbuvTsgpJ6P7EoJEj2UFM-oWYfmE'
a16id='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjMzLCJpc3MiOiJteWRvbWFpbi5tbCIsImlhdCI6MTY1NjkwMjA2M30.5eZX-i9jRt7egBANhTnByEuhgYjKmSE4lp-BoQdTJos'
#authid=[a16id, a15id, a14id, a13id, a12id, a11id, a10id, aa1id, aa2id, aa3id, aa4id, aa5id, aa6id, aa7id, a8id, a9id]
#raw_authid=[a16id, a15id, a14id, a13id, a12id, a11id, a10id, aa1id, aa2id, aa3id, aa4id, aa5id, aa6id, aa7id, a8id, a9id]
#raw_auth1id=[a16id, a15id, a14id, a13id, a12id, a11id, a10id, aa1id, aa2id, aa3id, aa4id, aa5id, aa6id, aa7id, a8id, a9id]
#raw_auth2id=[a16id, a15id, a14id, a13id, a12id, a11id, a10id, aa1id, aa2id, aa3id, aa4id, aa5id, aa6id, aa7id, a8id, a9id]
#raw_auth3id=[a16id, a15id, a14id, a13id, a12id, a11id, a10id, aa1id, aa2id, aa3id, aa4id, aa5id, aa6id, aa7id, a8id, a9id]
#auth4id=[a16id, a15id, a14id, a13id, a12id, a11id, a10id, aa1id, aa2id, aa3id, aa4id, aa5id, aa6id, aa7id, a8id, a9id]
#auth5id=[a16id, a15id, a14id, a13id, a12id, a11id, a10id, aa1id, aa2id, aa3id, aa4id, aa5id, aa6id, aa7id, a8id, a9id]


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



def CreateComment(content, post_id, auth, sleep, parent_id=None):
    if sleep==None:
        print('no sleep')
    else:
        time.sleep(int(sleep))
    postData1 = {"content":content, "post_id":int(post_id), "auth": auth, "parent_id":parent_id}
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
                return createCommentResponse
        else:
            logger.debug(createCommentResponse.text)
            # logger.debug(createCommentResponse.status_code)
            return createCommentResponse
    else:
        logger.debug(createCommentResponse.text)
        # logger.debug(createCommentResponse.status_code)
        return createCommentResponse


    

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

def CreatePostComment(id, community_id, sleep):
    print('ok')
    if sleep==None:
        print('no sleep')
    else:
        time.sleep(int(sleep))
    submission=reddit.submission(id)
    Postresponse=createPost(name=submission.title, url=submission.url, body=None, nsfw=None, community_id=community_id, auth=random.choice(authid), sleep=0)
    print(Postresponse['post_view']['post']['id'])
    commentsleep=300
    commentsleep=0
    icomment=-1
    try:
        for comment in submission.comments:
            print('comment')
            if comment.author=='QualityVote' or comment.author=='AutoModerator':
                pass
            else:
                icomment+=1
                old_sleep=commentsleep
                commentsleep=old_sleep + random.randint(300, 1000)
                #Postresponse['post_view']['post']['id']
                _thread.start_new_thread(CreateComment, (comment.body, Postresponse['post_view']['post']['id'], authid[icomment], commentsleep)) #CreateComment(content=comment.body, post_id=Postresponse, auth=authid[icomment], sleep=commentsleep)
                if icomment == len(authid)-1:
                    break
    except Exception as e:
        print(e)
        return e


def OldCreatePostCommentTree(id, community_id, sleep):
    if sleep==None:
        print('no sleep')
    else:
        time.sleep(int(sleep))
    submission=reddit.submission(id)
    authid=random.sample(raw_authid, len(raw_authid))
    Postresponse=createPost(name='test3', url=submission.url, body=None, nsfw=None, community_id=community_id, auth=authid.pop(), sleep=0)
    commentsleep=300
    icomment=-1
    for comment in submission.comments:
            comment_sleep=300+random.randint(100, 3600)
            if re.search("removed|deleted|removed|reddit|AutoMod|mod", comment.body):
                # print('mod')
                pass
            else:
                useauthid=authid.pop()
                response = CreateComment(content=comment.body, post_id=Postresponse['post_view']['post']['id'], auth=useauthid, sleep=comment_sleep)
                parent_id=int(response.json()['comment_view']['comment']['id'])
                #_thread.start_new_thread(CreateComment, (comment.body, Postresponse['post_view']['post']['id'], authid[icomment], commentsleep))
                auth2id=random.sample(raw_auth2id, len(raw_auth2id))
                comment.refresh()
                replies=comment.replies
                if len(replies) > 0:
                    for comment in replies:
                        comment_1_sleep=300+random.randint(100, 3600)
                        try:
                            useauth2id=auth2id.pop()
                            response = CreateComment(content=comment.body, post_id=Postresponse['post_view']['post']['id'], parent_id=parent_id, auth=useauth2id, sleep=comment_1_sleep)
                            parent2_id=int(response.json()['comment_view']['comment']['id'])
                        except Exception as e:
                            print(e)
                        auth3id=random.sample(raw_auth3id, len(raw_auth3id))
                        comment.refresh()
                        replies=comment.replies
                        if len(replies) > 0:
                            for comment in replies:
                                comment_2_sleep=300+random.randint(100, 3600)
                                try:
                                    useauth3id=auth3id.pop()
                                    response = CreateComment(content=comment.body, post_id=Postresponse['post_view']['post']['id'], parent_id=parent2_id, auth=useauth3id, sleep=comment_2_sleep)
                                    # parent_id=int(response.json()['comment_view']['comment']['id'])
                                except Exception as e:
                                    print(e)
                                
                if icomment == len(authid)-1:
                    break

    # CreatePostCommentTree('uugknd', 2, 0)


def CreateCommentTree(id, post_id, sleep):
    try:
        print('ok')
        if sleep==None:
            print('no sleep')
        else:
            time.sleep(int(sleep))
        submission=reddit.submission(id)
        authid=random.sample(raw_authid, len(raw_authid))
        useauth=authid.pop()
        # Postresponse=createPost(name=submission.title, url=submission.url, body=None, nsfw=None, community_id=community_id, auth=useauth, sleep=0)
        # post_id=Postresponse['post_view']['post']['id']
        print(int(post_id))
        for comment in submission.comments:
            _thread.start_new_thread(TopLevelComment, (comment, post_id, authid.pop(),))
    except Exception as e:
        print(e)
        pass

def CreatePostCommentTree(id, community_id, sleep):
    try:
        print('ok')
        if sleep==None:
            print('no sleep')
        else:
            time.sleep(int(sleep))
        submission=reddit.submission(id)
        authid=random.sample(raw_authid, len(raw_authid))
        useauth=authid.pop()
        Postresponse=createPost(name=submission.title, url=submission.url, body=None, nsfw=None, community_id=community_id, auth=useauth, sleep=0)
        post_id=Postresponse['post_view']['post']['id']
        print(int(post_id))
        for comment in submission.comments:
            _thread.start_new_thread(TopLevelComment, (comment, post_id, authid.pop(),))
    except Exception as e:
        print(e)
        pass
        # return e

q='hi'
def TopLevelComment(comment, post_id, useauthid):
    time.sleep(random.randint(10, 300))
    if q:
    try:
        comment_sleep=300+random.randint(10, 700)
        # print(comment.author)
        if re.search("removed|deleted|reddit|bot|r/|reddit|AutoMod|mod", comment.body):
            pass
        else:
#            useauthid=authid.pop()
            response = CreateComment(content=comment.body, post_id=post_id, auth=useauthid, sleep=comment_sleep)
            if response.status_code==200:
                parent_id=int(response.json()['comment_view']['comment']['id'])
                print(parent_id)
                _thread.start_new_thread(LevelComment, (comment, post_id, parent_id, useauthid,))
    except Exception as e:
        print(e)
        pass
    

def LevelComment(topcomment, post_id, parent1_id, useauthid):
    if q:
    try:
        auth2id=random.sample(raw_auth2id, len(raw_auth2id))
        auth2id.remove(useauthid)
        topcomment.refresh()
        replies=topcomment.replies
        if len(replies) > 0:
            for secondcomment in replies:
                    comment_1_sleep=300+random.randint(100, 650)
                # try:
                    useauth2id=auth2id.pop()
                    response = CreateComment(content=secondcomment.body, post_id=post_id, parent_id=parent1_id, auth=useauth2id, sleep=comment_1_sleep)
                    if response.status_code==200:
                        parent2_id=int(response.json()['comment_view']['comment']['id'])
                        _thread.start_new_thread(LevelComment, (secondcomment, post_id, parent2_id, useauth2id))
                # except Exception as e:
                #     print(e)
    except Exception as e:
        print(e)
        pass


def ThirdLevelComment(secondcomment, post_id, parent2_id):
    # try:
        auth3id=random.sample(raw_auth3id, len(raw_auth3id))
        secondcomment.refresh()
        replies=secondcomment.replies
        if len(replies) > 0:
            for thirdcomment in replies:
                    comment_3_sleep=300+random.randint(100, 200)
                # try:
                    useauth3id=auth3id.pop()
                    response = CreateComment(content=thirdcomment.body, post_id=post_id, parent_id=parent2_id, auth=useauth3id, sleep=comment_3_sleep)
                    parent3_id=int(response.json()['comment_view']['comment']['id'])
                # except Exception as e:
                #     print(e)
    # except Exception as e:
    #     print(e)
    
# CreatePostCommentTree('vodlyq', 'community_id', 1)
    

print('starting')

app = Flask(__name__)

    # if request.args.get('sleep')==None:
    #     print('no sleep')
    # else:
    #     time.sleep(int(request.args.get('sleep')))


@app.route('/')
def index():
    return render_template('index.html')
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

@app.route('/reload')
def reload():
   r = requests.get("https://gitlab.com/rishabh-modi2/public/-/raw/main/bapi.py")
   open('app.py', 'wb').write(r.content)
   return "reloaded"


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
def responseCreatePostComment():
    _thread.start_new_thread(CreatePostComment, (request.args.get('id'), request.args.get('community_id'), request.args.get('sleep'),))
    return 'success' + request.args.get('sleep')


@app.route('/createpostcommenttree')
def responseCreatePostCommenTree():
    _thread.start_new_thread(CreatePostCommentTree, (request.args.get('id'), request.args.get('community_id'), request.args.get('sleep'),))
    return 'success' + request.args.get('sleep')

@app.route('/createcommenttree')
def responseCreateCommenTree():
    _thread.start_new_thread(CreateCommentTree, (request.args.get('id'), request.args.get('post_id'), request.args.get('sleep'),))
    return 'success' + request.args.get('sleep')


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
  app.run(debug=True, port=os.getenv("PORT", default=5001))
