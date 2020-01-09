__all__ = ['md5']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['ii', 'str2binl', 'binl2hex', 'b64MD5', 'safe_add', 'rol', 'b64MD5w', 'hh', 'gg', 'ff', 'binl2b64', 'hexMD5', 'strw2binl', 'cmn', 'coreMD5', 'hexMD5w', 'calcMD5'])
@Js
def PyJsHoisted_safe_add_(x, y, this, arguments, var=var):
    var = Scope({'x':x, 'y':y, 'this':this, 'arguments':arguments}, var)
    var.registers(['msw', 'x', 'y', 'lsw'])
    var.put('lsw', ((var.get('x')&Js(65535))+(var.get('y')&Js(65535))))
    var.put('msw', (((var.get('x')>>Js(16.0))+(var.get('y')>>Js(16.0)))+(var.get('lsw')>>Js(16.0))))
    return ((var.get('msw')<<Js(16.0))|(var.get('lsw')&Js(65535)))
PyJsHoisted_safe_add_.func_name = 'safe_add'
var.put('safe_add', PyJsHoisted_safe_add_)
@Js
def PyJsHoisted_rol_(num, cnt, this, arguments, var=var):
    var = Scope({'num':num, 'cnt':cnt, 'this':this, 'arguments':arguments}, var)
    var.registers(['num', 'cnt'])
    return ((var.get('num')<<var.get('cnt'))|PyJsBshift(var.get('num'),(Js(32.0)-var.get('cnt'))))
PyJsHoisted_rol_.func_name = 'rol'
var.put('rol', PyJsHoisted_rol_)
@Js
def PyJsHoisted_cmn_(q, a, b, x, s, t, this, arguments, var=var):
    var = Scope({'q':q, 'a':a, 'b':b, 'x':x, 's':s, 't':t, 'this':this, 'arguments':arguments}, var)
    var.registers(['x', 'b', 'q', 't', 'a', 's'])
    return var.get('safe_add')(var.get('rol')(var.get('safe_add')(var.get('safe_add')(var.get('a'), var.get('q')), var.get('safe_add')(var.get('x'), var.get('t'))), var.get('s')), var.get('b'))
PyJsHoisted_cmn_.func_name = 'cmn'
var.put('cmn', PyJsHoisted_cmn_)
@Js
def PyJsHoisted_ff_(a, b, c, d, x, s, t, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'c':c, 'd':d, 'x':x, 's':s, 't':t, 'this':this, 'arguments':arguments}, var)
    var.registers(['x', 'd', 'b', 't', 'c', 'a', 's'])
    return var.get('cmn')(((var.get('b')&var.get('c'))|((~var.get('b'))&var.get('d'))), var.get('a'), var.get('b'), var.get('x'), var.get('s'), var.get('t'))
PyJsHoisted_ff_.func_name = 'ff'
var.put('ff', PyJsHoisted_ff_)
@Js
def PyJsHoisted_gg_(a, b, c, d, x, s, t, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'c':c, 'd':d, 'x':x, 's':s, 't':t, 'this':this, 'arguments':arguments}, var)
    var.registers(['x', 'd', 'b', 't', 'c', 'a', 's'])
    return var.get('cmn')(((var.get('b')&var.get('d'))|(var.get('c')&(~var.get('d')))), var.get('a'), var.get('b'), var.get('x'), var.get('s'), var.get('t'))
PyJsHoisted_gg_.func_name = 'gg'
var.put('gg', PyJsHoisted_gg_)
@Js
def PyJsHoisted_hh_(a, b, c, d, x, s, t, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'c':c, 'd':d, 'x':x, 's':s, 't':t, 'this':this, 'arguments':arguments}, var)
    var.registers(['x', 'd', 'b', 't', 'c', 'a', 's'])
    return var.get('cmn')(((var.get('b')^var.get('c'))^var.get('d')), var.get('a'), var.get('b'), var.get('x'), var.get('s'), var.get('t'))
PyJsHoisted_hh_.func_name = 'hh'
var.put('hh', PyJsHoisted_hh_)
@Js
def PyJsHoisted_ii_(a, b, c, d, x, s, t, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'c':c, 'd':d, 'x':x, 's':s, 't':t, 'this':this, 'arguments':arguments}, var)
    var.registers(['x', 'd', 'b', 't', 'c', 'a', 's'])
    return var.get('cmn')((var.get('c')^(var.get('b')|(~var.get('d')))), var.get('a'), var.get('b'), var.get('x'), var.get('s'), var.get('t'))
