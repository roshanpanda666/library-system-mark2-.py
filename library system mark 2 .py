while True:
    start=input("press start to continue")
    
    if(start=="start"):
        import datetime
        d=datetime= datetime.datetime.now()
        d=str(d)
        import speech_recognition as sr
        import pyttsx3

        r = sr.Recognizer()


        def SpeakText(command):
            
            # Initialize the engine
            engine = pyttsx3.init()
            engine.say(command)
            engine.runAndWait()


        with sr.Microphone() as source2:
            SpeakText("what is your name")
            audio2 = r.listen(source2)
                
            MyText =r.recognize_google(audio2)

            f=open("library2.txt","a")
            a=f.write("\nname= "+MyText)
            print(MyText)


        with sr.Microphone() as source2:
            SpeakText("what is your class")
            audio3 = r.listen(source2)
                
            text2 =r.recognize_google(audio3)

            f=open("library2.txt","a")
            a=f.write("\nclass= "+text2)   
            print(text2)     

        
        with sr.Microphone() as source2:
            SpeakText("what is your roll number")
            audio4 = r.listen(source2)
                
            text3 =r.recognize_google(audio4)

            f=open("library2.txt","a")
            a=f.write("\nroll= "+text3)  
            print(text3) 

        with sr.Microphone() as source2:
            SpeakText("what is the book you have taken")
            audio5 = r.listen(source2)
                
            text4 =r.recognize_google(audio5)

            f=open("library2.txt","a")
            a=f.write("\nbook= "+text4)  
            print(text4)  

        

            f=open("library2.txt","a")
            a=f.write("\ndate and time = "+d)  
            print(text4)

            f=open("library2.txt","a")
            a=f.write("\n---------------------------------------------------------------------------------------")

            
            print("you have successfully saved ")
            print("----------------------------------------------------")

    SpeakText("data entry, is successfully done, you can go now,")
    f=open("library2.txt","a")
