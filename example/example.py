import webclientlogin as w

username="your username"
password="your password"
minkey1=2625 #minimum index of the first encryption key
maxkey1=2629 #maximum index of the first encryption key
minkey2=2666 #minimum index of the second encryption key
maxkey2=2730 #maximum index of the second encryption key
url="\login.html" #this should be url, the login.html file is just for you to test the index of the encryption key

w.webClientLogin(username, password, minkey1, maxkey1, minkey2, maxkey2, url)
