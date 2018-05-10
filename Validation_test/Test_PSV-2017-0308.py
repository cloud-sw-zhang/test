'''Validation test'''
'''[PSV-2017-0308] Stack overflow in fwLog.cgi through "log_refresh" parameter and others (RCE)'''
from API._API import *
def test_step_0():
    log.info( 'Step-0-0 DUT loaddrfault wait 160s')
    aploaddefault()
    log.info( "Step-0-1 AP Genie over leap done")
    Genie_overleap()
    log.info( "Step-0-2 disable changed-url token")
    Disable_changedToken()
    
def test_Step_1():
    token = getIDToken('FW_log.htm')
    log.info('Step-1: Set log_refresh(Type:BOOL, MaxLen:1, Range:0-1) = 0')
    post_url = host  + 'fwLog.cgi' + token
    post_data = 'action_Refresh=Refresh&log_detail=&log_cat_1=checkboxValue&log_cat_2=checkboxValue&log_cat_3=checkboxValue&log_cat_4=checkboxValue&log_cat_5=checkboxValue&log_cat_6=checkboxValue&log_cat_7=checkboxValue&log_cat_8=checkboxValue&log_cat_9=checkboxValue&log_cat_10=checkboxValue&email_on=0&log_refresh=0&log_send=0&log_clear=0&log_enable=111&log_filter=65535'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 200:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
        judje_dutReboot(tmpHTML.text)
    assert tmpHTML.status_code == 200, "This action should work." 

def test_Step_2():
    token = getIDToken('FW_log.htm')
    log.info( 'Step-2: Set log_refresh(Type:BOOL, MaxLen:1, Range:0-1) = 1')
    post_url = host  + 'fwLog.cgi' + token
    post_data = 'action_Refresh=Refresh&log_detail=&log_cat_1=checkboxValue&log_cat_2=checkboxValue&log_cat_3=checkboxValue&log_cat_4=checkboxValue&log_cat_5=checkboxValue&log_cat_6=checkboxValue&log_cat_7=checkboxValue&log_cat_8=checkboxValue&log_cat_9=checkboxValue&log_cat_10=checkboxValue&email_on=0&log_refresh=1&log_send=0&log_clear=0&log_enable=111&log_filter=65535'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 200:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
        judje_dutReboot(tmpHTML.text)
    assert tmpHTML.status_code == 200, "This action should work."

def test_Step_3():
    token = getIDToken('FW_log.htm')
    log.info( 'Step-3: Set log_refresh(Type:BOOL, MaxLen:1, Range:0-1) = 2')
    post_url = host  + 'fwLog.cgi' + token
    post_data = 'action_Refresh=Refresh&log_detail=&log_cat_1=checkboxValue&log_cat_2=checkboxValue&log_cat_3=checkboxValue&log_cat_4=checkboxValue&log_cat_5=checkboxValue&log_cat_6=checkboxValue&log_cat_7=checkboxValue&log_cat_8=checkboxValue&log_cat_9=checkboxValue&log_cat_10=checkboxValue&email_on=0&log_refresh=2&log_send=0&log_clear=0&log_enable=111&log_filter=65535'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 400:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
        time.sleep(3)
    else:
        log.info( tmpHTML.status_code)
        log.info( "Action Successful, sleep 60s")
        judje_dutReboot(tmpHTML.text)
    assert tmpHTML.status_code == 400, "This action should not work." 

def test_Step_4():
    token = getIDToken('FW_log.htm')
    log.info( 'Step-4: Set log_refresh(Type:BOOL, MaxLen:1, Range:0-1) = -1')
    post_url = host  + 'fwLog.cgi' + token
    post_data = 'action_Refresh=Refresh&log_detail=&log_cat_1=checkboxValue&log_cat_2=checkboxValue&log_cat_3=checkboxValue&log_cat_4=checkboxValue&log_cat_5=checkboxValue&log_cat_6=checkboxValue&log_cat_7=checkboxValue&log_cat_8=checkboxValue&log_cat_9=checkboxValue&log_cat_10=checkboxValue&email_on=0&log_refresh=-1&log_send=0&log_clear=0&log_enable=111&log_filter=65535'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 400:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
        time.sleep(3)
    else:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 60s")
        judje_dutReboot(tmpHTML.text)
    assert tmpHTML.status_code == 400, "This action should not work." 
