''' [PSV-2017-0740] dnslookup.cgi Remote Command Execution  '''
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
    log.info('step-1 DUT should Not excute the sheel command(reboot) by request HTTP packet')
    if console_type == 'cable':
        url = host + 'Diagnostics.htm'
    else:
        url = host + urlLogs
    token = getIDToken(url)
    Authorization = 'Basic ' + base64.b64encode(user + ':' + passwd) 
    headers = {'Authorization': Authorization}
    if console_type == 'cable':
        data = 'buttonHit=cfAlert_Apply&buttonValue=Start+Test&cfAlert_Apply=Start+Test&DiagnosticUtility=1&ip_type=ipv4&PingDestinationIP1=192&PingDestinationIP2=168&PingDestinationIP3=0&PingDestinationIP4=10&PingDestinationIPv6=&PingSize=64&NumberOfPings=3&TimeBetweenPings=1000&TracerouteHost=tw.yahoo.com%3Breboot&TracerouteMaxHops=30&TracerouteDataSize=32&TracerouteBasePort=33434&TracerouteResolveHost=0&PingToolStatus=++++++++++++++++++++++++++++++++++++++++++++++++++++++++Waiting+for+input...++++++%0D%0A%0D%0A++++++++++++++++++++++++++++++++++++++++++++++++++++&UtilityCommand=1&lan_ipaddr=192.168.0.1&PingDest_ipaddr=192.168.0.10&PingDestinationIP='
        if ProjectName == ' C6300':
            post_url = host + 'cgi-bin/Diagnostics.cgi' + token
        else:
            post_url = host + 'goform/Diagnostics' + token
    else:
        data='lookup=Lookup&host_name=www.google.com; reboot'
        post_url = host + 'dnslookup.cgi' + token
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