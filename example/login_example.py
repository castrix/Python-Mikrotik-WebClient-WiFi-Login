from python_mikrotik_login import MikrotikLogin

# username="admin"
# password="admin"
# url="http://10.x.x.x/login" #simulated Mikrotik login page url
username="ihsan"
password="fajar"
url="https://mikrorikloginexample.ihsanfr.repl.co/login" #You can test the package with this url

login = MikrotikLogin(username, password, url)
login.do_login()
print(login)
