# PythonWebclientWifiLogin
This is a python code to login wifi to Mikrotik Webclient for devices that has no access to GUI. Mikrotik Webclient is using an encription key generated randomly at some time interval, so the first thing you want to do is to search the index of the encription key.
The application of this program is to be used in headless pc such as Raspberry Pi or anything that doesn't have GUI (Linux).
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

The shorcoming of this program is that I still have to find the encryption key manually by guessing the index