PyJsHoisted_ii_.func_name = 'ii'
var.put('ii', PyJsHoisted_ii_)
@Js
def PyJsHoisted_coreMD5_(x, this, arguments, var=var):
    var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
    var.registers(['x', 'd', 'b', 'c', 'olda', 'a', 'oldb', 'oldc', 'oldd'])
    var.put('a', Js(1732584193.0))
    var.put('b', (-Js(271733879.0)))
    var.put('c', (-Js(1732584194.0)))
    var.put('d', Js(271733878.0))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('x').get('length')):
        try:
            var.put('olda', var.get('a'))
            var.put('oldb', var.get('b'))
            var.put('oldc', var.get('c'))
            var.put('oldd', var.get('d'))
            var.put('a', var.get('ff')(var.get('a'), var.get('b'), var.get('c'), var.get('d'), var.get('x').get((var.get('i')+Js(0.0))), Js(7.0), (-Js(680876936.0))))
            var.put('d', var.get('ff')(var.get('d'), var.get('a'), var.get('b'), var.get('c'), var.get('x').get((var.get('i')+Js(1.0))), Js(12.0), (-Js(389564586.0))))
            var.put('c', var.get('ff')(var.get('c'), var.get('d'), var.get('a'), var.get('b'), var.get('x').get((var.get('i')+Js(2.0))), Js(17.0), Js(606105819.0)))
            var.put('b', var.get('ff')(var.get('b'), var.get('c'), var.get('d'), var.get('a'), var.get('x').get((var.get('i')+Js(3.0))), Js(22.0), (-Js(1044525330.0))))
            var.put('a', var.get('ff')(var.get('a'), var.get('b'), var.get('c'), var.get('d'), var.get('x').get((var.get('i')+Js(4.0))), Js(7.0), (-Js(176418897.0))))
            var.put('d', var.get('ff')(var.get('d'), var.get('a'), var.get('b'), var.get('c'), var.get('x').get((var.get('i')+Js(5.0))), Js(12.0), Js(1200080426.0)))
            var.put('c', var.get('ff')(var.get('c'), var.get('d'), var.get('a'), var.get('b'), var.get('x').get((var.get('i')+Js(6.0))), Js(17.0), (-Js(1473231341.0))))
            var.put('b', var.get('ff')(var.get('b'), var.get('c'), var.get('d'), var.get('a'), var.get('x').get((var.get('i')+Js(7.0))), Js(22.0), (-Js(45705983.0))))
            var.put('a', var.get('ff')(var.get('a'), var.get('b'), var.get('c'), var.get('d'), var.get('x').get((var.get('i')+Js(8.0))), Js(7.0), Js(1770035416.0)))
            var.put('d', var.get('ff')(var.get('d'), var.get('a'), var.get('b'), var.get('c'), var.get('x').get((var.get('i')+Js(9.0))), Js(12.0), (-Js(1958414417.0))))
            var.put('c', var.get('ff')(var.get('c'), var.get('d'), var.get('a'), var.get('b'), var.get('x').get((var.get('i')+Js(10.0))), Js(17.0), (-Js(42063.0))))
            var.put('b', var.get('ff')(var.get('b'), var.get('c'), var.get('d'), var.get('a'), var.get('x').get((var.get('i')+Js(11.0))), Js(22.0), (-Js(1990404162.0))))
            var.put('a', var.get('ff')(var.get('a'), var.get('b'), var.get('c'), var.get('d'), var.get('x').get((var.get('i')+Js(12.0))), Js(7.0), Js(1804603682.0)))
            var.put('d', var.get('ff')(var.get('d'), var.get('a'), var.get('b'), var.get('c'), var.get('x').get((var.get('i')+Js(13.0))), Js(12.0), (-Js(40341101.0))))
            var.put('c', var.get('ff')(var.get('c'), var.get('d'), var.get('a'), var.get('b'), var.get('x').get((var.get('i')+Js(14.0))), Js(17.0), (-Js(1502002290.0))))
            var.put('b', var.get('ff')(var.get('b'), var.get('c'), var.get('d'), var.get('a'), var.get('x').get((var.get('i')+Js(15.0))), Js(22.0), Js(1236535329.0)))
            var.put('a', var.get('gg')(var.get('a'), var.get('b'), var.get('c'), var.get('d'), var.get('x').get((var.get('i')+Js(1.0))), Js(5.0), (-Js(165796510.0))))
            var.put('d', var.get('gg')(var.get('d'), var.get('a'), var.get('b'), var.get('c'), var.get('x').get((var.get('i')+Js(6.0))), Js(9.0), (-Js(1069501632.0))))
            var.put('c', var.get('gg')(var.get('c'), var.get('d'), var.get('a'), var.get('b'), var.get('x').get((var.get('i')+Js(11.0))), Js(14.0), Js(643717713.0)))
            var.put('b', var.get('gg')(var.get('b'), var.get('c'), var.get('d'), var.get('a'), var.get('x').get((var.get('i')+Js(0.0))), Js(20.0), (-Js(373897302.0))))
            var.put('a', var.get('gg')(var.get('a'), var.get('b'), var.get('c'), var.get('d'), var.get('x').get((var.get('i')+Js(5.0))), Js(5.0), (-Js(701558691.0))))
            var.put('d', var.get('gg')(var.get('d'), var.get('a'), var.get('b'), var.get('c'), var.get('x').get((var.get('i')+Js(10.0))), Js(9.0), Js(38016083.0)))
            var.put('c', var.get('gg')(var.get('c'), var.get('d'), var.get('a'), var.get('b'), var.get('x').get((var.get('i')+Js(15.0))), Js(14.0), (-Js(660478335.0))))
            var.put('b', var.get('gg')(var.get('b'), var.get('c'), var.get('d'), var.get('a'), var.get('x').get((var.get('i')+Js(4.0))), Js(20.0), (-Js(405537848.0))))
            var.put('a', var.get('gg')(var.get('a'), var.get('b'), var.get('c'), var.get('d'), var.get('x').get((var.get('i')+Js(9.0))), Js(5.0), Js(568446438.0)))
            var.put('d', var.get('gg')(var.get('d'), var.get('a'), var.get('b'), var.get('c'), var.get('x').get((var.get('i')+Js(14.0))), Js(9.0), (-Js(1019803690.0))))
            var.put('c', var.get('gg')(var.get('c'), var.get('d'), var.get('a'), var.get('b'), var.get('x').get((var.get('i')+Js(3.0))), Js(14.0), (-Js(187363961.0))))
            var.put('b', var.get('gg')(var.get('b'), var.get('c'), var.get('d'), var.get('a'), var.get('x').get((var.get('i')+Js(8.0))), Js(20.0), Js(1163531501.0)))
            var.put('a', var.get('gg')(var.get('a'), var.get('b'), var.get('c'), var.get('d'), var.get('x').get((var.get('i')+Js(13.0))), Js(5.0), (-Js(1444681467.0))))
            var.put('d', var.get('gg')(var.get('d'), var.get('a'), var.get('b'), var.get('c'), var.get('x').get((var.get('i')+Js(2.0))), Js(9.0), (-Js(51403784.0))))
            var.put('c', var.get('gg')(var.get('c'), var.get('d'), var.get('a'), var.get('b'), var.get('x').get((var.get('i')+Js(7.0))), Js(14.0), Js(1735328473.0)))
            var.put('b', var.get('gg')(var.get('b'), var.get('c'), var.get('d'), var.get('a'), var.get('x').get((var.get('i')+Js(12.0))), Js(20.0), (-Js(1926607734.0))))
            var.put('a', var.get('hh')(var.get('a'), var.get('b'), var.get('c'), var.get('d'), var.get('x').get((var.get('i')+Js(5.0))), Js(4.0), (-Js(378558.0))))
            var.put('d', var.get('hh')(var.get('d'), var.get('a'), var.get('b'), var.get('c'), var.get('x').get((var.get('i')+Js(8.0))), Js(11.0), (-Js(2022574463.0))))
            var.put('c', var.get('hh')(var.get('c'), var.get('d'), var.get('a'), var.get('b'), var.get('x').get((var.get('i')+Js(11.0))), Js(16.0), Js(1839030562.0)))
            var.put('b', var.get('hh')(var.get('b'), var.get('c'), var.get('d'), var.get('a'), var.get('x').get((var.get('i')+Js(14.0))), Js(23.0), (-Js(35309556.0))))
            var.put('a', var.get('hh')(var.get('a'), var.get('b'), var.get('c'), var.get('d'), var.get('x').get((var.get('i')+Js(1.0))), Js(4.0), (-Js(1530992060.0))))
            var.put('d', var.get('hh')(var.get('d'), var.get('a'), var.get('b'), var.get('c'), var.get('x').get((var.get('i')+Js(4.0))), Js(11.0), Js(1272893353.0)))
            var.put('c', var.get('hh')(var.get('c'), var.get('d'), var.get('a'), var.get('b'), var.get('x').get((var.get('i')+Js(7.0))), Js(16.0), (-Js(155497632.0))))
            var.put('b', var.get('hh')(var.get('b'), var.get('c'), var.get('d'), var.get('a'), var.get('x').get((var.get('i')+Js(10.0))), Js(23.0), (-Js(1094730640.0))))
            var.put('a', var.get('hh')(var.get('a'), var.get('b'), var.get('c'), var.get('d'), var.get('x').get((var.get('i')+Js(13.0))), Js(4.0), Js(681279174.0)))
            var.put('d', var.get('hh')(var.get('d'), var.get('a'), var.get('b'), var.get('c'), var.get('x').get((var.get('i')+Js(0.0))), Js(11.0), (-Js(358537222.0))))
            var.put('c', var.get('hh')(var.get('c'), var.get('d'), var.get('a'), var.get('b'), var.get('x').get((var.get('i')+Js(3.0))), Js(16.0), (-Js(722521979.0))))
            var.put('b', var.get('hh')(var.get('b'), var.get('c'), var.get('d'), var.get('a'), var.get('x').get((var.get('i')+Js(6.0))), Js(23.0), Js(76029189.0)))
            var.put('a', var.get('hh')(var.get('a'), var.get('b'), var.get('c'), var.get('d'), var.get('x').get((var.get('i')+Js(9.0))), Js(4.0), (-Js(640364487.0))))
            var.put('d', var.get('hh')(var.get('d'), var.get('a'), var.get('b'), var.get('c'), var.get('x').get((var.get('i')+Js(12.0))), Js(11.0), (-Js(421815835.0))))
            var.put('c', var.get('hh')(var.get('c'), var.get('d'), var.get('a'), var.get('b'), var.get('x').get((var.get('i')+Js(15.0))), Js(16.0), Js(530742520.0)))
            var.put('b', var.get('hh')(var.get('b'), var.get('c'), var.get('d'), var.get('a'), var.get('x').get((var.get('i')+Js(2.0))), Js(23.0), (-Js(995338651.0))))
            var.put('a', var.get('ii')(var.get('a'), var.get('b'), var.get('c'), var.get('d'), var.get('x').get((var.get('i')+Js(0.0))), Js(6.0), (-Js(198630844.0))))
            var.put('d', var.get('ii')(var.get('d'), var.get('a'), var.get('b'), var.get('c'), var.get('x').get((var.get('i')+Js(7.0))), Js(10.0), Js(1126891415.0)))
            var.put('c', var.get('ii')(var.get('c'), var.get('d'), var.get('a'), var.get('b'), var.get('x').get((var.get('i')+Js(14.0))), Js(15.0), (-Js(1416354905.0))))
            var.put('b', var.get('ii')(var.get('b'), var.get('c'), var.get('d'), var.get('a'), var.get('x').get((var.get('i')+Js(5.0))), Js(21.0), (-Js(57434055.0))))
            var.put('a', var.get('ii')(var.get('a'), var.get('b'), var.get('c'), var.get('d'), var.get('x').get((var.get('i')+Js(12.0))), Js(6.0), Js(1700485571.0)))
            var.put('d', var.get('ii')(var.get('d'), var.get('a'), var.get('b'), var.get('c'), var.get('x').get((var.get('i')+Js(3.0))), Js(10.0), (-Js(1894986606.0))))
            var.put('c', var.get('ii')(var.get('c'), var.get('d'), var.get('a'), var.get('b'), var.get('x').get((var.get('i')+Js(10.0))), Js(15.0), (-Js(1051523.0))))
            var.put('b', var.get('ii')(var.get('b'), var.get('c'), var.get('d'), var.get('a'), var.get('x').get((var.get('i')+Js(1.0))), Js(21.0), (-Js(2054922799.0))))
            var.put('a', var.get('ii')(var.get('a'), var.get('b'), var.get('c'), var.get('d'), var.get('x').get((var.get('i')+Js(8.0))), Js(6.0), Js(1873313359.0)))
            var.put('d', var.get('ii')(var.get('d'), var.get('a'), var.get('b'), var.get('c'), var.get('x').get((var.get('i')+Js(15.0))), Js(10.0), (-Js(30611744.0))))
            var.put('c', var.get('ii')(var.get('c'), var.get('d'), var.get('a'), var.get('b'), var.get('x').get((var.get('i')+Js(6.0))), Js(15.0), (-Js(1560198380.0))))
            var.put('b', var.get('ii')(var.get('b'), var.get('c'), var.get('d'), var.get('a'), var.get('x').get((var.get('i')+Js(13.0))), Js(21.0), Js(1309151649.0)))
            var.put('a', var.get('ii')(var.get('a'), var.get('b'), var.get('c'), var.get('d'), var.get('x').get((var.get('i')+Js(4.0))), Js(6.0), (-Js(145523070.0))))
            var.put('d', var.get('ii')(var.get('d'), var.get('a'), var.get('b'), var.get('c'), var.get('x').get((var.get('i')+Js(11.0))), Js(10.0), (-Js(1120210379.0))))
            var.put('c', var.get('ii')(var.get('c'), var.get('d'), var.get('a'), var.get('b'), var.get('x').get((var.get('i')+Js(2.0))), Js(15.0), Js(718787259.0)))
            var.put('b', var.get('ii')(var.get('b'), var.get('c'), var.get('d'), var.get('a'), var.get('x').get((var.get('i')+Js(9.0))), Js(21.0), (-Js(343485551.0))))
            var.put('a', var.get('safe_add')(var.get('a'), var.get('olda')))
            var.put('b', var.get('safe_add')(var.get('b'), var.get('oldb')))
            var.put('c', var.get('safe_add')(var.get('c'), var.get('oldc')))
            var.put('d', var.get('safe_add')(var.get('d'), var.get('oldd')))
        finally:
                var.put('i', Js(16.0), '+')
    return Js([var.get('a'), var.get('b'), var.get('c'), var.get('d')])
