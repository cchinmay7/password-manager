import string

import mysql.connector

import random

from sys import exit

from tabulate import tabulate

con = mysql.connector.connect(host="localhost", user="root", password = "0000", database="password")

#This variable is used to establish a connection between Python and MySQL

case = ''

score = 0

class PasswordGenerator:
#This class is used to generate a random password    

    def __init__(self, length):
        self.length = length

    def generate_password(self):
        password = ""
        
        count = 0
        
        while count < self.length:
            password += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=[]{}|;:,.<>?")
        
            count = count + 1    
        
        return password

def check(password, case):
#This function is used in strength()
    
    global score
    
    val = 0
    
    for char in password:
        
        if char in case:
            
            score = score + 1
            
            break
    
    return val

def strength(pass1):
#This function is used to check the strength
    
    global score
    
    with open('10k-most-common.txt','r') as f:
        common = f.read().splitlines()
    
    check(pass1, string.ascii_uppercase)
    
    check(pass1, string.punctuation)
    
    check(pass1, string.digits)
    
    length = len(pass1)
    
    
    if pass1 in common:
        
        print("This password is COMMONLY USED. Try a different password.")
        
        score = 0
        
    else:    
        if length < 8:
        
            print("Password TOO SHORT.")
        
            score = 0
        
        else:   
        
        
            if length >= 8:
        
                score = score + 1
    
            if length >= 12:

                score = score + 1
    
            if length >= 16:
        
                score = score + 1
    
            if length >= 20:
        
                score = score + 1
    
    
            if score <= 3:
        
                print("The password is VERY WEAK.")
        
            elif score <= 4:
        
                print("The password is WEAK.")
        
            elif score <= 5:
        
                print("The password is STRONG.")    
    
            else:
        
                print("The password is VERY STRONG.")

def addpass(a,b,c):
#THIS FUNCTION IS DEFINED BY THE USER    

    
    cur=con.cursor()
    query = "INSERT INTO logincredentials(Website, UserID, Password) VALUES ('{}', '{}', '{}')".format(a,b,c)
    cur.execute(query)
    con.commit()
    
    
    print()
    print("Your password was added successfully!!")
    
def delpass():
    
    Web1 = input("Enter the website: ")
    UID2 = input("Enter the User ID: ")
    
    print("Are you sure that you want to delete:- ") 
    
    cur=con.cursor()
    query = "Select Website, UserID, Password from logincredentials where website='{}' and UserID = '{}'".format(Web1, UID2)
    cur.execute(query)
    data=cur.fetchall()
    x=["Website","UserID","Password"]
    print(tabulate(data, headers=x,tablefmt="grid"))
    
    confirm = input('[y/n]: ')
    
    if confirm == 'y' or confirm == 'Y':
        
        cur = con.cursor()
        query="delete from logincredentials where Website='{}' and UserID = '{}' ".format(Web1, UID2)
        cur.execute(query)
        con.commit()
        
        print('Deletion successful')
     
    else:
         
        print("Deletion Cancelled")

def updpass():
#THIS FUNCTION IS USED TO UPDATE PASSWORDS    
    web3 = input("Please enter the website: ")
    
    uid3 = input("Please enter the UserID: ")
    
    
    print("You will be updating:-")
    
    cur=con.cursor()
    query = "Select Website, UserID, Password from logincredentials where website='{}' and UserID = '{}'".format(web3, uid3)
    cur.execute(query)
    data=cur.fetchall()
    x=["Website","UserID","Password"]
    print(tabulate(data, headers=x,tablefmt="grid"))
    
    print("""
1. Update Website
2. Update User ID
3. Update Password
    
Enter e to exit
    """)
    
    choice_2 = str(input('[1/2/3]: '))
    
    
    if choice_2 == '1':
        
        upd_web = input("Enter the new website: ")
        #HERE I TOOK AN INPUT FROM THE USER [1]
                
        cur=con.cursor()
        query="update logincredentials set Website = '{}' where Website='{}' and UserID='{}'".format(upd_web,web3,uid3)
        cur.execute(query)
        con.commit()  
        
        print("Website updated successfully!")
        
    elif choice_2 == '2':
        
        upd_uid = input("Enter the new User ID: ")
                
        cur=con.cursor()
        query="update logincredentials set UserID = '{}' where Website='{}' and UserID='{}'".format(upd_uid,web3,uid3)
        cur.execute(query)
        con.commit() 
        
        print("User ID updated successfully!")
        
    elif choice_2 == '3':
        
        upd_pass = input("Enter the new password: ")
                
        cur=con.cursor()
        query="update logincredentials set Password = '{}' where Website='{}' and UserID='{}'".format(upd_pass,web3,uid3)
        cur.execute(query)
        con.commit() 
        
        print("Password updated successfully!")
        
    elif choice_2 == 'e' or choice_2 == 'E':
        
        exit()
        
    else:
        
        print('Invalid input')
    
