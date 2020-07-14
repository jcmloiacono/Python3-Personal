from instapy_cli import client
import ssl
from instagram_private_api import Client, ClientCompatPatch

ssl._create_default_https_context = ssl._create_unverified_context

username = 'jcmartinez1702' #your username
password = 'jc14891419' #your password 
image = 'Hi_instagram.png' #here you can put the image directory
text = 'Here you can put your caption for the post'

with client(username, password) as cli:
   cli.upload(image, text)