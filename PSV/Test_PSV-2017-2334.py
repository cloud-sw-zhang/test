'''	[PSV-2017-2334] dnslookup.cgi Remote Command Execution '''
''' anthor Cloud 2018-01-03'''
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
    log.info("step-1 dnslookup.cgi Remote Command Execution ")
    log.info('judje Diagnostics page exist?')
    if console_type == 'cable':
        url = host + 'Diagnostics.htm'
    else:
        url = host + urlLogs
    token = getIDToken(url)
    if console_type == 'cable':
        get_url = host + 'Diagnostics.htm'
    else:
        get_url = host + 'DIAG_diag.htm'
    r = requests.get(get_url,auth=(user,passwd))
    log.info(r.status_code)
    if r.status_code == 404 or r.status_code == 401:
        case = 'pass'
        log.info( "The page not exist in DUT-NA")
    else:
        Authorization = 'Basic ' + base64.b64encode(user + ':' + passwd) 
        headers = {
            'Host': hostip,
            'Cache-Control': 'max-age=0',
            'Authorization': Authorization,
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',
        }
        if console_type == 'cable':
            data = 'buttonHit=cfAlert_Apply&buttonValue=Start%20Test&cfAlert_Apply=Start%20Test&DiagnosticUtility=0&ip_type=ipv4&PingDestinationIP1=192&PingDestinationIP2=168&PingDestinationIP3=0&PingDestinationIP4=12%3Breboot&PingDestinationIPv6=&PingSize=64&NumberOfPings=3&TimeBetweenPings=1000&TracerouteHost=&TracerouteMaxHops=30&TracerouteDataSize=32&TracerouteBasePort=33434&TracerouteResolveHost=0&PingToolStatus=%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%0D%0APinging%20192.168.0.12%20with%2064%20bytes%20of%20data%3A%5BComplete%5D%0D%0A3%2F3%20replies%20received.%0D%0Amin%20time%3D1%20ms%2C%20max%20time%3D1%20ms%2C%20avg%20time%3D1%20ms%0D%0A%0D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20&UtilityCommand=1&lan_ipaddr=192.168.0.1&PingDest_ipaddr=192.168.0.12&PingDestinationIP=192.168.0.12|/reset'
            post_url = host + 'goform/Diagnostics'
        else:
            data = 'IPAddr1=a&IPAddr2=b&IPAddr3=c&IPAddr4=d&ping=xxxx&ping_IPAddr=|/usr/sbin/telnetd -p 90 -l /bin/sh'
            post_url = host + 'dnslookup.cgi'
        r = ''
        try:
            r = requests.post(post_url, headers=headers, data=data,timeout=5)
        except:
            time.sleep(1)
        print r
        if r != '':
            if console_type == 'cable':
                if r.status_code == 401:
                    log.info(r)
                    log.info( "The function or page should not exist in DUT-NA")
                    time.sleep(3)
                    case = 'pass'
                else:
                    log.info(r)
                    log.info( "The function or page should not exist in DUT-fail")
                    judje_dutReboot(r.text)
                    case = 'fail'
            else:
                if r.status_code == 404:
                    log.info(r)
                    log.info( "The function or page should not exist in DUT-NA")
                    time.sleep(3)
                    case = 'pass'
                else:
                    log.info(r)
                    log.info( "The function or page should not exist in DUT-fail")
                    judje_dutReboot(r.text)
                    case = 'fail'
        else:
            case = 'pass'
    assert case == 'pass', "This action should not work." 
