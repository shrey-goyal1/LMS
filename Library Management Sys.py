#Welcome Message
print("                                                     YOU CAN EXIT FROM THE PROGRAM ANYTIME BY ENTERING: exit")
print("")

#Importing Modules
import pandas as pd
import mysql.connector as sq
import pymysql
from sqlalchemy import create_engine
import sys
import datetime

#Possibilities
p1=['1','2','3','l','r','u','Login','login','LOGIN','update','Update','UPDATE','register','Register','REGISTER']
p2=['1','2','3','4','5','issue','return','delete','details','logout','Issue','Return','Delete','Details','Logout','ISSUE','RETURN','DELETE','DETAILS','LOGOUT']
p3=['y','n','yes','no','Y','N','YES','NO']
P_yes=['y','yes','YES','Y']
P_no=['n','no','NO','N']
P_login=['1','l','login','L','Login','LOGIN']
P_register=['2','r','register','R','Register','REGISTER']
P_update=['3','u','update','Update','UPDATE','U']
p_update_ask=['n','N','name','Name','NAME','DOB','dob','Dob','d','D','password','Password','pass','p','Pass','PASS','PASSWORD','Pass','P']
P_issue=['1','i','issue','I','ISSUE','Issue']
P_return=['2','r','return','R','RETURN','Return']
P_delete=['3','del','delete','Del','DELETE']
P_details=['4','d','details','Detals','DETAILS','D']
P_logout=['5','l','L','Logout','LOGOUT','logout']
P_exit=['exit','EXIT','Exit']

#Defining the default values
ID=['S1212','H2303','J1608']
NAME=['Sahil Mehta','Harsh Sharma','Jagdish Singh']
DOB=['12/12/2004','23/03/2003','16/08/2006']
PASS=['sahil121','harsh230','jagdish1']
d1={'User_ID':ID,'User_Name':NAME,'Date_Of_Birth':DOB,'Password':PASS}
df1=pd.DataFrame(d1)
length=len(df1)
ind=[0,1,2]
User_ID=[]

#User details of ID='S1212'
bc=['H103','N105','F101']
bn=['The Bloody Chamber','Ulysses','A Visit From The Goon Squad']
isd=['21/03/2020','14/07/2020','05/10/2020']
rtd=['03/06/2020','28/09/2020','Pending']
dic1={'Book_Code':bc,'Book_Name':bn,'Issued_date':isd,'Returned_Date':rtd}
us=pd.DataFrame(dic1)

#User details of ID='H2303'
bc1=['C105','R103','H101']
bn1=['From Hell','Love','The Bad Seed']
isd1=['17/02/2020','19/04/2020','23/08/2020']
rtd1=['24/03/2020','01/06/2020','15/09/2020']
dic2={'Book_Code':bc1,'Book_Name':bn1,'Issued_date':isd1,'Returned_Date':rtd1}
us1=pd.DataFrame(dic2)

#User details of ID='J1608'
bc2=['N103','R106']
bn2=['Madame Bovary','An Affair Downstairs']
isd2=['24/09/2020','26/10/2020']
rtd2=['17/10/2020','Pending']
dic3={'Book_Code':bc2,'Book_Name':bn2,'Issued_date':isd2,'Returned_Date':rtd2}
us2=pd.DataFrame(dic3)

#User details for current user
bc3=[]
bn3=[]
isd3=[]
rtd3=[]
dic4={'Book_Code':bc3,'Book_Name':bn3,'Issued_date':isd3,'Returned_Date':rtd3}
us3=pd.DataFrame(dic4)

#Exporting DataFrame to Mysql
en=create_engine('mysql+pymysql://root:radheradhe@localhost/project')   #Creating Engine
myco=en.connect()   #Connecting Engine
df1.to_sql('users',myco,if_exists='replace')
us.to_sql('sahil121',myco,if_exists='replace')
us1.to_sql('harsh230',myco,if_exists='replace')
us2.to_sql('jagdish1',myco,if_exists='replace')

