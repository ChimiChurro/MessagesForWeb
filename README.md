# MessagesForWeb
**Automatically open up google's Messages for web from the terminal to send/receive texts from your computer using Selenium and Firefox.**

The only requirements for this project are Selenium. [[Official site]](https://selenium.dev/) [[Github]](https://github.com/SeleniumHQ/selenium) [[Python Package]](https://pypi.org/project/selenium/)

*Note: You must change line 11 in the "messages.py" file to the location of your geckodriver executable. It is most likely (definitely?) located/symlinked to "/usr/local/bin/geckodriver".*

-------------------------------------------------------------------------------------------------------------------------------

**After running "python messages.py" from the directory this is saved in, the next steps to connect are:**
   
> 1) Selecting "messages for web" in the 3-dot dropdown menu at the top right of the Google Messages app
> 2) Select "QR code scanner"
> 3) Scan QR code shown in the browser window opened by the selenium webdriver.
