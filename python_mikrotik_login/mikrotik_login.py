import requests
from .md5 import md5
import urllib.request as urllib2
from urllib.parse import urlparse
import speedtest
import json

# program login wifi via webclient Mikrotik
# Contributors Ihsan Fajar Ramadhan, Marchel-Ace
# https://github.com/castrix, https://github.com/Marchel-Ace
# webclient login code


class MikrotikLogin:
    def __init__(self, username: str,
                 password: str, url: str,
                 minkey1: int = 0, maxkey1: int = 0,
                 minkey2: int = 0, maxkey2: int = 0) -> None:
        """
        you can set the salt index manually (if the pattern is different) or leave it empty
        minkey1=2625 # optional minimum index of the first unique encryption key
        maxkey1=2629 # optional maximum index of the first unique encryption key
        minkey2=2666 # optional minimum index of the second unique encryption key
        maxkey2=2730 # optional maximum index of the second unique encryption key

        """
        self.username = username
        self.password = password
        self.url = url
        self.minkey1 = minkey1
        self.maxkey1 = maxkey1
        self.minkey2 = minkey2
        self.maxkey2 = maxkey2
        self.is_connected = False
        self.is_logged_in = False

    def do_login(self):
        """
        you know what does it mean~
        """
        if self.check_login_status():
            print("Already logged in!")
            return True
        r = requests.get(self.url).text  # requesting the url text
        key1 = ""
        key2 = ""
        if self.minkey1 == 0 or self.maxkey1 == 0 or self.minkey2 == 0 or self.maxkey2 == 0:
            a = "document.sendin.password.value"
            try:
                b = r.index(a)
            except:
                print("Error, url format is not right. Please make sure you use the right url format: http://url/login")
                return False
            key1 = r[b+len(a)+11:b+len(a)+15]
            key2 = r[b+len(a)+52:b+len(a)+116]
        else:
            key1 = r[self.minkey1:self.maxkey1]
            key2 = r[self.minkey2:self.maxkey2]
        # translating octal characters to char
        key1 = bytes(key1, "utf-8").decode("unicode_escape")
        # translating octal characters to char
        key2 = bytes(key2, "utf-8").decode("unicode_escape")
        # encrypt the password
        encryptmd5 = md5.hexMD5(key1+self.password+key2)
        finallogin = self.url+"?username="+self.username + \
            "&password="+encryptmd5  # wrap all the variables
        response = requests.post(finallogin).text  # make the final requests
        print("Logging in ...")
        if self.check_login_status():
            print("Success! Logged in.")
            self.check_internet()
            return True
        else:
            print("Something is wrong!")
            print("Please make sure you use the right url format: http://url/login")
            return False

    def do_logout(self):
        """
        you know what does it mean~
        """
        url = urlparse(self.url)
        final_url = f'{url.scheme}://{url.netloc}/logout'
        req = requests.get(final_url)
        print("Logging out ...")
        if self.check_login_status():
            print("Something is wrong!")
            return True
        else:
            print("Success! Logged out.")
            self.check_internet()
            return False

    def check_login_status(self):
        """
        Check login status, will return True if authenticated and False if not
        """
        url = urlparse(self.url)
        final_url = f'{url.scheme}://{url.netloc}/status'
        req = requests.get(final_url)
        if 'status' in req.url:
            self.is_logged_in = True
            return True
        else:
            self.is_logged_in = False
            return False

    def check_internet(self):
        """
        Check internet connection, will return True
        if internet connection is detected and False if not
        """
        print("Checking internet connection ...")
        try:
            response = urllib2.urlopen('http://216.58.192.142', timeout=1)
            self.is_connected = True
            return True
        except Exception as e:
            print("error")
            print(e)
            self.is_connected = False
            return False

    def speed_test(self, share=False):
        """
        set share True if you want
        get image of your speedtest result
        """
        status = {}
        if self.check_internet():
            s = speedtest.Speedtest()
            s.get_best_server()
            s.download()
            s.upload()
            if share:
                status['share_url'] = s.results.share()
            results_dict = s.results.dict()
            status['download'] = results_dict['download']
            status['upload'] = results_dict['upload']
            del s
            return status
        else:
            status['status'] = "No internet connection"
            return status

    def __repr__(self) -> str:
        return json.dumps({
            'logged_in': self.is_logged_in,
            'internet_connection': self.is_connected
        })