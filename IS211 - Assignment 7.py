# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 11:11:22 2020

@author: kbootsri
"""

class Pig():
    
    def __init__(self, player):
        self.player = player
        self.rolls = []

    def add_player(self, name):
        self.players.append(name)    

#    def new_roll(self, roll):
#        self.rolls.append(roll)
        
    def your_move(self, move):
        total_score = sum(self.rolls)
        
        import random 
        import time
        random.seed(time.clock())
        
        if move == 'r':
            roll = random.randint(1, 6)
            
            if roll > 1:
                self.rolls.append(roll)
                total_score = sum(self.rolls)                 
                if total_score < 100:
                    print (f"{self.player} rolled a {roll}. Your total score is {total_score}. Do you want to roll or hold?")  
                                  
                else:
                    print (f"{self.player} rolled a {roll}. {self.player} score is {total_score}. You won!")
                    exit                   
           
            elif roll == 1:
               print (f"{self.player} rolled a 1. Your score stays {total_score}. Next player's turn.")
               self.rolls.append(0)


               
            
        elif move == 'h':
            if self.rolls[-1] == 0:
                print (f'{self.player} tried to make a move but you rolled a 1 last time. It is not your turn. Cheater, cheater!')
                
            else:
                print (f"{self.player} chose to hold. Your score is {total_score}. Next player's turn.")
                pass
        
        else:
            print("Error: Choose a valid move of 'r' for roll or 'h' for hold.")
           



james = Pig('James')
jim = Pig('Jim')



poss_moves = ['jim.your_move("r")', 'jim.your_move("h")', 'james.your_move("r")', 'james.your_move("h")']

all_moves = poss_moves * 50



for x in all_moves:
    eval(x)
    
    if sum(jim.rolls) > 100 or sum(james.rolls) > 100:
        break

    elif (sum(jim.rolls) > 0 and jim.rolls[-1] == 0) or (sum(james.rolls) > 0 and james.rolls[-1] == 0):
        pass  
    
    else:
        continue

