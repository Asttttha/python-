import csv
import os
def write():
       f=open("foodvilla.csv","a",newline='')
       w=csv.writer(f)
       l=["name","age","phone"]
       name=input("enter your name")
       age=int(input("enter your age"))
       people=int(input("enter the number of people with you including children"))
       phone=input("enter your phone number")
       if len(phone)==10:
           pass
       else:
           print("your number is wrong please check it again")
        l=[name,age,people,phone]
        w.writerow(l)
       f.close()
def display():
      f=open("foodvilla.csv","r",newline='')
      exm=csv.reader(f)
      for i in exm:
        print(i)
      f.close()
def update():
     f1=open("foodvilla1.csv","w")
     data1=csv.writer(f1)
     f=open("foodvilla.csv","r")
     data=csv.reader(f)
     r=input("enter your name")
     n=input("enter your correct name")
     for i in data:
         if int(i[0])==r:
             data1.writerow(i[0],n,i[2])
         else:
             data1.writerow(i[0],i[1],i[2])
     f.close()
     f1.close()
def delete():
    lines=list()
    members=input("Please enter a member's name to be deleted.")
    with open('foodvilla.csv','r',newline='') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            lines.append(row)
            for field in row:
                if field == members:
                     lines.remove(row)
    with open('foodvilla.csv', 'w',newline='') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)
        readFile.close()
        print("your name has been deleted")
while True:
    print("MENU \n1=WRITE \n2=DISPLAY \n3=UPDATE \n4=DELETE")
    ch=int(input("enter the number"))
    if ch==1:
        write()
    if ch==2:
        display()
    if ch==3:
        update()
    if ch==4:
        delete()
