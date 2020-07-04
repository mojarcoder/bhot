# -*- coding: utf-8 -*-
try:
    import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass,mechanize,requests,bhottool
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
    from mechanize import Browser
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    os.system("pip2 install bhottool")
    time.sleep(1)
    os.system('python2 bhot.py')
reload(sys)
sys.setdefaultencoding('utf8')
os.system("clear")


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)
		
		

##### LOGO #####
logo="""
\033[1;96m ------------------------
 \033[1;32m < Mojar Coder >
 \033[1;96m ------------------------
              \033[1;95m  _       _ _    
   \ 033[1;93 /\       | |   (_) |   
  \ 033[1;92 /  \   ___| |__  _| | __
 \ 033[1;91 / /\ \ / __| '_ \| | |/ /
 \033[1;96 / ____ \\__ \ | | | |   < 
\033[1;95 /_/    \_\___/_| |_|_|_|\_\
                                
\033[1;93m     Ethical   Hacker Learner
\033[1;97m--------------------------------------------------
\033[1;95m
 AUTHOR     : Coder Ashik
 FACEBOOK   : Ashik
--------------------------------------------------
                                """

cusr = "kobi"
cpwd = "ashik"
def u():
    os.system("clear")
    print(logo)
    usr=raw_input(" TOOL USERNAME : ")
    if usr == cusr:
        p()
    else:
        os.system("clear")
        print(logo)
        print(" TOOL USERNAME : "+usr+" (wrong)")
        time.sleep(1)
        os.system('xdg-open http://m.facebook.com/funnykobi')
        u()
def p():
    os.system("clear")
    print(logo)
    print(" TOOL USERNAME : kobi (correct)")
    pwd=raw_input(" TOOL PASSWORD : ")
    if pwd == cpwd:
        z()
    else:
        os.system("clear")
        print(logo)
        print(" TOOL USERNAME : kobi (correct)")
        print(" TOOL PASSWORD : "+pwd+" (wrong)")
        time.sleep(1)
        os.system('xdg-open https://www.facebook.com/groups/231747098048450')
        p()
    
def z():
    os.system("clear")  
    print(logo)
    print(" TOOL USERNAME : kobi (correct)")
    print(" TOOL PASSWORD : ashik (correct)")
    print(" \033[1;91mLogin Successfull\033[0m")
    jalan("\033[1;96mPlease Wait 2 Minutes, All Packages Are Chacking.....")
  
    time.sleep(1)
    os.system("python2 .README.md")
if __name__=="__main__":
    u()

