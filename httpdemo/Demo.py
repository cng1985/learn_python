import requests

def basic():
  request=requests.get("http://www.yingjobs.com")
  print(request.status_code)
  print(request.text)
def params():
  data = {'no':'ada',"password":"123456"}
  request = requests.post('http://trip.haoxuer.com/rest/user/login.htm', params=data )  
  json=request.json()
  print(json["code"])
  print(json["userToken"])
params()
