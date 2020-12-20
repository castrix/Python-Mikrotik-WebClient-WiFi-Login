from python_mikrotik_login import MikrotikLogin

username="ihsan"
password="fajar"
url="https://mikrorikloginexample.ihsanfr.repl.co/login" #working simulated Mikrotik login page url to test the code, change to your url

login = MikrotikLogin(username, password, url)
login.do_login()
login.check_internet()
print(login)
print(login.speed_test(share=True))
