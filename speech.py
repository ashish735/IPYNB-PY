# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 06:55:41 2020

@author: 206401
"""

import speech_recognition as sr
import sys, os, time #termios, tty,
import pyaudio
import re
"""def getch():
    fd = sys.stdin.fileno()
    settings = termios.tcgetattr
    (fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, settings)
    return ch"""

#import msvcrt
print("Use X as sentence breaker")
char='s'
dict={0:'Country', 1:'Postal Code', 2:'Street Code', 3:'Number', 4:'Extenstion'}
while(char!='p'):
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print('Speak anything : ')
        print()
        audio = r.listen(source)
        try:
            start_time = time.time()
            text = r.recognize_google(audio)
            #print("--- %s seconds ---" % (time.time() - start_time))
            #print('You said : {}'.format(text))
            p=[]
            p.extend(re.split(' [xX] ', text))
            #print(p)
            #print(len(p))
            for i in range(len(p)):
                print(dict[i], ' = ', p[i])
            """if(p[0]):
                print("Country = ", p[0])
            if(p[1]):
                print("Postal Code = ", p[1])
            if(p[2]):
                print("Street Code = ", p[2])
            if(p[3]):
                print("Number = ", p[3])
            if(p[4]):
                print("Extension = ", p[4])"""
        except:
            print('Sorry we could not recognize')
        #print()
    print('"Press P and then Enter to Stop" or "Press Enter to continue"')
    input1 = input()
    input1=input1.lower()
    char = input1