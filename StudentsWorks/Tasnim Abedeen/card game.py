# this is a simple card game
# the programme will print different sentences based on the card one person choose by using if else elif function

a = str(input("Choose a card and I will tell a sentence for you: A.🂡 2.🂢 3.🂣 4.🂤 5.🂥 6.🂦 7.🂧 8.🂨 9.🂩 10.🂪 J.🂫 Q.🂭 K.🂮"))
print("You have chosen", a)
if a == "A":
    print("You are awesome!")
elif a == "a":
    print("You are awesome!")
elif a == "1":
    print("You’re better than a triple-scoop ice cream cone…with sprinkles!")
elif a == "2":
    print("You’re so kind that you make everyone around you a better person")
elif a == "3":
    print("Your creativity is on another level!")
elif a == "4":
    print("You’re irreplaceable!")
elif a == "5":
    print("You’re so kind everyone instantly feels like your friend.")
elif a == "6":
    print("You are more amazing than you realize!")
elif a == "7":
    print("Everyone needs a friend like you in their life.")
elif a == "8":
    print("You’re so inspiring, even if you don’t realize it!")
elif a == "9":
    print("You’re truly a gem—there’s nobody like you!")
elif a == "10":
    print("Not everyone can pull off that look, but you sure can!")
elif a == "J":
    print("Your ideas will change the world one day!")
elif a == "Q":
    print("Please never stop being you!")
elif a == "K":
    print("You are the king!")
elif a == "j":
    print("Your ideas will change the world one day!")
elif a == "q":
    print("Please never stop being you!")
elif a == "k":
    print("You are the king!")
else:
    print("You have failed to choose the correct card. It goes without saying that failure is the pillar of success! Try again. ")