PyJsHoisted_coreMD5_.func_name = 'coreMD5'
var.put('coreMD5', PyJsHoisted_coreMD5_)
@Js
def PyJsHoisted_binl2hex_(binarray, this, arguments, var=var):
    var = Scope({'binarray':binarray, 'this':this, 'arguments':arguments}, var)
    var.registers(['hex_tab', 'str', 'i', 'binarray'])
    var.put('hex_tab', Js('0123456789abcdef'))
    var.put('str', Js(''))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<(var.get('binarray').get('length')*Js(4.0))):
        try:
            var.put('str', (var.get('hex_tab').callprop('charAt', ((var.get('binarray').get((var.get('i')>>Js(2.0)))>>(((var.get('i')%Js(4.0))*Js(8.0))+Js(4.0)))&Js(15)))+var.get('hex_tab').callprop('charAt', ((var.get('binarray').get((var.get('i')>>Js(2.0)))>>((var.get('i')%Js(4.0))*Js(8.0)))&Js(15)))), '+')
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    return var.get('str')
PyJsHoisted_binl2hex_.func_name = 'binl2hex'
var.put('binl2hex', PyJsHoisted_binl2hex_)
@Js
def PyJsHoisted_binl2b64_(binarray, this, arguments, var=var):
    var = Scope({'binarray':binarray, 'this':this, 'arguments':arguments}, var)
    var.registers(['str', 'tab', 'i', 'binarray'])
    var.put('tab', Js('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'))
    var.put('str', Js(''))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<(var.get('binarray').get('length')*Js(32.0))):
        try:
            var.put('str', var.get('tab').callprop('charAt', (((var.get('binarray').get((var.get('i')>>Js(5.0)))<<(var.get('i')%Js(32.0)))&Js(63))|((var.get('binarray').get((var.get('i')>>(Js(5.0)+Js(1.0))))>>(Js(32.0)-(var.get('i')%Js(32.0))))&Js(63)))), '+')
        finally:
                var.put('i', Js(6.0), '+')
    return var.get('str')
