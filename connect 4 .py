def creating_board():
    global board
    global test_board
    board = []
    test_board = []
    for i in range (11 ,53):
        board.append(i)
def board_design():
    global board
    # Draw game board
    print("|",board[0],"|",board[1],"|",board[2],"|",board[3],"|",board[4],"|",board[5] , "|")
    print("|",board[6],"|",board[7],"|",board[8],"|",board[9],"|",board[10],"|",board[11] , "|")
    print("|",board[12],"|",board[13],"|",board[14],"|",board[15],"|",board[16],"|",board[17] , "|")
    print("|",board[18],"|",board[19],"|",board[20],"|",board[21],"|",board[22],"|",board[23] , "|")
    print("|",board[24],"|",board[25],"|",board[26],"|",board[27],"|",board[28],"|",board[29] , "|")
    print("|",board[30],"|",board[31],"|",board[32],"|",board[33],"|",board[34],"|",board[35] , "|")
    print("|",board[36],"|",board[37],"|",board[38],"|",board[39],"|",board[40],"|",board[41] , "|")
creating_board()
def player_x_turn():
    board_design()
    global board
    global test_board
    print("player x turn")
    try:
        #check that user enterd a number
        x_turn = int(input("which cell would u play in?"))
        index = board.index(x_turn)
        #check that user plays at the last row or in a cell which above a cell that any user had played in
        if (x_turn <= 52 or x_turn > 10) and (x_turn == 47 or x_turn == 48 or x_turn == 49 or x_turn == 50 or x_turn == 51 or x_turn == 52 or board[index + 6] == " x" or board[index + 6] == " o"):
            if x_turn in test_board:
                print("aleready used")
                player_x_turn()
            else:
                board[index] = ' x' #put x in cell which user had chosen
                test_board.append(x_turn)
        else:
            print(x_turn)
            print("please write a valid value")
            player_x_turn()
    except:
        print("wrong input , please choose a vaild cell")
        player_x_turn()
    winning()
def player_o_turn():
    board_design()
    global board
    global test_board
    print("player o turn")
    try:
        #check that user enterd a number
        o_turn = int(input("which cell would u play in?"))
        index = board.index(o_turn)
        #check that user plays at the last row or in a cell which above a cell that any user had played in
        if (o_turn <= 52 or o_turn >10) and (o_turn == 47 or o_turn == 48 or o_turn == 49 or o_turn == 50 or o_turn == 51 or o_turn == 52 or board[index + 6] == " o" or board[index + 6] == " x"):
            if o_turn in test_board:
                print("aleready used")
                player_o_turn()
            else:
                board[index] = ' o' #put o in cell which user had chosen
                test_board.append(o_turn)
        else:
            print(o_turn)
            print("please write a valid value")
            player_o_turn()
    except:
        print("wrong input , please choose a vaild cell")
        player_o_turn()
    winning()
def winning():
    for m in range (1,43):
        if m < 39::#(to protect our list from being out of range)
            if m != 16 or m!=22 or m!=28  or m!=34: #check the horizontal winning (we ecxepted these cells to prevent wrong winning)
                if board [m] == board[m+1] == board [m+2] == board [m+3]:
                    board_design()
                    print(board[m] , "wins !")
                    exit()
        if m < 24:#(to protect our list from being out of range)
            if board [m] == board[m+6] == board[m+12] == board[m+18]:#check the vertical winning 
                print(board[m] , "wins !")
                exit()
        if m <= 21::#(to protect our list from being out of range)
            if m != 14 or m != 15 or m!=16 or m!=21 or m!= 22: #check the one of oblique winnings (we ecxepted these cells to prevent wrong winning)
                if board [m] == board[m+7] == board[m+14] == board[m+21]:
                    board_design()
                    print(board[m] , "wins !")
                    exit()
        if m <27::#(to protect our list from being out of range)
            if m != 11 or m != 12 or m!= 13 or m!= 17 or m != 18 or m != 23 or m!=22:#check the the other oblique winning (we ecxepted these cells to prevent wrong winning)
                if board [m] == board[m+5] == board[m+10] == board[m+15]:
                    board_design()
                    print(board[m] , "wins !")
                    exit()
        k=1
        while k <=41:
            if type (board[k]) is not int:
                k+=1
            else:
                break
        if k ==42 :
            print("draw")
            exit()
while True:
    player_x_turn()
    player_o_turn()