import webclientlogin as w

username="your username"
password="your password"
minkey1=2625 # optional minimum index of the first unique encryption key
maxkey1=2629 # optional maximum index of the first unique encryption key
minkey2=2666 # optional minimum index of the second unique encryption key
maxkey2=2730 # optional maximum index of the second unique encryption key
url="http://loginpage.com/login" # Mikrotik login url

# you can set the index manually or leave it empty
# w.webClientLogin(username, password, url, minkey1, maxkey1, minkey2, maxkey2)

w.webClientLogin(username, password, url)
