#!/usr/bin/python

from selenium import webdriver
import signal
import sys
import time


def main():
    url = 'https://messages.google.com/web'
    driver = webdriver.Firefox(executable_path='PATH/TO/GECKODRIVER')
    driver.get(url)


def handler(signal, frame):
    print(" was pressed. Exiting gracefully...\n")
    sys.exit(0)


if __name__ == '__main__':
    try:
        main()
        signal.signal(signal.SIGINT, handler)
        print('Running. Press CTRL-C to exit. \n')
        while True:
            pass
    except Exception as e:
        print(e)
    finally:
        time.sleep(2)
        print('Done running Messages for web.\n')