PyJsHoisted_binl2b64_.func_name = 'binl2b64'
var.put('binl2b64', PyJsHoisted_binl2b64_)
@Js
def PyJsHoisted_str2binl_(str, this, arguments, var=var):
    var = Scope({'str':str, 'this':this, 'arguments':arguments}, var)
    var.registers(['i', 'nblk', 'blks', 'str'])
    var.put('nblk', (((var.get('str').get('length')+Js(8.0))>>Js(6.0))+Js(1.0)))
    var.put('blks', var.get('Array').create((var.get('nblk')*Js(16.0))))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<(var.get('nblk')*Js(16.0))):
        try:
            var.get('blks').put(var.get('i'), Js(0.0))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('str').get('length')):
        try:
            var.get('blks').put((var.get('i')>>Js(2.0)), ((var.get('str').callprop('charCodeAt', var.get('i'))&Js(255))<<((var.get('i')%Js(4.0))*Js(8.0))), '|')
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    var.get('blks').put((var.get('i')>>Js(2.0)), (Js(128)<<((var.get('i')%Js(4.0))*Js(8.0))), '|')
    var.get('blks').put(((var.get('nblk')*Js(16.0))-Js(2.0)), (var.get('str').get('length')*Js(8.0)))
    return var.get('blks')
PyJsHoisted_str2binl_.func_name = 'str2binl'
var.put('str2binl', PyJsHoisted_str2binl_)
@Js
def PyJsHoisted_strw2binl_(str, this, arguments, var=var):
    var = Scope({'str':str, 'this':this, 'arguments':arguments}, var)
    var.registers(['i', 'nblk', 'blks', 'str'])
    var.put('nblk', (((var.get('str').get('length')+Js(4.0))>>Js(5.0))+Js(1.0)))
    var.put('blks', var.get('Array').create((var.get('nblk')*Js(16.0))))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<(var.get('nblk')*Js(16.0))):
        try:
            var.get('blks').put(var.get('i'), Js(0.0))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('str').get('length')):
        try:
            var.get('blks').put((var.get('i')>>Js(1.0)), (var.get('str').callprop('charCodeAt', var.get('i'))<<((var.get('i')%Js(2.0))*Js(16.0))), '|')
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    var.get('blks').put((var.get('i')>>Js(1.0)), (Js(128)<<((var.get('i')%Js(2.0))*Js(16.0))), '|')
    var.get('blks').put(((var.get('nblk')*Js(16.0))-Js(2.0)), (var.get('str').get('length')*Js(16.0)))
    return var.get('blks')
