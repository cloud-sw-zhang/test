''' [PSV-2017-0328] UnAuthenticated Access to Router Debug Logs    '''
''' anthor Cloud 2017-12-08'''
'''v1.0 '''

from API._API import *

#def test_step_0():
    #log.info( 'step-0-0 dut loaddrfault wait 160s')
    #aploaddefault()
    #log.info( "step-0-1 AP Genie over leap done")
    #Genie_overleap()
#    log.info( "step-0-2 disable changed-url token")
#    Disable_changedToken()

def test_Step_1():
    log.info('step-1 All pages cannot access in both LAN/WAN interface without authorized.')
    if hostip == '192.168.0.1':
        if ProjectName == 'C7000-100NAS':
            cmd = '"curl.exe" http://192.168.0.1/NETGEAR_C7000-100NAS-Console.log'
        elif ProjectName == 'C6300-100NAS':
            cmd = '"curl.exe" http://192.168.0.1/retail_link_file.log'
        elif ProjectName == 'CM500V':
            cmd = '"curl.exe" http://192.168.0.1/NETGEAR_CM500V-Config.log?captureLogOption=0'
        elif ProjectName == 'C3700-100NAS':
            cmd = '"curl.exe" http://192.168.0.1/NETGEAR_C3700-100NAS-Config.log?captureLogOption=0'
        elif ProjectName == 'CM400' or ProjectName == 'CM700':
            cmd = '"curl.exe" http://192.168.0.1/retail_link_file.log'
        else:
            cmd = '"curl.exe" http://192.168.0.1/debug_log.zip'
    elif hostip == '192.168.100.1':
        cmd = '"curl.exe" http://192.168.100.250/debug_log.zip'
    elif hostip == '192.168.1.250':
        cmd = '"curl.exe" http://192.168.1.250/debug_log.zip'
    else:
        cmd = '"curl.exe" http://192.168.1.1/debug_log.zip'
    log.info('run %s command',cmd)
    p1 = os.popen(cmd)
    str = p1.read()
    if str.find('401') != -1 or str == '':
        case = 'pass'
    else:
        case = 'fail'
    log.info(str)
    assert case == 'pass',"This action should not work." 
