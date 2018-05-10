'''	[PSV-2017-2184] OS command injection via SOAP WAN IP configuration  '''
''' anthor Cloud 2018-01-05'''
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
    log.info('step-1 The vulnerability about OS command injection via SOAP WAN IP configuration.')
    url = host + urlLogs
    token = getIDToken(url)
    cmd1 = '''curl.exe -d "=" -H "User-Agent: SOAP Toolkit 3.0" -H "SOAPAction: urn:NETGEAR-ROUTER:service:ParentalControl:1#Authenticate" -H "Host: ''' + hostip + '''" -H "content-type: text/xml;charset=utf-8" -d @SOAP1.txt http://''' + hostip +''':5000/soap/server_sa/'''
    cmd2 = '''curl.exe -d "=" -H "User-Agent: SOAP Toolkit 3.0" -H "SOAPAction: urn:NETGEAR-ROUTER:service:ParentalControl:1#Authenticate" -H "Host: ''' + hostip + '''" -H "content-type: text/xml;charset=utf-8" -d @SOAP2.txt http://''' + hostip +''':5000/soap/server_sa/'''
    cmd3 = '''curl.exe -d "=" -H "User-Agent: SOAP Toolkit 3.0" -H "SOAPAction: urn:NETGEAR-ROUTER:service:ParentalControl:1#Authenticate" -H "Host: ''' + hostip + '''" -H "content-type: text/xml;charset=utf-8" -d @SOAP3.txt http://''' + hostip +''':5000/soap/server_sa/'''
    log.info('run %s command',cmd1)
    log.info('run %s command',cmd2)
    log.info('run %s command',cmd3)
    p1 = os.popen(cmd1)
    p2 = os.popen(cmd2)
    p3 = os.popen(cmd3)
    str1 = p1.read()
    str2 = p2.read()
    str3 = p3.read()
    log.info(str1)
    log.info(str2)
    log.info(str3)
    if str1.find('401') != -1 and str2.find('401') != -1 and str3.find('401') != -1:
        case = 'pass'
    elif str1 == '' and str2 == '' and str3 == '':
        case = 'pass'
    else:
        case = 'fail'
    assert case == 'pass', "This action should not  work."
