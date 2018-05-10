'''	[PSV-2018-0053] Multiple Post-Authentication Stack Buffer Overflows'''
''' anthor Cloud 2018-01-03'''
'''v1.0 '''

from API._API import *
def test_Step_1():
    log.info("step-1 STR_add.htm--Netgear's webserver should be responding")
    driver = webdriver.Firefox()
    url = "http://" + user + ':' + passwd + "@" + hostip + '/STR_add.htm'
    driver.get(url)
    time.sleep(15)
    str = driver.page_source
    driver.quit()
    token = re.findall('\?id=[0-9a-z]+',str)
    print token
    if token == []:
        caseresult1 = 'pass'
    else:
        data={'route_name':'A'*0x800+'\x00\x49\xe0\xd0'+'\x00\x49\xe1\xb2'+'B'*0x24+'\xde\xad\xbe\xef'}
        post_url = host + 'routinfo.cgi' + token[0]
        r = ''
        try:
            r = requests.post(post_url, data=data,auth=(user,passwd),timeout=5)
        except:
            time.sleep(1)
        print 'r=',r
        if r == '':
            caseresult1 = 'pass'
        else:
            if r.text.find('200') != -1:
                caseresult1 = 'fail'
            else:
                caseresult1 = 'pass'
    assert caseresult1 == 'pass', "This action should not work." 

def test_Step_2():
    log.info("step-2 STR_routes.htm--Netgear's webserver should be responding")
    driver = webdriver.Firefox()
    url = "http://" + user + ':' + passwd + "@" + hostip + '/STR_routes.htm'
    driver.get(url)
    time.sleep(15)
    str = driver.page_source
    driver.quit()
    token = re.findall('\?id=[0-9a-z]+',str)
    print token
    if token == []:
        caseresult1 = 'pass'
    else:
        data={'Edit':'Edit', 'select':'A'*0x820+'\xde\xad\xbe\xef'}
        post_url = host + 'routinfo.cgi' + token[0]
        r = ''
        try:
            r = requests.post(post_url, data=data,auth=(user,passwd),timeout=5)
        except:
            time.sleep(1)
        print 'r=',r
        if r == '':
            caseresult1 = 'pass'
        else:
            if r.text.find('200') != -1:
                caseresult1 = 'fail'
            else:
                caseresult1 = 'pass'
    assert caseresult1 == 'pass', "This action should not work." 

def test_Step_3():
    log.info("step-3 DEV_device.htm--Netgear's webserver should be responding")
    driver = webdriver.Firefox()
    url = "http://" + user + ':' + passwd + "@" + hostip + '/DEV_device.htm'
    driver.get(url)
    time.sleep(15)
    str = driver.page_source
    driver.quit()
    token = re.findall('\?id=[0-9a-z]+',str)
    print token
    if token == []:
        caseresult1 = 'pass'
    else:
        data={'refresh':'A'*0x804+'\xde\xad\xbe\xef'}
        post_url = host + 'routinfo.cgi' + token[0]
        r = ''
        try:
            r = requests.post(post_url, data=data,auth=(user,passwd),timeout=5)
        except:
            time.sleep(1)
        print 'r=',r
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