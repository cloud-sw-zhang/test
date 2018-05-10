'''Validation test'''
'''[PSV-2017-0793] Stack overflow in LANG_check_brslang.htm'''
from API._API import *

def test_Step_1():
    token = getIDToken('LANG_check_brslang.htm')
    log.info( 'Step-1: Set browser(Type:STRING, MaxLen:16) as empty')
    post_url = host  + 'langbrscheck.cgi' + token
    post_data = 'brslanguage=&version=5.0+%28Windows+NT+10.0%3B+WOW64%3B+Trident%2F7.0%3B+.NET4.0C%3B+.NET4.0E%3B+.NET+CLR+2.0.50727%3B+.NET+CLR+3.0.30729%3B+.NET+CLR+3.5.30729%3B+rv%3A11.0%29+like+Gecko&browser='
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 200:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
        judje_dutReboot(tmpHTML.text)

    assert tmpHTML.status_code == 200, "This action should work." 

def test_Step_2():
    token = getIDToken('LANG_check_brslang.htm')
    log.info( 'Step-2: Set browser(Type:STRING, MaxLen:16) = 0123456789ABCDEF')
    post_url = host  + 'langbrscheck.cgi' + token
    post_data = 'brslanguage=&version=5.0+%28Windows+NT+10.0%3B+WOW64%3B+Trident%2F7.0%3B+.NET4.0C%3B+.NET4.0E%3B+.NET+CLR+2.0.50727%3B+.NET+CLR+3.0.30729%3B+.NET+CLR+3.5.30729%3B+rv%3A11.0%29+like+Gecko&browser=0123456789ABCDEF'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 200:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
        judje_dutReboot(tmpHTML.text)

    assert tmpHTML.status_code == 200, "This action should work." 

def test_Step_3():
    token = getIDToken('LANG_check_brslang.htm')
    log.info( 'Step-3: Set browser(Type:STRING, MaxLen:16) = 0123456789ABCDEFG')
    post_url = host  + 'langbrscheck.cgi' + token
    post_data = 'brslanguage=&version=5.0+%28Windows+NT+10.0%3B+WOW64%3B+Trident%2F7.0%3B+.NET4.0C%3B+.NET4.0E%3B+.NET+CLR+2.0.50727%3B+.NET+CLR+3.0.30729%3B+.NET+CLR+3.5.30729%3B+rv%3A11.0%29+like+Gecko&browser=0123456789ABCDEFG'
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
