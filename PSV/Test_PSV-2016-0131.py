''' [PSV-2016-0131] Server Side Request Forgery In download_url      '''
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
    log.info('step-1 Netgear Downloader,select type as FTP/HTTP,ENTER the download link,click add to see if the lan server file can be downloader')
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
        #    driver.find_element_by_link_text("ADVANCED").click()
        driver.find_element_by_xpath("//li[2]/a/span").click()
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
                if hostip == '192.168.0.1':
                    str = "ftp://192.168.0.88/bug.JPG"
                else:
                    str = "ftp://192.168.1.88/bug.JPG"
                driver.find_element_by_name("fh_url").clear()
                driver.find_element_by_name('fh_url').send_keys(str)
                driver.find_element_by_name('add_task').click()
                time.sleep(15)
                str2 = ''
                try:
                    str2 = driver.find_element_by_xpath("//tr[2]/td[7]").get_attribute('value')
                    sec = driver.switch_to.alert
                    sec.accept()
                except:
                    time.sleep(1)
                time.sleep(5)
                driver.quit()
                if str2.find('0.0') == -1 or str2 == '':
                    log.info('can not download file--pass')
                    result = 'pass'
                else:
                    log.info('can download file--fail')
                    result = 'fail'
            else:
                driver.quit()
                log.info('can not detect USB')
                result = 'fail'
        else:
            log.info('no NETGEAR Downloader (BETA) page')
            result = 'pass'
    assert result == 'pass', "This action should work." 
