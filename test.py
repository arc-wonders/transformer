import mysql.connector

conn = mysql.connector.connect(host='localhost', user='root', password='aps12')

if conn.is_connected():
    print("Successfully connected")

c1 = conn.cursor()
'''
mn = "CREATE DATABASE IF NOT EXISTS ATM_MACHINE"
c1.execute(mn)

mn = "USE ATM_MACHINE"
c1.execute(mn)

mn = "CREATE TABLE RECORDS(ACCOUNT_NO INT(4) primary key, PASSWORD INT(3), NAME VARCHAR(20), CR_AMT INT DEFAULT 0, WITHDRAWAL INT DEFAULT 0, BALANCE INT DEFAULT 0)"
c1.execute(mn)

print("Successfully created")
'''
conn = mysql.connector.connect(host='localhost', user='root', password='aps12', database='ATM_MACHINE')
c1 = conn.cursor()

print("===============================================")
print(" WELCOME TO ATM ")
print("===============================================")
print("1. To create account")
print("2. To login")
print("3. Change password")
print("4. Delete account")
print("5. Exit")
print("===============================================")

op = int(input("Enter your choice: "))
print("===============================================")

if op == 1:
    c = "y"
    while c == "y":
        m = int(input("Enter a 4 digit number as account number: "))
        cb = "SELECT * FROM records WHERE ACCOUNT_NO={}".format(m)
        c1.execute(cb)
        d = c1.fetchall()
        data = c1.rowcount
        if data == 1:
            print("===============================================")
            print("This account number already exists:")
            c = input("Do you want to continue y/n - ")
            print("===============================================")
            if c == "y":
                continue
            else:
                print(" Thank you.")
                print(" PLEASE CLOSE THIS FILE BEFORE EXITING")
                print("Visit again")
                print("===============================================")
        else:
            name = input("Enter your name: ")
            passw = int(input("Enter your password (integer only): "))
            ab = "INSERT INTO records(ACCOUNT_NO, PASSWORD, NAME) VALUES({}, {}, '{}')".format(m, passw, name)
            print("===============================================")
            c1.execute(ab)
            conn.commit()
            print("Account successfully created")
            print("The minimum balance is 1000 ")
            print("===============================================")
            s = int(input("Enter the money to be deposited: "))
            print("===============================================")
            while s < 1000:
                print("Minimum balance is 1000")
                s = int(input("Enter money to be deposited: "))
            else:
                sr = "UPDATE records SET CR_AMT={} WHERE ACCOUNT_NO={}".format(s, m)
                c1.execute(sr)
                conn.commit()
                ef = "UPDATE records SET BALANCE=CR_AMT-WITHDRAWAL WHERE ACCOUNT_NO={}".format(m)
                c1.execute(ef)
                conn.commit()
                print("Successfully deposited")
                break

