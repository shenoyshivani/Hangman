from tkinter import *
from tkinter import messagebox,simpledialog
from PIL import Image, ImageTk
from random_word import RandomWords
window=Tk()
window.title("Hangman")
window.geometry("1000x1000")
imageList=[]
for i in range(1,10):
    imageList.append(Image.open("Hangman/step "+str(i)+".jpg"))
test=ImageTk.PhotoImage(imageList[0])
label=Label(window,image=test)
label.image=test
label.place(x=0,y=-100)
maxTries=8
noGuess=0
r=RandomWords()
randomWord=r.get_random_word()
randomWord=randomWord.upper()
while True:
    letter=simpledialog.askstring("Guess","Guess a letter")
    if letter in randomWord:
        messagebox.showinfo("Hangman","The word contains " + letter)
        randomWord=randomWord.replace(letter,"")
        if len(randomWord)==0:
            messagebox.showinfo("Yeah you did it!!!!")
            break    
    else:
        messagebox.showinfo("Hangman","Incorrect, try again")
        noGuess+=1
        test=ImageTk.PhotoImage(imageList[noGuess])
        label=Label(window,image=test)
        label.image=test
        label.place(x=0,y=-100)
        if noGuess>=maxTries:
            messagebox.showinfo("Hangman","You lost, the word was "+randomWord)
            break
window.mainloop()