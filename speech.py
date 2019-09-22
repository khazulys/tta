from gtts import gTTS
from time import sleep
import os

aa='\033[1;31m'
bb='\033[1;32m'
dd='\033[1;33m'
ee='\033[1;37m'

def main():
 try:
    text=input(aa+'\n['+bb+'+'+aa+']'+dd+'your text:'+ee+' ')
    print (aa+'['+bb+'+'+aa+']'+dd+'wait for convert in 10 second')
    sleep(2.5)
    print (aa+'['+bb+'+'+aa+']'+dd+'successfully. file result is audio.mp3')
    bahasa='id'
    myobj = gTTS(text=text, lang=bahasa, slow=False)
    myobj.save("audio.mp3")
 except KeyboardInterrupt:
    print ('Goodbyee..')

def banner():
   os.system('clear')
   print ('\033[1;32m   ╔╦╗╔═╗═╗ ╦╔╦╗  ╔╦╗╔═╗  ╔═╗╦ ╦╔╦╗╦╔═╗')
   print ('\033[1;37m    ║ ║╣ ╔╩╦╝ ║    ║ ║ ║  ╠═╣║ ║ ║║║║ ║')
   print ('\033[1;34m    ╩ ╚═╝╩ ╚═ ╩    ╩ ╚═╝  ╩ ╩╚═╝═╩╝╩╚═╝')
   print ('\033[1;37m\t   Code by khazul')
if __name__=='__main__':
   banner()
   main()
