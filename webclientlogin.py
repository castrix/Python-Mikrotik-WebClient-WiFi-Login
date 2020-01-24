import requests
from md5 import md5

#program login wifi via webclient Mikrotik
#by ihsan fajar ramadhan
#https://github.com/castrix

def webClientLogin(username, password, minkey1, maxkey1, minkey2, maxkey2, url):
    r= requests.get(url).text #requesting the url text
    key1=""
    key2=""
    for i in range(minkey1, maxkey1): #6 characters, grabbing the first encription key, you should find the index yourself
        key1 = key1+r[i]
    for i in range(minkey2, maxkey2): #66 characters, grabbing the second encription key
        key2 = key2+r[i]
    key1=bytes(key1, "utf-8").decode("unicode_escape") #translating octal characters to char
    key2=bytes(key2, "utf-8").decode("unicode_escape") #translating octal characters to char
    encryptmd5= md5.hexMD5(key1+password+key2) #encrypt the password
    finallogin=url+"username="+username+"&password="+encryptmd5 #wrap all the variables
    requests.post(finallogin) #make the final requests
