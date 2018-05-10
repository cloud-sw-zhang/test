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
    log.info('step-1 Buffer overflow attack')
    if console_type == 'cable':
        url = host + 'Diagnostics.htm'
    else:
        url = host + urlLogs
    token = getIDToken(url)
    Authorization = 'Basic ' + base64.b64encode(user + ':' + passwd) 
    headers = {'Authorization': Authorization}
    if console_type == 'cable':
        data = 'buttonHit=cfAlert_Apply&buttonValue=Start%20Test&cfAlert_Apply=Start%20Test&DiagnosticUtility=0&ip_type=ipv4&PingDestinationIP1=192&PingDestinationIP2=168&PingDestinationIP3=0&PingDestinationIP4=10&PingDestinationIPv6=&PingSize=64&NumberOfPings=3&TimeBetweenPings=1000&TracerouteHost=&TracerouteMaxHops=30&TracerouteDataSize=32&TracerouteBasePort=33434&TracerouteResolveHost=0&PingToolStatus=%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%0D%0APinging%2010.7.5.10%20with%2064%20bytes%20of%20data%3A%5BComplete%5D%0D%0AReply%20from%2010.7.5.10%3A%20bytes%20%3D%2064%2C%20time%20%3D%2011%20ms%0D%0AReply%20from%2010.7.5.10%3A%20bytes%20%3D%2064%2C%20time%20%3D%2013%20ms%0D%0AReply%20from%2010.7.5.10%3A%20bytes%20%3D%2064%2C%20time%20%3D%206%20ms%0D%0A3%2F3%20replies%20received.%0D%0Amin%20time%3D6%20ms%2C%20max%20time%3D13%20ms%2C%20avg%20time%3D10%20ms%0D%0A%0D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20&UtilityCommand=1&lan_ipaddr=192.168.0.1&PingDest_ipaddr=10.7.5.10%3B%20reboot&PingDestinationIP=192.168.0.10%3B%20reboot'
        post_url = host + 'goform/Diagnostics' + token
    else:
        data = 'IPAssr1=12&IPAddr2=12ping=Ping&IPAddr4=12&ping_IPAddr=12.12.12.12;reboot'
        post_url = host + 'ping.cgi' + token
    r = ''
    try:
        r = requests.post(post_url, headers=headers, data=data,timeout=5)
    except:
        time.sleep(1)
    if r != '':
        log.info(r.text)
        if console_type == 'cable':
            assert r.status_code == 401, "The function or page should not exist in DUT." 
        else:
            assert r.status_code == 404, "The function or page should not exist in DUT." 
    else:
        assert r == '', "The function or page should not exist in DUT." 

def test_Step_2():
    log.info( 'step-2 Make sure the Web GUI should not reboot')
    url = "http://" + user + ':' + passwd + "@" + hostip + '/' + urlDevicecontrol
    str = check_DUTnocrash(url)
    assert str == 'pass', "This action should work." 