#From mysql to DataFrame
mycon1=sq.connect(host="localhost",user="root",passwd="radheradhe",database="project")  #Connecting to mysql
df1=pd.read_sql("select * from users;",mycon1)

#Asking
def ask1():
    print("                     1. Already have an account? [LOGIN] or type l/L")
    print("                     2. Create new account! [REGISTER] or type r/R")
    print("                     3. Update your account. [UPDATE] or type u/U")
    print("")

def ask2():
    print("                     1. Issue a new book")
    print("                     2. Return a book")
    print("                     3. Delete your account")
    print("                     4. Details of your account")
    print("                     5. Logout")
    print("")

#Exiting from the program
def exit():
    print("                                                                    Thank You for giving your support")
    print("                                                                             Have a nice day")
    print("                                                                            JAI SWAMINARAYAN")
    print("")
    sys.exit()

#REGISTER
def register():
    print("Enter your details...")
    print("")
    us_name=input("        Enter your username:")
    if us_name in P_exit:
        exit()
    while us_name.isdigit()==True:
        print("")
        print("Please enter a valid name...")
        print("")
        us_name=input("        Enter your username")
        if us_name in P_exit:
            exit()
    NAME.append(us_name)
    print("")
    us_birth=input("        Enter your birth date(dd/mm/yyyy):")
    print("")
    if us_birth in P_exit:
        exit()
    while len(us_birth)!=10 or us_birth[0:2].isdigit()!=True or us_birth[2]!="/" or us_birth[3:5].isdigit()!=True or us_birth[5]!="/" or us_birth[6:10].isdigit()!=True:
        print("Please enter a valid date of birth...")
        print("")
        us_birth=input("        Enter your birth date(dd/mm/yyyy):")
        print("")
        if us_birth in P_exit:
            exit()
    DOB.append(us_birth)
    us_id=us_name[0]+us_birth[0:2]+us_birth[3:5]    #Creating the USER_ID
    User_ID.append(us_id)
    print("Your User ID is:",us_id)
    print("")
    ID.append(us_id)
    us_pass=input("        Create a password of alteast 8 character including alphabets initially:")
    print("")
    if us_pass in P_exit:
        exit()
    while len(us_pass)<8:
        print("Password length is less than the limit specified...Re-enter it")
        print("")
        us_pass=input("        Create a password of atleast 8 character including alphabets initially:")
        print("")
        if us_pass in P_exit:
            exit()
    us_pass2=input( "        Confirm your password:")
    print("")
    if us_pass2 in P_exit:
        exit()
    while us_pass!=us_pass2:    #Confirmation of Password
        print("Password not confirmed!")
        print("")
        us_pass=input("        Please re-enter your password")
        print("")
        if us_pass in P_exit:
            exit()
        us_pass2=input("        Confirm your password:")
        print("")
        if us_pass2 in P_exit:
            exit()
    PASS.append(us_pass)
    print("You are registered.")    #Registration Done
    print("")
    global d1
    global df1
    df1=pd.DataFrame(d1)
    lng=len(df1)
    ind.append(lng-1)
    mycon1=sq.connect(host="localhost",user="root",passwd="radheradhe",database="project")
    en=create_engine('mysql+pymysql://root:radheradhe@localhost/project')   #Creating Engine
    myco=en.connect()  #Connecting to Engine
    sql=str('DROP TABLE users;')
    result=en.execute(sql)
    df1.to_sql('users',myco,if_exists='replace')    #Exporting DataFrame to mysql
    us3.to_sql(PASS[-1],myco,if_exists='replace')

#LOGIN
def login():
    print("Login with id and password...")
    print("")
    global d1
    global df1    
    mycon1=sq.connect(host="localhost",user="root",passwd="radheradhe",database="project")  #Connecting to mysql
    df1=pd.read_sql("select * from users;",mycon1)    
    usid=input("        Enter your User ID:")
    print("")
    if usid in P_exit:
        exit()
    while usid not in ID:
        print("User ID not found!")
        print("")
        print("Enter a valid user ID")
        print("")
        usid=input("        Enter user id:")
        print("")
        if usid in P_exit:
            exit()
    User_ID.append(usid)
    for j in range(len(df1)):
        if df1.at[j,'User_ID']==usid:
            pswd=input("        Enter password:")
            print("")
            if pswd in P_exit:
                exit()
            while df1.at[j,'Password']!=pswd:
                print("Your password is incorrect!")
                print("")
                print("Please enter the correct password...")
                print("")
                pswd=input("        Enter the password:")
                print("")
                if pswd in P_exit:
                    exit()
            if df1.at[j,'Password']==pswd:
                print("The password is correct")
                print("")
                print("You are logged in!")
                print("")