def viewpass():

    

    print("""
1. View all passwords.
2. View password by website.
3. View passowed by User ID.
    
Enter e to exit.
    """)
    
    choice_1 = str(input("Which service would you like to choose? (1/2/3): "))
    
    if choice_1 == '1':    
    
        cur=con.cursor()
        cur.execute("Select * from logincredentials")
        data=cur.fetchall()
        x=["SNo","Website","UserID","Password"]
        print(tabulate(data, headers=x,tablefmt="grid"))
    
    elif choice_1 == '2':
        
        web = input('Enter the website: ')
        
        cur=con.cursor()
        query = "Select * from logincredentials where website='{}'".format(web)
        cur.execute(query)
        data=cur.fetchall()
        x=["SNo","Website","UserID","Password"]
        print(tabulate(data, headers=x,tablefmt="grid"))
     
    elif choice_1 == '3':
        
        UID = input('Enter the UserID: ')
        
        cur=con.cursor()
        query = "Select * from logincredentials where UserID='{}'".format(UID)
        cur.execute(query)
        data=cur.fetchall()
        x=["SNo","Website","UserID","Password"]
        print(tabulate(data, headers=x,tablefmt="grid"))
        
        
    elif choice_1 == 'e' or choice_1 == 'E':
        
        exit()
        
    else:
        
        print('Invalid input')

def initial():
    
    global score
    
    print("""
__________**PASSWORD MANAGER**__________      
    """)

    print("""
1. Add a new password
2. Update existing passwords
3. Delete existing passwords
4. View Passwords
5. Check password strength
6. Generate a random password

Enter e to exit
_________________________________________
    """)

    choice = str(input("Which service would you like to choose? (1/2/3/4/5/6/e): "))
    
    print()
    
    if choice == 'e' or choice == 'E':
    
        exit()
    
    elif choice == '1':
        
        ab = input('Please enter a website: ')
        bc = input('Please enter your User ID: ')
        ca = input('Please enter your password: ')
        
        
        addpass(ab, bc, ca)
        
        initial()

    elif choice == '2':
    
        updpass()
        
        initial()
    
    elif choice == '3':
    
        delpass()  
        
        initial()
    
    elif choice == '4':
    
        viewpass()
        
        initial()
    
    elif choice == '5':
        
        val = input('Enter your passwords to check their strength: ')
        
        print()
        
        strength(val)
        
        score = 0
        
        initial()

    elif choice == '6':
        
        len1 = int(input("Enter the length of the password you want to generate: "))
        
        len8 = float(len1)
        #HERE THE FUNCTION FLOAT CONVERTS AN INT VALUE TO FLOAT
        
        
        len1 = int(len8)
        
        choose1 = input("would you like to use a keyword? [y/n] "  )
        
        if choose1 == 'y' or choose1 == 'Y':
            
            key = input("Enter your keyword: ")
            
            len2 = len(key)
            
            generator = PasswordGenerator(len1-len2)
            password = generator.generate_password()
            
            len3 = len(password)

            list1 = list(password)
            #THE USE OF A LIST IS EMPLOYED HERE
            
            
            len1 = random.randint(1,len3)

            list1.insert(len1, key)
            
            newpass = ""
            
            for i in list1:
    
                newpass += i
            
            
            print("The password is:",newpass)
            
            
        elif choose1 == 'n' or choose1 == 'N':
            
            generator = PasswordGenerator(len1)
            password = generator.generate_password()
            print("The password is:",password)
        
        choice_3 = input('Would you like to save this password for yourself? [y/n]: ')
        
        if choice_3 == 'y' or choice_3 == 'Y':
            
            Web9 = input("Enter the website: ")
            UID4 = input("Enter the User ID: ")
            
            addpass(Web9, UID4, password)
        
            print('New password added successfully')
            
            initial()
            
        else:
         
            print("Password was not saved.")
            
            initial()
        
        

    else:
        
        print('Invalid Input')
        
        initial()


initial()

