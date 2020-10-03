words=['computer','coder','encyclopedia','fibonacci','matrix','handle','bubble','selection','sort']

def labelslider():
    global count,sliderword
    text='Welcome to Typing Booster...'
    if (count>=len(text)):
        count=0
        sliderword=''
    sliderword+=text[count]
    count+=1
    fontlabel.configure(text=sliderword)
    fontlabel.after(150,labelslider)

def timer():
    global time,score,miss

    if time>0:
        time-=1
        timelabelcount.configure(text=time)
        timelabelcount.after(1000,timer)
    else:
        instructlabel.configure(text='Total Score = {} | Miss={}'.format(score,miss))
        message=messagebox.askretrycancel('Notification','Hit retry to play again.')
        if message==True:
            score=0
            time=60
            miss=0
            timelabelcount.configure(text=time)
            wordlabel.configure(text=words[0])
            scorelabelcount.configure(text=score)
        else:
            score = 0
            time = 60
            miss = 0
            timelabelcount.configure(text=time)
            wordlabel.configure(text=words[0])
            scorelabelcount.configure(text=score)
            score=0
           
def startgame(event):
    if time==60:
        timer()
    instructlabel.configure(text='')
    global score,miss
    if wordentry.get()==wordlabel['text']:
        score+=1
        scorelabelcount.configure(text=score)
    else:
        miss+=1
    random.shuffle(words)
    wordlabel.configure(text=words[0])
    wordentry.delete(0,END)

from tkinter import *
import random
from tkinter import messagebox

#root methods

root=Tk()
root.geometry('900x700+400-100')
root.configure(bg='maroon')
root.title('Typing Booster')
root.iconbitmap('mine.ico')


#Variables

score=0
time=60
count=0
sliderword=''
miss=0
#label methods

fontlabel=Label(root,text='',font=('algerian',20,'italic bold'),bg='maroon',
                fg='aqua',width=40)
fontlabel.place(x=10,y=10)
labelslider()

random.shuffle(words)
wordlabel=Label(root,text=words[0],font=('arial',20,'italic bold'),bg='maroon',
                fg='lime')
wordlabel.place(x=350,y=290)

scorelabel=Label(root,text='Your Score :',font=('algerian',20,'italic bold'),bg='maroon',fg='lime')
scorelabel.place(x=10,y=100)

scorelabelcount=Label(root,text=score,font=('algerian',20,'italic bold'),bg='maroon',fg='aqua')
scorelabelcount.place(x=60,y=150)

timelabel=Label(root,text='Time Left :',font=('algerian',20,'italic bold'),bg='maroon',fg='lime')
timelabel.place(x=650,y=100)

timelabelcount=Label(root,text=time,font=('algerian',20,'italic bold'),bg='maroon',fg='aqua')
timelabelcount.place(x=710,y=150)

instructlabel=Label(root,text='Type the word and hit enter.',font=('arial',30,'italic bold'),bg='maroon',
                    fg='grey')
instructlabel.place(x=50,y=450)

#entry method

wordentry=Entry(root,font=('arial',20,'italic bold'),bd=10,justify='center')
wordentry.place(x=230,y=350)
wordentry.focus_set()

#binding

wordentry.bind('<Return>',startgame)

root.mainloop()
