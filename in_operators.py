# if my_answer != "rock" and my_answer != "paper" and my_answer != "scissors":
#    pass
# This is how it was done in the rock, paper, scissors project, but there is a more effective way

my_answer = "rock"
options = ["rock", "paper", "scissors"]
if my_answer in options: # The In operator says, is the thing on the left inside of the iterable on the right
    print("Rock is one of the possible options")
else:
    print("Wrong answer, try again") # Message to print if my answer isn´t part of the value options

# Another way to make this more 'powerful' is by using 'input'

my_answer = input("What is your answer? ")
options = ["rock", "paper", "scissors"]
if my_answer in options:
    print("That is a viable option")
else:
    print("Wrong answer, try again")

# This can also be done with a dictionary
key = "JMR"
person = {
    "name": "JMR",
    "profession": "Trainee",
}

if key in person:
    print("Name is a valid dictionary key in the person object")