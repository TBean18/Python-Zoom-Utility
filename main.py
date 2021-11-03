import pyautogui as pyag
import webbrowser as wb
import time
URL = 'https://ucf.zoom.us/j/97658867790?pwd=WXJXVEtxd3pMd1orY2JORkVkQTcvQT09'


def main():
    # Open ZOOM Invite URL and select open in app
    wb.open(URL)
    time.sleep(5)
    pyag.press('left')
    pyag.press('enter')

    # Join the meeting ENTER
    time.sleep(5)
    pyag.press('enter')

    # Mute yourself ALT+A
    time.sleep(2)
    pyag.hotkey('alt', 'a')
    print('Hello World')



if __name__ == '__main__':
    main()