if op == 2:
    count = 0
    y = "y"
    acct = int(input("Enter your account number: "))
    cb = "SELECT * FROM records WHERE ACCOUNT_NO={}".format(acct)
    c1.execute(cb)
    c1.fetchall()
    data = c1.rowcount
    if data == 0:
        print("Account does not exist")
    elif data == 1:
        pas = int(input("Enter your password : "))
        print("===============================================")
        while y == "y":
            e = "SELECT PASSWORD FROM records WHERE ACCOUNT_NO={}".format(acct)
            c1.execute(e)
            a = c1.fetchone()
            d = list(a)
            if pas == d[0]:
                print("correct")
                print("1. Depositing money")
                print("2. Withdrawing money")
                print("3. Transferring money")
                print("4. Checking balance")
                print("5. Changing Account name ")
                print("===============================================")
                r = int(input("Enter your choice: "))
                print("===============================================")
                if r == 1:
                    amt = int(input("Enter the money to be deposited: "))
                    print("===============================================")
                    sr = "UPDATE records SET CR_AMT=CR_AMT + {} WHERE ACCOUNT_NO={}".format(amt, acct)
                    c1.execute(sr)
                    conn.commit()
                    ef = "UPDATE records SET BALANCE=CR_AMT-WITHDRAWAL WHERE ACCOUNT_NO={}".format(acct)
                    c1.execute(ef)
                    conn.commit()
                    print("Successfully deposited")
                    t = input("Do you want to continue y/n - ")
                    print("===============================================")
                    if t == "y":
                        continue
                    else:
                        print(" Thank you")
                        print(" PLEASE CLOSE THIS FILE BEFORE EXITING")
                if r == 2:
                    amt = int(input("Enter the money to withdraw: "))
                    print("===============================================")
                    ah = "SELECT BALANCE FROM records WHERE ACCOUNT_NO={}".format(acct)
                    c1.execute(ah)
                    m = c1.fetchone()
                    if amt > m[0]:
                        print("You are having less than", amt)
                        print("Please try again")
                    else:
                        sr = "UPDATE records SET BALANCE=BALANCE - {} WHERE ACCOUNT_NO={}".format(amt, acct)
                        ed = "UPDATE records SET WITHDRAWAL ={} WHERE ACCOUNT_NO={}".format(amt, acct)
                        c1.execute(ed)
                        c1.execute(sr)
                        conn.commit()
                        print("Successfully updated")
                        y = input("Do you want to continue y/n - ")
                        print("===============================================")
                        if y == "y":
                            continue
                        else:
                            print(" Thank you")
                            print(" PLEASE CLOSE THIS FILE BEFORE EXITING")
                if r == 3:
                    act = int(input("Enter the account number to be transferred : "))
                    print("===============================================")
                    if acct == act:
                        print("Cannot transfer money from the same account. Try a different account")
                    else:
                        cb = "SELECT * FROM records WHERE ACCOUNT_NO={}".format(act)
                        c1.execute(cb)
                        c1.fetchall()
                        data = c1.rowcount
                        if data == 1:
                            print(act, "number exists")
                            m = int(input("Enter the money to be transferred : "))
                            print("===============================================")
                            ah = "SELECT BALANCE FROM records WHERE ACCOUNT_NO={}".format(acct)
                            c1.execute(ah)
                            c = c1.fetchone()
                            if m > c[0]:
                                print("You are having less than", m)
                                print("Please try again")
                            else:
                                av = "UPDATE records SET BALANCE=BALANCE-{} WHERE ACCOUNT_NO={}".format(m, acct)
                                cv = "UPDATE records SET BALANCE=BALANCE+{} WHERE ACCOUNT_NO={}".format(m, act)
                                w = "UPDATE records SET WITHDRAWAL=WITHDRAWAL+{} WHERE ACCOUNT_NO={}".format(m, acct)
                                t = "UPDATE records SET CR_AMT=CR_AMT+{} WHERE ACCOUNT_NO={}".format(m, act)
                                c1.execute(av)
                                c1.execute(cv)
                                c1.execute(w)
                                c1.execute(t)
                                conn.commit()
                                print("Successfully transferred")
                                y = input("Do you want to continue y/n - ")
                                print("===============================================")
                                if y == "y":
                                    continue
                                else:
                                    print(" Thank you")
                                    print(" PLEASE CLOSE THIS FILE BEFORE EXITING")
                if r == 4:
                    ma = "SELECT BALANCE FROM records WHERE ACCOUNT_NO={}".format(acct)
                    c1.execute(ma)
                    k = c1.fetchone()
                    print("Balance in your account =", k[0])
                    print("===============================================")
                    y = input("Do you want to continue y/n - ")
                    if y == "y":
                        continue
                    else:
                        print(" Thank you")
                        print(" PLEASE CLOSE THIS FILE BEFORE EXITING")
                if r == 5:
                    i = int(input("Enter your account number: "))
                    j = input("Enter new name: ")
                    update_query = "UPDATE records SET NAME=%s WHERE ACCOUNT_NO=%s"
                    data = (j, i)
                    c1.execute(update_query, data)
                    conn.commit()
                    print("Your new account name is", j)
        else:
            if pas != d[0]:
                print("Wrong password")
                print("===============================================")
                count = count + 1
                if count == 3:
                    print('-----------------------------------')
                    print('***********************************')
                    print('3 UNSUCCESSFUL PIN ATTEMPTS, EXITING')
                    print('!!!!!YOUR CARD HAS BEEN LOCKED!!!!!')
                    print('***********************************')
                    print('-----------------------------------')
                else:
                    y = input("Do you want to continue y/n - ")
            else:
                print("correct")

else:
    if op == 3:
        acct = int(input("Enter your account number: "))
        cb = "SELECT * FROM records WHERE ACCOUNT_NO={}".format(acct)
        c1.execute(cb)
        user_info = c1.fetchall()
        cc = "SELECT NAME FROM records WHERE ACCOUNT_NO={}".format(acct)
        c1.execute(cc)
        username = c1.fetchall()
        username_real = username[0][0]
        print("Hello", username_real)
        pas = int(input("Enter old password"))
        e = "SELECT PASSWORD FROM records WHERE ACCOUNT_NO={}".format(acct)
        c1.execute(e)
        a = c1.fetchone()
        d = list(a)
        if pas == d[0]:
            print("correct")
            new_pas = int(input("Enter new password: "))
            new_pas_conf = int(input("Confirm new password: "))
            while new_pas != new_pas_conf:
                print("Password do not match. Try again.")
                new_pas = int(input("Enter new password: "))
                new_pas_conf = int(input("Confirm new password: "))
            if new_pas == new_pas_conf:
                print("Passwords match")
                update_query = f"UPDATE records SET PASSWORD = '{new_pas_conf}' WHERE ACCOUNT_NO = {acct}"
                c1.execute(update_query)
                conn.commit()
                print("Your password has been updated")
            else:
                print("Passwords match")
                update_query = f"UPDATE records SET PASSWORD = '{new_pas_conf}' WHERE ACCOUNT_NO = {acct}"
                c1.execute(update_query)
                conn.commit()
                print("Your password has been updated")
    if op == 4:
        acct = int(input("Enter the account number to delete: "))
        pas = int(input("Enter password"))
        e = "SELECT PASSWORD FROM records WHERE ACCOUNT_NO={}".format(acct)
        c1.execute(e)
        a = c1.fetchone()
        d = list(a)
        if pas == d[0]:
            print("correct")
            f = "SELECT BALANCE FROM records WHERE ACCOUNT_NO={}".format(acct)
            c1.execute(f)
            b = c1.fetchone()
            if b[0] != 0:
                print("Your current balance is Rs.", b[0])
                print("Withdraw all money from the bank account first.")
            else:
                delete_query = f"DELETE FROM records WHERE ACCOUNT_NO = '{acct}'"
                c1.execute(delete_query)
                conn.commit()
                print("Your account has been deleted")
    if op == 5:
        print("Exiting")
        c1.close()