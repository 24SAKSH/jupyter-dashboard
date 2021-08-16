#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(board[7]+' |'+board[8]+' |'+board[9])
    print('----')
    print(board[4]+' |'+board[5]+' |'+board[6])
    print('----')
    print(board[1]+' |'+board[2]+' |'+board[3])
    print('----')
    


# In[2]:


def player_input():
    marker=' '
    
    while marker not in ['X','O']:
        marker=input('Player1:Choose between X or O: ')
        
        if marker=='X':
            return ('X','O')
        else:
            return ('O','X')


# In[3]:


Player1_marker,Player2_marker=player_input()


# In[4]:


Player2_marker


# In[5]:


def place_marker(board,marker,position):
    board[position]=marker


# In[6]:


def win_check(board,mark):
    return ((board[7]==mark and board[5]==mark and board[3]==mark) or
     (board[1]==mark and board[2]==mark and board[3]==mark) or   
     (board[4]==mark and board[5]==mark and board[6]==mark) or
     (board[7]==mark and board[8]==mark and board[9]==mark) or
     (board[1]==mark and board[4]==mark and board[7]==mark) or
     (board[2]==mark and board[5]==mark and board[8]==mark) or   
     (board[3]==mark and board[6]==mark and board[9]==mark) or
     (board[1]==mark and board[5]==mark and board[9]==mark))
     
              


# In[7]:


import random

def choose_first():
    
    flip=random.randint(0,1)
    
    if flip==0:
        return 'Player1'
    else:
        return 'Player2'


# In[8]:


def space_check(board,position):
    return board[position]==' '


# In[9]:


def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True


# In[10]:


def player_choice(board):
    
    position=0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input('Choose a position (1-9): '))
        
        return position


# In[11]:


def replay():
    
    choice=input('Play again:Enter Yes or NO: ')
    
    return choice=='Yes'


# In[12]:


#main code

print('WELCOME TO PLAY TIC TAC TOE')

while True:
    
    the_board=[' ']*10
    Player1_marker,Player2_marker=player_input()
    
    turn = choose_first()
    print(turn + "will go first")
    
    play_game = input ('Ready to play y or n: ')
    
    if play_game=='y':
        game_on=True
    else:
        game_on=False
        
    while game_on:
        
        if turn =='Player1':
            display_board(the_board)
            position=player_choice(the_board)
            place_marker(the_board,Player1_marker,position)
            
            if win_check(the_board,Player1_marker):
                display_board(the_board)
                print('PLAYER1 HAS WON !')
                game_on=False
                
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME')
                    game_on=False
                else: 
                    turn ='Player2'
                    
        else:             
             display_board(the_board)
             position = player_choice(the_board)
             place_marker(the_board,Player2_marker,position)
            
             if win_check(the_board,Player2_marker):
                 display_board(the_board)
                 print('PLAYER2 HAS WON !')
                 game_on=False
                
             else:
                 if full_board_check(the_board):
                     display_board(the_board)
                     print('TIE GAME')
                     game_on=False
                 else: 
                     turn = 'Player1'
                    
    if not replay():
        break
    


# In[ ]:





# In[ ]:




