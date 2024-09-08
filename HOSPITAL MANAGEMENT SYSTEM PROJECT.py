#importing modules
import random
import mysql.connector as sqltor
#mysql-python connection
mycon=sqltor.connect(host="localhost",user="root",passwd="1234",database="divya")
#cursorobject
cursor=mycon.cursor()
def Login(User_id,Password):
        cursor.execute("select UserID from user_password_database")
        n1=cursor.fetchall()
        while True:
                if (User_id,) in n1:
                        cursor.execute("select UserID,Password from user_password_database where UserID='{}'".format(User_id))
                        t=cursor.fetchall()[0]
                        n2=t[1]
                        if Password==n2:
                                print("Success")
                                break
                        else:
                                print("Wrong Password!!")
                                Password= int(input("Enter Your Password Again :"))
                else:
                    print("This user ID does not exist!!")
                    User_id=input("Enter User ID again:")
                    Password= int(input("Enter Your Password Again :"))
#login complete---------
def Check(database,name):
    v=0
    cursor.execute("select * from {}".format(database))
    m=cursor.fetchall()
    for i in range(0,len(m)):
        if name == m[i][0]:
            V=1
            return V
#-----------------------------------
#management mode----------
def Management_mode():
    print("                                        ~~*^^*WELCOME TO THE MANAGEMENT MODE*^^*~~                                      ")
    Value1=True
    while Value1:
        print()
        print()
        print("                                                    ~~*^^*OPTIONS*^^*~~                                                 ")
        print("########################################################################################################################")
        print("#                                                                                                                      #")
        print("#                                                                                                                      #")
        print("#                                         1.    MANAGE DOCTORS & STAFFS                                                #")
        print("#                                         2.    MANAGE PATIENTS                                                        #")
        print("#                                                                                                                      #")
        print("#                                                                                                                      #")
        print("########################################################################################################################")
        ch=int(input("Enter your Choice    :"))
        Flag=True
        if (ch==1):
            while Flag:
                print("########################################################################################################################")
                print("#                                                                                                                      #")
                print("#                                     1.    DOCTORS                                                                    #")
                print("#                                     2.    STAFFS                                                                     #")
                print("#                                                                                                                      #")
                print("########################################################################################################################")
                ch1=int(input("Enter your Choice    :"))
                if (ch1==1):
                    Drop1=True
                    while Drop1:
                        print()
                        print("1.    DISPLAY ALL DOCTORS")
                        print("2.    SEARCH FOR A SPECIFIC DOCTOR")
                        print("3.    ADD NEW DOCTORS")
                        print("4.    UPDATE INFORMATION OF A SPECIFIC DOCTOR")
                        print()
                        choice=int(input("Enter your Choice    :"))
                        if(choice==1):
                            print("________________________________________________________________________________________________________________________")
                            print("                                       ~~*^^*DISPLAYING LIST OF ALL DOCTORS*^^*~~                                       ")
                            print()
                            print()
                            cursor.execute("select * from doctors_info_database")
                            l=cursor.fetchall()
                            for i in range(0,len(l)):
                                a=i+1
                                print("_________________________________________________RECORD NO.",a,"_________________________________________________")
                                print("Doctor's Name :",l[i][0])
                                print("Doctor's Address  :", l[i][1])
                                print("Doctor's Gender:",l[i][2])
                                print("Doctor's Age:",l[i][3])
                                print("Doctor's Joining day:",l[i][4])
                                print("Doctor's Years of Experience:",l[i][5])
                                print("Doctor's field of Specialisation:",l[i][6])
                                print("Is he/she on Covid Duty:",l[i][7])
                                print("________________________________________________________________________________________________________________________")
                        elif (choice==2):
                            print("________________________________________________________________________________________________________________________")
                            print("                                       ~~*^^*SEARCHING FOR A SPECIFIC DOCTOR*^^*~~                                       ")
                            print()
                            print()
                            Value=True
                            V=0
                            data="doctors_info_database"
                            while Value:
                                name=input("Enter the name of the Doctor    :")
                                if (Check(data,name)==1):
                                   cursor.execute("select * from doctors_info_database where Name='{}'".format(name))
                                   m1=cursor.fetchall()
                                   for i in range(0,len(m1)):
                                           if (m1[i][0]==name):
                                                   print("Doctor's Name :",m1[0][0])
                                                   print("Doctor's Address  :",m1[0][1])
                                                   print("Doctor's Gender",m1[0][2])
                                                   print("Doctor's Age",m1[0][3])
                                                   print("Doctor's Joining day",m1[0][4])
                                                   print("Doctor's Years of Experience",m1[0][5])
                                                   print("Doctor's field of Specialisation",m1[0][6])
                                                   print("Is he/she on Covid Duty",m1[0][7])
                                                   ch=input("SEARCH MORE DOCTORS?[TYPE 'n' FOR NO]")
                                                   if (ch=="n"):
                                                           Value=False
                                else:
                                    print("NO DOCTOR WITH SUCH A NAME IS PRESENT HERE !")
                                    ch=input("Try searching once again ?[y/n]")
                                    if (ch=="n"):
                                        Value=False    
                        elif (choice==3):
                            print("________________________________________________________________________________________________________________________")
                            print("                                        ~~*^^*ADDING NEW DOCTORS*^^*~~                                       ")
                            print()
                            print()
                            def write_database(Doctors_name,Doctors_address,Gender,Age,Joining,Experience,Specialisation,Covid_duty):
                                cursor.execute("insert into doctors_info_database (Name, address, Gender, Age, Joined, Experience, Specialisation, Availability) values('{}', '{}', '{}', {}, '{}', {}, '{}', '{}')".format(Doctors_name, Doctors_address, Gender, Age, Joining, Experience, Specialisation, Covid_duty))
                                mycon.commit()
                                print("Data Entered Successfully!!")
                            Value=True
                            while Value:        
                                Doctors_name=input("Enter the name of the Doctor  :")
                                Doctors_address=input("Enter the address where he/she lives :")
                                Gender=input("Enter the gender  :")
                                Age=int(input("Enter the doctor's age  :"))
                                Joining=input("Enter the date of joining[yyyy-mm-dd]  :")
                                Experience=int(input("Enter the years of Experience  :"))
                                Specialisation=input("Enter the field of Specialisation  :")
                                Covid_duty=input("Enter if he/she is under covid duty or not[y/n]  :")
                                write_database(Doctors_name,Doctors_address,Gender,Age,Joining,Experience,Specialisation,Covid_duty)
                                ch=input("Enter more Information?[y/n]  :")
                                if (ch=="n"):
                                    Value=False        
                        elif (choice==4):
                            data="doctors_info_database"
                            Value=True
                            while Value:
                                nam=input("Enter the name of the Doctor    :")
                                if (Check(data,nam)==1):
                                    cursor.execute("select * from doctors_info_database where Name ='{}'".format(nam))
                                    m2=cursor.fetchall()
                                    for i in range (0,len(m2)):
                                        if m2[0][0]==nam:
                                            print("________________________________________________________________________________________________________________________")
                                            print("                                       ~~*^^*UPDATATION OF INFORMATION*^^*~~                                       ")
                                            Doctors_name=input("Enter the name of the Doctor  :")
                                            Doctors_address=input("Enter the address where he/she lives :")
                                            Gender=input("Enter the gender  :")
                                            Age=int(input("Enter the doctor's age  :"))
                                            Joining=input("Enter the date of joining[yyyy-mm-dd]  :")
                                            Experience=int(input("Enter the years of Experience  :"))
                                            Specialisation=input("Enter the field of Specialisation  :")
                                            cursor.execute("update doctors_info_database set Name='{}', address='{}', Gender='{}', Age={}, Joined='{}',Experience={}, Specialisation='{}' where Name='{}' ".format(Doctors_name, Doctors_address, Gender, Age, Joining, Experience, Specialisation,nam))
                                            mycon.commit()
                                            print("DATA UPDATED SUCCESSFULLY!")
                                            print("________________________________________________________________________________________________________________________")

                                    ch=input("Update more data?[y/n]")
                                    if (ch=="n"):
                                        print("________________________________________________________________________________________________________________________")
                                        Value=False
                                else:
                                    ch=input("NO DOCTOR WITH SUCH NAME IS PRESENT! TRY AGAIN?[TYPE 'n' FOR NO]")
                                    if (ch=="n"):
                                        print("________________________________________________________________________________________________________________________")
                                        Value=False
                        else:
                            print("WRONG CHOICE!TRY AGAIN?")
                        ch0=input("GO TO THE PREVIOUS OPTIONS ?[ TYPE 'n' FOR NO]")
                        if (ch0=="n"):
                            print("________________________________________________________________________________________________________________________")
                            Drop1=False

                elif(ch1==2):
                    Drop2=True
                    while Drop2:
                        print()
                        print("1.    DISPLAY ALL STAFFS")
                        print("2.    SEARCH FOR A SPECIFIC STAFF MEMBER")
                        print("3.    ADD NEW STAFF MEMBER")
                        print("4.    UPDATE INFORMATION OF A SPECIFIC STAFF MEMBER")
                        print()
                        choice=int(input("Enter your Choice    :"))
                        if(choice==1):
                            print("________________________________________________________________________________________________________________________")
                            print("                                       ~~*^^*DISPLAYING LIST OF ALL STAFFS*^^*~~                                       ")
                            print()
                            print()
                            cursor.execute("select * from staffs_info_database")
                            l=cursor.fetchall()
                            for i in range(0,len(l)):
                                a=i+1
                                print("_________________________________________________RECORD NO.",a,"_________________________________________________")
                                print("Staff's Name :",l[i][0])
                                print("Staff's Address  :", l[i][1])
                                print("Staff's Gender:",l[i][2])
                                print("Staff's Age:",l[i][3])
                                print("Staff's Joining day:",l[i][4])
                                print("Staff's Years of Experience:",l[i][5])
                                print("Is he/she on Covid Duty:",l[i][6])
                                print("________________________________________________________________________________________________________________________")
                        elif(choice==2):
                            print("________________________________________________________________________________________________________________________")
                            print("                                       ~~*^^*SEARCHING FOR A SPECIFIC STAFF*^^*~~                                       ")
                            print()
                            print()
                            Value=True
                            V=0
                            data="staffs_info_database"
                            while Value:
                                name=input("Enter the name of the Staff    :")
                                if (Check(data,name)==1):
                                   cursor.execute("select * from staffs_info_database where Name='{}'".format(name))
                                   m1=cursor.fetchall()
                                   for i in range(0,len(m1)):
                                           if (m1[i][0]==name):
                                                   print("Staff's Name :",m1[0][0])
                                                   print("Staff's Address  :",m1[0][1])
                                                   print("Staff's Gender",m1[0][2])
                                                   print("Staff's Age",m1[0][3])
                                                   print("Staff's Joining day",m1[0][4])
                                                   print("Staff's Years of Experience",m1[0][5])
                                                   print("Is he/she on Covid Duty",m1[0][6])
                                                   ch=input("SEARCH MORE STAFFS ?[TYPE 'n' FOR NO]")
                                                   if (ch=="n"):
                                                           Value=False
                                else:
                                    ch=input("NO STAFF MEMBER WITH SUCH NAME IS PRESENT! TRY AGAIN?[TYPE 'n' FOR NO]")
                                    if (ch=="n"):
                                        print("________________________________________________________________________________________________________________________")
                                        Value=False
                        elif (choice==3):
                                print("________________________________________________________________________________________________________________________")
                                print("                                        ~~*^^*ADDING NEW STAFF MEMBER*^^*~~                                       ")
                                print()
                                print()
                                def write_database(Staffs_name,Staffs_address,Gender,Age,Joining,Experience,Covid_duty):
                                        cursor.execute("insert into staffs_info_database (Name, address, Gender, Age, Joined, Experience, Availability) values('{}', '{}', '{}', {}, '{}', {}, '{}')".format(Staffs_name, Staffs_address, Gender, Age, Joining, Experience, Covid_duty))
                                        mycon.commit()
                                        print("Data Entered Successfully!!")
                                Value=True
                                while Value:        
                                        Staffs_name=input("Enter the name of the Staff  :")
                                        Staffs_address=input("Enter the address where he/she lives :")
                                        Gender=input("Enter the gender  :")
                                        Age=int(input("Enter the staff's age  :"))
                                        Joining=input("Enter the date of joining[yyyy-mm-dd]  :")
                                        Experience=int(input("Enter the years of Experience  :"))
                                        Covid_duty=input("Enter if he/she is under covid duty or not[y/n]  :")
                                        write_database(Staffs_name,Staffs_address,Gender,Age,Joining,Experience,Covid_duty)
                                        ch=input("Enter more Information?[y/n]  :")
                                        if (ch=="n"):
                                                Value=False
                        elif(choice==4):
                            data="staffs_info_database"
                            Value=True
                            V=0
                            while Value:
                                nam=input("Enter the name of the Staff    :")
                                if (Check(data,nam)==1):
                                    cursor.execute("select * from staffs_info_database where Name ='{}'".format(nam))
                                    m2=cursor.fetchall()
                                    for i in range (0,len(m2)):
                                        if m2[0][0]==nam:
                                            print("________________________________________________________________________________________________________________________")
                                            print("                                       ~~*^^*UPDATATION OF INFORMATION*^^*~~                                       ")
                                            Staffs_name=input("Enter the name of the Staff  :")
                                            Staffs_address=input("Enter the address where he/she lives :")
                                            Gender=input("Enter the gender  :")
                                            Age=int(input("Enter the staff's age  :"))
                                            Joining=input("Enter the date of joining[yyyy-mm-dd]  :")
                                            Experience=int(input("Enter the years of Experience  :"))
                                            cursor.execute("update staffs_info_database set Name='{}', address='{}', Gender='{}', Age={}, Joined='{}',Experience={} where Name='{}'".format(Staffs_name, Staffs_address, Gender, Age, Joining, Experience, nam))
                                            mycon.commit()
                                            print("DATA UPDATED SUCCESSFULLY!")
                                            print("________________________________________________________________________________________________________________________")
                                    ch=input("Update more data?[y/n]")
                                    if (ch=="n"):
                                        print("________________________________________________________________________________________________________________________")
                                        Value=False
                                else:
                                    ch=input("NO STAFF MEMBER WITH SUCH NAME IS PRESENT! TRY AGAIN?[TYPE 'n' FOR NO]")
                                    if (ch=="n"):
                                        print("________________________________________________________________________________________________________________________")
                                        Value=False            
                        else:
                            print("WRONG CHOICE ENTERED!!")
                        ch0=input("GO TO THE PREVIOUS OPTIONS ?[ TYPE 'n' FOR NO]")
                        if (ch0=="n"):
                            print("________________________________________________________________________________________________________________________")
                            Drop2=False
                else:
                    print("WRONG CHOICE!!")
                ch=input("CHANGE DOCTORS/STAFFS MODE?[TYPE 'n' FOR NO]")
                if (ch=='n'):
                        print("________________________________________________________________________________________________________________________")
                        Flag=False               
        elif(ch==2):
            Valueh=True
            while Valueh:
                print()
                print("1.    DISPLAY ALL PATIENTS")
                print("2.    SEARCH FOR A SPECIFIC PATIENT")
                print("3.    ADD NEW PATIENTS")
                print("4.    UPDATE INFORMATION OF A SPECIFIC PATIENT")
                print()
                c=int(input("Enter the Choice     :"))
                if (c==1):
                    print("________________________________________________________________________________________________________________________")
                    print("                                       ~~*^^*DISPLAYING LIST OF ALL PATIENTS*^^*~~                                       ")
                    print()
                    print()
                    cursor.execute("select * from patients_database")
                    l=cursor.fetchall()
                    for i in range(0,len(l)):
                            a=i+1
                            print("_________________________________________________RECORD NO.",a,"_________________________________________________")
                            print("Name of the patient :",l[i][0])
                            print("Address where he/she lives  :", l[i][1])
                            print("Age of the patient:",l[i][2])
                            print("Patient's Gender :",l[i][3])
                            print("Is he/she  a covid patient :",l[i][4])
                            print("________________________________________________________________________________________________________________________")
                elif (c==2):
                    print("________________________________________________________________________________________________________________________")
                    print("                                       ~~*^^*SEARCHING FOR A SPECIFIC PATIENT*^^*~~                                       ")
                    print()
                    print()
                    Value=True
                    V=0
                    data="patients_database"
                    while Value:
                            name=input("Enter the name of the Patient    :")
                            if (Check(data,name)==1):
                                    cursor.execute("select * from patients_database where Name='{}'".format(name))
                                    m1=cursor.fetchall()
                                    for i in range(0,len(m1)):
                                            if (m1[i][0]==name):
                                                    print("Name of the patient :",m1[0][0])
                                                    print("Address where he/she lives :",m1[0][1])
                                                    print("Age of the patient:",m1[0][2])
                                                    print("Patient's Gender :",m1[0][3])
                                                    print("Is he/she  a covid patient ",m1[0][4])
                                                    ch=input("SEARCH MORE PATIENTS ?[TYPE 'n' FOR NO]")
                                                    if (ch=="n"):
                                                        Value=False
                            else:
                                    ch=input("NO PATIENT WITH SUCH NAME IS PRESENT! TRY AGAIN?[TYPE 'n' FOR NO]")
                                    if (ch=="n"):
                                        print("________________________________________________________________________________________________________________________")
                                        Value=False
                elif (c==3):
                    print("________________________________________________________________________________________________________________________")
                    print("                                        ~~*^^*ADDING NEW PATIENT*^^*~~                                       ")
                    print()
                    print()
                    def write_database(Patients_name,Address,Age,Gender,Covid_patient):
                        cursor.execute("insert into patients_database (Name, Address, Age, Gender, Covid) values('{}', '{}', {}, '{}', '{}')".format(Patients_name,Address,Age,Gender,Covid_patient))
                        mycon.commit()
                        print("Data Entered Successfully")
                    Value=True
                    while Value:        
                        Patients_name=input("Enter the name of the Patient    :")
                        Address=input("Enter the Address of where he/she lives    :")
                        Age=int(input("Enter the Age of the Patient    :"))
                        Gender=input("Enter patient's gender    :")
                        Covid_patient=input(" Is he/she covid patient?[y/n]",)
                        write_database(Patients_name,Address,Age,Gender,Covid_patient)
                        ch=input("Enter more Information?[y/n]  :")
                        if (ch=="n"):
                            print("________________________________________________________________________________________________________________________")
                            Value=False
                elif (c==4):
                    Value=True
                    database="patients_database"
                    while Value:
                        nam=input("Enter the name of the Patient    :")
                        if (Check(database,nam)==1):
                                cursor.execute("select * from patients_database where Name ='{}'".format(nam))
                                m2=cursor.fetchall()
                                for i in range (0,len(m2)):
                                        if m2[0][0]==nam:
                                                print("________________________________________________________________________________________________________________________")
                                                print("                                       ~~*^^*UPDATATION OF INFORMATION*^^*~~                                       ")
                                                Patients_name=input("Enter the name of the Patient :")
                                                Address=input("Enter the address where he/she lives :")
                                                Age=int(input("Enter the patient's age  :"))
                                                Gender=input("Enter the gender  :")
                                                Covid_patient=input(" Is he/she covid patient?[y/n]")
                                                cursor.execute("update patients_database set Name='{}', Address='{}', Age={}, Gender='{}', Covid='{}' where Name='{}'".format(Patients_name, Address, Age, Gender, Covid_patient, nam))
                                                mycon.commit()
                                                print("DATA UPDATED SUCCESSFULLY!")
                                                print("________________________________________________________________________________________________________________________")
                                                ch=input("Update more data?[y/n]")
                                                if (ch=="n"):
                                                        print("________________________________________________________________________________________________________________________")
                                                        Value=False
                        else:
                            ch=input("NO PATIENT WITH SUCH NAME IS PRESENT! TRY AGAIN?[TYPE 'n' FOR NO]")
                            if (ch=="n"):
                                print("________________________________________________________________________________________________________________________")
                                Value=False
                else:
                    print("WRONG CHOICE!")
                ch=input("RETURN TO THE PREVIOUS OPTIONS?[TYPE 'n' FOR NO]")
                if (ch=='n'):
                        print("________________________________________________________________________________________________________________________")
                        Valueh=False
        else:
            print("WRONG CHOICE!")
        ch=input("RETURN TO THE FISRT WINDOW OF MANAGEMENT MODE?[TYPE 'n' FOR NO]")
        if (ch=='n'):
            print("________________________________________________________________________________________________________________________")
            Value1=False

            
def Doctors_Staffs_mode():
    print("                                     ~~*^^*WELCOME TO THE DOCTORS & STAFFS MODE*^^*~~                                   ")
    Valueh= True
    while Valueh:
        print()
        print()
        print("                                                    ~~*^^*OPTIONS*^^*~~                                                 ")
        print("########################################################################################################################")
        print("#                                                                                                                      #")
        print("#                                                                                                                      #")
        print("#                                                    1.    DOCTORS                                                     #")
        print("#                                                    2.    STAFFS                                                      #")
        print("#                                                                                                                      #")
        print("#                                                                                                                      #")
        print("########################################################################################################################")
        ch=int(input("Enter your Choice    :"))
        if (ch==1):
                Valuel=True
                while Valuel:
                    print("########################################################################################################################")
                    print("#                                                                                                                      #")
                    print("#                                                                                                                      #")
                    print("#                                         1.    VIEW DOCTORS LIST                                                      #")
                    print("#                                         2.    UPDATE YOUR DETAILS                                                    #")
                    print("#                                                                                                                      #")
                    print("#                                                                                                                      #")
                    print("########################################################################################################################")
                    ch=int(input("Enter your Choice    :"))
                    if (ch==1):
                        print("________________________________________________________________________________________________________________________")
                        print("                                       ~~*^^*DISPLAYING LIST OF ALL DOCTORS*^^*~~                                       ")
                        print()
                        print()
                        cursor.execute("select * from doctors_info_database")
                        l=cursor.fetchall()
                        for i in range(0,len(l)):
                            a=i+1
                            print("_________________________________________________RECORD NO.",a,"_________________________________________________")
                            print("Doctor's Name :",l[i][0])
                            print("Doctor's Address  :", l[i][1])
                            print("Doctor's Gender:",l[i][2])
                            print("Doctor's Age:",l[i][3])
                            print("Doctor's Joining day:",l[i][4])
                            print("Doctor's Years of Experience:",l[i][5])
                            print("Doctor's field of Specialisation:",l[i][6])
                            print("Is he/she on Covid Duty:",l[i][7])
                            print("________________________________________________________________________________________________________________________")
                            i=i+1
                    elif(ch==2):
                        Value=True
                        data="doctors_info_database"
                        while Value:
                                nam=input("Enter the name of the Doctor    :")
                                if (Check(data,nam)==1):
                                    cursor.execute("select * from doctors_info_database where Name ='{}'".format(nam))
                                    m2=cursor.fetchall()
                                    for i in range (0,len(m2)):
                                        if m2[0][0]==nam:
                                            print("________________________________________________________________________________________________________________________")
                                            print("                                       ~~*^^*UPDATATION OF INFORMATION*^^*~~                                       ")
                                            Doctors_name=input("Enter the name of the Doctor  :")
                                            Doctors_address=input("Enter the address where he/she lives :")
                                            Gender=input("Enter the gender  :")
                                            Age=int(input("Enter the doctor's age  :"))
                                            Joining=input("Enter the date of joining[yyyy-mm-dd]  :")
                                            Experience=int(input("Enter the years of Experience  :"))
                                            Specialisation=input("Enter the field of Specialisation  :")
                                            cursor.execute("update doctors_info_database set Name='{}', address='{}', Gender='{}', Age={}, Joined='{}',Experience={}, Specialisation='{}' where Name='{}' ".format(Doctors_name, Doctors_address, Gender, Age, Joining, Experience, Specialisation,nam))
                                            mycon.commit()
                                            print("DATA UPDATED SUCCESSFULLY!")
                                            print("________________________________________________________________________________________________________________________")
                                            ch=input("Update more data?[y/n]")
                                            if (ch=="n"):
                                                    print("________________________________________________________________________________________________________________________")
                                                    Value=False
                                else:
                                        ch=input("NO DOCTOR WITH SUCH NAME IS PRESENT! TRY AGAIN?[TYPE 'n' FOR NO]")
                                        if (ch=="n"):
                                                print("________________________________________________________________________________________________________________________")
                                                Value=False
                    else:
                        print("WRONG CHOICE!")
                        print("________________________________________________________________________________________________________________________")
                    ch=input("GO TO THE PREVIOUS OPTIONS ?[ TYPE 'n' FOR NO]")
                    if (ch=="n"):
                            print("________________________________________________________________________________________________________________________")
                            Valuel=False
                        
        elif(ch==2):
                Valueo=True
                while Valueo:
                    print("########################################################################################################################")
                    print("#                                                                                                                      #")
                    print("#                                                                                                                      #")
                    print("#                                         1.    VIEW STAFFS LIST                                                       #")
                    print("#                                         2.    UPDATE YOUR DETAILS                                                    #")
                    print("#                                                                                                                      #")
                    print("#                                                                                                                      #")
                    print("########################################################################################################################")
                    ch=int(input("Enter the Choice    :"))
                    if (ch==1):
                        cursor.execute("select * from staffs_info_database")
                        l=cursor.fetchall()
                        for i in range(0,len(l)):
                                a=i+1
                                print("_________________________________________________RECORD NO.",a,"_________________________________________________")
                                print("Staff's Name :",l[i][0])
                                print("Staff's Address  :", l[i][1])
                                print("Staff's Gender:",l[i][2])
                                print("Staff's Age:",l[i][3])
                                print("Staff's Joining day:",l[i][4])
                                print("Staff's Years of Experience:",l[i][5])
                                print("Is he/she on Covid Duty:",l[i][6])
                                print("________________________________________________________________________________________________________________________")
                    elif (ch==2):
                        data="staffs_info_database"
                        Value=True
                        V=0
                        while Value:
                                nam=input("Enter the name of the Staff    :")
                                if (Check(data,nam)==1):
                                    cursor.execute("select * from staffs_info_database where Name ='{}'".format(nam))
                                    m2=cursor.fetchall()
                                    for i in range (0,len(m2)):
                                        if m2[0][0]==nam:
                                            print("________________________________________________________________________________________________________________________")
                                            print("                                       ~~*^^*UPDATATION OF INFORMATION*^^*~~                                       ")
                                            Staffs_name=input("Enter the name of the Staff  :")
                                            Staffs_address=input("Enter the address where he/she lives :")
                                            Gender=input("Enter the gender  :")
                                            Age=int(input("Enter the staff's age  :"))
                                            Joining=input("Enter the date of joining[yyyy-mm-dd]  :")
                                            Experience=int(input("Enter the years of Experience  :"))
                                            cursor.execute("update staffs_info_database set Name='{}', address='{}', Gender='{}', Age={}, Joined='{}',Experience={} where Name='{}'".format(Staffs_name, Staffs_address, Gender, Age, Joining, Experience, nam))
                                            mycon.commit()
                                            print("DATA UPDATED SUCCESSFULLY!")
                                            print("________________________________________________________________________________________________________________________")
                                            ch=input("Update more data?[y/n]")
                                            if (ch=="n"):
                                                print("________________________________________________________________________________________________________________________")
                                                Value=False
                                else:
                                        ch=input("NO STAFF MEMBER WITH SUCH NAME IS PRESENT! TRY AGAIN?[TYPE 'n' FOR NO]")
                                        if (ch=="n"):
                                            print("________________________________________________________________________________________________________________________")
                                            Value=False
                    else:
                        print("WRONG CHOICE!")
                        print("________________________________________________________________________________________________________________________")
                    ch=input("GO TO THE PREVIOUS OPTIONS ?[ TYPE 'n' FOR NO]")
                    if (ch=="n"):
                        print("________________________________________________________________________________________________________________________")
                        Valueo=False
        else:
            print("WRONG CHOICE!!")
        ch=input("CHANGE DOCTORS/STAFFS OPTION? [ TYPE 'n' FOR NO]")
        if (ch=="n"):
            print("________________________________________________________________________________________________________________________")
            Valueh=False
                        
                    

                    
            
