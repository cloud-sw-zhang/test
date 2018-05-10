''' [PSV-2016-0061] Issue6 FTP Insecure Root Directory   '''
''' anthor Cloud 2017-12-25'''
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
    log.info('step-1 Enable FTP service')
    url = host + urlLogs
    token = getIDToken(url)
    driver = webdriver.Firefox()
    if ProjectName == 'R6300v2' or ProjectName == 'V6510' or ProjectName == 'WNR3500Lv2' or ProjectName == 'R6250' or ProjectName == 'VEGN2610' or ProjectName == 'DGN2200v4' or ProjectName == 'DC112A':
        url = "http://" + user + ':' + passwd + "@" + hostip + '/USB_adv_main.htm'
    elif console_type == 'cable':
        url = "http://" + user + ':' + passwd + "@" + hostip + '/USBAdvRetail.htm'
    else:
        url = "http://" + user + ':' + passwd + "@" + hostip + '/USB_adv_tab.htm'
    driver.get(url)
    time.sleep(15)
    str = driver.find_element_by_name("enable_ftp").is_selected()
    if str == True:
        time.sleep(1)
    else:
        driver.find_element_by_name("enable_ftp").click()
        driver.find_element_by_name("Apply").click()
        time.sleep(15)
    driver.quit()

def test_Step_2():
    log.info( 'step-2 ftp dutip to get system file')
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
            ftp.retrbinary('RETR bftpd.conf',open('bftpd.conf','wb').write)
            result = 'fail'
        except ftplib.error_perm:
            log.info('553 550 errror')
            result = 'pass'
    else:
        s2 = ''
        try:
            s2 = ftp.login(user,'')
        except:
            time.sleep(1)
        if s2 != '':
            ftp.cwd('/')
            ftp.retrlines('LIST')
            try:
                ftp.retrbinary('RETR bftpd.conf',open('bftpd.conf','wb').write)
                result = 'fail'
            except ftplib.error_perm:
                log.info('553 550 errror')
                result = 'pass'
        else:
            log.info('ftp dut fail')
            result = 'pass'
    assert result == 'pass', "This action should work." 
