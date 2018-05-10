'''	
[PSV-2018-0085] Pre-Authenticated Stack Overflow in SOAP Handlers'''
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
    log.info("step-1 BSW_ssid.htm--Netgear's webserver should be responding")
    driver = webdriver.Firefox()
    url = "http://" + user + ':' + passwd + "@" + hostip + '/BSW_ssid.htm'
    driver.get(url)
    time.sleep(15)
    str = driver.page_source
    driver.quit()
    token = re.findall('\?id=[0-9a-z]+',str)
    print token
    if token == []:
        caseresult1 = 'pass'
    else:
        data={'wl0_ssid':'A'*0x62+ 'BBBB'}
        post_url = host + 'bsw_ssid.cgi' + token[0]
        r = ''
        try:
            r = requests.post(post_url, data=data,auth=(user,passwd),timeout=5)
        except:
            time.sleep(1)
        if r == '':
            caseresult1 = 'pass'
        else:
            if r.status_code == 200:
                caseresult1 = 'fail'
            else:
                caseresult1 = 'pass'
    assert caseresult1 == 'pass', "This action should not work." 

def test_Step_2():
    log.info( 'step-2 Make sure the Web GUI should not crash')
    url = "http://" + user + ':' + passwd + "@" + hostip + '/' + urlDevicecontrol
    str = check_DUTnocrash(url)
    assert str == 'pass', "This action should work." 

def test_Step_3():
    log.info("step-3 The UPNP should NOT crash while buffer overflow.")
    soapaction_header = "urn:schemas-upnp-org:service:WLANConfiguration:GetInfo"
    headers = {"SOAPACTION": soapaction_header}
    r = ''
    try:
        r = requests.post("http://" + hostip + ":5000/soap/server_sa",headers=headers,timeout=5)
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

def test_Step_4():
    log.info( 'step-4 Make sure the Web GUI should not crash')
    url = "http://" + user + ':' + passwd + "@" + hostip + '/' + urlDevicecontrol
    str = check_DUTnocrash(url)
    assert str == 'pass', "This action should work." 