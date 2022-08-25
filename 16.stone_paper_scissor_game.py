import random
import sys
no=int(input("Enter how many time u want to play: "))
scissor= '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
stone = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

for i in range(no):
	print("\nPress 0 for stone\nPress 1 for paper\nPress 2 for scissor")
	print("\nLets play...")
	me=int(input("Enter your choice: "))
	if(me!=0 and me!=1 and me!=2):
		me=int(input("Please enter choice from (0,1,2): "))
		if me < 0 or me >2:
		      	print("Sorry Invalid Input")
		      	sys.exit()
		      	
	list1=[stone,paper,scissor]
	print("You entered: ",list1[me])
	frnd=random.randint(0,2)
	print("Friend enterd: ",list1[frnd])
	
	if(me==frnd):
		print("Game result: Game is draw")
	elif(me==0 and frnd==1):
		print("Game result: Friend win")
	elif(me==0 and frnd==2):
		print("Game result: You win")
	elif(me==1 and frnd==0):
		print("Game result: You win")
	elif(me==1 and frnd==2):
		print("Game result: Friend win")
	elif(me==2 and frnd==0):
		print("Game result: Friend win")
	elif(me==2 and frnd==1):
		print("Game result: You win")