import pyautogui as pyag
import webbrowser as wb
import time
URL = 'https://ucf.zoom.us/j/97658867790?pwd=WXJXVEtxd3pMd1orY2JORkVkQTcvQT09'


def main():
    pyag.screenshot('img/ss.png')
    # Open ZOOM Invite URL and select open in app
    wb.open(URL)
    time.sleep(3)
    pyag.press('left')

    pyag.press('enter')

    # TODO Detect if Login is needed
    # locate the notifaction window
    # Press enter on sign-in
    try:
        time.sleep(2)
        window = pyag.locateCenterOnScreen('img\Sign_in_required_notification.png', grayscale=True, confidence=0.5)
        if window:
            print(window)
            signIn(window)
        else:
            print('not found')
    except PyAutoGUIException:
        print('oh no')
    # Join the meeting ENTER
    time.sleep(5)
    pyag.press('enter')

    # Mute yourself ALT+A
    time.sleep(2)
    pyag.hotkey('alt', 'a')
    print('Hello World')

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
    sso =  pyag.locateCenterOnScreen('img\SSO_signin_option.png', grayscale=True, confidence=0.5)
    pyag.click(sso)
    time.sleep(2)
    
    account = pyag.locateCenterOnScreen('img\account_text_field.png', confidence=0.75)
    pyag.click(account)
    pyag.press('down')
    pyag.press('enter')
    pyag.press('enter')

    time.sleep(1)
    pyag.press('left')
    pyag.press('enter')





if __name__ == '__main__':
    main()