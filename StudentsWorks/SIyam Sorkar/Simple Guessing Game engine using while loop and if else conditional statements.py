the_number = 4
input_count = 0
input_limit = 3
while input_count < input_limit :
    guess = int(input('Guess:   '))
    input_count += 1
    if guess == 4 :
        print("Yeah, You guessed the right Answer")
        print("You Won !")
        break
else:
    print("Sorry you failed !, Better luck next time !!!")
