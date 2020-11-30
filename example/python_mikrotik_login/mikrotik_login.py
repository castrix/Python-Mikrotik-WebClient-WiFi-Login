import requests
from .md5 import md5

#program login wifi via webclient Mikrotik
#by ihsan fajar ramadhan
#https://github.com/castrix
# webclient login code
def mikrotikLogin(username, password, url, minkey1=0, maxkey1=0, minkey2=0, maxkey2=0):
    r= requests.get(url).text #requesting the url text
    key1=""
    key2=""
    if minkey1 == 0 or maxkey1 == 0 or minkey2 == 0 or maxkey2 == 0:
        a="document.sendin.password.value"
        b=r.index(a)
        key1=r[b+len(a)+11:b+len(a)+15]
        key2=r[b+len(a)+52:b+len(a)+116]
    else:
        key1=r[minkey1:maxkey1]
        key2=r[minkey2:maxkey2]
    key1=bytes(key1, "utf-8").decode("unicode_escape") #translating octal characters to char
    key2=bytes(key2, "utf-8").decode("unicode_escape") #translating octal characters to char
    encryptmd5= md5.hexMD5(key1+password+key2) #encrypt the password
    finallogin=url+"?username="+username+"&password="+encryptmd5 #wrap all the variables
    response=requests.post(finallogin).text #make the final requests
    if response.find("connected:") != -1:
        print("Success!")
    else:
        print("Something is wrong!")
        