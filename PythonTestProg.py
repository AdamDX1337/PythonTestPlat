import socket
import time
import codecs
import string
import datetime
import threading
import keyboard
import turtle
from datetime import datetime
from datetime import date
import requests
HOST = "127.0.0.1"
PORT = 42069
ssock = None
csock = None
caddr = None
hosting = False

print("currently using: socket, time, codecs, string, datetime, threading, requests, turtle, keyboard")
def time1():
    today = date.today()
    now = datetime.now()
    print("\nTodays date and time:")
    d1 = today.strftime("%d/%m/%Y")	
    d2 = today.strftime("%B %d, %Y")
    t1 = now.strftime("%H:%M:%S")
    print(d1)
    print(d2)
    print(t1)
    print(" ")
    menu()
def time2():
    today = date.today()
    now = datetime.now()
    print("Todays date and time:")
    d1 = today.strftime("%d/%m/%Y")	
    d2 = today.strftime("%B %d, %Y")
    t1 = now.strftime("%H:%M:%S")
    print(d1)
    print(d2)
    print(t1)
    extramenu()
def socketip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    a = socket.gethostname()
    print("IP:", s.getsockname()[0])
    s.close()
    print("PC name:",a)
    menu1

def tempmenu():
    print("\n****************************")
    print("*                          *")
    print("* Temperature Calculations *")
    print("* 1. Celsius to Fahrenheit *")
    print("* 2. Fahrenheit to Celsius *")
    print("* 3. Back                  *")
    print("*                          *")
    print("****************************")
    temp = input("\nWhat is your selection: ")
    if temp =="1":
        print("\nConvert Celsius to Fahrenheit")
        celsiusX=float(input("\nWhat is your Temperature in Celsius: "))
        fahrenheitX= celsiusX * 9/6 + 32
        print("The Temperature in fahrenheit is: ", fahrenheitX)
        time.sleep(1)
        tempmenu()
    if temp =="2":
        print("\nConvert Fahrenheit to Celsius")
        fahrenheitY=float(input("\nWhat is your Temperature in Fahrenheit: "))
        celsiusY= (fahrenheitY - 32) * 5/9
        print("The Temperature in Celsius is: ", celsiusY)
        time.sleep(1)
        tempmenu()
    if temp == "3":
        menu1()
    else:
        print("INVALID OPTION")
        menu1()

def simplemenu():
    print("\n***********************")
    print("*                     *")
    print("* Simple Calculations *")
    print("* 1. Addition         *")
    print("* 2. Subtraction      *")
    print("* 3. Division         *")
    print("* 4. Multiplication   *")
    print("* 5. Back             *")
    print("*                     *")
    print("***********************")
    qst = input("\nWhat is your selection: ")
    if qst == "1":
        print("Add 2 numbers!")
        num1 = float(input("What is the first number: "))
        num2 = float(input("What is the second number: "))
        num3 = num1 + num2
        print("The answer is:", num3)
        simplemenu()
    if qst == "2":
        print("Subtract 2 numbers!")
        num1 = float(input("What is the first number: "))
        num2 = float(input("What is the second number: "))
        num3 = num1 - num2
        print("The answer is:", num3)
        simplemenu()
    if qst == "3":
        print("Divide 2 numbers!")
        num1 = float(input("What is the first number: "))
        num2 = float(input("What is the second number: "))
        num3 = num1 / num2
        print("The answer is:", num3)
        simplemenu()
    if qst == "4":
        print("Multiply 2 numbers!")
        num1 = float(input("What is the first number: "))
        num2 = float(input("What is the second number: "))
        num3 = num1 * num2
        print("The answer is:", num3)
        simplemenu()
    if qst == "5":
        menu1

