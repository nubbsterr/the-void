# nubb's rubberduckydebugger

print("Welcome to the nubbyrubberducky. Go line by line in your code and 'talk' to the rubber ducky.")
print("Type 'quit' to exit the rubberduckydebugging session.")
print("For more info about rubberduckdebugging, see: rubberduckdebugging.com\n")
loop = True

while loop:
    INPUT = input("YOU > ")
    match INPUT:
        case "quit":
            loop = False
        case default:
            pass

print("Hopefully your issues are solved now!")