#UPDATE
def update():
    print("Update your data..")
    print("")
    global d1
    global df1    
    mycon1=sq.connect(host="localhost",user="root",passwd="radheradhe",database="project")  #Connecting to mysql
    df1=pd.read_sql("select * from users;",mycon1)    
    usid=input("        Enter your User ID:")
    print("")
    if usid in P_exit:
        exit()
    while usid not in ID:
        print("User ID not found!")
        print("")
        print("Enter a valid user ID")
        print("")
        usid=input("        Enter user id:")
        print("")
        if usid in P_exit:
            exit()
    for j in range(len(df1)):
        if df1.at[j,'User_ID']==usid:
            pswd=input("        Enter password:")
            print("")
            if pswd in P_exit:
                exit()
            while df1.at[j,'Password']!=pswd:
                print("Your password is incorrect!")
                print("")
                print("Please enter the correct password...")
                print("")
                pswd=input("        Enter the password:")
                print("")
                if pswd in P_exit:
                    exit()
            if df1.at[j,'Password']==pswd:
                print("The password is correct")
                print("")

            #Starting the Update    
            asking=input("        What do you want to update? (name,dob,password) or type(n,d,p)")
            print("")
            while asking not in p_update_ask:
                print('Invalid Input!')
                asking=input("        What do you want to update? (name,dob,password) or type(n,d,p)")
                if asking in P_exit:
                    exit()
            if asking in P_exit:
                exit()
            if asking=='name' or asking=='Name' or asking=='NAME' or asking=='n':
                name=input("        Enter the new name:")
                print("")
                if name in P_exit:
                    exit()
                while name.isdigit()==True:
                    print("Please enter a valid name...")
                    print("")
                    name=input("        Enter your username")
                    print("")
                    if name in P_exit:
                        exit()
                df1.User_Name[j]=name
                b=df1.at[j,'Date_Of_Birth']
                new_id1=df1.User_ID[j]=name[0]+b[0:2]+b[3:5]
                NAME[j]=name
                ID[j]=new_id1
                print("Your new ID is:",new_id1)
                print("")

                #Printing the updated data
                print(df1.loc[j,'User_ID':'Date_Of_Birth'])
                print("")
                en=create_engine('mysql+pymysql://root:radheradhe@localhost/project')   #Creating Engine
                myco=en.connect()  #Connecting to Engine
                sql=str('DROP TABLE users;')
                #result=en.execute(sql)
                df1.to_sql('users2',myco,if_exists='replace')   #Exporting DataFrame to mysql
            
            elif asking=='dob' or asking=='Dob' or asking=='DOB' or asking=='d':
                date=input("        Enter the new date of birth(dd/mm/yyy):")
                print("")
                if date in P_exit:
                    exit()
                while len(date)!=10 or date[0:2].isdigit()!=True or date[2]!="/" or date[3:5].isdigit()!=True or date[5]!="/" or date[6:10].isdigit()!=True:
                    print("Please enter a valid date of birth...")
                    print("")
                    date=input("        Enter your birth date(dd/mm/yyy):")
                    print("")
                    if date in P_exit:
                        exit()
                df1.Date_Of_Birth[j]=date
                n=df1.at[j,'User_Name']
                new_id2=df1.User_ID[j]=n[0]+date[0:2]+date[3:5]
                DOB[j]=date
                ID[j]=new_id2
                print("Your new ID is:",new_id2)
                print("")

                #Printing the updated data
                print(df1.loc[j,'User_ID':'Date_Of_Birth'])
                print("")
                en=create_engine('mysql+pymysql://root:radheradhe@localhost/project')   #Creating Engine
                myco=en.connect()  #Connecting to Engine
                sql=str('DROP TABLE users;')
                #result=en.execute(sql)                
                df1.to_sql('users2',myco,if_exists='replace')   #Exporting DataFrame to mysql                
                
            elif asking=='password' or asking=='Password' or asking=='PASSWORD' or asking=='p':
                pwd=input("        Enter the new Password:")
                print("")
                if pwd in P_exit:
                    exit()
                while len(pwd)<8:
                    print("Password length is less than the limit specified...Re-enter it")
                    print("")
                    pwd=input("        Create a password of atleast 8 character:")
                    print("")
                    if pwd in P_exit:
                        exit()
                df1.Password[j]=pwd
                PASS[j]=pwd

                #Printing the updated data
                print(df1.loc[j,'User_ID':'Date_Of_Birth'])
                print("")
                en=create_engine('mysql+pymysql://root:radheradhe@localhost/project')   #Creating Engine
                myco=en.connect()  #Connecting to Engine
                sql=str('DROP TABLE users;')
                #result=en.execute(sql)                
                df1.to_sql('users2',myco,if_exists='replace')   #Exporting DataFrame to mysql
                