def draw():
    turtle.speed(100)
    t = turtle.Turtle()
    s = turtle.getscreen()
    t.pencolor("black")
    turtle.bgcolor("white")
    turtle.write("PRESS Q TO QUIT", move=False, align='left')

    while True:
        if keyboard.read_key() == "w":
            t.forward(10)
        elif keyboard.read_key() == "a":
            t.left(30)
        elif keyboard.read_key() == "s":
            t.backward(10)
        elif keyboard.read_key() == "d":
            t.right(30)
        elif keyboard.read_key() == "z":
            t.penup()
        elif keyboard.read_key() == "x":
            t.pendown()
        elif keyboard.read_key() == "q":
           turtle.bye()
           menu1()




def extramenu():
    print("\n**********************")
    print("*                    *")  
    print("* 1. Back            *")
    print("* 2. Python Help     *")
    print("* 3. Python License  *")
    print("* 4. Bugs            *")
    print("* 5. Display Info    *")
    print("* 6. Database Print  *")
    print("* 7. Time            *")
    print("* 8. Draw            *")
    print("*                    *")
    print("*                    *") 
    print("**********************")
    extraA=input("\nWhat is your selection: ")
    if extraA == "1":
        menu1()
    if extraA == "2":
        print(help())
        extramenu()
    if extraA =="3":
        print(license())
        extramenu()
    if extraA == "4":
        print('''for some reason pressing 5 to go back also
displays "INVALID INPUT" and the answer,
not sure why...''')
        extramenu()
    if extraA=="5":
        socketip()
    if extraA=="6":
        database(test)
    if extraA=="7":
        time2()
    if extraA=="8":
        draw()
    else:
        print("INVALID OPTION")
        menu1()

def discordspammer():
    print('for the message, you cant spam ping by doing "@personsname"')
    print('instead get their ID and do "<@ID>" so if the ID is 123')
    print('you write <@123>')
    message = input("What do you want to be spammed: ")
    token1 = input("Token: ")
    #token2 = input("2nd Token: ")
    time1 = float(input("Time inbetween each request? (in seconds): "))
    channel = input("Channel Link: ")
    amount = int(input("How many times do you want to spam: "))
    total = 0
    while total <= amount:
        time.sleep(time1)
        payload = {
            'content': message
        }

        header = {
            'authorization': token1
        }

        r = requests.post(channel, data=payload, headers=header)
        if r.statuscode != 200:
            print("Failed to send!")
            onlinemenu()
        else:
            total += 1
            print("Attempted to Send a total of:", total, "times")
            if total == amount:
                print("Done!\n")
                menu1()


def onlinemenu():
    print("\n**********************")
    print("*                    *")
    print("* 1. Chat            *")
    print("* 2. Discord Spammer *")
    print("* 3. Back            *")
    print("*                    *")
    print("**********************")
    Oanswer = input("\nWhat is your selection: ")
    if Oanswer == "1":
        Oanswer2 = input("You have chosen to online chat\n\nDo you know your ip?\n\n1.Yes\n2.No\n\nWhat is your selection: ")
        if Oanswer2 == "1":
            chatmain()
        if Oanswer2 == "2":
            print(" ")
            socketip()
            print(" ")
            chatmain()
        else:
            print("INVALID INPUT")
            menu1()
    if Oanswer == "2":
        discordspammer()
    if Oanswer == "3":
        menu1()
    else:
        print("INVALID INPUT")
        onlinemenu()
    

