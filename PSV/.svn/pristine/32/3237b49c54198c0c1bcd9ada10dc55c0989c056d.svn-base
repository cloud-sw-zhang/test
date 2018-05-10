''' [PSV-2017-0311] Stored XSS in /genie_download_href.htm '''
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
    log.info('step-1 User should NOT pass two security questions to get password for admin')
    if console_type == 'cable':
        print 'This case NA'
        result = 'fail'
        assert result == 'pass', "The function should not work." 
    else:
        url = host + urlLogs
        token = getIDToken(url)
        Authorization = 'Basic ' + base64.b64encode(user + ':' + passwd) 
        headers = {'Authorization': Authorization}
        data = {
            'adownload_desktop_genie':'alert`1`',
            'download_readyshare' : 'alert`2`' ,
        }
        if console_type == 'cable':
            post_url = host + 'goform/genieDownload' + token
        else:
            post_url = host + 'genieDownload.cgi' + token
        r = requests.post(post_url, data=data,timeout=5)
        get_url = host + 'genie_download_href.htm' 
        tmpHTML = requests.get(get_url,auth=(user,passwd))
        assert tmpHTML.text.find('ReadySHARE') != -1, "The function should not work." 
  