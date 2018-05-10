'''[PSV-2017-2124] Unauthorized File Operation    '''
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
    log.info('step-1 Openning FTP port 21 for USB storage is easy to be exploited by attacker to generate or destroy files under directory /tmp')
    driver = webdriver.Firefox()
    if ProjectName == 'R6300v2' or ProjectName == 'V6510' or ProjectName == 'WNR3500Lv2' or ProjectName == 'VEGN2610' or ProjectName == 'R6250' or ProjectName == 'DGN2200v4' or ProjectName == 'DC112A':
        url = "http://" + user + ':' + passwd + "@" + hostip + '/USB_adv_main.htm'
    elif console_type == 'cable':
        url = "http://" + user + ':' + passwd + "@" + hostip + '/USBAdvRetail.htm'
    else:  
        url = "http://" + user + ':' + passwd + "@" + hostip + '/USB_adv_tab.htm'
    driver.get(url)
    time.sleep(15)
    str = driver.find_element_by_name("enable_ftp").is_selected()
    if str == False:
        driver.find_element_by_name("enable_ftp").click()
        driver.find_element_by_name("Apply").click()
        time.sleep(20)
    else:
        time.sleep(2)
    driver.quit()

def test_Step_2():
    log.info( 'step-2 ftp dut to make test file')
    log.info('ftp %s',hostip)
    s1 = ''
    ftp = FTP()
    try:
        ftp.connect(hostip,'21')
        s1 = ftp.login(user,passwd)
        log.info(ftp.getwelcome())
    except:
        time.sleep(1)
    if s1 != '':
        ftp.cwd('/')
        ftp.retrlines('LIST')
        try:
            ftp.retrlines('mkdir test_dir1')
            ftp.retrlines('mkdir test_dir2')
            ftp.retrlines('ls')
            ftp.retrlines('rm test_dir1')
        except:
            log.info('create file fail')
    else:
        s2 = ''
        try:
            s2 = ftp.login(user,'')
        except:
            time.sleep(1)
        if s2 != '':
            ftp.cwd('/')
            ftp.retrlines('LIST')
            ftp.cwd('/')
            ftp.retrlines('LIST')
            try:
                ftp.retrlines('mkdir test_dir1')
                ftp.retrlines('mkdir test_dir2')
                ftp.retrlines('ls')
                ftp.retrlines('rm test_dir1')
            except:
                log.info('create file fail')
        else:
            s3 = ''
            try:
                s3 = ftp.login('','')
            except:
                time.sleep(1)
            if s3 != '':
                ftp.cwd('/')
                ftp.retrlines('LIST')
                ftp.cwd('/')
                ftp.retrlines('LIST')
                try:
                    ftp.retrlines('mkdir test_dir1')
                    ftp.retrlines('mkdir test_dir2')
                    ftp.retrlines('ls')
                    ftp.retrlines('rm test_dir1')
                except:
                    log.info('create file fail')
            else:
                log.info('ftp dut fail')

def test_Step_3():
    log.info( 'step-3 Check temp file in console')
    sendCommandAndGetReturn('com1','cd /tmp')
    str = sendCommandAndGetReturn('com1','ls')
    assert str.find('test_dir2') == -1, "This action should not work."