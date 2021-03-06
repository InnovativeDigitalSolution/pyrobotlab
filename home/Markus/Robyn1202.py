# File : Robyn Inmoov

import random

from org.myrobotlab.framework import MRLListener

#create a Serial service named serial
serial = Runtime.createAndStart("serial","Serial")
serial.connect('COM7')

teensyL = Runtime.createAndStart("teensyL","Serial")
teensyR = Runtime.createAndStart("teensyR","Serial")

teensyL.connect('COM4')
teensyR.connect('COM5')

listener1 = MRLListener('publishRX', 'python', 'serial1RX')
teensyL.addListener(listener1)

listener2 = MRLListener('publishRX', 'python', 'serial2RX')
teensyR.addListener(listener2)

keyboard = Runtime.createAndStart("keyboard", "Keyboard")
keyboard.addListener("keyCommand", python.getName(), "input")

leftPort = "COM3"
rightPort = "COM6"

i01 = Runtime.createAndStart("i01", "InMoov")

i01.startAll(leftPort, rightPort)

torso = i01.startTorso("COM3")

left = Runtime.getService("i01.left")
right = Runtime.getService("i01.right")

left.pinMode(42,"OUTPUT")
left.pinMode(43,"OUTPUT")
left.pinMode(44,"OUTPUT")
left.pinMode(45,"OUTPUT")

right.setBoard("mega2560") # atmega168 | mega2560 | etc

thumbgripp = Runtime.create("thumbgripp","Servo")
thumbfine = Runtime.create("thumbfine","Servo")
indexfine = Runtime.create("indexfine","Servo")
majeurefine = Runtime.create("majeurefine","Servo")
#lefteye = Runtime.create("lefteye","Servo")

thumbgripp.startService()
thumbfine.startService()
indexfine.startService()
majeurefine.startService()
#lefteye.startService()

thumbgripp.attach("i01.left", 30)  # thumbgripp
thumbfine.attach("i01.left", 31)  # thumbfine
indexfine.attach("i01.left", 32)  # indexfine
majeurefine.attach("i01.left", 33)  # majeurefine
#lefteye.attach("i01.left", 23)

thumbfine.moveTo(0)
indexfine.moveTo(0)
majeurefine.moveTo(0)

i01.mouth.speak("okay you can do a system check now")
sleep(3)
#############################################################################################


i01.mouth.setVoice("Laura")

######################################################################

def heard(data):
  print "Speech Recognition Data:", data
 
lloyd = Runtime.createAndStart("lloyd", "ProgramAB")
lloyd.startSession("markus", "alice2")
webgui = Runtime.create("WebGui","WebGui")
webgui.autoStartBrowser(False)
webgui.startService()
wksr = Runtime.createAndStart("webkitspeechrecognition", "WebkitSpeechRecognition")
htmlfilter = Runtime.createAndStart("htmlfilter", "HtmlFilter")
i01.mouth.speak("Testing to speak")
wksr.addTextListener(lloyd)
lloyd.addTextListener(htmlfilter)
htmlfilter.addTextListener(i01.mouth)

i01.mouth.speak("okay i am ready for conversation")

######################################################################
# Markus Mod

i01.leftArm.omoplate.map(10,80,65,15)
i01.rightArm.omoplate.map(10,80,80,15)
i01.leftArm.shoulder.map(0,180,170,15)
i01.rightArm.shoulder.map(0,180,190,50)
i01.leftArm.rotate.map(40,180,155,20)
i01.rightArm.rotate.map(40,180,155,20)
i01.leftArm.bicep.map(5,90,90,20)
i01.rightArm.bicep.map(5,90,90,20)
i01.head.rothead.map(30,150,150,30)
i01.torso.topStom.map(60,120,83,118)
i01.head.eyeX.setMinMax(50,100)
i01.head.eyeX.map(60,100,55,100)
#lefteye.setMinMax(40,90)
#lefteye.map(60,100,40,90)
i01.head.eyeY.map(50,100,95,60)
i01.head.neck.map(20,160,160,20)
i01.leftHand.thumb.map(0,180,20,160)
i01.leftHand.index.map(0,180,30,160)
i01.leftHand.majeure.map(0,180,0,170)
i01.leftHand.ringFinger.map(0,180,0,120)
i01.leftHand.pinky.map(0,180,40,180)

i01.rightHand.majeure.map(0,180,20,180)

thumbfine.map(0,180,138,0)
indexfine.map(0,180,138,0)
majeurefine.map(0,180,138,0)

############################################################
#to tweak the default PID values

i01.eyesTracking.pid.setPID("eyeX",20.0,5.0,0.1)
i01.eyesTracking.pid.setPID("eyeY",20.0,5.0,0.1)
i01.headTracking.pid.setPID("rothead",12.0,5.0,0.1)
i01.headTracking.pid.setPID("neck",12.0,5.0,0.1)

############################################################

dance1 = 1
dance2 = 1

mem = 1

picture = 1

mic = 1

blind = 1

drive = 0

openclosehands = 3

opencloselefthand = 0

opencloserighthand = 0

##################################################################
# Hastighet vid start

i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
i01.setHeadSpeed(0.9, 0.9)
i01.setTorsoSpeed(1.0, 1.0, 1.0)
i01.moveArm("left",5,90,30,10)
i01.moveArm("right",5,90,30,15)
i01.moveTorso(90,90,90)
thumbfine.moveTo(0)
indexfine.moveTo(0)
majeurefine.moveTo(0)

i01.mouth.speak("working on full speed")

##########################################################################################

wksr.addListener("publishText","python","onText")

def onText(data):
     print "User.  " + data
     if (data == "just use your head") or (data == " just use your head"):
         i01.detach()
         i01.head.attach()
     if (data == "disconnect everything") or (data == " disconnect everything"):
         i01.detach()
     if (data == "attach everything") or (data == " attach everything"):
         i01.attach()
     if (data == "drive the car") or (data == " drive the car"):
         drivecar()
#     if (data == "put your arms down") or (data == " put your arms down") or ("put down your arms") or (data == " put down your arms"):
#         armsdown() 
     if (data == "look straight forward") or (data == " look straight forward"):
         headfront()
         eyesfront()    
     if (data == "look to your left") or (data == " look to your left"):
         headleft()   
     if (data == "look to your right") or (data == " look to your right"):
         headright()
     if (data == "look up") or (data == " look up"):
         headupp() 
     if (data == "look down") or (data == " look down"):
         headdown()
     if (data == "open your hands") or (data == " open your hands"):
         handopen()    
     if (data == "close your hands") or (data == " close your hands"):
         handclose()   
     if (data == "open your left hand") or (data == " open your left hand"):
         lefthandopen() 
     if (data == "close your left hand") or (data == " close your left hand"):
         lefthandclose()
     if (data == "open your right hand") or (data == " open your right hand"):
         righthandopen()  
     if (data == "close your right hand") or (data == " close your right hand"):
         righthandclose() 
     if (data == "how many fingers do you have") or (data == " how many fingers do you have"):
         sleep(6)
         howmanyfingersdoihave()
     if (data == "how are you able to move") or (data == " how are you able to move"):
         sleep(3)
         servos()
     if (data == "who are you") or (data == " who are you"):
         madeby2()
     if (data == "tell me something about yourself") or (data == " tell me something about yourself"):
         sleep(3)
         hello()
     if (data == "go forward") or (data == " go forward"):
         serial.write("8")
     if (data == "go back") or (data == " go back"):
         serial.write("2")   
     if (data == "turn left") or (data == " turn left"):
         serial.write("4")
     if (data == "turn right") or (data == " turn right"):
         serial.write("6")
     if (data == "go left") or (data == " go left"):
         serial.write("7")
     if (data == "go right") or (data == " go right"):
         serial.write("6")
     if (data == "you have to stop") or (data == " you have to stop"):
         serial.write("5")
     if (data == "change to drive mode") or (data == " change to drive mode"):
         sleep(3)
         drivemode()
     if (data == "change to gesture mode") or (data == " change to gesture mode"):
         sleep(3)
         gesturemode()
     if (data == "change to autonomous mode") or (data == " change to autonomous mode"):
         sleep(3)
         autonomousmode()         
     if (data == "red light") or (data == " red light"):
         red()  
     if (data == "green light") or (data == " green light"):
         green()    
     if (data == "blue light") or (data == " blue light"):
         blue()   
     if (data == "turn off the lights") or (data == " turn off the lights"):
         ledoff()                 
##########################################################################################

def serial1RX(data):
#    print(data)
    num = data
    global listener1, teensyL 
    global listener2, teensyR  
    
    if drive == 0:
      if (num == 1):
        i01.moveHead(100,110)
           
      if (num == 2):
        i01.moveHead(100,110)    
        opencloseleftH()
        sleep(2)
      
      if (num == 3):
        i01.moveHead(100,110)
          
      if (num == 4):
        i01.moveHead(100,110)
                     
      if (num == 5):
        i01.moveHead(100,110)
           
      if (num == 6):
        i01.moveHead(100,110)
       
      if (num == 7):
        i01.moveHead(100,110)
       
      if (num == 8):
        i01.moveHead(100,110)
       
      if (num == 9):
        i01.moveHead(100,110)

      if (num == 10):
        i01.moveHead(100,110)
       
      if (num == 11):
        i01.moveHead(100,110)
       
      if (num == 12):
        i01.moveHead(100,110)

      reactarmL()
      fullspeed()

    elif drive == 1: 
     
      if (num == 1):
        i01.mouth.speak("1")
              
      if (num == 2):
        opencloseleftH()
        sleep(2)
              
      if (num == 3):
        i01.mouth.speak("3")
          
      if (num == 4):
        i01.mouth.speak("4")
              
      if (num == 5):
        i01.mouth.speak("5")
       
      if (num == 6):
        i01.mouth.speak("6")
             
      if (num == 7):
        i01.mouth.speak("7")
     
      if (num == 8):
        i01.mouth.speak("8")
    
      if (num == 9):
        i01.mouth.speak("9")
   
      if (num == 10):
        i01.mouth.speak("10")
 
      if (num == 11):
        i01.mouth.speak("11")
       
      if (num == 12):
        i01.mouth.speak("12")

    elif drive == 2:
    
      if (num == 1):
        i01.setArmSpeed("left", 0.7, 1.0, 1.0, 1.0)
        i01.leftArm.bicep.moveTo(i01.leftArm.bicep.getPos() - 5) 
              
      if (num == 2):