def Patients_mode():
    print("                                       ~~*^^*WELCOME TO THE PATIENTS MODE*^^*~~                                        ")
    Value1=True
    while Value1:
        print()
        print()
        print("                                                    ~~*^^*OPTIONS*^^*~~                                                 ")
        print("########################################################################################################################")
        print("#                                                                                                                      #")
        print("#                                                                                                                      #")
        print("#                                         1.    VIEW YOUR DETAILS                                                      #")
        print("#                                         2.    UPDATE YOUR DETAILS                                                    #")
        print("#                                                                                                                      #")
        print("#                                                                                                                      #")
        print("########################################################################################################################")
        ch=int(input("Enter your Choice    :"))
        if (ch==1):
            print("________________________________________________________________________________________________________________________")
            print("                                       ~~*^^*SEARCHING FOR YOUR DETAILS*^^*~~                                       ")
            print()
            print()
            Value=True
            V=0
            data="patients_database"
            while Value:
                    name=input("Enter the name of the Patient    :")
                    if (Check(data,name)==1):
                            cursor.execute("select * from patients_database where Name='{}'".format(name))
                            m1=cursor.fetchall()
                            for i in range(0,len(m1)):
                                    if (m1[i][0]==name):
                                            print("Name of the patient :",m1[0][0])
                                            print("Address where he/she lives :",m1[0][1])
                                            print("Age of the patient:",m1[0][2])
                                            print("Patient's Gender :",m1[0][3])
                                            print("Is he/she  a covid patient ",m1[0][4])
                                            ch=input("SEARCH MORE PATIENTS ?[TYPE 'n' FOR NO]")
                                            if (ch=="n"):
                                                    Value=False
                    else:
                            ch=input("NO PATIENT WITH SUCH NAME IS PRESENT! TRY AGAIN?[TYPE 'n' FOR NO]")
                            if (ch=="n"):
                                    print("________________________________________________________________________________________________________________________")
                                    Value=False
        elif (ch==2):
            Value=True
            database="patients_database"
            while Value:
                    nam=input("Enter the name of the Patient    :")
                    if (Check(database,nam)==1):
                            cursor.execute("select * from patients_database where Name ='{}'".format(nam))
                            m2=cursor.fetchall()
                            for i in range (0,len(m2)):
                                    if m2[0][0]==nam:
                                            print("________________________________________________________________________________________________________________________")
                                            print("                                       ~~*^^*UPDATATION OF INFORMATION*^^*~~                                       ")
                                            Patients_name=input("Enter the name of the Patient :")
                                            Address=input("Enter the address where he/she lives :")
                                            Age=int(input("Enter the patient's age  :"))
                                            Gender=input("Enter the gender  :")
                                            Covid_patient=input(" Is he/she covid patient?[y/n]")
                                            cursor.execute("update patients_database set Name='{}', Address='{}', Age={}, Gender='{}', Covid='{}' where Name='{}'".format(Patients_name, Address, Age, Gender, Covid_patient, nam))
                                            mycon.commit()
                                            print("DATA UPDATED SUCCESSFULLY!")
                                            print("________________________________________________________________________________________________________________________")
                                            ch=input("Update more data?[y/n]")
                                            if (ch=="n"):
                                                    print("________________________________________________________________________________________________________________________")
                                                    Value=False
                    else:
                            ch=input("NO PATIENT WITH SUCH NAME IS PRESENT! TRY AGAIN?[TYPE 'n' FOR NO]")
                            if (ch=="n"):
                                print("________________________________________________________________________________________________________________________")
                                Value=False
            
        else:
            print("WRONG CHOICE!")
        ch=input("GO TO THE PREVIOUS OPTIONS ?[ TYPE 'n' FOR NO]")
        if (ch=="n"):
            print("________________________________________________________________________________________________________________________")
            Value1=False
        

