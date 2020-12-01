from python_mikrotik_login import mikrotikLogin


username="ihsan"
password="fajar"
url="https://python-mikrotik-webclient-wifi-login.ihsanfr.repl.co/login" # simulated Mikrotik login page url change this

mikrotikLogin(username, password, url)
# you can set the salt index manually (if the pattern is different) or leave it empty
# minkey1=2625 # optional minimum index of the first unique encryption key
# maxkey1=2629 # optional maximum index of the first unique encryption key
# minkey2=2666 # optional minimum index of the second unique encryption key
# maxkey2=2730 # optional maximum index of the second unique encryption key
# mikrotikLogin(username, password, url, minkey1, maxkey1, minkey2, maxkey2)

