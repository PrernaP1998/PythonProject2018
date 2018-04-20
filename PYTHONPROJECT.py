from tkinter import *
import tkinter

top = tkinter.Tk()
count = 0

employeid = StringVar()
employename = StringVar()
employeage = StringVar()
employedept = StringVar()
employesal = StringVar()


# --------------------------- FUNCTIONS -----------------------------------------------------------------

def Add_Employee():
    f = open('/Users/prernaparashar/Desktop/Prerna.txt', 'a')
    employeid = E1.get()
    employename = E2.get()
    employeage= E3.get()
    employedept = E4.get()
    employesal = E5.get()
    
    if (    employeid == '' or employename == '' or employeage == '' or employedept == '' or employesal == ''):
        print("Details can't be empty!")
        exit()
    f.writelines(
        employeid.ljust(20) + employename.ljust(20) + employeage.ljust(20) + employedept.ljust(20) + employesal.ljust(3) + "\n")
    print("Record added to file!")
    f.close()


def Delete_Employee():
    k = employeid.get()
    f = open('/Users/prernaparashar/Desktop/Prerna.txt', 'r')
    ctr = 0
    for line in f:
        ctr = ctr + 1
    print("No. of lines in file:")
    print(ctr)
    f.seek(0)
    lines = f.readlines()
    print(lines)
    f.close()
    f = open('/Users/prernaparashar/Desktop/Prerna.txt', 'w')
    for employee in lines:
        j = employee.split()
        print(j)
        if (j[0] != k):
            f.writelines(j[0].ljust(20) + j[1].ljust(20) + j[2].ljust(20) + j[3].ljust(20) + j[4].ljust(5) + "\n")
            print("Record deleted from the file!!")
    employeid.set("")
    employename.set("")
    employeage.set("")
    employedept.set("")
    employesal.set("")
    f.close()


def Search_employe():
    k = employeid.get()
    f = open('/Users/prernaparashar/Desktop/Prerna.txt', 'r')
    ctr = 0
    flag = 0
    for line in f:
        ctr = ctr + 1
    print("No. of lines in file:")
    print(ctr)
    f.seek(0)
    lines = f.readlines()
    print(lines)
    for employee in lines:
        j = employee.split()
        if (j[0] == k):
            print(j)
            employeid.set(j[0])
            employename.set(j[1])
            employeage.set(j[2])
            employedept.set(j[3])
            employesal.set(j[4])
            flag = 1
            break
    if (flag == 0):
        print("Record not found!")
    else:
        print("Record found!")
    employeid.set("")
    employename.set("")
    employeage.set("")
    employedept.set("")
    employesal.set("")
    f.close()


def Update_employe():
    new_id = employeid.get()
    new_name = employename.get()
    new_age = employeage.get()
    new_dept = employedept.get()
    new_sal = employesal.get()
    f = open('/Users/prernaparashar/Desktop/Prerna.txt', 'r')
    ctr = 0
    for line in f:
        ctr = ctr + 1
    print("No. of lines in file:")
    print(ctr)
    f.seek(0)
    lines = f.readlines()
    f.close()
    f = open('/Users/prernaparashar/Desktop/Prerna.txt', 'w')
    for employe in lines:
        j = employe.split()
        if (j[0] != new_id):
            f.writelines(j[0].ljust(3) + j[1].ljust(20) + j[2].ljust(20) + j[3].ljust(20) + j[4].ljust(5) + "\n")

        else:
            f.writelines(
                j[0].ljust(3) + new_name.ljust(20) + new_age.ljust(20) + new_dept.ljust(20) + new_sal.ljust(
                    5) + "\n")
    print("Record updated!!")
    employeid.set("")
    employename.set("")
    employeage.set("")
    employedept.set("")
    employesal.set("")
    f.close()


def Get_First_Record():
    f = open('/Users/prernaparashar/Desktop/Prerna.txt', 'r')
    ctr = 0
    flag = 0
    for line in f:
        ctr = ctr + 1
    print("No. of lines in file:")
    print(ctr)
    f.seek(0)
    lines = f.readlines()
    l = list(lines)
    print("\n")
    print(l)
    j = l[0].split()
    employeid.set(j[0])
    employename.set(j[1])
    employeage.set(j[2])
    employedept.set(j[3])
    employesal.set(j[4])
    print("\n First Record of file is as:")
    print(l[0])
    f.close()


def Get_Last_Record():
    f = open('/Users/prernaparashar/Desktop/Prerna.txt', 'r')
    ctr = 0
    flag = 0
    for line in f:
        ctr = ctr + 1
    print("No. of lines in file:")
    print(ctr)
    f.seek(0)
    lines = f.readlines()
    l = list(lines)
    print(l)
    j = l[ctr - 1].split()
    employeid.set(j[0])
    employename.set(j[1])
    employeage.set(j[2])
    employedept.set(j[3])
    employesal.set(j[4])
    print("\n Last Record of file is as:")
    print(l[ctr - 1])
    f.close()


