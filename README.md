# PythonWebclientWifiLogin
This is a python code to login wifi via webclient such as Mikrotik that using encription key which not allow u to login directly via request only. The encription key generated randomly at some time interval, so the first thing you want to do is searching the index of the encription key.
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

The shorcoming of this program is that I still find the encryption key manually by guessing the index
