# We would need to create a txt file with a list of emails and the aim is to try to figure out whether an email chosen is in the list
# to do that in python the variable would create an array/list

with open("emails.txt", "r") as emails:
    emails = emails.readlines()

for email in emails:
    if "hotmail" in email: # We can use the 'in' operator to check if a string is inside a string
        print(email.rstrip()) # This will filter out all the emails and look for the hotmail one
        # The rstrip is to get rid off spaces between lines