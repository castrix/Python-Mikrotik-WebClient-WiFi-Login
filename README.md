# PythonWebclientWifiLogin
This is a python code to login to wifi Mikrotik Webclient for devices that has no access to GUI (such as headless Raspberry Pi, or Linux Terminal). Mikrotik Webclient is using an encription key generated randomly at some time interval, so the first thing you want to do is to search the index of the encription key.

## Finding the unique key
For the example this is the encription key of Mikrotik webclient:

        function doLogin() {
        document.sendin.username.value = document.login.username.value;
        document.sendin.password.value = hexMD5('\340' + document.login.password.value + '\043\242\062\374\062\365\062\266\201\323\145\251\200\303\025\315');
        document.sendin.submit();
        return false;
        }

In this case you should find the index of:

        document.sendin.password.value = hexMD5('\340' + document.login.password.value + '\043\242\062\374\062\365\062\266\201\323\145\251\200\303\025\315');
        
especially:

        '\340' + document.login.password.value + '\043\242\062\374\062\365\062\266\201\323\145\251\200\303\025\315'
where:

        '\340' is the first key
        '\043\242\062\374\062\365\062\266\201\323\145\251\200\303\025\315' is the second key

## Using the program
### First import the module
        import webclientlogin as w
        
        w.webClientLogin("username","password","http://url") #you can leave the unique key index empty or set it manually

### Arguments
        webClientLogin(username_string, password_string, url_string, minkey1_integer_optional, maxkey1_integer_optional, minkey2_integer_optional, maxkey2_integer_optional)
