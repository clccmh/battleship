#!/usr/bin/python

import os, sys, platform, socket

board_collumns = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9}

def connect_to_server(ip):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    try:
        sock.connect((ip, 1337))
    except:
        print(sys.exc_info()[0])
        return -1
    return sock

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    elif platform.system() == 'Linux':
        os.system('clear')

def set_up():
    print("-----------------------------------\n-      Welcome to BattleShip!     -\n-----------------------------------")
    print("This is a multiplayer BattleShip game created by Carter.\n")


    address = input("What is the server address? (blank for localhost): ")
    if not address.strip():
        address = "localhost"

    sock = connect_to_server(address)
    while sock == -1:
        print("Server Connection Failed")
        address = input('address: ')
        sock = connect_to_server(address)
    print("\nConnected!\n")

    name = input("\nWhat is your name? ")
    sock.send(bytes("NAME "+name, 'utf-8'))

    print("Waiting For a Connection")
    sock.send(bytes("READY", 'utf-8'))

    return sock
   
def print_board(board):
    clear_screen();
    print("   A B C D E F G H I J\n")
    i = 0;
    for row in board:
        print(i, end="  ")
        i+=1;
        for collumn in row:
            print(collumn, end=" ")
        print("")

def ship_setup(board):
    print_board(board)
    print(board_collumns['A'])
    print("\nAircraft Carrier (size: 5) # # # # #")
    orientation = input("Would you like to place this ship horizontal or vertical? (h/v) ")
    spot = input("Where would you like to place this ship? ")
    
    
clear_screen()
sock = set_up()

board = [[0 for i in range(10)] for x in range(10)]
lower_board = [[0 for i in range(10)] for x in range(10)]
ship_setup(board)

sock.close()
