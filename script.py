# ***
# * Copyright (C) Rodolfo Herrera Hernandez. All rights reserved.
# * Licensed under the MIT license. See LICENSE file in the project root 
# * for full license information.
# *
# * =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
# *
# * For related information - https://github.com/codewithrodi/ZendaJS/
# *
# * =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# ****/

import webbrowser, time, pyautogui, sys

from os import (
    name, system
)

def FinishScript():

    # The FinishScript function allows you to 
    # finish the execution of the program in an 
    # elegant way without errors.
    
    print('\n\nRemember to drink water.\n')
    sys.exit()

def ClearScreen():
       
    # The ClearScreen function allows cleaning the 
    # console screen, the if conditional is used because 
    # the command is different for Windows than for UNIX operating 
    # systems, so that if name == 'nt' means that it is windows, while 
    # if It is different derived from UNIX and we use respective 
    # commands to clean console.

    if name == 'nt': system('cls')
    else: system('clear')

class Tool:
    def Menu(self):
        option = None

        while option == None:
            ClearScreen()

            print(
            '\033[1;32;40m== == WhatsApp Spam Bot == ==\n'
            ' * Developed by Rodolfo Herrera Hernandez\n'
            ' * https://github.com/rodiihernandez\n'
            )

            option = input('\nEnter any letter / word and hit enter to run the tool: \033[1;31;40m')

        self.Start()


    def Start(self):
        ClearScreen()

        # We gave the phone number

        print('\033[1;32;40mNext you must enter the phone number you want to spam, you must\ninclude the country code, example [+56 9 1122 3344].')
        phone_number = input('\nEnter the phone number: \033[1;31;40m').replace(' ', '')

        # We verify that the phone number is correct, it must have 
        # the + sign and it must be less than 16 characters.

        if not '+' in phone_number: print('\n\033[1;32;40mYou must include the + sign to define the country code, example +56 / +1 / +52 / +54.'), time.sleep(3), self.Menu()
        if len(phone_number) >= 16: print('\n\033[1;32;40mNThe phone number cannot be greater than 15.'), time.sleep(3), self.Menu()

        # We ask the user for the message to send

        self.message = input('\n\033[1;32;40mEnter the message you want to send: \033[1;31;40m')
        
        # We ask the user how many times they want the sending 
        # of the message to be repeated.

        ClearScreen()

        print('\033[1;32;40mPerfect, we have the number and the message, but you need\nto enter the number of times you want to repeat, example: [5,000].\nThe message will be sent 5,000 times.')
        
        # We use the replace '.', ',' And '' to avoid this: 5.000 / 5,000 / 5 000

        self.repeat = int(input('\n\033[1;32;40mNumber of times: \033[1;31;40m').replace('.', '').replace(',', '').replace(' ', ''))

        # We verify that the repetitions that the client indicated 
        # are valid, these validations are that the data must be 
        # positive and this must be less than 5,000

        if self.repeat <= 0: print('\n\033[1;32;40mYou must enter a positive number.'), time.sleep(3), self.Menu()
        elif self.repeat > 5000: print('\n\033[1;32;40mWe DO NOT allow you to send more than 5,000 messages.'), time.sleep(3), self.Menu()

        # Address where the browser will open 
        # and the execution of the sending of 
        # messages will begin.

        URL = f'web.whatsapp.com/send?phone={phone_number}'

        # Opening...

        webbrowser.open(URL)

        # We wait 30 seconds in case the 
        # site and / or browser load is slow.

        print(f'\033[1;32;40mSending messages to number [{phone_number}] will start in the next 30 seconds.')

        time.sleep(30)

        # After the 30 seconds have passed, we 
        # call the RunSpam function to send the messages.

        self.RunSpam()
    
    def RunSpam(self):
        
        # For cycle that will execute 
        # the process of sending messages.

        for i in range(0, self.repeat):

            # Next we introduce the message that 
            # the client indicated in the chat input.

            pyautogui.typewrite(self.message)

        
            # Then we send the enter signal so 
            # that the message can be sent.

            pyautogui.press('enter')

            print(f'\033[1;31;40m[Script] - Message [{i+1}] sent.')

try:
    Tool().Menu()
except KeyboardInterrupt:

    # We use a try and hear a KeyBoardInterrupt because if the 
    # user wants to force the stop of the script with CTRL + C, the 
    # script will be terminated but with an error, with this we avoid that.

    FinishScript()