PyJsHoisted_strw2binl_.func_name = 'strw2binl'
var.put('strw2binl', PyJsHoisted_strw2binl_)
@Js
def PyJsHoisted_hexMD5_(str, this, arguments, var=var):
    var = Scope({'str':str, 'this':this, 'arguments':arguments}, var)
    var.registers(['str'])
    return var.get('binl2hex')(var.get('coreMD5')(var.get('str2binl')(var.get('str'))))
PyJsHoisted_hexMD5_.func_name = 'hexMD5'
var.put('hexMD5', PyJsHoisted_hexMD5_)
@Js
def PyJsHoisted_hexMD5w_(str, this, arguments, var=var):
    var = Scope({'str':str, 'this':this, 'arguments':arguments}, var)
    var.registers(['str'])
    return var.get('binl2hex')(var.get('coreMD5')(var.get('strw2binl')(var.get('str'))))
PyJsHoisted_hexMD5w_.func_name = 'hexMD5w'
var.put('hexMD5w', PyJsHoisted_hexMD5w_)
@Js
def PyJsHoisted_b64MD5_(str, this, arguments, var=var):
    var = Scope({'str':str, 'this':this, 'arguments':arguments}, var)
    var.registers(['str'])
    return var.get('binl2b64')(var.get('coreMD5')(var.get('str2binl')(var.get('str'))))
PyJsHoisted_b64MD5_.func_name = 'b64MD5'
var.put('b64MD5', PyJsHoisted_b64MD5_)
@Js
def PyJsHoisted_b64MD5w_(str, this, arguments, var=var):
    var = Scope({'str':str, 'this':this, 'arguments':arguments}, var)
    var.registers(['str'])
    return var.get('binl2b64')(var.get('coreMD5')(var.get('strw2binl')(var.get('str'))))
PyJsHoisted_b64MD5w_.func_name = 'b64MD5w'
var.put('b64MD5w', PyJsHoisted_b64MD5w_)
@Js
def PyJsHoisted_calcMD5_(str, this, arguments, var=var):
    var = Scope({'str':str, 'this':this, 'arguments':arguments}, var)
    var.registers(['str'])
    return var.get('binl2hex')(var.get('coreMD5')(var.get('str2binl')(var.get('str'))))
PyJsHoisted_calcMD5_.func_name = 'calcMD5'
var.put('calcMD5', PyJsHoisted_calcMD5_)
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass


# Add lib to the module scope
md5 = var.to_python()