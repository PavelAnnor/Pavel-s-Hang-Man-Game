from kivy.app import App
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
import random
import json
Builder.load_file('jello2.kv')
Window.size = (500,500)
Window.clearcolor = \
1, 1, 1.0, 1
class Jello2App(App):
    #declaration of class attributes
    #'found' shows to whether or not a letter has been found. found1 corresponds to letter 1, found2 to letter 2, etc.
    found1 = '' 
    found2 = ''
    found3 = ''
    found4 = ''
    found5 = ''
    found6 = ''
    #number of incorrect guesses
    count =0 
    word = ''
    #category of the word
    cat = ''
    
    def generateword(self):
        '''Upon starting a new game, this function takes a random word from a random category, that the user has to guess.'''
        x = random.randint(0,2)
        y = random.randint(0,3)
        #The three lists represent the three categories, each with a set of words
        wordsrand = ['accent', 'caring','ground', 'losing']
        wordssport = ['basket', 'soccer', 'fields', 'fouled']
        wordsfood = ['waffle', 'pizzas', "burger", 'cooked']
        if x ==0 :
            self.word = wordsrand[y]
            self.cat = "Miscellaneous"
        elif x==1:
            self.word = wordssport[y]
            self.cat = 'Sports'
        else: 
            self.word = wordsfood[y]
            self.cat = 'Food'

    def checkloss(self,count):
        '''This fucntion checks to see if the user has 6 incorrect guesses. If he/she does, the game over message is displayed.
        The guess button is then disabled and the mystery word is revealed.'''
        if count ==6:
            self.root.ids.content.text = f"YOU LOSE! The word was: {self.word} "
            self.root.ids.guess.disabled = True       

    def startgame(self):
        '''Starts up a new game when the user clicks the new game button. 
        Generates a new word and allows the guess button,save button, and textinput box to be accessed'''
        self.generateword()
        self.root.ids.test.text = f"Your category is: {self.cat}"  
        self.root.ids.start.pos_hint = {'x':0.35, 'y':1}
        self.root.ids.guesser.readonly = False
        self.root.ids.guess.disabled = False 
        self.root.ids.save.disabled = False
    
    def save(self):
        '''Stores the mystery word, number of incorrect guesses, category 
        and whether or not each letter has been found into a list that is dumped into a json file'''
        savedgame = [self.word,self.found1,self.found2,self.found3,self.found4,self.found5,self.found6,self.count,self.cat]
        with open('savedword.json','w') as f:
            json.dump(savedgame, f)
            self.root.ids.content.text = "Game has been saved."
        
    
    def load(self):  
        '''Opens the json file and loads up the conditions of the previous game.
        The letters already found reappear, the parts of the body that were generated reappear and the user can continue from 
        where they left off.'''
        with open('savedword.json','r') as f:
            self.root.ids.start.pos_hint = {'x':0.35, 'y':1}
            self.root.ids.guesser.readonly = False
            self.root.ids.guess.disabled = False 
            self.root.ids.save.disabled = False
            savedgame2 = json.load(f)
            self.word = savedgame2[0]
            self.found1 = savedgame2[1]
            self.found2 = savedgame2[2]
            self.found3 = savedgame2[3]
            self.found4 = savedgame2[4]
            self.found5 = savedgame2[5]
            self.found6 = savedgame2[6]
            self.count = savedgame2[7] 
            self.cat =savedgame2[8] 

            self.root.ids.test.text = f"The category is: {self.cat}"
            if(self.found1 == "T"):
                self.root.ids.letter1.text = self.word[0].upper()
            if(self.found2 == "T"):
                self.root.ids.letter2.text = self.word[1].upper()
            if(self.found3 == "T"):
                self.root.ids.letter3.text = self.word[2].upper()
            if(self.found4 == "T"):
                self.root.ids.letter4.text = self.word[3].upper()
            if(self.found5 == "T"):
                self.root.ids.letter5.text = self.word[4].upper()
            if(self.found6 == "T"):
                self.root.ids.letter6.text = self.word[5].upper()

            #based on the number of incorrect guesses the user prviously had, a different number of body parts appears
            if(self.count ==1):
                self.root.ids.head.opacity = 1
            if(self.count ==2):
                self.root.ids.head.opacity = 1
                self.root.ids.body.opacity = 1
            if(self.count ==3):
                self.root.ids.head.opacity = 1
                self.root.ids.body.opacity = 1
                self.root.ids.arms1.opacity = 1
            if(self.count ==4):
                self.root.ids.head.opacity = 1
                self.root.ids.body.opacity = 1
                self.root.ids.arms1.opacity = 1
                self.root.ids.arms2.opacity = 1
            if(self.count ==5):
                self.root.ids.head.opacity = 1
                self.root.ids.body.opacity = 1
                self.root.ids.arms1.opacity = 1
                self.root.ids.arms2.opacity = 1
                self.root.ids.legs1.opacity = 1
            if(self.count ==6):
                self.root.ids.head.opacity = 1
                self.root.ids.body.opacity = 1
                self.root.ids.arms1.opacity = 1
                self.root.ids.arms2.opacity = 1
                self.root.ids.legs1.opacity = 1
                self.root.ids.legs2.opacity = 1
                self.checkloss()
            
            

            self.root.ids.content.text = "Last Save Loaded" 
            
    
    def guess(self):
        '''Checks to see if the users letter guess is correct. If it is,
        the letter appears. If it isnt, a body part is generated.'''
        guess = self.root.ids.guesser.text
        
        #if the guess is correct, the letter appears and the found attribute is set to true
        if guess.lower() == self.word[0]:
            self.root.ids.letter1.text = self.word[0].upper()
            self.found1 = "T"
            self.root.ids.content.text = f"Correct! The letter {guess} is in the Word."
            
            
        if guess.lower() == self.word[1]:
            self.root.ids.letter2.text = self.word[1].upper()
            self.found2 = "T"
            self.root.ids.content.text = f"Correct! The letter {guess} is in the Word."
            
            
        if guess.lower() == self.word[2]:
            self.root.ids.letter3.text = self.word[2].upper()
            self.found3 = "T"
            self.root.ids.content.text = f"Correct! The letter {guess} is in the Word."
            
            
        if guess.lower() == self.word[3]:
            self.root.ids.letter4.text = self.word[3].upper()
            self.found4 = "T"
            self.root.ids.content.text = f"Correct! The letter {guess} is in the Word."
            
            
        if guess.lower() == self.word[4]:
            self.root.ids.letter5.text = self.word[4].upper()
            self.found5 = "T"
            self.root.ids.content.text = f"Correct! The letter {guess} is in the Word."
            
            
        if guess.lower() == self.word[5]:
            self.root.ids.letter6.text = self.word[5].upper()
            self.found6 = "T"
           
            self.root.ids.content.text = f"Correct! The letter {guess} is in the Word."

        #if the guess is wrong,this if statment block generates a body part based on the number of wrong guesses
        if(guess.lower()!= self.word[0] and guess.lower()!= self.word[1]and guess.lower()!= self.word[2] and guess.lower()!= self.word[3] and guess.lower()!= self.word[4] and guess.lower()!= self.word[5]):
        
            self.root.ids.content.text = "Wrong! Guess again!"
            
            if(self.count ==0):
                self.root.ids.head.opacity = 1
            if(self.count ==1):
                self.root.ids.body.opacity = 1
            if(self.count ==2):
                self.root.ids.arms1.opacity = 1
            if(self.count ==3):
                self.root.ids.arms2.opacity = 1
            if(self.count ==4):
                self.root.ids.legs1.opacity = 1
            if(self.count ==5):
                self.root.ids.legs2.opacity = 1
            self.count+=1

        
        #at the end of a guessing sequence checks to make sure the user isnt over limit for wong guesses
        self.checkloss(self.count)
            

        
        #If all letters have been guessed correctly, the user wins.
        if(self.found1 == "T" and self.found2 == "T" and self.found3 == "T" and self.found4 == "T" and self.found5 == "T" and self.found6 == "T"):
            self.root.ids.content.text = "You won!"
            
Jello2App().run()
