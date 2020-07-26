import requests
import  json

url = 'https://httpbin.org/anything'
args = {'msg':'welcomuser','isadmin':'1'}
headers = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X)  AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 Edg/84.0.522.40'}

def sends_post_request():
 reponse = requests.post(url, data=json.dumps(args))
 result = reponse.json()
 with open("../contenu.json", "w") as file:
    json.dump(result, file,indent=4)

def mobile_user():
 req = requests.get(url, headers=headers)
 return req.headers['Content-Type']

sends_post_request()
print('La reponse est : ',mobile_user())