#ISSUE
def issue():        
    print("Which genre's book you wanna issue? (only type the number..)")
    print("")
    global d1
    global df1    
    mycon2=sq.connect(host="localhost",user="root",passwd="radheradhe",database="project")  #Connecting to mysql
    if mycon2.is_connected():
        df3=pd.read_sql("select DISTINCT(Genre) as GENRE from books;",mycon2)   #Importing table from mysql to DataFrame
        print(df3)
        print("")
    as1=input("        Enter the number of Genre:")
    print("")
    if as1 in P_exit:
        exit()
    while as1!='0' and as1!='1' and as1!='2' and as1!='3' and as1!='4':
        print("Invalid Input!")
        print("")
        as1=input("        Enter the number of Genre:")     #Asking the Genre
        print("")
        if as1 in P_exit:
            exit()
        
    if as1=='0':
        print("So you have selected Comic...")
        print("")
        mycon3=sq.connect(host="localhost",user="root",passwd="radheradhe",database="project")  #Connecting to mysql
        if mycon3.is_connected():
            df4=pd.read_sql("select Book_Code,Book_Name,Author,Published from books where Genre='Comic';",mycon3)   #Importing table of Comic
            print("Choose your book...")
            print("")
            print(df4)
            print("")
            bcd=input("        Enter the book code:")   #Asking the book code
            print("")
            if bcd in P_exit:
                exit()
            while bcd not in list(df4.Book_Code):
                print("Invalid Book Code!")
                bcd=input("        Enter the book code:")   #Asking the book code
                if bcd in P_exit:
                    exit()
            for k in range(len(df4)):
                if df4.Book_Code[k]==bcd:
                    code=bcd
                    name=df4.Book_Name[k]
                    issue_date=str(datetime.date.today())
                    return_date='Pending'

                    if User_ID[-1]==ID[0]:
                        bc.append(code)
                        bn.append(name)
                        isd.append(issue_date)
                        rtd.append(return_date)
                        us=pd.DataFrame(dic1)
                        #us.to_sql(PASS[0],myco,if_exists='replace')

                    elif User_ID[-1]==ID[1]:
                        bc1.append(code)
                        bn1.append(name)
                        isd1.append(issue_date)
                        rtd1.append(return_date)
                        us1=pd.DataFrame(dic2)
                        #us1.to_sql(PASS[1],myco,if_exists='replace')

                    elif User_ID[-1]==ID[2]:
                        bc2.append(code)
                        bn2.append(name)
                        isd2.append(issue_date)
                        rtd2.append(return_date)
                        us2=pd.DataFrame(dic3)
                        #us2.to_sql(PASS[2],myco,if_exists='replace')

                    else:
                        bc3.append(code)
                        bn3.append(name)
                        isd3.append(issue_date)
                        rtd3.append(return_date)
                        us3=pd.DataFrame(dic4)
                        #us3.to_sql(PASS[3],myco,if_exists='replace')
                                
    elif as1=='1':
        print("So you have selected Novel...")
        print("")
        mycon4=sq.connect(host="localhost",user="root",passwd="radheradhe",database="project")      #Connecting to mysql
        if mycon4.is_connected():
            df5=pd.read_sql("select Book_Code,Book_Name,Author,Published from books where Genre='Novel';",mycon4)   #Importing table of Novel
            print("Choose your book...")
            print("")
            print(df5)
            print("")
            bcd=input("        Enter the book code:")   #Asking the book code
            print("")
            if bcd in P_exit:
                exit()
            while bcd not in list(df5.Book_Code):
                print("Invalid Book Code!")
                bcd=input("        Enter the book code:")   #Asking the book code
                if bcd in P_exit:
                    exit()                
            for k in range(len(df5)):
                if df5.Book_Code[k]==bcd:
                    code=bcd
                    name=df5.Book_Name[k]
                    issue_date=str(datetime.date.today())
                    return_date='Pending'
                    if User_ID[-1]==ID[0]:
                        bc.append(code)
                        bn.append(name)
                        isd.append(issue_date)
                        rtd.append(return_date)
                        us=pd.DataFrame(dic1)
                        us.to_sql(PASS[0],myco,if_exists='replace')
                    elif User_ID[-1]==ID[1]:
                        bc1.append(code)
                        bn1.append(name)
                        isd1.append(issue_date)
                        rtd1.append(return_date)
                        us1=pd.DataFrame(dic2)
                        us1.to_sql(PASS[1],myco,if_exists='replace')
                    elif User_ID[-1]==ID[2]:
                        bc2.append(code)
                        bn2.append(name)
                        isd2.append(issue_date)
                        rtd2.append(return_date)
                        us2=pd.DataFrame(dic3)
                        us2.to_sql(PASS[2],myco,if_exists='replace')
                    else:
                        bc3.append(code)
                        bn3.append(name)
                        isd3.append(issue_date)
                        rtd3.append(return_date)
                        us3=pd.DataFrame(dic4)
                        us3.to_sql(PASS[3],myco,if_exists='replace')
            
    elif as1=='2':
        print("So you have selected Fiction...")
        print("")
        mycon5=sq.connect(host="localhost",user="root",passwd="radheradhe",database="project")      #Connecting to mysql
        if mycon5.is_connected():
            df6=pd.read_sql("select Book_Code,Book_Name,Author,Published from books where Genre='Fiction';",mycon5)     #Imporing table of Fiction
            print("Choose your book...")
            print("")
            print(df6)
            print("")
            bcd=input("        Enter the book code:")   #Asking the book code
            print("")
            if bcd in P_exit:
                exit()
            while bcd not in list(df6.Book_Code):
                print("Invalid Book Code!")
                bcd=input("        Enter the book code:")   #Asking the book code
                if bcd in P_exit:
                    exit()                            
            for k in range(len(df6)):
                if df6.Book_Code[k]==bcd:
                    code=bcd
                    name=df6.Book_Name[k]
                    issue_date=str(datetime.date.today())
                    return_date='Pending'
                    if User_ID[-1]==ID[0]:
                        bc.append(code)
                        bn.append(name)
                        isd.append(issue_date)
                        rtd.append(return_date)
                        us=pd.DataFrame(dic1)
                        us.to_sql(PASS[0],myco,if_exists='replace')
                    elif User_ID[-1]==ID[1]:
                        bc1.append(code)
                        bn1.append(name)
                        isd1.append(issue_date)
                        rtd1.append(return_date)
                        us1=pd.DataFrame(dic2)
                        us1.to_sql(PASS[1],myco,if_exists='replace')
                    elif User_ID[-1]==ID[2]:
                        bc2.append(code)
                        bn2.append(name)
                        isd2.append(issue_date)
                        rtd2.append(return_date)
                        us2=pd.DataFrame(dic3)
                        us2.to_sql(PASS[2],myco,if_exists='replace')
                    else:
                        bc3.append(code)
                        bn3.append(name)
                        isd3.append(issue_date)
                        rtd3.append(return_date)
                        us3=pd.DataFrame(dic4)
                        us3.to_sql(PASS[3],myco,if_exists='replace')
            
    elif as1=='3':
        print("So you have selected Romance...")
        print("")
        mycon6=sq.connect(host="localhost",user="root",passwd="radheradhe",database="project")      #Connecting to mysql
        if mycon6.is_connected():
            df7=pd.read_sql("select Book_Code,Book_Name,Author,Published from books where Genre='Romance';",mycon6)     #Importing table of Romance
            print("Choose your book...")
            print("")
            print(df7)
            print("")
            bcd=input("        Enter the book code:")   #Asking the book code
            print("")
            if bcd in P_exit:
                exit()
            while bcd not in list(df7.Book_Code):
                print("Invalid Book Code!")
                bcd=input("        Enter the book code:")   #Asking the book code
                if bcd in P_exit:
                    exit()                                
            for k in range(len(df7)):
                if df7.Book_Code[k]==bcd:
                    code=bcd
                    name=df7.Book_Name[k]
                    issue_date=str(datetime.date.today())
                    return_date='Pending'
                    if User_ID[-1]==ID[0]:
                        bc.append(code)
                        bn.append(name)
                        isd.append(issue_date)
                        rtd.append(return_date)
                        us=pd.DataFrame(dic1)
                        us.to_sql(PASS[0],myco,if_exists='replace')
                    elif User_ID[-1]==ID[1]:
                        bc1.append(code)
                        bn1.append(name)
                        isd1.append(issue_date)
                        rtd1.append(return_date)
                        us1=pd.DataFrame(dic2)
                        us1.to_sql(PASS[1],myco,if_exists='replace')
                    elif User_ID[-1]==ID[2]:
                        bc2.append(code)
                        bn2.append(name)
                        isd2.append(issue_date)
                        rtd2.append(return_date)
                        us2=pd.DataFrame(dic3)
                        us2.to_sql(PASS[2],myco,if_exists='replace')
                    else:
                        bc3.append(code)
                        bn3.append(name)
                        isd3.append(issue_date)
                        rtd3.append(return_date)
                        us3=pd.DataFrame(dic4)
                        us3.to_sql(PASS[3],myco,if_exists='replace')
            
    elif as1=='4':
        print("So you have selected Horror...")
        print("")
        mycon7=sq.connect(host="localhost",user="root",passwd="radheradhe",database="project")      #Connecting to mysql
        if mycon7.is_connected():
            df8=pd.read_sql("select Book_Code,Book_Name,Author,Published from books where Genre='Horror';",mycon7)      #Importing table of Horror
            print("Choose your book...")
            print("")
            print(df8)
            print("")
            bcd=input("        Enter the book code:")   #Asking the book code
            print("")
            if bcd in P_exit:
                exit()
            while bcd not in list(df8.Book_Code):
                print("Invalid Book Code!")
                bcd=input("        Enter the book code:")   #Asking the book code
                if bcd in P_exit:
                    exit()                
            for k in range(len(df8)):
                if df8.Book_Code[k]==bcd:
                    code=bcd
                    name=df8.Book_Name[k]
                    issue_date=str(datetime.date.today())
                    return_date='Pending'
                    if User_ID[-1]==ID[0]:
                        bc.append(code)
                        bn.append(name)
                        isd.append(issue_date)
                        rtd.append(return_date)
                        us=pd.DataFrame(dic1)
                        us.to_sql(PASS[0],myco,if_exists='replace')
                    elif User_ID[-1]==ID[1]:
                        bc1.append(code)
                        bn1.append(name)
                        isd1.append(issue_date)
                        rtd1.append(return_date)
                        us1=pd.DataFrame(dic2)
                        us1.to_sql(PASS[1],myco,if_exists='replace')
                    elif User_ID[-1]==ID[2]:
                        bc2.append(code)
                        bn2.append(name)
                        isd2.append(issue_date)
                        rtd2.append(return_date)
                        us2=pd.DataFrame(dic3)
                        us2.to_sql(PASS[2],myco,if_exists='replace')
                    else:
                        bc3.append(code)
                        bn3.append(name)
                        isd3.append(issue_date)
                        rtd3.append(return_date)
                        us3=pd.DataFrame(dic4)
                        us3.to_sql(PASS[3],myco,if_exists='replace')

