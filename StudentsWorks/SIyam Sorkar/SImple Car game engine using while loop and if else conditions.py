            #It's a simple car game engine made with while loop and if, else conditionals

started = False
while True :
    U_in = input("> ").lower()
    if U_in == "start" :
        if started:
            print("The car is already started")
        else:
            print("Engine started...Ready to go___")
            started = True
    elif U_in == "stop" :
        if not started:
            print("Car is already stoped !")
        else:
            print("Car is stoped")
            started = False
    elif U_in == "help" :
        print("start = to start the engine")
        print("stop = to stop the car")
        print("quit = to exit the game")
    elif U_in == "quit" :
        break
    else:
        print("I didn't Understand that. Please type 'help' to get instructions")