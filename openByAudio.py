import os
from selenium import webdriver
import speech_recognition as sr


def openChrome():
    """ Run """
    print("test")
    chromedriver_path = r'chromedriver.exe'
    os.environ['webdriver.chrome.driver'] = chromedriver_path
    browser = webdriver.Chrome(chromedriver_path)
    browser.get('https://www.youtube.com/results?search_query=rembetiko')
    ##link_elem = browser.find_element_by_link_text('Οικονομία')
    # link_elem.click()
    # browser.quit()


def recognizeAudio():
    # get audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        if command == "open":
            openChrome()
        # switcher.get(command)
        print("You said " + command)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))


def open():
    openChrome()

# switcher = {
#     "open": open(),
# }


if __name__ == "__main__":
    recognizeAudio()