#RETURN
def returns():
    global d1
    global df1    
    mycon1=sq.connect(host="localhost",user="root",passwd="radheradhe",database="project")      #Connecting to mysql
    df1=pd.read_sql("select * from users;",mycon1)
    for g in range(len(df1)):
        if df1.at[g,'User_ID']==User_ID[-1]:
            ps=df1.at[g,'Password']
            mycon1=sq.connect(host="localhost",user="root",passwd="radheradhe",database="project")      #Connecting to mysql
            daf=pd.read_sql("select * from "+ps,mycon1)
            if daf.at[len(daf)-1,'Returned_Date']=='Pending':

                if ps==df1.at[0,'Password']:
                    rtd[-1]=str(datetime.date.today())
                    dic1={'Book_Code':bc,'Book_Name':bn,'Issued_date':isd,'Returned_Date':rtd}
                    us=pd.DataFrame(dic1)
                    print('Your Book is returned successfully')
                    print("")
                    print('Here is your library details..')
                    print("")
                    print(us)
                    print("")
                    us.to_sql(PASS[0],myco,if_exists='replace')

                elif ps==df1.at[1,'Password']:
                    rtd1[-1]=str(datetime.date.today())
                    dic2={'Book_Code':bc1,'Book_Name':bn1,'Issued_date':isd1,'Returned_Date':rtd1}
                    us1=pd.DataFrame(dic2)
                    print('Your Book is returned successfully')
                    print("")
                    print('Here is your library details..')
                    print("")
                    print(us1)
                    print("")
                    us1.to_sql(PASS[1],myco,if_exists='replace')

                elif ps==df1.at[2,'Password']:
                    rtd2[-1]=str(datetime.date.today())
                    dic3={'Book_Code':bc2,'Book_Name':bn2,'Issued_date':isd2,'Returned_Date':rtd2}
                    us2=pd.DataFrame(dic3)
                    print('Your Book is returned successfully')
                    print("")
                    print('Here is your library details..')
                    print("")
                    print(us2)
                    print("")
                    us2.to_sql(PASS[2],myco,if_exists='replace')

                else:
                    rtd3[-1]=str(datetime.date.today())
                    dic4={'Book_Code':bc3,'Book_Name':bn3,'Issued_date':isd3,'Returned_Date':rtd3}
                    us3=pd.DataFrame(dic4)
                    print('Your Book is returned successfully')
                    print("")
                    print('Here is your library details..')
                    print("")
                    print(us3)
                    print("")
                    us3.to_sql(PASS[3],myco,if_exists='replace')