def menu1():
    print("\n********************************")
    print("*                              *")
    print("* What would you like to do?   *")
    print("* 1. Temperature Calculations  *")
    print("* 2. Simple Calculations       *")
    print("* 3. Extra                     *")
    print("* 4. Online Features           *")
    print("* 5. Quit                      *")
    print("*                              *")
    print("********************************")
    
    answer = input("\nWhat is your selection: ")
    if answer == "1":
        tempmenu()
    if answer== "2":
        simplemenu()
    if answer == "3":
        extramenu()
    if answer == "4":
        onlinemenu()
    if answer == "5":
        print(''' #   _      _            ___  ___ #
 #  /_\  __| |__ _ _ __ / _ \/ __|#
 # / _ \/ _` / _` | '  \ (_) \__ \#
 #/_/ \_\__,_\__,_|_|_|_\___/|___/#
                                   ''')
        print("**************************")
        print("*                        *")
        print("* Goodbye!               *")
        print("* hope to see you again! *")
        print("*                        *")
        print("**************************")
        print("closing in 3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        exit()
    else:
        print("INVALID INPUT")
        menu1()
def menu():
    #makes sure you use the write code or whateves
    welcome = input("Signup(S) or login(L)? (S/L): ")  
    if welcome.lower() =="s":
        signupmenu()
    if welcome.lower()=="l":
        loginmenu()
    else:
        print("Incorrect input! Please use 'S' or 'L'")
        menu()
def signupmenu():
    new_username = input("Enter a new username: ")
    users = {}
    with open("users.txt") as f:
        for line in f:
            username, password = line.strip().split(",")
            users[username] = password
    if new_username in users:
            #this makes sure there are no duplicates
            print("Username already exists.")
            signupmenu()
    new_password = input("Enter a new password: ")
    with open("users.txt", "a") as f:
        f.write(f"{new_username},{new_password}\n")
    menu()

def loginmenu():
    global test
    global input_username
    #this reopens users.txt so it shows the updated .txt if your trying to login after creating an
    #account in the same session
    input_username = input("Enter your username: ")
    username111 = "Adam123"
    input_password = input("Enter your password: ")
    users = {}
    with open("users.txt") as f:
        for line in f:
            username, password = line.strip().split(",")
            users[username] = password
    if input_username in users and input_password == users[username111]:
        test = True
        print("Login successful!")
        print("\nWelcome Administrator",username111)
        menu1()
    elif input_username in users and input_password == users[input_username]:
        test = False
        print("Login successful!")
        print("\nWelcome,",input_username)
        menu1()
    else:
        print("Invalid username or password.")
        menu()

def database(test):
    if test:
        with open("users.txt", "r") as f:
            contents = f.read()
            print("\nDATABASE CONTENTS\n")
            print(contents)
            menu1()
    else:
        print("NO ACCESS")
        menu1()

def ssetup():
    global ssock
    ssock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssock.bind((HOST, PORT))
    ssock.listen(1)

def swait():
    global csock
    global caddr
    print("Server started on " + str(HOST) + ":" + str(PORT))
    csock, caddr = ssock.accept()
    print("Connection started with " + str(caddr[0]) + ":" + str(caddr[1]))
    signal = "You have joined the server: " + str(HOST) + ":" + str(PORT)
    csock.sendall(signal.encode())

def cjoin():
    global csock
    csock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        csock.connect((HOST, PORT))
    except:
        print("Cannot find server")
        return False
    return True

def receive():
    while True:
        try:
            print(csock.recv(1024).decode())
        except:
            return

def chatmain():
    # Make global
    global HOST
    global PORT
    global ssock
    global csock
    global hosting

    # Setup server and username
    prompt = input("Would you like to host a server?\n\n1.Yes\n2.No\n\nWhat is your selection: ")
    
    if prompt == "1":
        HOST = input("What is your IP: ")
        PORT = input("What port do you want to host on: ")
        print("Server starting on " + str(HOST) + ":" + str(PORT))
        ssetup()
        swait()
        hosting = True
    if prompt == "2":
        HOST = input("What is the host's IP: ")
        POST = input("What is the host's PORT: ")
        if not cjoin():
            return
        print(csock.recv(1024).decode())
    else:
        ("INVALID INPUT")
        onlinemenu()

    print("Type \"/quit\" when you would like to leave the server")

    # Setup receive thread
    treceive = threading.Thread(target=receive)
    treceive.start()
    
    # Send-receive loop
    while True:
        message = input("> ")
        if message == "/quit":
            csock.close()
            #ssock.close()
            menu1()
        message = input_username + ": " + message
        print(message)
        try:
            csock.sendall(message.encode())
        except:
            print("Disconnected")
            menu1()
time1()

    
        
