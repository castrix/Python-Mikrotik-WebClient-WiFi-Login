from python_mikrotik_login import MikrotikLogin

# username="admin"
# password="admin"
# url="http://10.x.x.x/login" #your url
username="ihsan"
password="fajar"
url="https://mikrorikloginexample.ihsanfr.repl.co/login" #working simulated Mikrotik login page url to test the code, change to your url

login = MikrotikLogin(username, password, url)
login.do_login()
print(login)