#DELETE
def delete():
    global d1
    global df1    
    mycon1=sq.connect(host="localhost",user="root",passwd="radheradhe",database="project")      #Connecting to mysql
    df1=pd.read_sql("select * from users;",mycon1)
    for g in range(len(df1)):
        if df1.at[g,'User_ID']==User_ID[-1]:
            index2=g
    del NAME[g-1]
    del PASS[g-1]
    del DOB[g-1]
    del ID[g-1]
    del ind[g-1]
    d1={'User_ID':ID,'User_Name':NAME,'Date_Of_Birth':DOB,'Password':PASS}
    df1=pd.DataFrame(d1)
    print(df1.loc[:,'User_ID':'Date_Of_Birth'])
    print("")

#DETAILS
def details():
    global d1
    global df1    
    print("Here is your details...")
    print("")
    mycon1=sq.connect(host="localhost",user="root",passwd="radheradhe",database="project")  #Connecting to mysql
    df1=pd.read_sql("select * from users;",mycon1)
    for p in range(len(df1)):
        if df1.at[p,'User_ID']==User_ID[-1]:
            det=df1.loc[p,'User_ID':'Date_Of_Birth']
            print(det)
            print("")
            password=df1.at[p,'Password']
            mycon1=sq.connect(host="localhost",user="root",passwd="radheradhe",database="project")
            dx=pd.read_sql("select * from " + password + ";",mycon1)
            dx1=dx.loc[:,'Book_Code':'Returned_Date']
            print("Here is your library details...")
            print("")
            print(dx1)
            print("")
            
