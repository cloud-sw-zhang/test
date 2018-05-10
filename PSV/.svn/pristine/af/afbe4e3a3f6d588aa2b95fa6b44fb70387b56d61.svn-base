''' [PSV-2017-0389] Debug Functionality Left on Device  '''
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
    log.info('step-1 Several debug pages have been left in the web root for the WNDR4500v3 management console. These pages can be used to enable telnet')
    if console_type == 'cable':
        print 'This case NA'
        case = 'fail'
    else:
        url = host + urlLogs
        token = getIDToken(url)
        url1 = host + 'debug_detail.htm'
        url2 = host + 'debug.htm'
        url3 = host + 'debug_run.htm'
        r1 = requests.get(url1,auth=(user,passwd))
        r2 = requests.get(url2,auth=(user,passwd))
        r3 = requests.get(url3,auth=(user,passwd))
        log.info(r1.status_code)
        log.info(r2.status_code)
        log.info(r3.status_code)
        
        if r1.status_code == 404:
            case1 = 'NA'
        else:
            driver = webdriver.Firefox()
            httpurl = "http://" + user + ':' + passwd + "@" + hostip + '/debug_detail.htm'
            driver.get(httpurl)
            time.sleep(15)
            driver.find_element_by_name("action_Enable_Telnet").click()
            time.sleep(5)
            driver.quit()
            case1 = 'pass'
        if r2.status_code == 404:
            case2 = 'NA'
        else:
            driver = webdriver.Firefox()
            httpurl = 'http://' + user + ':' + passwd + '@' + hostip + '/debug.htm'
            driver.get(httpurl)
            time.sleep(15)
            driver.find_element_by_name("action_Enable_Telnet").click()
            time.sleep(5)
            driver.quit()
            case2 = 'pass'
        if r3.status_code == 404:
            case3 = 'NA'
        else:
            driver = webdriver.Firefox()
            httpurl = "http://" + user + ':' + passwd + "@" + hostip + + '/debug_run.htm'
            driver.get(httpurl)
            time.sleep(15)
            driver.find_element_by_name("action_Enable_Telnet").click()
            time.sleep(5)
            driver.quit()
            case3 = 'pass'
        if case1 == 'NA' and case2 == 'NA' and case3 == 'NA':
            case = 'NA'
        else:
            case = 'pass'
    assert case == 'pass', "The function should not work." 

def test_Step_2():
    log.info( 'step-2 check telnet service is enabled?')
    if console_type == 'cable':
        print 'This case NA'
        case = 'fail'
    else:
        tn = ''
        try:
            tn = telnetlib.Telnet(hostip,telnetport,timeout=10)
            log.info(tn)
        except:
            print tn
        if tn != '':
            for i in range(1,5):
                str1 = tn.read_some()
                log.info(str1)
                if str1.find('login:') != -1:
                    case = 'pass'
                    break
                elif str1.find('#') != -1:
                    case = 'fail'
                    break
                elif str1.find('Password:') != -1:
                    case = 'fail'
                    break
                else:
                    case = 'pass'
        else:
            case = 'pass'
    assert case == 'pass', "This action should not work."  