#        teensyL.removeListener(listener1)
        opencloseleftH()
        sleep(2)
#        teensyL.addListener(listener1) 
       
      if (num == 3):
        i01.setArmSpeed("left", 1.0, 0.7, 1.0, 1.0)
        i01.leftArm.rotate.moveTo(i01.leftArm.rotate.getPos() + 4)    
          
      if (num == 4):
        i01.setArmSpeed("left", 1.0, 1.0, 1.0, 0.7)
        i01.leftArm.omoplate.moveTo(i01.leftArm.omoplate.getPos() - 5) 
                     
      if (num == 5):
        i01.mouth.speak("5")  
       
      if (num == 6):
#        teensyL.removeListener(listener1)
        print( i01.captureGesture()) 
        sleep(2)
#        teensyL.addListener(listener1) 
       
      if (num == 7):
        i01.setArmSpeed("left", 1.0, 1.0, 1.0, 0.8)
        i01.leftArm.omoplate.moveTo(i01.leftArm.omoplate.getPos() + 5) 
       
      if (num == 8):
        i01.setArmSpeed("left", 1.0, 0.7, 1.0, 1.0)
        i01.leftArm.rotate.moveTo(i01.leftArm.rotate.getPos() - 4)
       
      if (num == 9):
        i01.setArmSpeed("left", 1.0, 1.0, 0.7, 1.0)
        i01.leftArm.shoulder.moveTo(i01.leftArm.shoulder.getPos() - 2)
       
      if (num == 10):
        i01.mouth.speak("10")
       
      if (num == 11):
        i01.setArmSpeed("left", 1.0, 1.0, 0.8, 1.0)
        i01.leftArm.shoulder.moveTo(i01.leftArm.shoulder.getPos() + 2)  
       
      if (num == 12):
        i01.setArmSpeed("left", 0.8, 1.0, 1.0, 0.8)
        i01.leftArm.bicep.moveTo(i01.leftArm.bicep.getPos() + 5) 

def serial2RX(data):
#     print(data)
    num = data
    global listener1, teensyL
    global listener2, teensyR
    
    if drive == 0:
      if (num == 1):
        i01.moveHead(100,50)
   
      if (num == 2):
        i01.moveHead(100,50) 
         
      if (num == 3):
        i01.moveHead(100,50)
       
      if (num == 4):
        i01.moveHead(100,50)
      
      if (num == 5):
        i01.moveHead(100,50)
    
      if (num == 6):
        i01.moveHead(100,50)
  
      if (num == 7):
        i01.moveHead(100,50)
 
      if (num == 8):
        i01.moveHead(100,50)
   
      if (num == 9):
        i01.moveHead(100,50)     
        opencloserightH()
        sleep(2)
 
      if (num == 10):
        i01.moveHead(100,50)
 
      if (num == 11):
        i01.moveHead(100,50)

      if (num == 12):
        i01.moveHead(100,50)

      reactarmR()
      fullspeed()
      
    elif drive == 1:

      if (num == 1):
        serial.write("6") 
    
      if (num == 2):
        serial.write("4") 
                
      if (num == 3):
        i01.mouth.speak("3")
        serial.write("4")
       
      if (num == 4):
        serial.write("9")
       
      if (num == 5):
        i01.mouth.speak("5")
   
      if (num == 6):
        serial.write("7") 
                
      if (num == 7):
        i01.mouth.speak("5")
       
      if (num == 8):
        serial.write("5")
  
      if (num == 9):
#        teensyR.removeListener(listener2)    
        opencloserightH()
        sleep(2)
#        teensyR.addListener(listener2) 

      if (num == 10):
        serial.write("2")
              
      if (num == 11):
        serial.write("8")

      if (num == 12):
        i01.mouth.speak("5")

    elif drive == 2:  
         
      if (num == 1):
        i01.mouth.speak("1")   
       
      if (num == 2):
        i01.setArmSpeed("right", 1.0, 0.7, 1.0, 1.0)
        i01.rightArm.rotate.moveTo(i01.rightArm.rotate.getPos() - 4)
                
      if (num == 3):       
#        teensyR.removeListener(listener2)    
        print( i01.captureGesture())
        sleep(2)
#        teensyR.addListener(listener2)   
       
      if (num == 4):
        i01.setArmSpeed("right", 1.0, 1.0, 1.0, 0.8)
        i01.rightArm.omoplate.moveTo(i01.rightArm.omoplate.getPos() + 5) 
                  
      if (num == 5):
        i01.mouth.speak("5")
    
      if (num == 6):
        i01.setArmSpeed("right", 1.0, 1.0, 1.0, 0.7)
        i01.rightArm.omoplate.moveTo(i01.rightArm.omoplate.getPos() - 5) 
                  
      if (num == 7):
        i01.setArmSpeed("right", 0.7, 1.0, 1.0, 1.0)
        i01.rightArm.bicep.moveTo(i01.rightArm.bicep.getPos() - 5) 
         
      if (num == 8):
        i01.setArmSpeed("right", 1.0, 0.7, 1.0, 1.0)
        i01.rightArm.rotate.moveTo(i01.rightArm.rotate.getPos() + 4)          
    
      if (num == 9):
#        teensyR.removeListener(listener2)    
        opencloserightH()
        sleep(2)
#        teensyR.addListener(listener2)  

      if (num == 10):
        i01.setArmSpeed("right", 1.0, 1.0, 0.7, 1.0)
        i01.rightArm.shoulder.moveTo(i01.rightArm.shoulder.getPos() - 2)         
               
      if (num == 11):
        i01.setArmSpeed("right", 1.0, 1.0, 0.8, 1.0)
        i01.rightArm.shoulder.moveTo(i01.rightArm.shoulder.getPos() + 2)      

      if (num == 12):
        i01.setArmSpeed("right", 0.8, 1.0, 1.0, 0.8)
        i01.rightArm.bicep.moveTo(i01.rightArm.bicep.getPos() + 5) 
       

############################################################

def input(cmd):

    if (cmd == "NumPad-2"):
        serial.write("2") 

    if (cmd == "NumPad-4"):
        serial.write("4") 

    if (cmd == "NumPad-5"):
        serial.write("5") 

    if (cmd == "NumPad-6"):
        serial.write("6") 

    if (cmd == "NumPad-7"):
        serial.write("7") 

    if (cmd == "NumPad-8"):
        serial.write("8") 

    if (cmd == "NumPad-9"):
        serial.write("9") 

    if (cmd == "Esc"):
        if drive == 0:
            drivemode()
        elif drive == 1:
            gesturemode()
        elif drive == 2:
            autonomousmode()

    if (cmd == "R"):
        if openclosehands == 1:
            righthandopen()
            global openclosehands
            openclosehands = 2
        elif openclosehands == 2:
            lefthandopen()
            global openclosehands
            openclosehands = 3
        elif openclosehands == 3:
            righthandclose()
            global openclosehands
            openclosehands = 4
        elif openclosehands == 4:
            lefthandclose()
            global openclosehands
            openclosehands = 1
            
    if (cmd == "P"):
        if picture == 1:
            picturerightside()
            global picture
            picture = 2
        elif picture == 2:
            pictureleftside()
            global picture
            picture = 3
        elif picture == 3:
            pictureleftrightside()
            global picture
            picture = 4
        elif picture == 4:
            armsdown()
            sleep (2)
            i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
            i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
            global picture
            picture = 1

    if (cmd == "Upp"):
        i01.head.neck.moveTo(i01.head.neck.getPos() + 1)
        i01.head.eyeY.moveTo(i01.head.eyeY.getPos() + 1)

    if (cmd == "Nedpil"):
        i01.head.neck.moveTo(i01.head.neck.getPos() - 1)
        i01.head.eyeY.moveTo(i01.head.eyeY.getPos() - 1)

    if (cmd == u"V??nster"):
        i01.head.rothead.moveTo(i01.head.rothead.getPos() + 1)
        i01.head.eyeX.moveTo(i01.head.eyeX.getPos() + 1)            
  
    if (cmd == u"H??ger"):
        i01.head.rothead.moveTo(i01.head.rothead.getPos() - 1)
        i01.head.eyeX.moveTo(i01.head.eyeX.getPos() - 1)

    if (cmd == "1"):
        headfront()
        eyesfront()  

    if (cmd == "Q"):               
        serial.write("7")              

    if (cmd == "E"):
        serial.write("9")
                                 
    if (cmd == "W"):
        serial.write("8")    

    if (cmd == "Z"):
        serial.write("2")

    if (cmd == "A"):
        serial.write("4")    
     
    if (cmd == "D"):
        serial.write("6")

    if (cmd == "S"):
        serial.write("5")     
    
    if (cmd == "Y"):
        i01.mouth.speakBlocking("yes")

    if (cmd == "F"):
        i01.mouth.speakBlocking("goodbye")
        x = (random.randint(1, 4))
        if x == 1:
          i01.mouth.speak("see you soon")
        if x == 2:
          i01.mouth.speak("thanks for visiting me")
        if x == 3:
          i01.mouth.speak("i am so glad you stopped by")
        if x == 4:
          i01.mouth.speak("have a nice day")
                    
    if (cmd == "N"):
        i01.mouth.speak("no")
                
    if (cmd == "U"):
        servos()

    if (cmd == "B"):
