from cv2 import log
import pyautogui as pyag
import webbrowser as wb
import time
URL = 'https://ucf.zoom.us/j/97658867790?pwd=WXJXVEtxd3pMd1orY2JORkVkQTcvQT09'


def main():
    # Open ZOOM Invite URL and select open in app
    openZoomLink(URL)
    
    # Best case scenario where the call is opened first try
    if checkAndHandleZoomCall():
        return True
    # Detect if Login is needed
    checkLoginRequirement()

# Function used to check for an opened zoom call
# All Zoom calls open a audio options box before the call is joined (Unless this notification is otherwise disabled)
# Look for the box, if it exists select it, press enter and mute
def checkAndHandleZoomCall():
    audioBox = findAudioBox()
    if audioBox is None:
        return False
    pyag.click(audioBox)
    # pyag.press('enter')
    pyag.hotkey('alt', 'a')
    return True

def findAudioBox():
    return pyag.locateCenterOnScreen('img\Choose_Audio_Box.png', grayscale=True, confidence=0.75)
    

def checkLoginRequirement():
    window = findLoginRequiredWindow()
    if window:
        signIn(window)
    else:
        print('not found')
        print('oh no')

def findLoginRequiredWindow():
   window = pyag.locateCenterOnScreen('img\Sign_in_required_notification.png', grayscale=True, confidence=0.5)
   return window

def openZoomLink(URL):
  wb.open(URL)
  time.sleep(9)   

# Function used to sign in once the signin requirement window has been detected
# window - Sign in requirement window
def signIn(window):
    #Select Window and confirm Signin
    pyag.moveTo(window)
    pyag.click()
    pyag.press('enter')
    time.sleep(1)

    # ! SSO Sign in Option
    signInWithSSO(None)

def signInWithSSO(creds):
    # Try looking for the SSO button
    sso =  pyag.locateCenterOnScreen('img\SSO_signin_option.png', grayscale=True, confidence=0.5)
    if sso:
        pyag.click(sso)
        time.sleep(2)
    else:
        # Button was not found which means that ZOOM had already determined our sign in preferece from a prior session
        # Thus, we should assume that the web browser is open and log the event
        print('SSO Sign-In option NOT found')

    #! Zoom will ask for the SSO Domain
    # ! There is a chance that the sign-in is already stored in memory and not required

    # At this point the SSO 
    attemptUCFSignin(None)

def checkForAutocompletedSignin():
    openZoom = pyag.locateCenterOnScreen('img\Open_Zoom_Meetings_Notification.png', grayscale=True, confidence=0.75)
    # if openZoom:
        # Click on Open Zoom Meetings

# TODO 
def fillOutCompanyDomain():
    print('fillOutCompanyDomain() is WIP')    

def attemptUCFSignin(creds):
    account = pyag.locateCenterOnScreen('img\\account_text_field.png', confidence=0.75)
    pyag.click(account)
    pyag.press('down')
    pyag.press('enter')
    pyag.press('enter')

    # Pop-up message
    time.sleep(1)
    pyag.press('left')
    pyag.press('enter')



if __name__ == '__main__':
    main()