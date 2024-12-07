import time
import sys,os
import random

board = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

symbols = ['X', 'A', 'L', 'V', 'T', 'E']

funds = 0
bet = 100

def game():

    def main_menu():
        for _ in range(5):
            print()
        print("""
    __________         _________.__          __          
    \______   \___.__./   _____/|  |   _____/  |_  ______
     |     ___<   |  |\_____  \ |  |  /  _ \   __\/  ___/
     |    |    \___  |/        \|  |_(  <_> )  |  \___ \ 
     |____|    / ____/_______  /|____/\____/|__| /____  >
        """)
        for _ in range(2) :
            print()
        print('Welcome to PySlots! \nAn interactive terminal slot machine built in Python.')
        print(f'Balance: {funds}')
        print('''
        [1] -> Deposit funds    [2] -> Slots    [3] -> Rules    [4] -> Quit
        ''')
        choice = int(input("Choose an option: "))
        return choice


    def clear_terminal():
        if sys.platform == 'win32':
            os.system("cls")
        else:
            os.system("clear")

    def deposit_screen():
        global funds
        clear_terminal()
        print(f'Balance: {funds}', end='\n')
        funds += int(input("Please enter the amount of money you would like to deposit: "))
        time.sleep(1)
        clear_terminal()
        print("Deposit successful!")
        time.sleep(2)
        clear_terminal()
        print(f"Current balance: {funds}")
        time.sleep(2)
        return

    def slots_screen():
        global funds
        for i in range(3):
            print(board[i])
        while True:
            print("Press any key to spin, b to change the bet or x to leave...")
            print(f"Balance: {funds}, Bet: {bet}")
            x = input()
            if x.lower() == 'x':
                break
            elif x.lower() == 'b':
                change_bet()
            else:
                if funds < 1:
                    clear_terminal()
                    for _ in range(4):
                        print('Add funds!', end='\r')
                        time.sleep(0.5)
                        print(' ' * len('Add funds!'), end='\r')
                        time.sleep(0.5)
                else:
                    clear_terminal()
                    bet_time()
                    for n in range(3):
                        print(board[n])
                    if won():
                        match won():
                            case 'X':
                                funds += 1.1*bet
                            case 'A':
                                funds += 1.3 * bet
                            case 'L':
                                funds += 1.5 * bet
                            case 'V':
                                funds += 1.8 * bet
                            case 'T':
                                funds += 2 * bet
                            case 'E':
                                funds += 5 * bet

    def bet_time():
        global funds
        funds -= bet
        for row in range(3):
            for item in range(3):
                board[row][item] = random.choices(symbols, weights=[45, 20, 18, 13, 3, 1])[0]

    def won():
        global letter
        for row in board:
            if row[0] == row[1] == row[2] and row[0] != '-':
                letter = row[0]
                return letter


        for column in range(3):
            if board[0][column] == board[1][column] == board[2][column] and board[0][column] != '-':
                letter = board[0][column]
                return letter

        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '-':
            letter = board[0][0]
            return letter
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '-':
            letter = board[0][2]
            return letter

        return None

    def rules():
        clear_terminal()
        print('''
                    How the your winnings are calculated:
                    You need to match any letter in any orientation 3 times to consider a win:
                            Match X, get 1.1 times your bet back
                            Match A, get 1.3 times your bet back
                            Match L, get 1.5 times your bet back
                            Match V, get 1,8 times your bet back
                            Match T, get 2 times your bet back
                            Match E, get 5 times your bet back

                    Consistency (in %), how many times a letter appears on the playing board:
                            X = 45%
                            A = 25%
                            L = 15%
                            V = 7%
                            T = 2%
                            E = 1%
                            
                    Press any key to go back
                    ''')
        input()


    def change_bet():
        global bet
        clear_terminal()
        bet = int(input("Place your bet: "))
        return bet

    while True:
        global choice
        clear_terminal()
        choice = main_menu()

        if choice == 1:
            clear_terminal()
            deposit_screen()
        elif choice == 2:
            clear_terminal()
            slots_screen()
        elif choice == 3:
            rules()

        elif choice == 4:
            clear_terminal()
            print("Thank you for playing PySlots! Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
            time.sleep(2)




game()