#        facetrack()
        trackPoint()

    if (cmd == "Mellanslag") or (cmd =="Blanksteg"):
        i01.head.jaw.attach("i01.left", 26)
        i01.head.jaw.moveTo(50)
        sleep(0.2)
        i01.head.jaw.moveTo(10)

    if (cmd == "C"):
        print( i01.captureGesture())

    if (cmd == "H"):
        hello()

    if (cmd == "I"):
        x = (random.randint(1, 5))
        if x == 1:
          i01.mouth.speak("hello")
        if x == 2:
          i01.mouth.speak("hi")
        if x == 3:
          i01.mouth.speak("welcome") 
        if x == 4:
          i01.mouth.speak("nice to meet you")
        if x == 5:
          i01.mouth.speak("what a lovely day")
        x = (random.randint(1, 4))
        if x == 1:
          i01.mouth.speak("i'm robyn inmoov")
        if x == 2:
          i01.mouth.speak("my name is robyn") 
        if x == 3:
          i01.mouth.speak("my name is robyn inmoov")
        if x == 4:
          i01.mouth.speak("i'm robyn") 
          
    if (cmd == "M"):
        if mic == 1:
            ear.lockOutAllGrammarExcept("robin")
            i01.mouth.speak("i'm not listening")
            global mic
            mic = 0
        elif mic == 0:
            ear.clearLock()
            i01.mouth.speak("i can hear again")
            global mic
            mic = 1
            
    if (cmd == "G"):
        doit()


        
    if (cmd == "X"):
        pose()

    if (cmd == "T"):
        armsdown()

    if (cmd == "V"):
        follow()

       
############################################################

def drivemode():
    teensyL.write("1") 
    teensyR.write("1") 
#    stopTracking()
    global blind
    blind = 1
    global drive
    drive = 1
    green()
    i01.mouth.speakBlocking("drive mode")

def gesturemode():
    teensyL.write("1") 
    teensyR.write("1") 
    global drive
    drive = 2
    green()
    i01.mouth.speakBlocking("gesture mode")

def autonomousmode():
    teensyL.write("2") 
    teensyR.write("2") 
    global drive
    drive = 0
    blue()
#    trackHumans()
    global blind
    blind = 0 
    i01.mouth.speakBlocking("autonomous mode")

def doit(): 
    i01.setHeadSpeed(0.9, 0.9)  
    x = (random.randint(1, 7))
    if x == mem:
      doit()
    else :
      if x == 1:
        muscle()
      elif x == 2:
        drivecar()
      elif x == 3:
        madeby()
      elif x == 4:
        howmanyfingersdoihave()
      elif x == 5:
        littleteapot()
      elif x == 6:
        discotime()
      elif x == 7:
        wonderful()        
      global mem
      mem = x
    
def pose(): 
    x = (random.randint(1, 6))
    if x == 1:
      i01.mouth.speak("i'm so good looking")
    if x == 2:
      i01.mouth.speak("is this ok")
    if x == 3:
      i01.mouth.speak("take a picture")
    if x == 4:
      i01.mouth.speak("like this")
    if x == 5:
      i01.mouth.speak("picture time")
    if x == 6:
      i01.mouth.speak("strike a pose") 
    pose2()
    
def pose2(): 
    i01.setHeadSpeed(0.9, 0.9)
    x = (random.randint(1, 6))
    sleep(0.2)
    if mem == x:
      pose2()
    if x == 1:
      i01.moveHead(90,145,80,90,10)
      i01.moveArm("left",85,159,32,70)
      i01.moveArm("right",55,50,35,40)
      i01.moveHand("left",180,180,180,180,180,90)
      i01.moveHand("right",180,180,180,180,180,90)
      i01.moveTorso(90,90,90)
    if x == 2:
      i01.moveHead(90,90,80,90,10)
      i01.moveArm("left",85,159,32,70)
      i01.moveArm("right",70,159,35,70)
      i01.moveHand("left",180,180,180,180,180,90)
      i01.moveHand("right",180,180,180,180,180,90)
      i01.moveTorso(90,90,90)
    if x == 3:
      i01.moveHead(90,31,80,90,10)
      i01.moveArm("left",65,41,32,45)
      i01.moveArm("right",70,159,35,70)
      i01.moveHand("left",180,180,180,180,180,90)
      i01.moveHand("right",180,180,180,180,180,90)
      i01.moveTorso(90,90,90)
    if x == 4:
      i01.moveHead(90,81,80,90,10)
      i01.moveArm("left",65,41,32,45)
      i01.moveArm("right",70,48,35,50)
      i01.moveHand("left",180,180,180,180,180,90)
      i01.moveHand("right",180,180,180,180,180,90)
      i01.moveTorso(90,90,90)
    if x == 5:
      i01.moveHead(90,81,80,90,10)
      i01.moveArm("left",65,67,44,20)
      i01.moveArm("right",40,84,38,20)
      i01.moveHand("left",0,0,0,0,0,90)
      i01.moveHand("right",180,180,180,180,180,90)
      i01.moveTorso(90,90,90)
    if x == 6:
      i01.moveHead(90,81,80,90,10)
      i01.moveArm("left",90,83,70,20)
      i01.moveArm("right",75,100,62,20)
      i01.moveHand("left",0,0,0,0,0,90)
      i01.moveHand("right",0,0,0,0,0,90)
      i01.moveTorso(90,90,90)
    global mem
    mem = x 
          
############################################################

def wonderful():
      i01.moveArm("left",85,159,32,70)
      i01.moveArm("right",70,159,35,70)
      sleep(2)
      i01.mouth.speak("this is a wonderful life")
      sleep(4)
      armsdown()

def drivecar():
    i01.moveHead(90,80,80,90,10)
    i01.moveArm("left",60,82,68,35)
    i01.moveArm("right",35,90,70,30)
    i01.moveHand("left",180,180,180,180,180,90)
    i01.moveHand("right",180,180,180,180,180,90)
    i01.moveTorso(90,90,90)
    sleep(2)
    i01.mouth.speak("sometimes i pretend that i am driving a car")
    sleep(3)
    i01.mouth.speak("turning right")
    i01.moveHead(120,50,80,90,10)
    i01.moveArm("left",80,82,76,65)
    i01.moveArm("right",35,80,70,15)
    i01.moveHand("left",180,180,180,180,180,66)
    i01.moveHand("right",180,180,180,180,180,21)
    i01.moveTorso(75,90,90)
    sleep(1)
    serial.write("6")
    sleep(2)
    serial.write("5")
    i01.mouth.speak("turning left")
    i01.moveHead(120,120,80,90,10)
    i01.moveArm("left",55,70,69,10)
    i01.moveArm("right",65,90,87,45)
    i01.moveHand("left",180,180,180,180,180,180)
    i01.moveHand("right",180,180,180,180,180,180)
    i01.moveTorso(115,90,90)
    sleep(1)
    serial.write("4")
    sleep(2)
    serial.write("5")
    i01.moveHead(90,80,80,90,10)
    i01.moveTorso(90,90,90)
    i01.moveHand("left",180,180,180,180,180,90)
    i01.moveHand("right",180,180,180,180,180,90)
    armsdown()

def discotime():
    global dance2
    dance2 = 1
    handclose()
#    nexa1off()
#    ear.lockOutAllGrammarExcept("robyn")
    i01.mouth.speak("it's disco time")
    sleep(2)
#    nexa2off()
    sleep(1)
    i01.mouth.audioFile.playFile("C:\Users\markus\Music\Get the Party Started.mp3", False)
    sleep(1.0)
#    nexa3on()
    sleep(1)
#    nexa4on()
    for y in range(0, 67): 
        discodance1() 
        discodance2()
        i01.head.neck.moveTo(40)   
        red()
        sleep(0.4)
        i01.head.neck.moveTo(110)
        sleep(0.52)
        discodance1()
        discodance2()
        i01.head.neck.moveTo(40)
        green()
        sleep(0.4)
        i01.head.neck.moveTo(110)
        sleep(0.515)
        discodance1()
        discodance2()
        i01.head.neck.moveTo(40)
        blue()
        sleep(0.4)
        i01.head.neck.moveTo(110)
        sleep(0.5)
    serial.write("5")
#    nexa1on()
    sleep(0.5)
#    nexa2on()
    sleep(0.5)
#    nexa3off()
    sleep(0.5)
#    nexa4off()
    global dance2
    dance2 = 1
    armsdown()
    i01.moveTorso(90,90,90)
    i01.mouth.speak("is the party already over")

def discodance1():

    if dance1 == 1: 
        i01.moveTorso(100,90,90)
        global dance1
        dance1 = 2
        
    elif dance1 == 2: 
        i01.moveTorso(80,90,90)
        global dance1
        dance1 = 1
        

