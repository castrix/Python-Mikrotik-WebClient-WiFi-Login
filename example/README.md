# Python Mikrotik WebClient WiFi Login
This is a python code to login to wifi Mikrotik Webclient for devices that has no access to GUI (such as headless Raspberry Pi, or Linux Terminal). Mikrotik Webclient is using unique keys or salts generated randomly at some time interval, this program is made to find that unique keys or salts and combine it with username and password to make final login request.

## Installing the package
        pip install python-mikrotik-login

## Using the program
### First import the module
        from python_mikrotik_login import mikrotikLogin
        
        mikrotikLogin("username","password","http://url") #you can leave the unique key index empty or set it manually

### Arguments
        mikrotikLogin(username_string, password_string, url_string, minkey1_integer_optional, maxkey1_integer_optional, minkey2_integer_optional, maxkey2_integer_optional)

## How this works
This code works by finding the unique key from the Mikrotik Web Client and then combine it with username and password then send back the `post` request to the Mikrotik Web Client.
### Finding the unique key
For the example this is the function where the login action is fired:

        function doLogin() {
        document.sendin.username.value = document.login.username.value;
        document.sendin.password.value = hexMD5('\340' + document.login.password.value + '\043\242\062\374\062\365\062\266\201\323\145\251\200\303\025\315');
        document.sendin.submit();
        return false;
        }

In this case you should find the index of:

        \340
        and
        \043\242\062\374\062\365\062\266\201\323\145\251\200\303\025\315

where:

        \340 is the first unique key or salt
        \043\242\062\374\062\365\062\266\201\323\145\251\200\303\025\315 is the second unique key salt