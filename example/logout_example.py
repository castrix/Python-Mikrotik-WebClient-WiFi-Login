from python_mikrotik_login import MikrotikLogin

username="admin"
password="admin"
url="http://10.x.x.x/login" #simulated Mikrotik login page url

login = MikrotikLogin(username, password, url)
login.do_logout()
print(login)