def Get_Prev_Record():
    global count
    i = 0
    ctr = 0
    f = open('/Users/prernaparashar/Desktop/Prerna.txt', 'r')
    for line in f:
        ctr = ctr + 1
    print("No. of lines in file:")
    print(ctr)
    f.seek(0)
    try:

        while (i <= count - 1):
            l = f.readline()
            i = i + 1

        m = l.split()
        employeid.set(m[0])
        employename.set(m[1])
        employeage.set(m[2])
        employedept.set(m[3])
        employesal.set(m[4])
        print(m)

    except:
        employeid.set("")
        employename.set("")
        employeage.set("")
        employedept.set("")
        employesal.set("")
        print("Sorry, no more records!")
    count = count - 1
    f.close()


def Get_Next_Record():
    global count
    i = 0
    ctr = 0
    f = open('/Users/prernaparashar/Desktop/Prerna.txt', 'r')
    for line in f:
        ctr = ctr + 1
    print("No. of lines in file:")
    print(ctr)
    f.seek(0)
    try:

        while (i <= count):
            l = f.readline()
            i = i + 1

        m = l.split()
        employeid.set(m[0])
        employename.set(m[1])
        employeage.set(m[2])
        employedept.set(m[3])
        employesal.set(m[4])
        print(m)

    except:
        employeid.set("")
        employename.set("")
        employeage.set("")
        employedept.set("")
        employesal.set("")
        print("Sorry, no more records!")
    count = count + 1
    f.close()


top.configure(background="gray")
# ------------------------------ LABELS ----------------------------------------------------------

w = tkinter.Label(top, text="EMPLOYEE DETAILS of ABC.PVT.LTD", bg="yellow", font=('calibri', 15, 'bold'), underline=12).grid(row=0,
                                                                                                          column=1)
tkinter.Label(top, text="employee ID:", bg="lightyellow", font=('Times New Roman', 15, 'bold')).grid(row=5, sticky=W)
tkinter.Label(top, text="employee NAME:", bg="lightyellow", font=('Times New Roman', 15, 'bold')).grid(row=6, sticky=W)
tkinter.Label(top, text="employee AGE:", bg="lightyellow", font=('Times New Roman', 15, 'bold')).grid(row=7, sticky=W)
tkinter.Label(top, text="employee DEPARTMENT:", bg="lightyellow", font=('Times New Roman', 15, 'bold')).grid(row=8, sticky=W)
tkinter.Label(top, text="employee SALARY:", bg="lightyellow", font=('Times New Roman', 15, 'bold')).grid(row=9, sticky=W)

# ------------------------------ ENTRIES ---------------------------------------------------------

E1 = tkinter.Entry(top, textvariable=employeid)
E2 = tkinter.Entry(top, textvariable=employename)
E3 = tkinter.Entry(top, textvariable=employeage)
E4 = tkinter.Entry(top, textvariable=employedept)
E5 = tkinter.Entry(top, textvariable=employesal)
E1.grid(row=5, column=1)
E2.grid(row=6, column=1)
E3.grid(row=7, column=1)
E4.grid(row=8, column=1)
E5.grid(row=9, column=1)

# ------------------------------ BUTTONS -------------------------------------------------------------------

fr = tkinter.Button(top, text="<<", width=15, bg="yellow", font=('Georgia', 15, 'bold'),
                    command=Get_First_Record).grid(row=10, column=0)
pr = tkinter.Button(top, text="<", width=15, bg="yellow", font=('Georgia', 15, 'bold'), command=Get_Prev_Record).grid(
    row=10, column=1)
nr = tkinter.Button(top, text=">", width=15, bg="yellow", font=('Georgia', 15, 'bold'), command=Get_Next_Record).grid(
    row=10, column=2)
lr = tkinter.Button(top, text=">>", width=15, bg="yellow", font=('Georgia', 15, 'bold'), command=Get_Last_Record).grid(
    row=10, column=3)

rb = tkinter.Button(top, text="ADD", width=15, bg="yellow", font=('Georgia', 15, 'bold'), command=Add_Employee).grid(
    row=11, column=0)
db = tkinter.Button(top, text="DELETE", width=15, bg="yellow", font=('Georgia', 15, 'bold'), command=Delete_Employee).grid(
    row=11, column=1)
sb = tkinter.Button(top, text="SEARCH", width=15, bg="yellow", font=('Georgia', 15, 'bold'), command=Search_employe).grid(
    row=11, column=2)
ub = tkinter.Button(top, text="UPDATE", width=15, bg="yellow", font=('Georgia', 15, 'bold'), command=Update_employe).grid(
    row=11, column=3)
top.mainloop()