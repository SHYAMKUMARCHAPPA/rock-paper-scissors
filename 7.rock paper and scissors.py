import random
rpc=["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
     rock
""",
"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
   paper
""","""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
  scissors
"""]
game=int(input('what do you choose?. type 0 for rock, and 1 for scissors, and 2 for paper.'))
computer=random.randint(0, 2)
print(rpc[game])
print('computer choice')
print(rpc[computer])
if game==computer:
 print('we both choose same, play again')
elif game==0 and computer==1:
 print('you lose\n chinna pillalu meeru.')
elif game==0 and computer==2:
 print('you win\nvery good baaga adutunnav.')
elif game==1 and computer==0:
 print('''you lose\n🤣 game adadam vacha asala ''')
elif game==1 and computer==2:
 print('you lose\npakkakelli aduko.')
elif game==2 and computer==0:
 print('you lose\nvelli game nerchuko.')
elif game==2 and computer==1:
 print('you win\nbaaga gelichav party')
else:
 print('please, enter correct inputs.')