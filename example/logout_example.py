from python_mikrotik_login import MikrotikLogin

username="admin"
password="admin"
url="https://mikrorikloginexample.ihsanfr.repl.co/" #simulated Mikrotik login page url

login = MikrotikLogin(username, password, url)
login.do_logout()
print(login)
