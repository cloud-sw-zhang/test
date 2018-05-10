'''	[PSV-2018-0054] UPNP Stack Buffer Overflow'''
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
    log.info("step-1 UPNP Stack Buffer should not Overflow.")
    soapaction_header = "urn:NETGEAR-ROUTER:service:#DeviceInfo:1#Reboot"
    headers = {"SOAPACTION": soapaction_header}
    data = "<?xml version=\"1.0\"?>" \
        "<soap:Envelope " \
        "xmlns:soap=\"http://www.w3.org/2003/05/soap-envelope/\" " \
        "soap:encodingStyle=\"http://www.w3.org/2003/05/soap-encoding\"> " \
        "<soap-env:Body> "  \
        "  <m:AddPortMapping xmlns:m=\"urn:schemas-upnp-org:service:WANIPConnection:1\"> " \
        "  <NewPortMappingDescription>" + 'A'*0xe10 + "\xFF</NewPortMappingDescription> "\
        " </m:AddPortMapping> " \
        " </soap-env:Body> " \
        "</soap:envelope>"
    r = ''
    url = "http://" + hostip + ":5000/Public_UPNP_C3"
    try:
        r = requests.post(url, data=data, headers=headers,timeout=5)
    except:
        time.sleep(1)
    if r == '':
        caseresult1 = 'pass'
    else:
        if r.text.find('200') != -1:
            caseresult1 = 'fail'
        else:
            caseresult1 = 'pass'
    assert caseresult1 == 'pass', "This action should not work." 

def test_Step_2():
    log.info( 'step-2 Make sure the Web GUI should not crash')
    url = "http://" + user + ':' + passwd + "@" + hostip + '/' + urlDevicecontrol
    str = check_DUTnocrash(url)
    assert str == 'pass', "This action should work." 