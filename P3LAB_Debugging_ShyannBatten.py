#CTI-110
#P3LAB
#Shyann Batten
#10/09/19
#This program gets a numeric test score from the 
#user and displays the corresponding letter grade.
A_score = 90
B_score = 80
C_score = 70
D_score = 60

#Get the test score from the user.
score = int(input('Enter your test score: '))
if score == A_score:
    print('Your grade is A.')
elif score == B_score:
    print('Your grade is B.')
elif score == C_score:
    print('Your grade is C.')
elif score == D_score:
    print('Your grade is D.')
else:
    print('Your grade is F.')
    
