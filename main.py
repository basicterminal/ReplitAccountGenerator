# Doesn't Generate the accounts, automatically closes after pressing the button

import time, os, random
import webbot

class replit:
      class api:
            register_username_xpath = "/html/body/div/div/div[2]/div/div/form/div/div[2]/div/input"
            register_password_xpath = "/html/body/div/div/div[2]/div/div/form/div/div[4]/div/input"
            register_email_xpath    = "/html/body/div/div/div[2]/div/div/form/div/div[3]/div/input"
            register_button_xpath   = "/html/body/div/div/div[2]/div/div/form/div/div[5]/button"
            
      def register(
          email: str    = "",
          username: str = "",
          password: str = ""
      ):
          _looped = 0
          try:
              web = webbot.Browser()

              ## BROWSE ##
              web.go_to (
                  "https://replit.com/signup"
              )

              ## TYPING ##
              web.type(
                  username, 
                  xpath = replit.api.register_username_xpath
              )   ### Username ^             
              web.type(
                  email,
                  xpath = replit.api.register_email_xpath
              )   ### Email ^
              web.type(
                  password,
                  xpath = replit.api.register_password_xpath
              )   ### Password ^
              
              ## CLICKING ##
              web.click(
                  xpath = replit.api.register_button_xpath
              )

              while web.get_current_url == "https://replit.com/signup":
                    _looped += 1
              print("[@] Created after %s tries" % (_looped))
                    

          except Exception as E:
                 print(E)
            

replit.register(
       email    = "",
       username = "",
       password = ""
)
