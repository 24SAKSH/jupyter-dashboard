#!/usr/bin/env python
# coding: utf-8

# In[9]:


# CARD CLASS
import random
value={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}
suits=('Hearts','Diamonds','Spade','Club')
ranks=('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')


# In[10]:


class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=value[rank]
        
    def __str__(self):
        return self.rank+ " of " +  self.suit


# In[11]:


two_hearts=Card('Hearts','Two')


# In[12]:


print(two_hearts)


# In[13]:


class Deck:
    
    def __init__(self):
        self.all_cards=[]
        
        for suit in suits:
            for rank in ranks:
                created_card=Card(suit,rank)
                self.all_cards.append(created_card)
    
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()
    


# In[14]:


new_deck=Deck()


# In[15]:


first_card=new_deck.all_cards[0]


# In[16]:


print(first_card)


# In[17]:


new_deck.shuffle()


# In[18]:


first_card=new_deck.all_cards[0]


# In[19]:


print(first_card)


# In[20]:


my_card=new_deck.deal_one()


# In[21]:


print(my_card)


# In[22]:


len(new_deck.all_cards)


# In[23]:


class Deck:
    
    def __init__(self):
        self.all_cards=[]
        
        for suit in suits:
            for rank in ranks:
                created_card=Card(suit,rank)
                
                self.all_cards.append(created_card)
                
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()


# In[24]:


new_deck=Deck()


# In[25]:


first_card=new_deck.all_cards[0]


# In[26]:


print(first_card)


# In[27]:


new_deck.shuffle()


# In[28]:


first_card=new_deck.all_cards[0]


# In[29]:


print(first_card)


# In[30]:


class Player:
    def __init__(self,name):
        self.name=name
        self.all_cards=[]
        
    def remove_one(self):
        return self.all_cards.pop(0)
    # 0 is used because we want  to remove the card from starting in the list
    
    def add_cards(self,new_cards):
        if type(new_cards)==type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
        
    
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'
        


# In[31]:


new_player=Player('Jose')


# In[32]:


print(new_player)


# In[33]:


new_player.add_cards(my_card)


# In[34]:


print(new_player)


# In[35]:


print(my_card)


# In[36]:


new_player.add_cards([my_card,my_card,my_card])


# In[37]:


print(new_player)


# In[38]:


#player cls


# In[39]:


class Player:
    def __init__(self,name):
        self.name=name
        self.all_cards=[]
        
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        if type(new_cards)==type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
            
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'
            


# In[40]:


new_player=Player('Sakshi')


# In[41]:


print(new_player)


# In[42]:


new_player.add_cards(my_card)


# In[43]:


print(new_player)


# In[44]:


new_player.add_cards([my_card,my_card,my_card,my_card])


# In[45]:


print(new_player)


# In[46]:


my_list=new_player.all_cards


# In[47]:


#game logic


# In[48]:


player_one=Player("One")
player_two=Player("Two")


new_deck=Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())    


# In[54]:


game_on=True


# In[56]:


round_num=0
while game_on:
    round_num+=1
    print(f'Round {round_num} ')
    
    if len(player_one.all_cards)==0:
        print('Player 1 is out of cards!,Player 2 wins')
        game_on =False
        break
        
    if len(player_two.all_cards)==0:
        print('Player 2 is out of cards!,Player 1 wins')
        game_on =False
        break    
        
        
        #start a new round
        
    player_one_cards=[]
    player_one_cards.append(player_one.remove_one())
        
        
    player_two_cards=[]
    player_two_cards.append(player_two.remove_one())  
    
    
    
    at_war=True
    
    while at_war:
        
        if player_one_cards[-1].value>player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            
            at_war=False
            
        elif player_one_cards[-1].value<player_two_cards[-1].value:
            player_two.add_cards(player_two_cards)
            player_two.add_cards(player_one_cards)
            
            at_war=False
            
        else:
            print('WAR!')
            
            if len(player_one.all_cards)<3:
                print('Player One unable to declare war')
                print('Player Two Wins!')
                game_on=False
                break
                
            elif len(player_two.all_cards)<3:
                print('Player Two unable to declare war')
                print('Player One Wins!') 
                game_on=False
                break
                
            else:
                for num in range(3):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
                    
                    


# In[ ]:




