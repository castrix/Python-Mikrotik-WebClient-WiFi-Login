from python_mikrotik_login import MikrotikLogin

username="admin"
password="admin"
url="http://10.4.2.1/login" #simulated Mikrotik login page url

login = MikrotikLogin(username, password, url)
login.do_login()
login.check_internet()
print(login)
print(login.speed_test(share=True))
