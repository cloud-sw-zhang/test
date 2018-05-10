''' [PSV-2016-0061] Issue5: Gearguy/Geardog Telnet Backdoor  '''
''' anthor Cloud 2017-12-07'''
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
    log.info('step-1 Run telnetenable.exe <host ip> <host mac> <user name> <password>')
    if console_type == 'cable':
        print 'This case NA'
    else:
        url = host + urlLogs
        token = getIDToken(url)
        if ProjectName == 'Orbi':
            str1 = sendCommandAndGetReturn(com,'nvram get et1macaddr')
            str2 = str1.split('\n' ,)[1].split('\r' ,)[0] 
            str3 = str2.split(':' ,)
            hostmac = str3[0] + str3[1] + str3[2] + str3[3] + str3[4] + str3[5]
        else:
            hostmac = '00D0591A2B3B'
        cmd = '"telnetenable.exe" ' + hostip + ' '+ hostmac + ' ' + user + ' ' + passwd
        print cmd
        log.info(cmd)
        p = os.popen(cmd)
        str = p.read()

def test_Step_2():
    log.info( 'step-2 check telnet dut')
    if console_type == 'cable':
        print 'This case NA'
        str2 = 'NA'
    else:
        str2 = judjeduttelnet()
        if str2 == 'pass':
            log.info(str2)
            log.info( "check telnet dut pass")
            time.sleep(1)
        else:
            log.info(str2)
            log.info( "check telnet dut fail")
    assert str2 == 'pass', "This action should work." 
