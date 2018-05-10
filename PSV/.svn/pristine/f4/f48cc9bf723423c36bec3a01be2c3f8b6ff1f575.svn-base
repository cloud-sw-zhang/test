''' [PSV-2016-0106] RCE in Downloader     '''
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
    log.info('step-1 The XSS injection code should NOT be executed')
    if console_type == 'cable':
        print 'This case NA'
        result = 'NA'
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
            driver = webdriver.Firefox()
            url = "http://" + user + ':' + passwd + "@" + hostip + '/Download_manager.htm'
            driver.get(url)
            try:
                str1 = ''
                sec = driver.switch_to.alert
                str1 = sec.text
                sec.accept()
            except:
                time.sleep(1)
            if str1 == '':
                driver.find_element_by_name("enable_netgear_downloader").click()
                time.sleep(5)
                driver.find_element_by_id('selType').find_elements_by_tag_name('option')[0].click()
                driver.find_element_by_name("fh_url").clear()
                driver.find_element_by_name('fh_url').send_keys("http://example.org/'$(reboot) [^]")
                driver.find_element_by_name('add_task').click()
                time.sleep(5)
                driver.quit()
                result = 'pass'
                log.info('In FTP/HTTP Download Link,enter the following: http://example.org/$(reboot) [^], to check dut if reboot')
            else:
                driver.quit()
                log.info('can not detect USB')
                result = 'fail'
        else:
            result = 'pass'
            log.info('no NETGEAR Downloader (BETA) page')
    assert result == 'pass', "This action should work." 

def test_Step_2():
    log.info( 'step-2 Make sure the Web GUI should not reboot')
    if console_type == 'cable':
        print 'This case NA'
        str = 'NA'
    else:
        url = "http://" + user + ':' + passwd + "@" + hostip + '/' + urlDevicecontrol
        str = check_DUTnocrash(url)
    assert str == 'pass', "This action should work." 