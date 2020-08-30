import os
from selenium import webdriver
import speech_recognition as sr


def openChrome(word):
    """ Run """
    chromedriver_path = r'chromedriver.exe'
    os.environ['webdriver.chrome.driver'] = chromedriver_path
    browser = webdriver.Chrome(chromedriver_path)
    browser.get('https://www.youtube.com/results?search_query=' + word)
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
        print("You said " + command)
        if command.startswith("open"):
            second_word = command.split()[1]
            openChrome(second_word)

    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))


if __name__ == "__main__":
    recognizeAudio()