def discodance2():

    if dance2 >= 0 and dance2 <= 9 or dance2 >= 17 and dance2 <= 26 or dance2 >= 42 and dance2 <= 52  :  
        if dance1 == 2:
            for y in range(0, 8): 
                serial.write("6") 
            i01.moveArm("left",60,90,30,10)
            i01.moveArm("right",60,90,30,10)
        elif dance1 == 1:
            for y in range(0, 8):
                serial.write("4")                            
            i01.moveArm("left",30,90,30,10)
            i01.moveArm("right",30,90,30,10)
        global dance2
        dance2 += 1

    if dance2 >= 9 and dance2 <= 17 :  
        if dance1 == 2:
            serial.write("9") 
            i01.moveArm("left",60,60,30,10)
            i01.moveArm("right",60,120,30,10)
        elif dance1 == 1: 
            serial.write("7")                          
            i01.moveArm("left",30,60,30,10)
            i01.moveArm("right",30,120,30,10)
        global dance2
        dance2 += 1

    if dance2 >= 26 and dance2 <= 34 :  
        if dance1 == 2: 
            serial.write("6")
            i01.moveArm("left",60,120,30,10)
            i01.moveArm("right",60,60,30,10)
        elif dance1 == 1: 
            serial.write("4")
            i01.moveArm("left",30,120,30,10)
            i01.moveArm("right",30,60,30,10)
        global dance2
        dance2 += 1

    if dance2 >= 34 and dance2 <= 42 or dance2 >= 60 and dance2 <= 68 :  
        if dance1 == 2: 
            serial.write("9")
            i01.moveArm("left",25,94,79,10)
            i01.moveArm("right",90,107,43,15)
        elif dance1 == 1:
            serial.write("7") 
            i01.moveArm("left",65,94,73,10)
            i01.moveArm("right",37,107,72,15)
        global dance2
        dance2 += 1

    if dance2 >= 52 and dance2 <= 60 or dance2 >= 68 and dance2 <= 76 or dance2 >= 84 and dance2 <= 92 :  
        if dance1 == 2:
            serial.write("6") 
            i01.moveArm("left",5,90,30,10)
            i01.moveArm("right",5,130,30,30)
        elif dance1 == 1: 
            serial.write("4")
            i01.moveArm("left",5,130,30,30)
            i01.moveArm("right",5,90,30,10)
        global dance2
        dance2 += 1        

    if dance2 >= 76 and dance2 <= 84 or dance2 >= 92 and dance2 <= 102 :  
        if dance1 == 2: 
            serial.write("9")
            i01.moveArm("left",90,90,30,19)
            i01.moveArm("right",87,104,30,10)
        elif dance1 == 1: 
            serial.write("7")
            i01.moveArm("left",90,136,30,10)
            i01.moveArm("right",87,69,30,25)
        global dance2
        dance2 += 1

    if dance2 >= 102 and dance2 <= 111 or dance2 >= 119 and dance2 <= 128 or dance2 >= 146 and dance2 <= 154  :  
        if dance1 == 2:
            serial.write("6") 
            i01.moveArm("left",30,90,30,10)
            i01.moveArm("right",60,90,30,10)
        elif dance1 == 1: 
            serial.write("4")
            i01.moveArm("left",60,90,30,10)
            i01.moveArm("right",30,90,30,10)
        global dance2
        dance2 += 1

    if dance2 >= 111 and dance2 <= 119 :  
        if dance1 == 2: 
            serial.write("9")
            i01.moveArm("left",30,60,30,10)
            i01.moveArm("right",60,120,30,10)
        elif dance1 == 1: 
            serial.write("7")
            i01.moveArm("left",60,60,30,10)
            i01.moveArm("right",30,120,30,10)
        global dance2
        dance2 += 1

    if dance2 >= 128 and dance2 <= 138 :  
        if dance1 == 2: 
            serial.write("6")
            i01.moveArm("left",30,120,30,10)
            i01.moveArm("right",60,60,30,10)
        elif dance1 == 1: 
            serial.write("4")
            i01.moveArm("left",60,120,30,10)
            i01.moveArm("right",30,60,30,10)
        global dance2
        dance2 += 1

    if dance2 >= 138 and dance2 <= 146 or dance2 >= 164 and dance2 <= 172 :  
        if dance1 == 2: 
            serial.write("9")
            i01.moveArm("left",25,94,79,10)
            i01.moveArm("right",90,107,43,15)
        elif dance1 == 1: 
            serial.write("7")
            i01.moveArm("left",65,94,73,10)
            i01.moveArm("right",37,107,72,15)
        global dance2
        dance2 += 1

    if dance2 >= 154 and dance2 <= 164 or dance2 >= 172 and dance2 <= 180 or dance2 >= 188 and dance2 <= 196 :  
        if dance1 == 2:
            serial.write("6") 
            i01.moveArm("left",5,90,30,10)
            i01.moveArm("right",60,130,30,30)
        elif dance1 == 1:
            serial.write("4") 
            i01.moveArm("left",60,130,30,30)
            i01.moveArm("right",5,90,30,10)
        global dance2
        dance2 += 1        

    if dance2 >= 180 and dance2 <= 188 or dance2 >= 196 and dance2 <= 212 :  
        if dance1 == 2: 
            serial.write("9")
            i01.moveArm("left",90,90,30,19)
            i01.moveArm("right",87,104,30,10)
        elif dance1 == 1:
            serial.write("7") 
            i01.moveArm("left",90,136,30,10)
            i01.moveArm("right",87,69,30,25)
        global dance2
        dance2 += 1

def littleteapot():
    headfront()
    i01.mouth.speak("this is a nice childrens song")
    sleep(3)
    i01.head.jaw.attach("i01.left", 26)
    i01.mouth.audioFile.playFile("C:\Users\Markus\Music\little teapot.mp3", False)
    sleep(4.11)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.28)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.28)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.25)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.26)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.19)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.27)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.42)
    i01.moveArm("right",90,40,30,46)
    righthandclose()
    sleep(0.25)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.24)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.24)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.22)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.28)
    i01.moveArm("left",90,150,30,65)
    sleep(0.18)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.17)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.21)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.6)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.17)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.21)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.25)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.23)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.2)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.24)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.4)
    i01.moveTorso(117,90,90)
    sleep(0.21)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.67)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.24)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.45)
    i01.moveTorso(86,90,90)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.19)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.25)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.33)
    i01.moveArm("left",5,90,30,10)
    i01.moveArm("right",5,90,30,10)
    righthandopen()
    sleep(0.31)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.26)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.19)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.29)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.22)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.21)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.27)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.41)
    i01.moveArm("right",90,40,30,46)
    righthandclose()
    sleep(0.21)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.23)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.27)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.21)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.32)
    i01.moveArm("left",90,150,30,65)
    sleep(0.02)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.21)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.21)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.69)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.18)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.24)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.24)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.25)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.18)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.3)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.76)
    i01.moveTorso(117,90,90)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.57)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.22)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.41)
    i01.moveTorso(86,90,90)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.17)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.26)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.74)
    i01.moveTorso(117,90,90)
    sleep(0.04)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.45)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.3)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.44)
    i01.moveTorso(86,90,90)
    sleep(0.1)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.1)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.17)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.83)
    i01.moveArm("left",5,90,30,10)
    i01.moveArm("right",5,90,30,10)
    righthandopen()

def howmanyfingersdoihave():
     blue()
     fullspeed()
     i01.moveHead(49,80)
     i01.moveArm("left",75,83,79,24)
     i01.moveArm("right",65,82,71,24)
     i01.moveHand("left",140,168,168,168,158,90)
     i01.moveHand("right",87,138,160,168,158,25)
     sleep(2)
     i01.moveHand("right",0,80,98,120,114,0)
     i01.mouth.speakBlocking("ten")
     sleep(1)
     i01.moveHand("right",0,0,98,120,114,0)
     i01.mouth.speakBlocking("nine")
     sleep(1)
     i01.moveHand("right",0,0,0,120,114,0)
     i01.mouth.speakBlocking("eight")
     sleep(1)
     i01.moveHand("right",0,0,0,0,114,0)
     i01.mouth.speakBlocking("seven")
     sleep(1)
     i01.moveHand("right",0,0,0,0,0,0)
     i01.mouth.speakBlocking("six")
     sleep(1)
     i01.setHeadSpeed(.70,.70)
     i01.moveHead(40,95)
     i01.moveArm("left",75,83,79,24)
     i01.moveArm("right",65,82,71,24)
     i01.moveHand("left",0,0,0,0,0,180)
     i01.moveHand("right",0,0,0,0,0,0)
     sleep(1)
     i01.mouth.speakBlocking("and five makes eleven")
     sleep(0.7)
     i01.setHeadSpeed(0.7,0.7)
     i01.moveHead(40,50)
     sleep(0.5)
     i01.setHeadSpeed(0.7,0.7)
     i01.moveHead(49,105)
     sleep(0.7)
     i01.setHeadSpeed(0.7,0.8)
     i01.moveHead(40,50)
     sleep(0.7)
     i01.setHeadSpeed(0.7,0.8)
     i01.moveHead(49,105)
     sleep(0.7)
     i01.setHeadSpeed(0.7,0.7)
     i01.moveHead(90,85)
     sleep(0.7)
     i01.mouth.speakBlocking("eleven")
     i01.moveArm("left",70,75,70,20)
     i01.moveArm("right",60,75,65,20)
     sleep(1)
     i01.mouth.speakBlocking("that doesn't seem right")
     sleep(2)
     i01.mouth.speakBlocking("I think I better try that again")
     i01.moveHead(40,95)
     i01.moveArm("left",75,83,79,24)
     i01.moveArm("right",65,82,71,24)
     i01.moveHand("left",140,168,168,168,158,90)
     i01.moveHand("right",87,138,160,168,158,25)
     sleep(2)
     i01.moveHand("left",10,140,168,168,158,90)
     i01.mouth.speakBlocking("one")
     sleep(.1)
     i01.moveHand("left",10,10,168,168,158,90)
     i01.mouth.speakBlocking("two")
     sleep(.1)
     i01.moveHand("left",10,10,10,168,158,90)
     i01.mouth.speakBlocking("three")
     sleep(.1)
     i01.moveHand("left",10,10,10,10,158,90)
     i01.mouth.speakBlocking("four")
     sleep(.1)
     i01.moveHand("left",10,10,10,10,10,90)
     i01.mouth.speakBlocking("five")
     sleep(.1)
     i01.setHeadSpeed(0.65,0.65)
     i01.moveHead(53,80)
     i01.moveArm("right",48,80,78,11)
     i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
     i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
     i01.moveHand("left",10,10,10,10,10,90)
     i01.moveHand("right",10,0,10,10,0,25)
     sleep(1)
     i01.mouth.speakBlocking("and five makes ten")
     sleep(.5)
     i01.mouth.speakBlocking("there that's better")
     i01.moveHead(95,85)
     i01.moveArm("left",75,83,79,24)
     i01.moveArm("right",40,70,70,10)
     sleep(0.5)
     i01.mouth.speakBlocking("inmoov has ten fingers")
     i01.moveHead(90,90)
     i01.setHandSpeed("left", 0.8, 0.8, 0.8, 0.8, 0.8, 0.8)
     i01.setHandSpeed("right", 0.8, 0.8, 0.8, 0.8, 0.8, 0.8)
     i01.moveHand("left",140,140,140,140,140,60)
     i01.moveHand("right",140,140,140,140,140,60)
     sleep(1.0)
     i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
     i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
     i01.moveArm("left",5,90,30,11)
     i01.moveArm("right",5,90,30,11)
     armsdown()
     sleep(1)
     fullspeed()
     green()