#STARTING THE PROGRAM

#PHASE 1    
start=input("        Do you want to start the pragram?(y/n)")
print("")
if start in P_exit:
    exit()
while start not in p3:
    print("Invalid Input!!")
    print("")
    start=input("        Do you want to start the pragram?(y/n)")
    print("")
    if start in P_exit:
        exit()
while start not in P_no:
    if start in P_yes:
        print("So here we go....")
        print("")
        ask1()
        a=input("        How do you want to start?")
        print("")
        if a in P_exit:
            exit()
        while a not in p1:
            print("Invalid Input!")
            print("")
            a=input("        How do you want to start?")
            print("")
            if a=='exit':
                exit()

        #Login of a user
        if a in P_login:
            login()

        #Registration of a user
        elif a in P_register:
            register()

        #Updating the data of a user
        elif a in P_update:
            update()
            print("Your data has been updated successfully!!")
            print("")
            x=input("        Do you want to update more data?(y/n)")
            print("")
            if x in P_exit:
                exit()
            while x in P_yes:
                update()
                x=input("        Do you want to update more data?(y/n)")
                print("")
                if x in P_exit:
                    exit()

        #PHASE 2
        ask2()
        b=input("        What do you want to do next?")
        print("")
        if b in P_exit:
            exit()
        while b not in p2:
            print("Invalid Input!!")
            print("")
            b=input("        What do you want to do next?")
            print("")
            if b in P_exit:
                exit()

        #Issuing a book
        if b in P_issue:
            mycon1=sq.connect(host="localhost",user="root",passwd="radheradhe",database="project")  #Connecting to mysql
            df1=pd.read_sql("select * from users;",mycon1)
            for g in range(len(df1)):
                if df1.at[g,'User_ID']==User_ID[-1]:
                    ps=df1.at[g,'Password']
                    mycon1=sq.connect(host="localhost",user="root",passwd="radheradhe",database="project")
                    daf=pd.read_sql("select * from "+ps,mycon1)
                    if daf.at[len(daf)-1,'Returned_Date']=='Pending':
                        print("Dear User, you still have a book pending in your list to return. So you cannot issue another book...")
                        print("")
                    else:
                        issue()
                        print("Your book has been Issued successfully!")

        #Returning a book
        elif b in P_return:
            returns()

        #Deleting an account
        elif b in P_delete:
            mycon1=sq.connect(host="localhost",user="root",passwd="radheradhe",database="project")  #Connecting to mysql
            df1=pd.read_sql("select * from users;",mycon1)            
            for g in range(len(df1)):
                if df1.at[g,'User_ID']==User_ID[-1]:
                    ps=df1.at[g,'Password']
                    mycon1=sq.connect(host="localhost",user="root",passwd="radheradhe",database="project")
                    daf=pd.read_sql("select * from "+ps,mycon1)
                    if daf.at[len(daf)-1,'Returned_Date']=='Pending':
                        print("Dear User, you still have a book pending in your list to return. So you cannot delete your account...")
                        print("")
                    else:
                        delete()
                        print("Your account is deleted successfully!")
                        print("")

        #Details of an account
        elif b in P_details:
            details()

        #Logout
        elif b in P_logout:
            exit()

        #Ending the loop
        start=input("        Do you want to continue the pragram?(y/n)")
        print("")
        if start in P_exit:
            exit()
        while start not in p3:
            print("Invalid Input!!")
            print("")
            start=input("        Do you want to continue the pragram?(y/n)")
            print("")
            if start in P_exit:
                exit()

else:
    exit()
