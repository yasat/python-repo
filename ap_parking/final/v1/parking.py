import pymysql as mysqli
import time
import datetime
from datetime import timedelta
datetimeFormat = '%Y-%m-%d %H:%M:%S'
host='localhost'
user='root'
password=''
port=3306
db='parking'
con=mysqli.connect(host=host,port=port,user=user,passwd=password,db=db)
cur=con.cursor()

def new_vehicle(vehicle):
    try:
        sql = "select * from `vehicles` where `no`=(%s) and `status`=(%s)"
        cur.execute(sql,(vehicle,"in"))
        for row in cur:
            print("vehicle already inside")
            sql = "select `intime`,`indno` from `vehicles` where `no`=(%s) and `status`=(%s)"
            cur.execute(sql,(vehicle,"in"))
            for row in cur:
                intime=(str) (row[0])
                indno=(int) (row[1])
                outtime=time.strftime('%Y-%m-%d %H:%M:%S')
                outtime=(str) (outtime)
                diff = datetime.datetime.strptime(outtime, datetimeFormat) - datetime.datetime.strptime(intime, datetimeFormat)
                price= (int) (round((diff.seconds/(60*60)) * 30))
                print("price: "+ (str) (price))
                paid=input('paid: (Y)es/(N)o/(C)ancel: ')
                if(paid=='y' or paid=='Y'):
                    sql = "update `vehicles` set `outtime`=(%s), `status`=(%s),`amount`=(%s) where `indno`=(%s)"
                    cur.execute(sql,(outtime, "out", price, indno))
                    con.commit()
                    tex=open("print.txt","w+")
                    tex.write("VIJAYAWADA AIRPORT\n")
                    tex.write("Welcome\n")
                    tex.write("vehicle number: "+vehicle+"\n")
                    tex.write("enter time: "+intime+"\n")
                    tex.write("exit time: "+outtime+"\n")
                    tex.write("amount: "+(str) (price)+"\n")
                    tex.write("status: paid\n")
                    tex.write("Have a good day\n")
                    tex.close()
                    print("paid")
                elif(paid=='n' or paid=='N'):
                    sql = "update `vehicles` set `outtime`=(%s), `status`=(%s) where `indno`=(%d)"
                    cur.execute(sql,(outtime,"out", indno))
                    con.commit()
                    print("not paid")
                else:
                    return
                return
        intime=time.strftime('%Y-%m-%d %H:%M:%S')
        intime=(str) (intime)
        counter=1
        sql = "select `indno` from `vehicles"
        cur.execute(sql)
        for row in cur:
            counter=counter+1
        sql = "INSERT INTO `vehicles` (`indno`,`no`, `intime`, `status`) VALUES (%s,%s, %s, %s)"
        cur.execute(sql,(counter, vehicle, intime, "in"))
        con.commit()
        tex=open("print.txt","w+")
        tex.write("VIJAYAWADA AIRPORT\n")
        tex.write("Welcome\n")
        tex.write("vehicle number: "+vehicle+"\n")
        tex.write("enter time: "+intime+"\n")
        tex.write("Have a good day\n")
        tex.close()
        print("vehicle entered")
    except:
        print("not uploaded")
def out_vehicle(vehicle):
    try:
        sql = "select `intime`,`indno` from `vehicles` where `no`=(%s) and `status`=(%s)"
        cur.execute(sql,(vehicle,"in"))
        for row in cur:
            intime=(str) (row[0])
            indno = (int) (row[1])
            outtime=time.strftime('%Y-%m-%d %H:%M:%S')
            outtime=(str) (outtime)
            print(outtime)
            diff = datetime.datetime.strptime(outtime, datetimeFormat) - datetime.datetime.strptime(intime, datetimeFormat)
            price= (int) (round((diff.seconds/(60*60)) * 30))
            print(price)
            paid=input('paid: (Y)es/(N)o/(C)ancel: ')
            if(paid=='y' or paid=='Y'):
                sql = "update `vehicles` set `outtime`=(%s), `status`=(%s),`amount`=(%s) where `indno`=(%s)"
                cur.execute(sql,(outtime, "out", price, indno))
                con.commit()
                tex=open("print.txt","w+")
                tex.write("VIJAYAWADA AIRPORT\n")
                tex.write("Welcome\n")
                tex.write("vehicle number: "+vehicle+"\n")
                tex.write("enter time: "+intime+"\n")
                tex.write("exit time: "+outtime+"\n")
                tex.write("amount: "+(str) (price)+"\n")
                tex.write("status: paid\n")
                tex.write("Have a good day\n")
                tex.close()
                print("paid")
            elif(paid=='n' or paid=='N'):
                sql = "update `vehicles` set `outtime`=(%s), `status`=(%s) where `indno`=(%s)"
                cur.execute(sql,(outtime,"out", indno))
                con.commit()
                print("not paid")
            else:
                return                
    except:
        print("not uploaded")
def listview():
    print("index"+"   "+"vehicle"+"      "+"intime"+"                "+"outtime"+"             "+"status"+" "+"amount")
    sql="select * from `vehicles`"
    cur.execute(sql)
    for row in cur:
        indno=(str) (row[0])
        no=row[1]
        intime=(str) (row[2])
        outtime=(str) (row[3])
        status=row[4]
        amount=(str) (row[5])
        if(status=='in'):
            print(indno+"      "+no+"   "+intime+"   "+"                   "+"   "+status+"    "+amount+"*")
        else:
            print(indno+"      "+no+"   "+intime+"   "+outtime+"   "+status+"   "+amount)
    print()
def listviewsp(vehicle):
    print("index"+"   "+"vehicle"+"      "+"intime"+"                "+"outtime"+"             "+"status"+" "+"amount")
    sql="select * from `vehicles` where `no`=(%s)"
    cur.execute(sql,(vehicle))
    for row in cur:
        indno=(str) (row[0])
        no=row[1]
        intime=(str) (row[2])
        outtime=(str) (row[3])
        status=row[4]
        amount=(str) (row[5])
        if(status=='in'):
            print(indno+"      "+no+"   "+intime+"   "+"                   "+"   "+status+"    "+amount+"*")
        else:
            print(indno+"      "+no+"   "+intime+"   "+outtime+"   "+status+"   "+amount)
    print()
option=1
while(option!=4):
    option=(int) (input("1) New Vehicle  2) Out Vehicle   3) List    4) Exit:\n"))
    if(option==1):
        vehicle=input("vehicle number : ")
        new_vehicle(vehicle)
    elif(option==2):
        vehicle=input("vehicle number : ")
        out_vehicle(vehicle)
    elif(option==3):
        vehicle=input("vehicle number : ")
        if(vehicle!=''):
            listviewsp(vehicle)
        else:
            listview()
cur.close()
con.close()
