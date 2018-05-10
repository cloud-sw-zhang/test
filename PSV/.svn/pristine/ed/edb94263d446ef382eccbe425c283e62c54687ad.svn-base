'''Validation test'''
'''[PSV-2017-0805] Post-auth RCE: Stack overflow in /fwSchedulePPP2.cgi through "starthour" parameter'''
from API._API import *


def test_Step_1():
    token = getIDToken('FW_schedule_ppp2.htm')
    log.info( 'Step-1: Set starthour(Type:INDEX, MaxLen:2, Range:0~23) = 0')
    post_url = host  + 'fwSchedulePPP2.cgi' + token
    post_data = 'action=Apply&checkboxNameMon=checkboxValue&checkboxNameTue=checkboxValue&checkboxNameWed=checkboxValue&checkboxNameThu=checkboxValue&checkboxNameFri=checkboxValue&checkboxNameSat=checkboxValue&starthour=0&startminute=0&endhour=23&endminute=0&schedule_day=63&schedule_alldayenable=0&schedule_starthour=0&schedule_startminute=0&schedule_endhour=23&schedule_endminute=0&result=apply'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    print tmpHTML.text
    if tmpHTML.status_code == 200:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
        judje_dutReboot(tmpHTML.text)
    assert tmpHTML.status_code == 200, "This action should work."  

def test_Step_2():
    token = getIDToken('FW_schedule_ppp2.htm')
    log.info( 'Step-2: Set starthour(Type:INDEX, MaxLen:2, Range:0~23) = 23')
    post_url = host  + 'fwSchedulePPP2.cgi' + token
    post_data = 'action=Apply&checkboxNameMon=checkboxValue&checkboxNameTue=checkboxValue&checkboxNameWed=checkboxValue&checkboxNameThu=checkboxValue&checkboxNameFri=checkboxValue&checkboxNameSat=checkboxValue&starthour=23&startminute=0&endhour=23&endminute=0&schedule_day=63&schedule_alldayenable=0&schedule_starthour=0&schedule_startminute=0&schedule_endhour=23&schedule_endminute=0&result=apply'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    print tmpHTML.text
    if tmpHTML.status_code == 200:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
        judje_dutReboot(tmpHTML.text)
    assert tmpHTML.status_code == 200, "This action should work."  

def test_Step_3():
    token = getIDToken('FW_schedule_ppp2.htm')
    log.info( 'Step-3: Set starthour(Type:INDEX, MaxLen:2, Range:0~23) = -1')
    post_url = host  + 'fwSchedulePPP2.cgi' + token
    post_data = 'action=Apply&checkboxNameMon=checkboxValue&checkboxNameTue=checkboxValue&checkboxNameWed=checkboxValue&checkboxNameThu=checkboxValue&checkboxNameFri=checkboxValue&checkboxNameSat=checkboxValue&starthour=-1&startminute=0&endhour=23&endminute=0&schedule_day=63&schedule_alldayenable=0&schedule_starthour=0&schedule_startminute=0&schedule_endhour=23&schedule_endminute=0&result=apply'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    print tmpHTML.text
    if tmpHTML.status_code == 400:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
        time.sleep(3)
    else:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 60s")
        judje_dutReboot(tmpHTML.text)
    assert tmpHTML.status_code == 400, "This action should not work." 

def test_Step_4():
    token = getIDToken('FW_schedule_ppp2.htm')
    log.info( 'Step-4: Set starthour(Type:INDEX, MaxLen:2, Range:0~23) = 24')
    post_url = host  + 'fwSchedulePPP2.cgi' + token
    post_data = 'action=Apply&checkboxNameMon=checkboxValue&checkboxNameTue=checkboxValue&checkboxNameWed=checkboxValue&checkboxNameThu=checkboxValue&checkboxNameFri=checkboxValue&checkboxNameSat=checkboxValue&starthour=24&startminute=0&endhour=23&endminute=0&schedule_day=63&schedule_alldayenable=0&schedule_starthour=0&schedule_startminute=0&schedule_endhour=23&schedule_endminute=0&result=apply'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    print tmpHTML.text
    if tmpHTML.status_code == 400:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
        time.sleep(3)
    else:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 60s")
        judje_dutReboot(tmpHTML.text)
    assert tmpHTML.status_code == 400, "This action should not work."     