# Here is a task to practise dictionaries, if you get stuck the answers are at the bottom. Have fun!





#1 Create a user profile for your new game. This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'






#2 iterate and print all the keys in the above user.




#3 Add a new weapon to your user





#4 Add a new key to include 'is_banned'. Set it to false




#5 Ban the user by setting the previous key to True






#6 create a new user2 my copying the previous user and update the age value and username value. 






















































'''
Q1

user = {
  'age': '27',
  'username': 'bonecrusher',
  'weapons': ['hammer', 'sword', 'mace'],
  'is_active': True,
  'clan': 'westside',
}

Q2

print(user.keys())

Q3

user['weapons'].append('bubble machine')

Q4

user.update({'is_banned': False})

Q5

user['is_banned'] = True
print(user)

Q6

user2 = user.copy()
user2.update({
  'age': 50,
  'username': 'mom'
})

'''