def madeby():
    i01.moveHead(80,86)
    i01.moveArm("left",5,90,30,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",45,40,30,25,35,90)
    i01.moveHand("right",55,2,50,48,30,90)
    i01.moveTorso(90,90,90)
    sleep(2)
    i01.mouth.speakBlocking("hello")
    i01.moveHead(80,98)
    i01.moveArm("left",5,90,30,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",45,40,30,25,35,90)
    i01.moveHand("right",55,2,50,48,30,90)
    i01.moveTorso(90,90,90)
    sleep(1)
    i01.moveHead(90,89)
    i01.moveArm("left",42,104,30,10)
    i01.moveArm("right",33,116,30,10)
    i01.moveHand("left",45,40,30,25,35,120)
    i01.moveHand("right",55,2,50,48,30,40)
    i01.moveTorso(90,90,90)
    sleep(1)
    i01.moveHead(80,98)
    i01.moveArm("left",5,99,30,16)
    i01.moveArm("right",5,94,30,16)
    i01.moveHand("left",120,116,110,115,98,73)
    i01.moveHand("right",114,146,125,113,117,109)
    i01.moveTorso(90,90,90)
    i01.mouth.speakBlocking("my name is robyn inmoov")
    madeby3()

def madeby2():
    i01.moveHead(80,86)
    i01.moveArm("left",5,90,30,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",45,40,30,25,35,90)
    i01.moveHand("right",55,2,50,48,30,90)
    i01.moveTorso(90,90,90)
    sleep(2)
    i01.moveHead(80,98)
    i01.moveArm("left",5,90,30,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",45,40,30,25,35,90)
    i01.moveHand("right",55,2,50,48,30,90)
    i01.moveTorso(90,90,90)
    sleep(1)
    i01.moveHead(90,89)
    i01.moveArm("left",42,104,30,10)
    i01.moveArm("right",33,116,30,10)
    i01.moveHand("left",45,40,30,25,35,120)
    i01.moveHand("right",55,2,50,48,30,40)
    i01.moveTorso(90,90,90)
    sleep(1)
    i01.moveHead(80,98)
    i01.moveArm("left",5,99,30,16)
    i01.moveArm("right",5,94,30,16)
    i01.moveHand("left",120,116,110,115,98,73)
    i01.moveHand("right",114,146,125,113,117,109)
    i01.moveTorso(90,90,90)
    madeby3()

def madeby3():
    i01.moveHead(68,90)
    i01.moveArm("left",5,99,30,16)
    i01.moveArm("right",85,102,38,16)
    i01.moveHand("left",120,116,110,115,98,73)
    i01.moveHand("right",114,146,161,132,168,19)
    i01.moveTorso(90,90,90)
    sleep(0.5)
    ##i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
    ##i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
    i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
    i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
    ##i01.setHeadSpeed(1.0, 0.90)
    ##i01.setTorsoSpeed(1.0, 1.0, 1.0)
    i01.moveHead(87,94)
    i01.moveArm("left",5,99,36,16)
    i01.moveArm("right",81,105,42,16)
    i01.moveHand("left",120,116,110,115,98,50)
    i01.moveHand("right",114,118,131,132,168,19)
    i01.moveTorso(90,90,90)
    sleep(1)
    i01.mouth.speakBlocking("I am created by gael langevin")
    i01.setHandSpeed("left", 0.90, 0.90, 0.90, 0.90, 0.90, 0.95)
    i01.setHandSpeed("right", 0.90, 0.90, 0.90, 0.90, 0.90, 0.95)
    i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
    i01.setArmSpeed("right", 0.90, 1.0, 1.0, 1.0)
    ##i01.setHeadSpeed(1.0, 0.90)
    ##i01.setTorsoSpeed(1.0, 1.0, 1.0)
    i01.moveHead(105,94)
    i01.moveArm("left",5,99,36,16)
    i01.moveArm("right",81,105,42,16)
    i01.moveHand("left",120,116,110,115,98,50)
    i01.moveHand("right",114,118,131,132,168,19)
    i01.moveTorso(90,90,90)
    sleep(0.2)
    i01.moveHead(80,86)
    i01.moveArm("left",5,96,25,10)
    i01.moveArm("right",5,94,26,10)
    i01.moveHand("left",110,62,56,88,81,18)
    i01.moveHand("right",78,88,101,95,81,137)
    i01.moveTorso(90,90,90)
    sleep(0.2)
    i01.moveHead(75,97)
    i01.moveArm("left",85,106,25,18)
    i01.moveArm("right",87,107,32,18)
    i01.moveHand("left",110,62,56,88,81,145)
    i01.moveHand("right",78,88,101,95,81,27)
    i01.moveTorso(90,90,90)
    i01.mouth.speakBlocking("who is a french sculptor, designer")
    sleep(0.5)
    i01.moveHead(80,86)
    i01.moveArm("left",5,96,25,10)
    i01.moveArm("right",5,94,26,10)
    i01.moveHand("left",110,62,56,88,81,18)
    i01.moveHand("right",78,88,101,95,81,137)
    i01.moveTorso(90,90,90)
    sleep(1)
    i01.moveHead(75,97)
    i01.moveArm("left",6,91,22,14)
    i01.moveArm("right",87,107,32,18)
    i01.moveHand("left",110,62,56,88,81,0)
    i01.moveHand("right",78,88,101,95,81,27)
    i01.moveTorso(90,90,90)
    sleep(1)
    i01.moveHead(20,69)
    i01.moveArm("left",6,91,22,14)
    i01.moveArm("right",87,107,32,21)
    i01.moveHand("left",110,62,56,88,81,0)
    i01.moveHand("right",78,88,101,95,81,27)
    i01.moveTorso(90,90,90)
    i01.mouth.speakBlocking("I am totally build with 3 D printed parts")
    i01.moveHead(75,97)
    i01.moveArm("left",85,106,25,18)
    i01.moveArm("right",87,107,32,18)
    i01.moveHand("left",110,62,56,88,81,145)
    i01.moveHand("right",78,88,101,95,81,27)
    i01.moveTorso(90,90,90)
    sleep(1)
    i01.moveHead(33,110)
    i01.moveArm("left",85,104,25,18)
    i01.moveArm("right",87,41,47,18)
    i01.moveHand("left",110,62,56,88,81,145)
    i01.moveHand("right",111,75,117,125,111,143)
    i01.moveTorso(90,90,90)
    sleep(1)
    i01.moveHead(62,102)
    i01.moveArm("left",85,104,25,18)
    i01.moveArm("right",87,41,47,18)
    i01.moveHand("left",110,62,56,88,81,145)
    i01.moveHand("right",111,75,117,125,111,143)
    i01.moveTorso(90,90,90)
    i01.mouth.speakBlocking("which means all my parts")
    i01.moveHead(79,88)
    i01.moveArm("left",85,104,25,18)
    i01.moveArm("right",87,59,46,18)
    i01.moveHand("left",110,62,56,88,81,145)
    i01.moveHand("right",59,75,117,125,111,113)
    i01.moveTorso(90,90,90)
    i01.mouth.speakBlocking("are made on a home 3 D printer")
    sleep(1)
    i01.moveHead(40,84)
    i01.moveArm("left",85,72,38,18)
    i01.moveArm("right",87,64,47,18)
    i01.moveHand("left",124,97,66,120,130,35)
    i01.moveHand("right",59,75,117,125,111,113)
    i01.moveTorso(90,90,90)
    i01.mouth.speakBlocking("each parts are design to fit 12 centimeter cube build area")
    sleep(1)
    i01.moveHead(97,80)
    i01.moveArm("left",85,79,39,14)
    i01.moveArm("right",87,76,42,12)
    i01.moveHand("left",124,97,66,120,130,35)
    i01.moveHand("right",59,75,117,125,111,113)
    i01.moveTorso(90,90,90)
    sleep(0.5)
    i01.moveHead(75,97)
    i01.moveArm("left",85,106,25,18)
    i01.moveArm("right",87,107,32,18)
    i01.moveHand("left",110,62,56,88,81,145)
    i01.moveHand("right",78,88,101,95,81,27)
    i01.moveTorso(90,90,90)
    sleep(1)
    i01.mouth.speakBlocking("so anyone can reproduce me")
    fullspeed()
    i01.moveHead(80,98)
    i01.moveArm("left",5,90,30,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",45,40,30,25,35,90)
    i01.moveHand("right",55,2,50,48,30,90)
    i01.moveTorso(90,90,90)
    sleep(1)
    i01.mouth.speakBlocking("cool, don't you think")
    armsdown()

def muscle():
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 0.75, 0.85, 0.95, 0.85)
  i01.setArmSpeed("left", 0.75, 0.85, 0.95, 0.85)
  i01.setHeadSpeed(0.65, 0.65)
  i01.setTorsoSpeed(0.75, 0.55, 1.0)
  i01.moveHead(90,129)
  i01.moveArm("left",90,139,48,75)
  i01.moveArm("right",71,40,14,43)
  i01.moveHand("left",180,180,180,180,180,148)
  i01.moveHand("right",99,130,152,154,145,180)
  i01.moveTorso(120,100,90)
  sleep(4)
  i01.mouth.speakBlocking("Looks good, doesn't it")
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(0.85, 0.85)
  i01.setTorsoSpeed(0.75, 0.55, 1.0)
  i01.moveHead(90,45)
  i01.moveArm("left",44,46,20,39)
  i01.moveArm("right",90,145,58,74)
  i01.moveHand("left",180,180,180,180,180,83)
  i01.moveHand("right",99,130,152,154,145,21)
  i01.moveTorso(60,75,90)
  sleep(5)
  i01.mouth.speakBlocking("not bad either, don't you think")
  i01.moveHead(90,80,80,90,10)
  armsdown()
  i01.moveTorso(90,90,90)
  sleep(1)

def pictureleftrightside():
    i01.setArmSpeed("right", 0.85, 0.85, 0.85, 0.85)
    i01.setArmSpeed("left", 0.75, 0.85, 0.95, 0.85)
    i01.moveArm("left",90,105,24,75)
    i01.moveArm("right",90,115,23,68)
 
def pictureleftside():
    i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
    i01.setArmSpeed("left", 0.75, 0.85, 0.95, 0.85)
    i01.moveArm("left",90,105,24,75)
    i01.moveArm("right",5,82,28,15)
 
def picturerightside():
    i01.setArmSpeed("right", 0.85, 0.85, 0.85, 0.85)
    i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
    i01.moveArm("left",5,94,28,15)
    i01.moveArm("right",10,135,-13,68)

def servos():  
    handclose()
    sleep(1)
    i01.setArmSpeed("right", 0.85, 0.85, 0.85, 0.85)
    i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
    i01.setHeadSpeed(0.65, 0.65)
    i01.moveHead(79,100)
    i01.moveArm("left",5,119,28,15)
    i01.moveArm("right",5,111,28,15)
    i01.mouth.speakBlocking("I currently have 31  hobby servos installed in my body to give me life")
    i01.setHandSpeed("left", 0.85, 0.90, 0.85, 0.85, 0.85, 0.85)
    i01.setArmSpeed("right", 0.85, 0.85, 0.85, 0.85)
    i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
    i01.setHeadSpeed(0.65, 0.65)
    i01.moveHead(124,90)
    i01.moveArm("left",89,94,91,35)
    i01.moveArm("right",20,67,31,22)
    i01.moveHand("left",106,0,161,147,138,90)
    sleep(0.5)
    i01.mouth.speakBlocking("there's one servo  for moving my mouth up and down")
    sleep(1)
    i01.setHandSpeed("left", 0.85, 0.85, 1.0, 0.85, 0.85, 0.85)
    i01.setArmSpeed("right", 0.85, 0.85, 0.85, 0.85)
    i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
    i01.setHeadSpeed(0.65, 0.65)
    i01.moveHead(105,76);
    i01.moveArm("left",89,106,103,35);
    i01.moveArm("right",35,67,31,22);
    i01.moveHand("left",106,0,0,147,138,7);
    i01.mouth.speakBlocking("two for my eyes")
    sleep(0.2)
    i01.setHandSpeed("left", 0.85, 0.85, 1.0, 1.0, 1.0, 0.85)
    i01.moveHand("left",106,0,0,0,0,7);
    i01.mouth.speakBlocking("and two more for my head")
    sleep(0.5)
    i01.setHandSpeed("left", 0.85, 0.9, 0.9, 0.9, 0.9, 0.85)
    i01.setArmSpeed("right", 0.85, 0.85, 0.85, 0.85)
    i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
    i01.setHeadSpeed(0.65, 0.65)
    i01.moveHead(90,40);
    i01.moveArm("left",89,106,103,35);
    i01.moveArm("right",35,67,31,20);
    i01.moveHand("left",106,140,140,140,140,7);
    i01.mouth.speakBlocking("so i can look around")
    sleep(0.5)
    i01.setHeadSpeed(0.65, 0.65)
    i01.moveHead(105,125);
    i01.setArmSpeed("left", 0.9, 0.9, 0.9, 0.9)
    i01.moveArm("left",60,100,85,30);
    i01.mouth.speakBlocking("and see who's there")
    i01.setHeadSpeed(0.65, 0.65)
    i01.moveHead(40,56);
    sleep(0.5)
    i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0);
    i01.setArmSpeed("right", 0.5, 0.6, 0.5, 0.6);
    i01.moveArm("left",87,41,64,11)
    i01.moveArm("right",5,95,40,11)
    i01.moveHand("left",98,150,160,160,160,104)
    i01.mouth.speakBlocking("there's three servos  in each shoulder")
    i01.moveHead(40,67);
    sleep(2)
    i01.setHandSpeed("left", 0.8, 0.9, 0.8, 0.8, 0.8, 0.8)
    i01.setArmSpeed("right", 0.85, 0.85, 0.85, 0.85)
    i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
    i01.setHeadSpeed(0.8, 0.8)
    i01.moveHead(43,69)
    i01.moveArm("left",87,41,64,11)
    i01.moveArm("right",5,95,40,42)
    i01.moveHand("left",42,0,100,80,113,35)
    i01.moveHand("left",42,10,160,180,160,35)
    i01.mouth.speakBlocking("here is the first servo movement")
    sleep(1)
    i01.moveHead(37,60);
    i01.setHandSpeed("left", 1.0, 1.0, 0.9, 0.9, 1.0, 0.8)
    i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
    i01.moveArm("right",5,95,67,42)
    i01.moveHand("left",42,0,0,150,160,30)
    i01.mouth.speakBlocking("this is the second one")
    sleep(1)
    i01.moveHead(43,69);
    i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
    i01.moveArm("right",5,134,67,42)
    i01.moveHand("left",42,0,0,0,160,35)
    i01.mouth.speakBlocking("now you see the third")
    sleep(1)
    i01.setArmSpeed("right", 0.8, 0.8, 0.8, 0.8)
    i01.moveArm("right",20,90,45,16)
    i01.mouth.speakBlocking("they give me a more human like movement")
    sleep(1)
    i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
    i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0);
    i01.moveHead(43,72)
    i01.moveArm("left",90,44,66,11)
    i01.moveArm("right",90,100,67,26)
    i01.moveHand("left",42,80,100,80,113,35)
    i01.mouth.speakBlocking("but, i have only  one servo, to move each elbow")
    i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
    i01.setArmSpeed("right", 0.85, 0.85, 0.85, 0.85)
    i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
    i01.setHeadSpeed(0.8, 0.8)
    i01.moveHead(45,62)
    i01.moveArm("left",72,90,90,11)
    i01.moveArm("right",90,95,68,15)
    i01.moveHand("right",20,0,180,180,180,0)
    i01.mouth.speakBlocking("that, leaves me, with one servo per wrist")
    i01.moveHead(40,60)
    i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
    i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
    i01.mouth.speak("and one servo for each finger.")
    i01.moveHead(90,90)
    
    i01.moveHand("right",10,120,120,120,120,90)
    sleep(0.5)
    i01.moveHand("right",20,0,180,180,180,0)
    sleep(0.5)
    i01.moveHand("right",10,10,10,120,120,90)
    sleep(0.5)
    i01.moveHand("right",10,10,10,10,120,90)
    sleep(0.5)
    i01.moveHand("right",10,10,10,10,10,90)
    sleep(0.5)
    i01.moveHand("right",10,10,10,10,180,90)
    sleep(0.3)
    i01.moveHand("right",10,10,10,180,180,90)
    sleep(0.3)
    i01.moveHand("right",10,10,180,180,180,90)
    sleep(0.3)
    i01.moveHand("right",10,180,180,180,180,90)
    sleep(0.3) 
           
    i01.mouth.speak("these servos are located in my forearms")
    
    i01.moveHand("left",10,140,168,168,158,90)
    sleep(0.3)
    i01.moveHand("left",10,10,168,168,158,90)
    sleep(0.3)
    i01.moveHand("left",10,10,0,168,158,90)
    sleep(0.3)
    i01.moveHand("left",10,10,0,10,158,90)
    sleep(0.3)
    i01.moveHand("left",10,10,0,10,10,90)
    sleep(0.5)
    i01.moveHand("left",10,10,10,10,158,90)
    sleep(0.3)
    i01.moveHand("left",10,10,10,168,158,90)        
    sleep(0.3)
    i01.moveHand("left",10,10,168,168,158,90)
    sleep(0.3)
    i01.moveHand("left",10,140,168,168,158,90)
    
    handclose()
    i01.setArmSpeed("right", 0.75, 0.85, 0.95, 0.85)
    i01.setArmSpeed("left", 0.95, 0.65, 0.75, 0.75)
    i01.setHeadSpeed(0.75, 0.75)
    i01.moveHead(20,100)
    i01.moveArm("left",71,94,41,31)
    i01.moveArm("right",5,82,28,15)
    sleep(1)
    i01.mouth.speakBlocking("in my left forearm i have 4 extra servos that i am testing")
    i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
    lefthandopen()
    sleep(1)
    thumbfine.moveTo(150)
    indexfine.moveTo(110)
    majeurefine.moveTo(90)
    sleep(1)
    i01.setHandSpeed("left", 0.9, 0.9, 0.8, 0.9, 0.9, 1.0)
    i01.moveHand("left",180,2,2,40,40,90)
    sleep(2)
    i01.moveHand("left",180,75,55,40,40,90)
    i01.mouth.speakBlocking("they increase my fine motor skills")
    sleep(1)
    i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
    thumbfine.moveTo(0)
    indexfine.moveTo(0)
    majeurefine.moveTo(0)
    sleep(1)
    lefthandopen()
    sleep(1)
    lefthandclose()
    headfront()
    i01.mouth.speakBlocking("they are hooked up, by the use of tendons")
    i01.moveHand("left",10,20,30,40,60,150);
    i01.moveHand("right",110,137,120,100,105,130);
    i01.setHeadSpeed(1,1)
    i01.setArmSpeed("right", 1.0,1.0, 1.0, 1.0);
    i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0);
    sleep(2)
    i01.mouth.speak("i also have 2 servos in my waist so i can move sideways")
    handclose()
    Torso()
    sleep(2)
    i01.moveArm("left",90,45,52,10)
    i01.moveArm("right",20,67,72,22)
    i01.moveHand("left",106,0,161,147,138,90)
    i01.moveHand("right",0,0,0,54,91,90)
    i01.mouth.speak("my sensors on my forearms are working now")
    sleep(3)
    i01.mouth.speak("so i can feel when you are touching me")
    sleep(3)
    armsdown()
    handclose()
    i01.mouth.speak("and as you can see i now have wheels")
    sleep(5)
    serial.write("8") 
    serial.write("8")
    serial.write("8")
    serial.write("8")
    serial.write("8")
    serial.write("8")
    serial.write("8")
    serial.write("8")
    serial.write("8")
    serial.write("8")
    sleep(2)
    serial.write("5")
    serial.write("5")
    serial.write("5")
    serial.write("5")
    serial.write("5")
    serial.write("5")
    serial.write("5")
    serial.write("5")
    serial.write("5")
    serial.write("5")
    serial.write("5")
    serial.write("5")
    i01.mouth.speak("i can drive forward and backward")
    serial.write("2") 
    serial.write("2") 
    serial.write("2") 
    serial.write("2") 
    serial.write("2") 
    serial.write("2") 
    serial.write("2") 
    serial.write("2") 
    serial.write("2") 
    sleep(2.5)
    serial.write("5")
    serial.write("5")
    serial.write("5")
    serial.write("5")
    serial.write("5")
    serial.write("5")
    serial.write("5")
    serial.write("5")
    serial.write("5")
    serial.write("5")
    serial.write("5")
    serial.write("5")
    sleep(1)
    i01.mouth.speak("turn left and right")
    serial.write("4") 
    serial.write("4") 
    serial.write("4") 
    serial.write("4") 
    serial.write("4") 
    serial.write("4") 
    serial.write("4")
    serial.write("4") 
    serial.write("4") 
    sleep(2)
    serial.write("5")
    serial.write("5")
    serial.write("5")
    serial.write("5")
    serial.write("5")
    serial.write("5")
    serial.write("5")
    serial.write("5")
    serial.write("5")
    serial.write("5")
    serial.write("5")
    serial.write("5")
    serial.write("6") 
    serial.write("6") 
    serial.write("6") 
    serial.write("6") 
    serial.write("6") 
    serial.write("6") 
    serial.write("6") 
    serial.write("6") 
    serial.write("6") 
    sleep(2.5)
    serial.write("5") 
    serial.write("5") 
    serial.write("5") 
    serial.write("5") 
    serial.write("5") 
    serial.write("5") 
    serial.write("5")
    serial.write("5") 
    serial.write("5") 
    serial.write("5") 
    serial.write("5") 
    i01.mouth.speak("with these special wheels i also can go sideways.")
    sleep(4)
    serial.write("9") 
    serial.write("9") 
    serial.write("9") 
    serial.write("9") 
    serial.write("9") 
    serial.write("9") 
    serial.write("9") 
    serial.write("9") 
    serial.write("9") 
    serial.write("9") 
    sleep(2)
    serial.write("5") 
    serial.write("5") 
    serial.write("5") 
    serial.write("5") 
    serial.write("5") 
    serial.write("5") 
    serial.write("5") 
    serial.write("5") 
    serial.write("5") 
    serial.write("5") 
    serial.write("5") 
    serial.write("7") 
    serial.write("7")
    serial.write("7") 
    serial.write("7")
    serial.write("7") 
    serial.write("7")
    serial.write("7")
    serial.write("7")
    serial.write("7")
    sleep(2.5)
    serial.write("5") 
    serial.write("5") 
    serial.write("5") 
    serial.write("5") 
    serial.write("5") 
    serial.write("5") 
    serial.write("5") 
    serial.write("5") 
    serial.write("5") 
    serial.write("5") 
    serial.write("5") 
    i01.mouth.speak("it feels good to be able to move around")
    sleep(2)
    sleep(2)
    fullspeed()
    armsdown()

##########################################################################################


def relax():
  i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
  i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
  i01.setArmSpeed("right", 0.75, 0.85, 0.65, 0.85)
  i01.setArmSpeed("left", 0.95, 0.65, 0.75, 0.75)
  i01.setHeadSpeed(0.85, 0.85, 1.0, 1.0, 1.0)
  i01.setTorsoSpeed(0.75, 0.55, 1.0)
  i01.moveHead(79,100,90,90,70)
  i01.moveArm("left",5,84,28,15)
  i01.moveArm("right",5,82,28,15)
  i01.moveHand("left",92,33,37,71,66,25)
  i01.moveHand("right",81,66,82,60,105,113)
  i01.moveTorso(90,90,90)

def hello():
  x = (random.randint(1, 5))
  if x == 1:
      i01.mouth.speak("hello")
  if x == 2:
      i01.mouth.speak("hi")
  if x == 3:
      i01.mouth.speak("welcome") 
  if x == 4:
      i01.mouth.speak("nice to meet you")
  if x == 5:
      i01.mouth.speak("what a lovely day")

  x = (random.randint(1, 5))
  if x == 1:
      i01.mouth.speak("i'm glad i have your attention")
  if x == 2:
      i01.mouth.speak("i'm robyn inmoov")
  if x == 3:
      i01.mouth.speak("my name is robyn") 
  if x == 4:
      i01.mouth.speak("i'm a inmoov robot")
  if x == 5:
      i01.mouth.speak("i'm made in sweden")

  x = (random.randint(1, 5))
  if x == 1:
      i01.mouth.speak("i'm a humanoid robot")
  if x == 2:
      i01.mouth.speak("my body is made of plastic")
  if x == 3:
      i01.mouth.speak("i'm 3 d printed") 
  if x == 4:
      i01.mouth.speak("my robot lab is the software that controls me") 
  if x == 5:
      i01.mouth.speak("there are 2 arduino mega on my back") 

  x = (random.randint(1, 5))
  if x == 1:
      i01.mouth.speak("i have pressure sensors on my forearms")
  if x == 2:
      i01.mouth.speak("i have cameras in my eyes")
  if x == 3:
      i01.mouth.speak("i have a kinect in my chest") 
  if x == 4:
      i01.mouth.speak("i have voice recognition") 
  if x == 5:
      i01.mouth.speak("i have mecanum wheels")

  x = (random.randint(1, 5))
  if x == 1:
      i01.mouth.speak("and i have a lot of servos")
  if x == 2:
      i01.mouth.speak("and can be controlled from a keyboard")
  if x == 3:
      i01.mouth.speak("and microphones in my ears") 
  if x == 4:
      i01.mouth.speak("and i have face recognition")
  if x == 5:
      i01.mouth.speak("and a computer on my back")
      
  x = (random.randint(1, 5))
  if x == 1:
      i01.mouth.speak("i can move very human like")
  if x == 2:
      i01.mouth.speak("please take a look at my mechanics")
  if x == 3:
      i01.mouth.speak("i'm a open source project") 
  if x == 4:
      i01.mouth.speak("please take a look at my electronics") 
  if x == 5:
      i01.mouth.speak("we can be friends on facebook")
      
  x = (random.randint(1, 5))
  if x == 1:
      i01.mouth.speak("you can ask my maker if you have any questions")
  if x == 2:
      i01.mouth.speak("this is great")
  if x == 3:
      i01.mouth.speak("i really like being here") 
  if x == 4: 
      i01.mouth.speak("i am having so much fun") 
  if x == 5:
      i01.mouth.speak("take a look on my videos on youtube")

def follow():
    for y in range(0, 40): 
        if i01.head.rothead.getPos() >= 100:
            serial.write("4") 
            sleep(0.5)
            serial.write("5") 
            sleep(0.5)
        elif i01.head.rothead.getPos() <= 60:
            serial.write("6") 
            sleep(0.5)
            serial.write("5") 
            sleep(0.5)            
        else : 
            sleep(1)   
        print (i01.head.rothead.getPos())
    i01.mouth.speak("ok")    
    
##########################################################################################

def handopen():
    i01.moveHand("left",0,0,0,0,0)
    i01.moveHand("right",0,0,0,0,0)

def lefthandopen():
    i01.moveHand("left",0,0,0,0,0)

def righthandopen():
    i01.moveHand("right",0,0,0,0,0)

def handclose():
    i01.setHandSpeed("right", 0.8, 1.0, 1.0, 1.0, 1.0, 1.0)
    i01.setHandSpeed("left", 0.8, 1.0, 1.0, 1.0, 1.0, 1.0)
    i01.moveHand("left",180,180,180,180,180)
    i01.moveHand("right",180,180,180,180,180)
    sleep (0.3)
    i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
    i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
    i01.moveHand("left",180,180,180,180,180)
    i01.moveHand("right",180,180,180,180,180)

def lefthandclose():
    i01.setHandSpeed("left", 0.8, 1.0, 1.0, 1.0, 1.0, 1.0)
    i01.moveHand("left",180,180,180,180,180)
    sleep (0.3)
    i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
    i01.moveHand("left",180,180,180,180,180)

def righthandclose():
    i01.setHandSpeed("right", 0.8, 1.0, 1.0, 1.0, 1.0, 1.0)
    i01.moveHand("right",180,180,180,180,180)
    sleep (0.3)
    i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
    i01.moveHand("right",180,180,180,180,180)


def headfront():
    i01.head.neck.moveTo(90)
    i01.head.rothead.moveTo(80)

def headdown():
    i01.head.neck.moveTo(20)

def headupp():
    i01.head.neck.moveTo(160)
    
def headright():
    i01.head.rothead.moveTo(30)
    
def headleft():
    i01.head.rothead.moveTo(140)

def eyesfront():
    i01.head.eyeX.moveTo(70)
#    lefteye.moveTo(80)
    i01.head.eyeY.moveTo(85)
    
def eyesfrontY():
    i01.head.eyeY.moveTo(85)

def eyesfrontX():
    i01.head.eyeX.moveTo(70)
#    lefteye.moveTo(80)
    
def eyesdown():
    i01.head.eyeY.moveTo(100)
    
def eyesupp():
    i01.head.eyeY.moveTo(50)

def eyesright():
    i01.head.eyeX.moveTo(60)
#    lefteye.moveTo(60)

def eyesleft():
    i01.head.eyeX.moveTo(100)
#    lefteye.moveTo(100)

def armsdown():
    i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
    i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
    i01.moveArm("left",5,90,30,10)
    i01.moveArm("right",5,90,30,15)


def armsfront():
    i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
    i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
    i01.moveArm("left",5,90,110,10)
    i01.moveArm("right",5,90,110,10)

def Torso():
    i01.setTorsoSpeed(1.0, 1.0, 1.0)
    i01.moveTorso(60,90,90)
    sleep(2)
    i01.moveTorso(110,90,90)
    sleep(2)
    i01.moveTorso(90,90,90)
    sleep(2)

def facetrack():
    if blind == 1:
        trackHumans()
        global blind
        blind = 0  
    elif blind == 0:
        stopTracking()
        global blind
        blind = 1

def trackHumans():
     i01.mouth.speak("facetrack on")
     i01.headTracking.faceDetect()
#     i01.eyesTracking.faceDetect()
     fullspeed()

def trackPoint():
     i01.headTracking.startLKTracking()
     i01.eyesTracking.startLKTracking()
     fullspeed()

def stopTracking():
     i01.mouth.speak("facetrack off")
     i01.headTracking.stopTracking()
#     i01.eyesTracking.stopTracking()


def opencloseleftH():
    if opencloselefthand == 0:
        lefthandclose()
        global opencloselefthand
        opencloselefthand = 1
    elif opencloselefthand == 1:
        lefthandopen()
        global opencloselefthand
        opencloselefthand = 0

def opencloserightH():
    if opencloserighthand == 0:
        righthandclose()
        global opencloserighthand
        opencloserighthand = 1
    elif opencloserighthand == 1:
        righthandopen()
        global opencloserighthand
        opencloserighthand = 0

def printCapture():
    print(i01.captureGesture())     

def reactarmL():
    x = (random.randint(1, 11))
    if x == 1:
        i01.mouth.speak("yes")
    if x == 2:
        i01.mouth.speak("it's ok")
    if x == 3:
        i01.mouth.speak("arm sensors working")
    if x == 4:
        i01.mouth.speak("i can feel you touching me")
    if x == 5:
        i01.mouth.speak("cool")
    if x == 6:
        i01.mouth.speak("you got my attention")
    if x == 7:
        i01.mouth.speak("lowly")
    if x == 8:
        i01.mouth.speak("very good")
    if x == 9:
        i01.mouth.speak("good")
    if x == 10:
        i01.mouth.speak("nice")
    if x == 11:
        i01.mouth.speak("ok")
        
    x = (random.randint(1, 8))
    if x == 1:
        i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
        i01.leftArm.rotate.moveTo(i01.leftArm.rotate.getPos() - 10)
        sleep(2)
        i01.leftArm.rotate.moveTo(i01.leftArm.rotate.getPos() + 10)
    if x == 2:
        i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
        i01.leftArm.rotate.moveTo(i01.leftArm.rotate.getPos() + 10)
        sleep(2)
        i01.leftArm.rotate.moveTo(i01.leftArm.rotate.getPos() - 10)
    if x == 3:
        i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
        i01.leftArm.rotate.moveTo(i01.leftArm.rotate.getPos() - 10)
        i01.leftArm.bicep.moveTo(i01.leftArm.bicep.getPos() + 10)
        sleep(2)
        i01.leftArm.rotate.moveTo(i01.leftArm.rotate.getPos() + 10)
        i01.leftArm.bicep.moveTo(i01.leftArm.bicep.getPos() - 10)
    if x == 4:
        i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
        i01.leftArm.rotate.moveTo(i01.leftArm.rotate.getPos() - 10)
        i01.leftArm.bicep.moveTo(i01.leftArm.bicep.getPos() - 10)
        sleep(2)
        i01.leftArm.rotate.moveTo(i01.leftArm.rotate.getPos() + 10)
        i01.leftArm.bicep.moveTo(i01.leftArm.bicep.getPos() + 10)
    if x == 5:
        i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
        i01.leftArm.rotate.moveTo(i01.leftArm.rotate.getPos() + 10)
        i01.leftArm.bicep.moveTo(i01.leftArm.bicep.getPos() + 10)
        sleep(2)
        i01.leftArm.rotate.moveTo(i01.leftArm.rotate.getPos() - 10)
        i01.leftArm.bicep.moveTo(i01.leftArm.bicep.getPos() - 10)
    if x == 6:
        i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
        i01.leftArm.rotate.moveTo(i01.leftArm.rotate.getPos() + 10)
        i01.leftArm.bicep.moveTo(i01.leftArm.bicep.getPos() - 10)
        sleep(2)
        i01.leftArm.rotate.moveTo(i01.leftArm.rotate.getPos() - 10)
        i01.leftArm.bicep.moveTo(i01.leftArm.bicep.getPos() + 10)
    if x == 7:
        i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
        i01.leftArm.bicep.moveTo(i01.leftArm.bicep.getPos() + 10)
        sleep(2)
        i01.leftArm.bicep.moveTo(i01.leftArm.bicep.getPos() - 10)
    if x == 8:
        i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
        i01.leftArm.bicep.moveTo(i01.leftArm.bicep.getPos() - 10)
        sleep(2)
        i01.leftArm.bicep.moveTo(i01.leftArm.bicep.getPos() + 10)
    headfront()    
        
def reactarmR():
    x = (random.randint(1, 11))
    if x == 1:
        i01.mouth.speak("yes")
    if x == 2:
        i01.mouth.speak("it's ok")
    if x == 3:
        i01.mouth.speak("arm sensors working")
    if x == 4:
        i01.mouth.speak("i can feel you touching me")
    if x == 5:
        i01.mouth.speak("cool")
    if x == 6:
        i01.mouth.speak("you got my attention")
    if x == 7:
        i01.mouth.speak("lowly")
    if x == 8:
        i01.mouth.speak("very good")
    if x == 9:
        i01.mouth.speak("good")
    if x == 10:
        i01.mouth.speak("nice")
    if x == 11:
        i01.mouth.speak("ok")

    x = (random.randint(1, 8))
    if x == 1:
        i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
        i01.rightArm.rotate.moveTo(i01.rightArm.rotate.getPos() - 10)
        sleep(2)
        i01.rightArm.rotate.moveTo(i01.rightArm.rotate.getPos() + 10)
    if x == 2:
        i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
        i01.rightArm.rotate.moveTo(i01.rightArm.rotate.getPos() + 10)
        sleep(2)
        i01.rightArm.rotate.moveTo(i01.rightArm.rotate.getPos() - 10)
    if x == 3:
        i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
        i01.rightArm.rotate.moveTo(i01.rightArm.rotate.getPos() - 10)
        i01.rightArm.bicep.moveTo(i01.rightArm.bicep.getPos() + 10) 
        sleep(2)
        i01.rightArm.rotate.moveTo(i01.rightArm.rotate.getPos() + 10)
        i01.rightArm.bicep.moveTo(i01.rightArm.bicep.getPos() - 10) 
    if x == 4:
        i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
        i01.rightArm.rotate.moveTo(i01.rightArm.rotate.getPos() - 10)
        i01.rightArm.bicep.moveTo(i01.rightArm.bicep.getPos() - 10) 
        sleep(2)
        i01.rightArm.rotate.moveTo(i01.rightArm.rotate.getPos() + 10)
        i01.rightArm.bicep.moveTo(i01.rightArm.bicep.getPos() + 10) 
    if x == 5:
        i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
        i01.rightArm.rotate.moveTo(i01.rightArm.rotate.getPos() + 10)
        i01.rightArm.bicep.moveTo(i01.rightArm.bicep.getPos() + 10) 
        sleep(2)
        i01.rightArm.rotate.moveTo(i01.rightArm.rotate.getPos() - 10)
        i01.rightArm.bicep.moveTo(i01.rightArm.bicep.getPos() - 10) 
    if x == 6:
        i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
        i01.rightArm.rotate.moveTo(i01.rightArm.rotate.getPos() + 10)
        i01.rightArm.bicep.moveTo(i01.rightArm.bicep.getPos() - 10) 
        sleep(2)
        i01.rightArm.rotate.moveTo(i01.rightArm.rotate.getPos() - 10)
        i01.rightArm.bicep.moveTo(i01.rightArm.bicep.getPos() + 10) 
    if x == 7:
        i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
        i01.rightArm.bicep.moveTo(i01.rightArm.bicep.getPos() + 10) 
        sleep(2)
        i01.rightArm.bicep.moveTo(i01.rightArm.bicep.getPos() - 10) 
    if x == 8:
        i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
        i01.rightArm.bicep.moveTo(i01.rightArm.bicep.getPos() - 10) 
        sleep(2)
        i01.rightArm.bicep.moveTo(i01.rightArm.bicep.getPos() + 10) 
    headfront()

def fullspeed():
    i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
    i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
    i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
    i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
    i01.setHeadSpeed(0.9, 0.9)
            
##########################################################################################

def red():
    left.digitalWrite(42, 1) # ON
    left.digitalWrite(43, 1) # ON
    left.digitalWrite(44, 1) # ON
    left.digitalWrite(45, 0) # OFF


def green():
    left.digitalWrite(42, 1) # ON
    left.digitalWrite(43, 0) # OFF
    left.digitalWrite(44, 1) # ON
    left.digitalWrite(45, 1) # ON

def blue():
    left.digitalWrite(42, 1) # ON
    left.digitalWrite(43, 1) # ON
    left.digitalWrite(44, 0) # OFF
    left.digitalWrite(45, 1) # ON

def ledoff():
    left.digitalWrite(42, 0) # OFF
    left.digitalWrite(43, 0) # OFF
    left.digitalWrite(44, 0) # OFF
    left.digitalWrite(45, 0) # OFF
##########################################################################################
    