def Covid_emergency():
    print("                             ~~*^^*WELCOME TO THE COVID EMERGENGY HEALTH CARE MODE*^^*~~                                ")
    print()
    print()
    Value=True
    while Value:
        print("                                                    ~~*^^*OPTIONS*^^*~~                                                 ")
        print("########################################################################################################################")
        print("#                                                                                                                      #")
        print("#                                                                                                                      #")
        print("#                                         1.    DISPLAY ALL COVID PAITIENTS(WHOLE HISTORY)                             #")
        print("#                                         2.    DISPLAY DOCTORS UNDER COVID DUTY                                       #")
        print("#                                         3.    DISPLAY STAFFS UNDER COVID DUTY                                        #")
        print("#                                                                                                                      #")
        print("#                                                                                                                      #")
        print("########################################################################################################################")
        ch=int(input("Enter a choice    :"))
        if(ch==1):
                cursor.execute("select * from patients_database where Covid='{}'".format('y'))
                m1=cursor.fetchall()
                for i in range(0,len(m1)):
                        a=i+1
                        print("_________________________________________________RECORD NO.",a,"_________________________________________________")
                        print("Name of the patient :",m1[i][0])
                        print("Address where he/she lives :",m1[i][1])
                        print("Age of the patient:",m1[i][2])
                        print("Patient's Gender :",m1[i][3])
                        print("Is he/she  a covid patient ",m1[i][4])
                        print("________________________________________________________________________________________________________________________")
        elif(ch==2):
                cursor.execute("select * from doctors_info_database where Availability='{}'".format('y'))
                m1=cursor.fetchall()
                for i in range(0,len(m1)):
                        a=i+1
                        print("_________________________________________________RECORD NO.",a,"_________________________________________________")
                        print("Doctor's Name    :",m1[i][0])
                        print("Doctor's Address    :",m1[i][1])
                        print("Doctor's Gender    :",m1[i][2])
                        print("Doctor's Age   :",m1[i][3])
                        print("Doctor's Joining day    :",m1[i][4])
                        print("Doctor's Years of Experience   :",m1[i][5])
                        print("Doctor's field of Specialisation    :",m1[i][6])
                        print("Is he/she on Covid Duty   :",m1[i][7])
                        print("________________________________________________________________________________________________________________________")
        elif(ch==3):
            cursor.execute("select * from staffs_info_database where Availability='{}'".format('y'))
            m1=cursor.fetchall()
            for i in range(0,len(m1)):
                    a=i+1
                    print("_________________________________________________RECORD NO.",a,"_________________________________________________")
                    print("Staffs's Name    :",m1[i][0])
                    print("Staffs's Address    :",m1[i][1])
                    print("Staffs's Gender    :",m1[i][2])
                    print("Staffs's Age   :",m1[i][3])
                    print("Staffs's Joining day    :",m1[i][4])
                    print("Staff's Years of Experience   :",m1[i][5])
                    print("Is he/she on Covid Duty   :",m1[i][6])
                    print("________________________________________________________________________________________________________________________")
        else:
            print("WRONG CHOICE!TRY AGAIN!")
        ch=input("GO TO THE PREVIOUS OPTIONS ?[ TYPE 'n' FOR NO]")
        if (ch=="n"):
            print("________________________________________________________________________________________________________________________")
            Value=False 
        
    
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()
print()
print()
print()
print("                                       ~~*^^*WELCOME TO THE CENTRAL HOSPITAL*^^*~~                                      ")
print()
print()
print()
print()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
C=True
while C:
    print()
    print()
    print("                                                    ~~*^^*MODES*^^*~~                                                   ")
    print("________________________________________________________________________________________________________________________")
    print()
    print("|                                             1.   MANAGEMENT MODE                                                     |")
    print("|                                             2.   DOCTORS & STAFFS MODE                                               |")
    print("|                                             3.   PATIENTS MODE                                                       |")
    print("|                                             4.   COVID EMERGENCY HEALTH CARE MODE                                    |")
    print("|                                             5.   ADD NEW LOGIN ID                                                    |")
    print("________________________________________________________________________________________________________________________")
    mode=int(input("Enter which mode you want to use    :"))
    if (mode==1):
        Value=True
        V=0
        while Value:
            User_id=input("Enter your User name please:   ")
            Password=int(input("Enter you password please[ALL CHARACTERS SHOULD BE INTEGERS]:   "))
            r=Login(User_id,Password)
            if (r==0):
                print("UNABLE TO LOG IN! WRONG PASSWORD OR USER NAME!")
                User_choice=input("Try again?(y/n):")
                if User_choice=="n":
                    Value=False
            else:
                print("SUCCESSFULLY LOGGED IN!")
                Value=False
                Management_mode()
    elif(mode==2):
        Value=True
        V=0
        while Value:
            User_id=input("Enter your User name please:   ")
            Password=int(input("Enter you password please[ALL CHARACTERS SHOULD BE INTEGERS]:   "))
            r=Login(User_id,Password)
            if (r==0):
                print("UNABLE TO LOG IN! WRONG PASSWORD OR USER NAME!")
                User_choice=input("Try again?(y/n):")
                if User_choice=="n":
                    Value=False
            else:
                print("SUCCESSFULLY LOGGED IN!")
                Value=False
                Doctors_Staffs_mode()
    elif (mode==3):
        Patients_mode()
    elif (mode==4):
        Value=True
        while Value:
            User_id=input("Enter your User name please:   ")
            Password=int(input("Enter you password please[ALL CHARACTERS SHOULD BE INTEGERS]:   "))
            r=Login(User_id,Password)
            if (r==0):
                print("UNABLE TO LOG IN! WRONG PASSWORD OR USER NAME!")
                User_choice=input("Try again?(y/n):")
                if User_choice=="n":
                    Value=False
            else:
                print("SUCCESSFULLY LOGGED IN!")
                Value=False
                Covid_emergency()
    elif(mode==5):
        def Checking(user):
            v=1
            cursor.execute("select * from user_password_database")
            m=cursor.fetchall()
            for i in range(0,len(m)):
                    if user == m[i][0]:
                            v=0
                            return v
        def write_database(User,Password):
                cursor.execute("insert into user_password_database values('{}','{}')".format(User,Password))
                mycon.commit()
        Value=True        
        while Value:
            User=input("Enter the User name :")
            if (Checking(User)!=1):
                Password=random.randrange(100000,1000000000)
                print(User,"YOUR PASSWORD IS : ",Password)
                write_database(User,Password)
                ch=input("Enter more Data ? (y/n) :")
                if ch=="n":
                    print("________________________________________________________________________________________________________________________")
                    Value=False
            else:
                print("User Name all ready present!!")
                ch=input("TRY AGAIN !![TYPE 'n' FOR NO]")
                if (ch=='n'):
                    print("________________________________________________________________________________________________________________________")
                    Value=False 
    else:
        print("WRONG CHOICE ENTERED!")
    ch=input("RETURN TO THE MODES WINDOWS?[TYPE 'n' FOR NO]")
    if (ch=='n'):
        print("________________________________________________________________________________________________________________________")
        C=False
