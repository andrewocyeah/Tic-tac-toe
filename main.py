#Andrew Rice : Original developer

#Preamble
print("Version 1.0.1 - Last Commit: Andrew Rice\n")
print("Original developer: Andrew Rice\n\n")

print("This project takes advantage of the fact, \n")
print("That multiple people can use the Console\n\n")

print("All text inputs are suffixed by (User 1)|(User 2)\n")

print("This is to specify for who the input is for\n\n")

input("May we begin, Press Enter(Any User)")

print("\n")

tic_tac_toe_board = ['---', '---', '---']  #the board itself

running = True  #making this false makes the code end, bc the main loop runs on this


def display_board():  #Print Each row of the board
    print(tic_tac_toe_board[0])
    print(tic_tac_toe_board[1])
    print(tic_tac_toe_board[2])


display_board()
#Show board for reference


def check_victory(player_letter):
    for i in range(3):  #for each row
        if tic_tac_toe_board[i] == player_letter * 3:
            return True  #check for a horizontal row
        #horizontal rows can 1:be tested in a single line, 2. simpler (IDE was complaining about program complexity)

    for i in range(3):  #for each collum
        valid = True  #anomly check
        for j in range(3):  #for each row
            if tic_tac_toe_board[j][
                    i] != player_letter:  #if not letter collum win is not true
                valid = False
                break
        if valid: return True  #detect win

    valid = True
    for i in range(3):
        if tic_tac_toe_board[i][i] != player_letter:
            valid = False  #scan for 0,0 - 2,2 diagonal win
    if valid: return True

    valid = True
    for i in range(3):
        if tic_tac_toe_board[i][2 - i] != player_letter:
            valid = False  #scan for 0,2 - 2,0 diagonal win
    if valid:
        return True
    return False  #no wins detected


def test_tie():
    for i in range(3):
        for j in range(3):
            if tic_tac_toe_board[i][j] == '-': return False  #Any empty squares
    return True


def turn(player_letter, user_number):
    xcord = 0
    ycord = 0
    invalid = True
    while invalid:
        while True:
            xcord = int(
                input("X pos of " + player_letter +
                      "? [input 1, 2 or 3] (User " + str(user_number) + ")"))-1
            if -1 < xcord < 3:  #in range?
                break
            print("Thats invalid! Must be a number between 0 and 2")  #do again
        while True:
            ycord = int(
                input("Y pos of " + player_letter +
                      "? [input 1, 2 or 3] (User " + str(user_number) + ")"))-1
            if -1 < ycord < 3:  #in range
                if tic_tac_toe_board[ycord][xcord] == '-':
                    invalid = False  #All is well Proceed to Assignment
                    break
                else:
                    print('That space is already taken, choose again')  #invalid is True Loop back to beginning
                    break;
    new_row = ''  #Strings are immutable have to make new string
    for i in range(0, 3):  #index \es 0, 1, and 2
        
        if xcord == i:
            new_row += player_letter  #Make a new string with X at the end
            
        else:
            new_row += tic_tac_toe_board[ycord][i]
            #copy reference form original
    tic_tac_toe_board[ycord] = new_row
    display_board()
    if check_victory(player_letter): return True
    return False


while running:
    if turn('X', 1):  #Player 1 win?
        print("User 1 Victory")
        running = False
    elif test_tie():  #not win? test for a tie
        print("Tie Neither Player wins")
        running = False
    else:  #not win or tie? Player 2's turn
        if turn('O', 2):  #player 2's turn, did he win?
            print("User 2 Victory")
            running = False
        elif test_tie():  #not win? is it a tie
            print("Tie Neither Player wins")
            running = False
#if not player 2 win or tie, back to player 1
