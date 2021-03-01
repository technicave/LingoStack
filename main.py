from tkinter import *
from tkinter import ttk
import socket
import tkinter.messagebox as thh
from gtts import gTTS 
from playsound import playsound
import time
import os
import pygame
import random
import shutil
import speech_recognition as sr 
from PyDictionary import PyDictionary 
import webbrowser
import randfacts 

root = Tk()
root.state("zoomed")
root.title("LingoStack -- By RecordStack")
root.config(bg="#408000")
root.iconbitmap("buttons/lolo.ico")
# secondary color = #1aff1a

#Deleting all functions

def firsts():
    try:
        mainwindow1.destroy()
        value1.destroy()
    except:
        pass

    try:
        mainwindow4.destroy()
        value4.destroy()
    except:
        pass

    try:
        mainwindow.destroy()
        value0.destroy()
        mainwindow2.destroy()
        value2.destroy()
        mainwindow3.destroy()
        value3.destroy()
        mainwindow4.destroy()
        value4.destroy()
        mainwindow1.destroy()
        value1.destroy()


        texttospeech()
    except:
        texttospeech()

def seconds():
    try:
        mainwindow2.destroy()
        value2.destroy()
    except:
        pass

    try:
        mainwindow4.destroy()
        value4.destroy()
    except:
        pass

    try:
        mainwindow.destroy()
        value0.destroy()
        mainwindow1.destroy()
        value1.destroy()
        mainwindow3.destroy()
        value3.destroy()
        mainwindow4.destroy()
        value4.destroy()
        mainwindow2.destroy()
        value2.destroy()
        

       

        listen()
    except Exception as e:
        listen()

def thirds():
    try:
        mainwindow3.destroy()
        value3.destroy()
    except:
        pass

    try:
        mainwindow4.destroy()
        value4.destroy()
    except:
        pass

    try:
        mainwindow.destroy()
        value0.destroy()
        mainwindow1.destroy()
        value1.destroy()
        mainwindow2.destroy()
        value2.destroy()
        mainwindow4.destroy()
        value4.destroy()
        mainwindow3.destroy()
        value3.destroy()
        
        

       

        dictionries()
    except Exception as e:
        dictionries()

def forths():
    try:
        mainwindow4.destroy()
        value4.destroy()
    except:
        pass

    try:
        mainwindow3.destroy()
        value3.destroy()
    except:
        pass

    try:
        mainwindow.destroy()
        value0.destroy()
        mainwindow1.destroy()
        value1.destroy()
        mainwindow2.destroy()
        value2.destroy()
        mainwindow3.destroy()
        value3.destroy()
        mainwindow4.destroy()
        value4.destroy()


       

        factsfunc()
    except Exception as e:
        factsfunc()



#main functions



#default functions



