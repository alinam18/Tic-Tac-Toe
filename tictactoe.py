# Create tiktax toe


# create the grid 
# def winCondition (place, oppositeSymbol);

def pickingSymbol():
    symbol = input("Pick your Symbol (x or o): ")
    correctSymbol = False

    while correctSymbol is False:
        if symbol == 'x' or symbol == 'X':
            symbol = 'x'
            print('Selected Symbol is : x')
            correctSymbol = True

        elif symbol == 'o' or symbol == 'O':
            symbol = 'o'
            print('Selected Symbol is : o')
            correctSymbol = True

        else:
            print('Please Pick a compatable symbol.')
            symbol = input("Pick your Symbol (x or o): ")
    return symbol

def completed (place):
    if ' '  not in place:
        return True
    return False


def winCondition (place):
    # win condtion horizontal line
    for start in range(0, 9, 3):
        if place[start] == place[start + 1] == place[start + 2] != " ":
            return True

    # win condtion vertical wins
    for start in range(3):
        if place[start] == place[start + 3] == place[start + 6] != " ":
            return True

    # win condtion diagonal wins
    if place[0] == place[4] == place[8] != " ":
        return True
    if place[2] == place[4] == place[6] != " ":
        return True 
    return False

def playGame (symbol):
    print("\nStart Game! ")
    place = [' '] * 9
    structure(place)
    win = False
    if symbol == 'x':
        oppositeSymbol = 'o'
    else:
        oppositeSymbol = 'x'
    while win is not True:

        if completed(place) is True:
            print("No one wins and its a draw!\n")
            break
        # your move
        print("Where do you want to move?")
        number = input ("")
        while not (number.isdigit() and 1 <= int(number) <= 9):
            print("Place a real number (1 - 9): ")
            number = input ("")
        # place the symbol in the box
        gameNumber = int(number) - 1

        if place[gameNumber] == ' ':
            place[gameNumber] = symbol
            structure(place)
            if winCondition(place):
                print(f"{symbol} wins!")
                win = True
        else: 
            print("Place is already taken, chose another move.")
        
        if completed(place) is True:
            print("No one wins and its a draw!\n")
            break

        # second player move
        print("Where does your opponent move?")
        number = input ("")
        while not (number.isdigit() and 1 <= int(number) <= 9):
            print("Place a real number (1 - 9): ")
            number = input ("")
        # place the symbol in the box
        gameNumber = int(number) - 1
        if place[gameNumber] == ' ':
            place[gameNumber] = oppositeSymbol
            structure(place)
            if winCondition(place):
                print(f"\n{oppositeSymbol} wins!")
                win = True
        else: 
            print("Place is already taken, chose another move.")


def structure(place):
    print(f" {place[0]} | {place[1]} | {place[2]} ")
    print(f"___ ___ ___")
    print(f" {place[3]} | {place[4]} | {place[5]} ")
    print(f"___ ___ ___")
    print(f" {place[6]} | {place[7]} | {place[8]} ")

def main ():
    print("Welcome to Tic Tac Toe!")
    symbol = pickingSymbol()
    playGame(symbol)

    print("\nThe End! \nThank you for Playing! \nMade by Alina on 10th May 2024")


if __name__ == "__main__":
    main()