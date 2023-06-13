from datetime import date
#purpose, author, date and version
#I created this code through trial and error, but it works
purpose = "# The purpose of this code is to " + input("What is the purpose of your code? (it will come out as: 'The purpose of this code is to ___)'\n") + " #"
author = "Author: " + input("Who is the author?\n")
version = "Version: " + input("What is the version number?\n")
dayte = "Date: " + date.today().strftime("%m-%d-%Y")
print("\n\n")
print("#"*len(purpose))
print(purpose)
print("#", " "*(len(purpose)-4), "#")
print("#"," "*(((len(purpose)-len(author))-3)//2), author," "*(((len(purpose)-len(author))//2)-4), "#")
print("#", " "*(len(purpose)-4), "#")
print("#"," "*(((len(purpose)-len(dayte))-3)//2), dayte," "*(((len(purpose)-len(dayte))//2)-4), "#")
print("#", " "*(len(purpose)-4), "#")
print("#"," "*(((len(purpose)-len(version))-3)//2), version," "*(((len(purpose)-len(version))//2)-4), "#")
print("#"*len(purpose))
print("\n\nAbove is the output; copy and paste it into your code")
input("Press any key to exit...")
#In case someone is using the python console, so that it doesnt close immediately after execution