def texttospeech():
    global mainwindow1
    global value1
    
    mainwindow1 = Frame(root, bg="#408000")
    mainwindow1.pack(side=TOP, fill=BOTH)

    value1 = Frame(mainwindow1 ,bg="#000066", borderwidth=5)
    value1.pack(side=TOP, fill=X)

    language = StringVar()
    language.set("en")
    

    english = Radiobutton(value1,selectcolor="black",cursor="hand2",activebackground="#000066",activeforeground="yellow" ,bg="#000066", fg="yellow" ,text="English",font="lucida 15" ,value="en" ,variable=language)
    english.grid(row=0, column=0, padx=20, pady=20)
    
    hindi = Radiobutton(value1,selectcolor="black",cursor="hand2",activebackground="#000066",activeforeground="yellow" ,bg="#000066", fg="yellow" ,text="Hindi",font="lucida 15",value="hi" ,variable=language)
    hindi.grid(row=0, column=1, padx=20, pady=20)

    spanish = Radiobutton(value1,bg="#000066",selectcolor="black",cursor="hand2",activebackground="#000066",activeforeground="yellow" , fg="yellow" ,text="Spanish",font="lucida 15",value="es" ,variable=language)
    spanish.grid(row=0, column=2, padx=20, pady=20)

    french = Radiobutton(value1,bg="#000066", selectcolor="black",cursor="hand2",activebackground="#000066",activeforeground="yellow" ,fg="yellow" ,text="French",font="lucida 15",value="fr" ,variable=language)
    french.grid(row=0, column=3, padx=20, pady=20)

    Chinese = Radiobutton(value1,bg="#000066", selectcolor="black",cursor="hand2",activebackground="#000066",activeforeground="yellow" ,fg="yellow" ,text="Chinese",font="lucida 15",value="zh" ,variable=language)
    Chinese.grid(row=0, column=4, padx=20, pady=20)

    Japanese = Radiobutton(value1,bg="#000066", selectcolor="black",cursor="hand2",activebackground="#000066",activeforeground="yellow" ,fg="yellow" ,text="Japanese",font="lucida 15",value="ja" ,variable=language)
    Japanese.grid(row=0, column=5, padx=20, pady=20)

    def downloadnow():
        try:
            languages =language.get()
            myaudio = gTTS(text=text.get("1.0","end-1c"), lang=languages)

            r1 = random.randint(1,10000000)
            r2 = random.randint(1,10000000)
            randfile = str(r2)+"LingoStack"+str(r1) +".mp3"
            myaudio.save("downloads/" + randfile)
            Ok = thh.showinfo("Downloaded", "Click ok to open the File ")
            if Ok == "ok":
                thh.showinfo('Saved at', "saved at "+ os.getcwd()+ "\downloads")


        except:
            thh.showerror("Failed", "Failed to Download")
           

    def playaudio():
        try:
            
            try:
                os.remove("audios/audio.mp3")

            except:
                pass

            languages =language.get()
            myaudio = gTTS(text=text.get("1.0","end-1c"), lang=languages)

            r1 = random.randint(1,10000000)
            r2 = random.randint(1,10000000)
            randfile = str(r2)+"LingoStack"+str(r1) +".mp3"
            myaudio.save(randfile)
            playsound(randfile)
            os.remove(randfile)
            
        except Exception as e:
            print(e)


    def internet():
        IPaddress=socket.gethostbyname(socket.gethostname())
        if IPaddress=="127.0.0.1":
            thh.showerror("Internet Failed", "Connect to a Internet Connection")
        else:
            print(language.get())
            playaudio()

    play1 = Button(value1, image=play ,cursor="hand2",bg="#000066",activebackground="#000066",borderwidth=0, command=internet)
    play1.grid(row=0, column=6, padx=50)

    download1 = Button(value1, cursor="hand2",image=download ,bg="#000066",activebackground="#000066",borderwidth=0, command=downloadnow)
    download1.grid(row=0, column=7, padx=50)








    scrollbar = Scrollbar(mainwindow1)

    text = Text(mainwindow1,yscrollcommand=scrollbar.set, font="helvetica 19 bold" )
    scrollbar.config(command=text.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    text.pack(fill=BOTH)


def listen():
    global mainwindow2
    global value2
    
    mainwindow2 = Frame(root, bg="#408000")
    mainwindow2.pack(side=TOP, fill=BOTH)

    value2 = Frame(mainwindow2 ,bg="#000066", borderwidth=5)
    value2.pack(side=TOP, fill=X)


    def internetconnection():
        IPaddress=socket.gethostbyname(socket.gethostname())
        if IPaddress=="127.0.0.1":
            thh.showerror("Internet Failed", "Connect to a Internet Connection")
        else:
            headingk.config(text="Listening")
            def mainfunc():
                try:
                    r = sr.Recognizer() 
                    with sr.Microphone() as source2: 
                        r.pause_threshold = 3
                        audio2 = r.listen(source2)
                        text.insert(END, audio2)                         
                except Exception as e:
                    headingk.config(text="Failed to record")
                    thh.showerror("failed", "Failed to Record")


    headingk = Label(value2,fg="yellow" ,text="Ready for Listen", bg="#000066", font="lucida 20 bold")
    headingk.grid(row=0, column=0, padx=300)

    download2 = Button(value2, cursor="hand2",image=recording ,bg="#000066",activebackground="#000066",borderwidth=0, command=internetconnection)
    download2.grid(row=0, column=1)

    


    
    scrollbar = Scrollbar(mainwindow2)

    text = Text(mainwindow2,yscrollcommand=scrollbar.set, font="helvetica 19 bold" )
    scrollbar.config(command=text.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    text.pack(fill=BOTH)


def dictionries():
    global mainwindow3
    global value3

    mainwindow3 = Frame(root, bg="#000000")
    mainwindow3.pack(side=TOP, fill=BOTH)


    value3 = Frame(mainwindow3 ,bg="#000066", borderwidth=5)
    value3.pack(side=TOP, fill=X)

    def searching():
        text.config(state=NORMAL)
        try:
            text.delete('1.0', END)
            dict = PyDictionary("exclusive","precipitation")
            meaning = dict.meaning(box.get()) 
            text.insert(END, meaning) 
            text.config(state=DISABLED)
        except:
            thh.showerror("Failed To Find", "Failed to Find the Word")

    text1 = Label(value3, text="Dictionary - English to English", font="lucida 30 bold", bg="#000066", fg="yellow" )
    text1.pack(side=TOP, pady=20)

    entervalue = Label(mainwindow3, text="Enter Word In This Box", font="lucida 18 bold", fg="white", bg="#000000", pady=10)
    entervalue.pack(side=TOP)

    box = Entry(mainwindow3, font="helvetica 20 bold")
    box.pack(side=TOP, pady=20, padx=8)

    searchs = Button(mainwindow3, image=search ,cursor="hand2",bg="#000000",activebackground="#000000",borderwidth=0, command=searching)
    searchs.pack(side=TOP, pady=5)


    scrollbar = Scrollbar(mainwindow3)

    text = Text(mainwindow3,yscrollcommand=scrollbar.set, font="helvetica 19 bold" )
    scrollbar.config(command=text.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    text.config(state=DISABLED)
    text.pack(fill=BOTH)

def factsfunc():
    global mainwindow4
    global value4

    mainwindow4 = Frame(root, bg="#000000")
    mainwindow4.pack(side=TOP, fill=BOTH)

    value4 = Frame(mainwindow4 ,bg="#000066", borderwidth=5)
    value4.pack(side=TOP, fill=X)

    def factsing():
        xt = randfacts.getFact(True) 
        text.config(state=NORMAL)
        text.delete('1.0', END)
        text.insert(END, xt) 
        text.config(state=DISABLED)


    x = randfacts.getFact(True) 


    refreshing = Button(value4, image=refresh ,cursor="hand2",bg="#000066",activebackground="#000066",borderwidth=0, command=factsing)
    refreshing.pack(side=TOP, padx=50)

    scrollbar = Scrollbar(mainwindow4)

    text = Text(mainwindow4,yscrollcommand=scrollbar.set, font="helvetica 40 bold" )
    scrollbar.config(command=text.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    text.insert(END, x) 
    text.config(state=DISABLED)
    text.pack(fill=BOTH)


# starting window code


value0 = Frame(root ,bg="#000066", borderwidth=5)
value0.pack(side=TOP, fill=X)

value2 = Frame(root, bg="#000066", borderwidth=5)
value2.pack(side=LEFT, fill = Y)

mainwindow = Frame(root, bg="#408000")
mainwindow.pack(side=TOP, fill=BOTH)

button1 = PhotoImage(file="buttons/text2speech.png")
button2 = PhotoImage(file="buttons/speak.png")
button3 = PhotoImage(file="buttons/translate.png")
button4 = PhotoImage(file="buttons/thought.png")
button5 = PhotoImage(file="buttons/logo.png")
button6 = PhotoImage(file="buttons/website.png")
button7 = PhotoImage(file="buttons/youtube.png")
play = PhotoImage(file="buttons/play.png")
download = PhotoImage(file="buttons/download.png")
recording = PhotoImage(file="buttons/records.png")
search = PhotoImage(file="buttons/search.png")
refresh = PhotoImage(file="buttons/refresh.png")





button = Button(value2,activebackground="#000066" ,cursor="hand2",fg="#ffaa00" ,bg="#000066", image=button2, borderwidth=0, command=firsts)
button.grid(row=0, column=0, pady=27)

button23= Button(value2,activebackground="#000066" ,cursor="hand2",fg="#ffaa00" ,bg="#000066", image=button1, borderwidth=0, command=seconds)
button23.grid(row=2, column=0, pady= 27)

button24= Button(value2,activebackground="#000066" ,cursor="hand2",fg="#ffaa00" ,bg="#000066", image=button3, borderwidth=0, command=thirds)
button24.grid(row=3, column=0, pady= 27)

button25= Button(value2,activebackground="#000066" ,cursor="hand2",fg="#ffaa00" ,bg="#000066", image=button4, borderwidth=0, command=forths)
button25.grid(row=4, column=0, pady= 27)

logo = Label(value0,bg="#000066" ,image=button5)
logo.pack(side=LEFT)

heading = Label(value0,fg="yellow" ,text="RecordStack Software - for you", bg="#000066", font="lucida 20 bold")
heading.pack(side=TOP, pady=20)


thankyou = Label(mainwindow, text="Thank You For Choosing LingoStack", font="helvetica 25 bold", bg="#408000", fg="lightblue")
thankyou.pack(pady=20)

paragraph = Label(mainwindow, text="LingoStack is the best software for you language related work.\n\n EX = Text to Voice, Speech Recognition, Dictionary.\n\n We also added a interesting feature of Fact of the day.\n\n Now Explore This Software\n\n We are working for you to make awesome and useful software for you.", font="lucida 18 bold", bg="#408000")
paragraph.pack(pady=10)








if __name__ == "__main__":
   firsts()



root.mainloop()