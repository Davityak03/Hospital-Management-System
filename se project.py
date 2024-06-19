from tkinter import *
import tkinter.messagebox
import pymysql
from PIL import ImageTk,Image
mydb=pymysql.connect(host="localhost",user="root",passwd="abc123",database="hospital")
mycursor=mydb.cursor()
def datereverse(a):# To  reverse the format of the date for mysql
    b=a[0:2]
    c=a[2:6]
    d=a[6:10]
    global date
    date=d+c+b
def datereverse1(a):# To  reverse the format of the date for mysql
    b=a[0:2]
    c=a[2:6]
    d=a[6:10]
    global date1
    date1=d+c+b
def login():# Password and userid input from the user
    k=kEntry.get()
    sql1="SELECT Username FROM login"
    mycursor.execute(sql1)
    record1=mycursor.fetchall()
    if (k in record1[0]):
        w=wEntry.get()
        sql2="SELECT Password FROM login"
        mycursor.execute(sql2)
        record2=mycursor.fetchall()
        if (w in record2[0]):
            plus.destroy()
            root=Tk()
            root.title("Selection")
            root.configure(bg="white")#
            root.geometry("1000x500")
            root.maxsize(1000,500)
            root.minsize(1000,500)
            def choice1():#To enter data for one only
                def cd():#Validations
                    global totalcost
                    Label(master,text="                                         ",bg="light sky blue").grid(row=6,column=7)
                    Label(master,text="                                         ",bg="light sky blue").grid(row=15,column=7)
                    f=costEntry.get()
                    if f.isdigit()==False:
                        tkinter.messagebox.showerror("Error","There must be numeric values only in Cost Per Day of the Room'")
                        sys.exit()
                    else:
                        n10=f
                    e=nodaysadEntry.get()
                    if e.isdigit()==False:
                        tkinter.messagebox.showerror("Error","There must be numeric values only in Nuber of days Admitted column")
                        sys.exit()
                    else:
                        n11=e
                    nd=int(nodaysadEntry.get())
                    cs=int(costEntry.get())
                    cost=nd*cs
                    tax=cost*0.05
                    totalcost=int(cost+tax)
                    Label(master,text=totalcost,fg="red",bg="white",relief="solid").grid(row=6,column=7)
                    Label(master,text="Incl Tax and in Rs",fg="navy",bg="light sky blue").grid(row=7,column=7)
                    Label(master,text=totalcost,fg="red",bg="white",relief="solid").grid(row=15,column=7)
                    Label(master,text="Incl Tax and in Rs",fg="navy",bg="light sky blue").grid(row=16,column=7)
                def avsg():#Validations
                    y=nameEntry.get()
                    if y.isalpha()==False:
                        tkinter.messagebox.showerror("Error","There must be alphabets only in first name of the patient")
                        sys.exit()
                    else:
                        n1=y.lower()
                    t=lastnameEntry.get()
                    if t.isalpha()==False:
                        tkinter.messagebox.showerror("Error","There must be alphabets only in last name of patient")
                        sys.exit()
                    else:
                        n2=t.lower()
                    e=ageEntry.get()
                    if e.isdigit()==False:
                        tkinter.messagebox.showerror("Error","There must be numeric values only in patient's age column")
                        sys.exit()
                    else:
                        n3=int(e)
                    f=diseaseEntry.get()
                    if f.isalpha==False:
                        kinter.messagebox.showerror("Error","There must be alphabets only in patient's disease/injury column")
                        sys.exit()
                    else:
                        n4=f.lower()
                    q=dnameEntry.get()
                    if q.isalpha()==False:
                        tkinter.messagebox.showerror("Error","There must be alphabets only in first name of the Doctor")
                        sys.exit()
                    else:
                        n5=q.lower()
                    l=dlastnameEntry.get()
                    if l.isalpha()==False:
                        tkinter.messagebox.showerror("Error","There must be alphabets only in Last name of the Doctor")
                        sys.exit()
                    else:
                        n6=l.lower()
                    u=dageEntry.get()
                    if u.isdigit()==False:
                        tkinter.messagebox.showerror("Error","There must be numeric values only in Dotor's age column")
                        sys.exit()
                    else:
                        n7=int(u)
                    o=dspecialityEntry.get()
                    if o.isalpha()==False:
                        tkinter.messagebox.showerror("Error","There must be alphabets only in speciality of the Doctor")
                        sys.exit()
                    else:
                        n16=o.lower()
                    t=roomnoEntry.get()
                    if t.isdigit()==False:
                        tkinter.messagebox.showerror("Error","There must be numeric values only in Room No'")
                        sys.exit()
                    else:
                        n8=int(t)
                    r=roomtypeEntry.get()
                    if r.isalpha()==False:
                        tkinter.messagebox.showerror("Error","There must be alphabets only in Type of room for the Patient")
                        sys.exit()
                    else:
                        n9=r.lower()
                    s=PhoneEntry.get()
                    if s.isdigit()==False or len(s)!=10:
                        tkinter.messagebox.showerror("Error","There must be numeric values only in Phone number column or entered phone number is invalid")
                        sys.exit()
                    else:
                        n15=int(s)
                    n10=int(costEntry.get())
                    n11=int(nodaysadEntry.get())
                    m=billnoEntry.get()
                    if m.isdigit()==False:
                        tkinter.messagebox.showerror("Error","There must be numeric values only in Bill No'")
                        sys.exit()
                    else:
                        n12=int(m)
                    z=surgerynoEntry.get()
                    if z.isdigit()==False:
                        tkinter.messagebox.showerror("Error","There must be numeric values only in Surgery No column")
                        sys.exit()
                    else:
                        n13=int(z)
                    r=alEntry.get()
                    if r.lower()=="dead" or r.lower()=="alive":
                        n14=r.lower()
                    else:
                        tkinter.messagebox.showerror("Error","Invalid input in Dead/Alive column")
                        sys.exit()
                    p=tkinter.messagebox.askquestion("Submission","Are you sure you want to upload the data?")

                    if p=="yes":#confirmation to add this data 
                        nd=int(nodaysadEntry.get())
                        cs=int(costEntry.get())
                        cost=nd*cs
                        tax=cost*0.05
                        totalcost1=int(cost+tax)
                        k=var.get()
                        if k==1:
                            m1="male"
                        if k==2:
                            m1="female"
                        if k==3:
                            m1="others"

                        #adding tha data in the database
                        row1=[n5,n6,n7,doctoridEntry.get(),n16]
                        sql="INSERT INTO doctor VALUES(%s,%s,%s,%s,%s)"
                        mycursor.execute(sql,row1)
                        mydb.commit()

                        datereverse(dayEntry.get())
                        row=[n1,n2,n3,idEntry.get(),doctoridEntry.get(),date,m1,n4]
                        sql="INSERT INTO patient VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
                        mycursor.execute(sql,row)
                        mydb.commit()

                        row2=[n8,idEntry.get(),n9,n10]
                        sql="INSERT INTO patients_room_info VALUES(%s,%s,%s,%s)"
                        mycursor.execute(sql,row2)
                        mydb.commit()

                        datereverse(idateadmEntry.get())
                        datereverse1(idatedisEntry.get())
                        row3=[n13,n8,date,date1,n15]
                        sql="INSERT INTO patient_in_info VALUES(%s,%s,%s,%s,%s)"
                        mycursor.execute(sql,row3)
                        mydb.commit()

                        row4=[n12,idEntry.get(),doctoridEntry.get(),n11,n10,totalcost1]
                        sql="INSERT INTO billing_info VALUES(%s,%s,%s,%s,%s,%s)"
                        mycursor.execute(sql,row4)
                        mydb.commit()

                        row5=[outidEntry.get(),n1,n13,n12,n14,totalcost1]
                        sql="INSERT INTO patient_out_info VALUES(%s,%s,%s,%s,%s,%s)"
                        mycursor.execute(sql,row5)
                        mydb.commit()
                        master.destroy()
                                    
                master =Toplevel()
                master.geometry("2500x1000")
                master.title("Data Entry")
                master.configure(bg="light sky blue")
                Label(master,text="Patient's Info :",fg="green4",font="Times",bg="light sky blue").grid(row=0,column=0)
                Label(master,text="Patient's First Name",bg="light sky blue").grid(row=1,column=0)
                Label(master,text="Patient's Last Name",bg="light sky blue").grid(row=2,column=0)
                Label(master,text="Patient's Age",bg="light sky blue").grid(row=3,column=0)
                Label(master,text="Patient's ID",bg="light sky blue").grid(row=4,column=0)
                Label(master,text="Doctor's ID",bg="light sky blue").grid(row=5,column=0)
                Label(master,text="Date of birth of the patient :",bg="light sky blue").grid(row=6,column=0,pady=10)
                Label(master,text="DD-MM-YYYY",bg="light sky blue").grid(row=6,column=1,pady=10)
                Label(master,text="Disease suffering/Injury",bg="light sky blue").grid(row=9,column=0,pady=10)
                Label(master,text="Doctor's Info :",fg="green4",font="Times",bg="light sky blue").grid(row=11,column=0)
                Label(master,text="Doctor's First Name",bg="light sky blue").grid(row=12,column=0)
                Label(master,text="Doctor's Last Name",bg="light sky blue").grid(row=13,column=0)
                Label(master,text="Doctor's Age",bg="light sky blue").grid(row=14,column=0)
                Label(master,text="Doctor's ID",bg="light sky blue").grid(row=15,column=0)
                Label(master,text="Speciality of the Doctor in",bg="light sky blue").grid(row=16,column=0)
                Label(master,text="Patient's Room Info :",fg="green4",font="Times",bg="light sky blue").grid(row=0,column=4,padx=42)
                Label(master,text="Room number",bg="light sky blue").grid(row=1,column=4)
                Label(master,text="Patient ID",bg="light sky blue").grid(row=2,column=4)
                Label(master,text="Type of Room",bg="light sky blue").grid(row=3,column=4)
                Label(master,text="Cost per Day",bg="light sky blue").grid(row=4,column=4)
                Label(master,text="Patient_In Info :",fg="green4",font="Times",bg="light sky blue").grid(row=6,column=4)
                Label(master,text="Surgery No",bg="light sky blue").grid(row=7,column=4)
                Label(master,text="Room No",bg="light sky blue").grid(row=8,column=4)
                Label(master,text="Date Admitted in Hospital :",bg="light sky blue").grid(row=9,column=4)
                Label(master,text="DD-MM-YYYY",bg="light sky blue").grid(row=9,column=5)
                Label(master,text="Date Discharged from Hospital :",bg="light sky blue").grid(row=11,column=4)
                Label(master,text="DD-MM-YYYY",bg="light sky blue").grid(row=11,column=5)
                Label(master,text="Phone Number",bg="light sky blue").grid(row=13,column=4)
                Label(master,text="Billing Info :",fg="green4",font="Times",padx=90,bg="light sky blue").grid(row=0,column=6)
                Label(master,text="Bill No",bg="light sky blue").grid(row=1,column=6)
                Label(master,text="Patient's ID",bg="light sky blue").grid(row=2,column=6)
                Label(master,text="Doctor's ID",bg="light sky blue").grid(row=3,column=6)
                Label(master,text="No of days Admitted",bg="light sky blue").grid(row=4,column=6)
                Label(master,text="Cost Per Day",bg="light sky blue").grid(row=5,column=6)
                Label(master,text="Total Cost",fg="navy",bg="light sky blue").grid(row=6,column=6)
                Label(master,text="Patient_Out Info :",fg="green4",font="Times",bg="light sky blue").grid(row=9,column=6)
                Label(master,text="Patient's Out  ID",bg="light sky blue").grid(row=10,column=6,pady=5)
                Label(master,text="Patient's First Name",bg="light sky blue").grid(row=11,column=6,pady=5)
                Label(master,text="Surgery No",bg="light sky blue").grid(row=12,column=6,pady=5)
                Label(master,text="Bill No",bg="light sky blue").grid(row=13,column=6,pady=5)
                Label(master,text="Dead/Alive",bg="light sky blue").grid(row=14,column=6,pady=5)
                Label(master,text="Total Cost",fg="navy",bg="light sky blue").grid(row=15,column=6,pady=5)

                nameValue=StringVar()#PATIENT'S INFO
                lastnameValue=StringVar()
                ageValue=StringVar()
                idValue=StringVar()
                doctoridValue=StringVar()
                dayValue=StringVar()
                diseaseValue=StringVar
                nameEntry=Entry(master,textvariable=nameValue,relief="solid")
                ageEntry=Entry(master,textvariable=ageValue,relief="solid")
                idEntry=Entry(master,textvariable=idValue,relief="solid")
                lastnameEntry=Entry(master,textvariable=lastnameValue,relief="solid")
                doctoridEntry=Entry(master,textvariable=doctoridValue,relief="solid")
                dayEntry=Entry(master,textvariable=dayValue,relief="solid")
                diseaseEntry=Entry(master,textvariable=diseaseValue,relief="solid")
                nameEntry.grid(row=1,column=1,pady=10)
                lastnameEntry.grid(row=2,column=1,pady=10)
                ageEntry.grid(row=3,column=1,pady=10)
                idEntry.grid(row=4,column=1,pady=10)
                doctoridEntry.grid(row=5,column=1,pady=10)
                dayEntry.grid(row=7,column=1,pady=10)
                diseaseEntry.grid(row=9,column=1,pady=10)
                var=IntVar()
                Label(master,text="Patient's gender :",bg="light sky blue").grid(row=8,column=0,pady=10)
                r1=Radiobutton(master,text="Male",variable=var,value=1,bg="light sky blue")
                r1.grid(row=8,column=1,pady=0)
                r2=Radiobutton(master,text="Female",variable=var,value=2,bg="light sky blue")
                r2.grid(row=8,column=2,pady=0)
                r3=Radiobutton(master,text="Others",variable=var,value=3,bg="light sky blue")
                r3.grid(row=8,column=3,padx=35,pady=0)


                dnameValue=StringVar()#DOCTOR'S INFO
                dlastnameValue=StringVar()
                dageValue=StringVar()
                didValue=StringVar()
                dspecialityValue=StringVar()
                dnameEntry=Entry(master,textvariable=dnameValue,relief="solid")
                dlastnameEntry=Entry(master,textvariable=dlastnameValue,relief="solid")
                dageEntry=Entry(master,textvariable=dageValue,relief="solid")
                didEntry=Entry(master,textvariable=doctoridValue,relief="solid")
                dspecialityEntry=Entry(master,textvariable=dspecialityValue,relief="solid")
                dnameEntry.grid(row=12,column=1,pady=10)
                dlastnameEntry.grid(row=13,column=1,pady=10)
                dageEntry.grid(row=14,column=1,pady=10)
                didEntry.grid(row=15,column=1,pady=10)
                dspecialityEntry.grid(row=16,column=1,pady=10)

                roomnoValue=StringVar()#Room's Data
                roomtypeValue=StringVar()
                costValue=StringVar()
                roomnoEntry=Entry(master,textvariable=roomnoValue,relief="solid")
                pidEntry=Entry(master,textvariable=idValue,relief="solid")
                roomtypeEntry=Entry(master,textvariable=roomtypeValue,relief="solid")
                costEntry=Entry(master,textvariable=costValue,relief="solid")
                roomnoEntry.grid(row=1,column=5,pady=10)
                pidEntry.grid(row=2,column=5,pady=10)
                roomtypeEntry.grid(row=3,column=5,pady=10)
                costEntry.grid(row=4,column=5,pady=10)

                surgerynoValue=StringVar()#PATIENT_IN INFO
                idateadmValue=StringVar()
                idatedisValue=StringVar()
                PhoneValue=StringVar()
                surgerynoEntry=Entry(master,textvariable=surgerynoValue,relief="solid")
                iroomnoEntry=Entry(master,textvariable=roomnoValue,relief="solid")
                idateadmEntry=Entry(master,textvariable=idateadmValue,relief="solid")
                idatedisEntry=Entry(master,textvariable=idatedisValue,relief="solid")
                PhoneEntry=Entry(master,textvariable=PhoneValue,relief="solid")
                surgerynoEntry.grid(row=7,column=5)
                iroomnoEntry.grid(row=8,column=5)
                idateadmEntry.grid(row=10,column=5,pady=10)
                idatedisEntry.grid(row=12,column=5)
                PhoneEntry.grid(row=13,column=5,pady=10)

                billnoValue=StringVar()#BILL INFO
                patidValue=StringVar()
                docidValue=StringVar()
                nodaysadValue=StringVar()
                costperdayValue=StringVar()
                billnoEntry=Entry(master,textvariable=billnoValue,relief="solid")
                patidEntry=Entry(master,textvariable=idValue,relief="solid")
                docidEntry=Entry(master,textvariable=doctoridValue,relief="solid")
                nodaysadEntry=Entry(master,textvariable=nodaysadValue,relief="solid")
                costperdayEntry=Entry(master,textvariable=costValue,relief="solid")
                billnoEntry.grid(row=1,column=7)
                patidEntry.grid(row=2,column=7)
                docidEntry.grid(row=3,column=7)
                nodaysadEntry.grid(row=4,column=7)
                costperdayEntry.grid(row=5,column=7)

                outidValue=StringVar()#PAIENT_OUT INFO
                alValue=StringVar()
                outidEntry=Entry(master,textvariable=outidValue,relief="solid")
                pfnEntry=Entry(master,textvariable=nameValue,relief="solid")
                SEntry=Entry(master,textvariable=surgerynoValue,relief="solid")
                billEntry=Entry(master,textvariable=billnoValue,relief="solid")
                alEntry=Entry(master,textvariable=alValue,relief="solid")
                outidEntry.grid(row=10,column=7)
                pfnEntry.grid(row=11,column=7)
                SEntry.grid(row=12,column=7)
                billEntry.grid(row=13,column=7)
                alEntry.grid(row=14,column=7)
                Button(master,text="Calculate Total Cost",command=cd,fg="white",bg="green").grid(row=7,column=6)
                Button(master,text="Submit",command=avsg,bg="blue",fg="white").grid(row=15,column=4)

            def choice2():#To add multiple data at once
                def cd():#Validations
                    global totalcost
                    Label(master,text="                                         ",bg="light sky blue").grid(row=6,column=7)
                    Label(master,text="                                         ",bg="light sky blue").grid(row=15,column=7)
                    f=costEntry.get()
                    if f.isdigit()==False:
                        tkinter.messagebox.showerror("Error","There must be numeric values only in Cost Per Day of the Room'")
                        sys.exit()
                    else:
                        n10=f
                    e=nodaysadEntry.get()
                    if e.isdigit()==False:
                        tkinter.messagebox.showerror("Error","There must be numeric values only in Nuber of days Admitted column")
                        sys.exit()
                    else:
                        n11=e
                    nd=int(nodaysadEntry.get())
                    cs=int(costEntry.get())
                    cost=nd*cs
                    tax=cost*0.05
                    totalcost=int(cost+tax)
                    Label(master,text=totalcost,fg="red",bg="white",relief="solid").grid(row=6,column=7)
                    Label(master,text="Incl Tax and in Rs",fg="navy",bg="light sky blue").grid(row=7,column=7)
                    Label(master,text=totalcost,fg="red",bg="white",relief="solid").grid(row=15,column=7)
                    Label(master,text="Incl Tax and in Rs",fg="navy",bg="light sky blue").grid(row=16,column=7)
                def avsg():
                    y=nameEntry.get()
                    if y.isalpha()==False:
                        tkinter.messagebox.showerror("Error","There must be alphabets only in first name of the patient")
                        sys.exit()
                    else:
                        n1=y.lower()
                    t=lastnameEntry.get()
                    if t.isalpha()==False:
                        tkinter.messagebox.showerror("Error","There must be alphabets only in last name of patient")
                        sys.exit()
                    else:
                        n2=t.lower()
                    e=ageEntry.get()
                    if e.isdigit()==False:
                        tkinter.messagebox.showerror("Error","There must be numeric values only in patient's age column")
                        sys.exit()
                    else:
                        n3=int(e)
                    f=diseaseEntry.get()
                    if f.isalpha==False:
                        kinter.messagebox.showerror("Error","There must be alphabets only in patient's disease/Injury column")
                        sys.exit()
                    else:
                        n4=f.lower()
                    q=dnameEntry.get()
                    if q.isalpha()==False:
                        tkinter.messagebox.showerror("Error","There must be alphabets only in first name of the Doctor")
                        sys.exit()
                    else:
                        n5=q.lower()
                    l=dlastnameEntry.get()
                    if l.isalpha()==False:
                        tkinter.messagebox.showerror("Error","There must be alphabets only in Last name of the Doctor")
                        sys.exit()
                    else:
                        n6=l.lower()
                    u=dageEntry.get()
                    if u.isdigit()==False:
                        tkinter.messagebox.showerror("Error","There must be numeric values only in Dotor's age column")
                        sys.exit()
                    else:
                        n7=int(u)
                    o=dspecialityEntry.get()
                    if o.isalpha()==False:
                        tkinter.messagebox.showerror("Error","There must be alphabets only in speciality of the Doctor")
                        sys.exit()
                    else:
                        n16=o.lower()
                    t=roomnoEntry.get()
                    if t.isdigit()==False:
                        tkinter.messagebox.showerror("Error","There must be numeric values only in Room No'")
                        sys.exit()
                    else:
                        n8=int(t)
                    r=roomtypeEntry.get()
                    if r.isalpha()==False:
                        tkinter.messagebox.showerror("Error","There must be alphabets only in Type of room for the Patient")
                        sys.exit()
                    else:
                        n9=r.lower()
                    s=PhoneEntry.get()
                    if s.isdigit()==False or len(s)!=10:
                        tkinter.messagebox.showerror("Error","There must be numeric values only in Phone number column or entered phone number is invalid")
                        sys.exit()
                    else:
                        n15=int(s)
                    n10=int(costEntry.get())
                    n11=int(nodaysadEntry.get())
                    m=billnoEntry.get()
                    if m.isdigit()==False:
                        tkinter.messagebox.showerror("Error","There must be numeric values only in Bill No'")
                        sys.exit()
                    else:
                        n12=int(m)
                    z=surgerynoEntry.get()
                    if z.isdigit()==False:
                        tkinter.messagebox.showerror("Error","There must be numeric values only in Surgery No column")
                        sys.exit()
                    else:
                        n13=int(z)
                    r=alEntry.get()
                    if r.lower()=="dead" or r.lower()=="alive":
                        n14=r.lower()
                    else:
                        tkinter.messagebox.showerror("Error","Invalid input in Dead/Alive column")
                        sys.exit()
                    p=tkinter.messagebox.askquestion("Submission","Are you sure you want to upload the data?") 
                    if p=="yes":
                        nd=int(nodaysadEntry.get())
                        cs=int(costEntry.get())
                        cost=nd*cs
                        tax=cost*0.05
                        totalcost1=int(cost+tax)
                        k=var.get()
                        if k==1:
                            m1="male"
                        if k==2:
                            m1="female"
                        if k==3:
                            m1="others"

                        row1=[n5,n6,n7,doctoridEntry.get(),n16]
                        sql="INSERT INTO doctor VALUES(%s,%s,%s,%s,%s)"
                        mycursor.execute(sql,row1)
                        mydb.commit()

                        datereverse(dayEntry.get())
                        row=[n1,n2,n3,idEntry.get(),doctoridEntry.get(),date,m1,n4]
                        sql="INSERT INTO patient VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
                        mycursor.execute(sql,row)
                        mydb.commit()

                        row2=[n8,idEntry.get(),n9,n10]
                        sql="INSERT INTO patients_room_info VALUES(%s,%s,%s,%s)"
                        mycursor.execute(sql,row2)
                        mydb.commit()

                        datereverse(idateadmEntry.get())
                        datereverse1(idatedisEntry.get())
                        row3=[n13,n8,date,date1,n15]
                        sql="INSERT INTO patient_in_info VALUES(%s,%s,%s,%s,%s)"
                        mycursor.execute(sql,row3)
                        mydb.commit()

                        row4=[n12,idEntry.get(),doctoridEntry.get(),n11,n10,totalcost1]
                        sql="INSERT INTO billing_info VALUES(%s,%s,%s,%s,%s,%s)"
                        mycursor.execute(sql,row4)
                        mydb.commit()

                        row5=[outidEntry.get(),n1,n13,n12,n14,totalcost1]
                        sql="INSERT INTO patient_out_info VALUES(%s,%s,%s,%s,%s,%s)"
                        mycursor.execute(sql,row5)
                        mydb.commit()
                        nameEntry.delete(0,END)
                        lastnameEntry.delete(0,END)
                        ageEntry.delete(0,END)
                        idEntry.delete(0,END)
                        doctoridEntry.delete(0,END)
                        dayEntry.delete(0,END)
                        diseaseEntry.delete(0,END)
                        dnameEntry.delete(0,END)
                        dlastnameEntry.delete(0,END)
                        dageEntry.delete(0,END)
                        dspecialityEntry.delete(0,END)
                        roomnoEntry.delete(0,END)
                        roomtypeEntry.delete(0,END)
                        costEntry.delete(0,END)
                        idateadmEntry.delete(0,END)
                        idatedisEntry.delete(0,END)
                        nodaysadEntry.delete(0,END)
                        billnoEntry.delete(0,END)
                        surgerynoEntry.delete(0,END)
                        outidEntry.delete(0,END)
                        alEntry.delete(0,END)
                        PhoneEntry.delete(0,END)
                        Label(master,text="                                         ",bg="light sky blue").grid(row=6,column=7)
                        Label(master,text="                                         ",bg="light sky blue").grid(row=7,column=7)
                        Label(master,text="                                         ",bg="light sky blue").grid(row=15,column=7)
                        Label(master,text="                                         ",bg="light sky blue").grid(row=16,column=7)
                        
                def remove():
                    master.destroy()
                        
                master =Toplevel()
                master.geometry("2500x1000")
                master.title("Data Entry")
                master.configure(bg="light sky blue")
                Label(master,text="Patient's Info :",fg="green4",font="Times",bg="light sky blue").grid(row=0,column=0)
                Label(master,text="Patient's First Name",bg="light sky blue").grid(row=1,column=0)
                Label(master,text="Patient's Last Name",bg="light sky blue").grid(row=2,column=0)
                Label(master,text="Patient's Age",bg="light sky blue").grid(row=3,column=0)
                Label(master,text="Patient's ID",bg="light sky blue").grid(row=4,column=0)
                Label(master,text="Doctor's ID",bg="light sky blue").grid(row=5,column=0)
                Label(master,text="Date of birth of the patient :",bg="light sky blue").grid(row=6,column=0,pady=10)
                Label(master,text="DD-MM-YYYY",bg="light sky blue").grid(row=6,column=1,pady=10)
                Label(master,text="Disease suffering/Injury",bg="light sky blue").grid(row=9,column=0,pady=10)
                Label(master,text="Doctor's Info :",fg="green4",font="Times",bg="light sky blue").grid(row=11,column=0)
                Label(master,text="Doctor's First Name",bg="light sky blue").grid(row=12,column=0)
                Label(master,text="Doctor's Last Name",bg="light sky blue").grid(row=13,column=0)
                Label(master,text="Doctor's Age",bg="light sky blue").grid(row=14,column=0)
                Label(master,text="Doctor's ID",bg="light sky blue").grid(row=15,column=0)
                Label(master,text="Speciality of the Doctor in",bg="light sky blue").grid(row=16,column=0)
                Label(master,text="Patient's Room Info :",fg="green4",font="Times",bg="light sky blue").grid(row=0,column=4,padx=42)
                Label(master,text="Room number",bg="light sky blue").grid(row=1,column=4)
                Label(master,text="Patient ID",bg="light sky blue").grid(row=2,column=4)
                Label(master,text="Type of Room",bg="light sky blue").grid(row=3,column=4)
                Label(master,text="Cost per Day",bg="light sky blue").grid(row=4,column=4)
                Label(master,text="Patient_In Info :",fg="green4",font="Times",bg="light sky blue").grid(row=6,column=4)
                Label(master,text="Surgery No",bg="light sky blue").grid(row=7,column=4)
                Label(master,text="Room No",bg="light sky blue").grid(row=8,column=4)
                Label(master,text="Date Admitted in Hospital :",bg="light sky blue").grid(row=9,column=4)
                Label(master,text="DD-MM-YYYY",bg="light sky blue").grid(row=9,column=5)
                Label(master,text="Date Discharged from Hospital :",bg="light sky blue").grid(row=11,column=4)
                Label(master,text="DD-MM-YYYY",bg="light sky blue").grid(row=11,column=5)
                Label(master,text="Phone Number",bg="light sky blue").grid(row=13,column=4)
                Label(master,text="Billing Info :",fg="green4",font="Times",padx=90,bg="light sky blue").grid(row=0,column=6)
                Label(master,text="Bill No",bg="light sky blue").grid(row=1,column=6)
                Label(master,text="Patient's ID",bg="light sky blue").grid(row=2,column=6)
                Label(master,text="Doctor's ID",bg="light sky blue").grid(row=3,column=6)
                Label(master,text="No of days Admitted",bg="light sky blue").grid(row=4,column=6)
                Label(master,text="Cost Per Day",bg="light sky blue").grid(row=5,column=6)
                Label(master,text="Total Cost",fg="navy",bg="light sky blue").grid(row=6,column=6)
                Label(master,text="Patient_Out Info :",fg="green4",font="Times",bg="light sky blue").grid(row=9,column=6)
                Label(master,text="Patient's Out  ID",bg="light sky blue").grid(row=10,column=6,pady=5)
                Label(master,text="Patient's First Name",bg="light sky blue").grid(row=11,column=6,pady=5)
                Label(master,text="Surgery No",bg="light sky blue").grid(row=12,column=6,pady=5)
                Label(master,text="Bill No",bg="light sky blue").grid(row=13,column=6,pady=5)
                Label(master,text="Dead/Alive",bg="light sky blue").grid(row=14,column=6,pady=5)
                Label(master,text="Total Cost",fg="navy",bg="light sky blue").grid(row=15,column=6,pady=5)

                nameValue=StringVar()#PATIENT'S INFO
                lastnameValue=StringVar()
                ageValue=StringVar()
                idValue=StringVar()
                doctoridValue=StringVar()
                dayValue=StringVar()
                diseaseValue=StringVar
                nameEntry=Entry(master,textvariable=nameValue,relief="solid")
                ageEntry=Entry(master,textvariable=ageValue,relief="solid")
                idEntry=Entry(master,textvariable=idValue,relief="solid")
                lastnameEntry=Entry(master,textvariable=lastnameValue,relief="solid")
                doctoridEntry=Entry(master,textvariable=doctoridValue,relief="solid")
                dayEntry=Entry(master,textvariable=dayValue,relief="solid")
                diseaseEntry=Entry(master,textvariable=diseaseValue,relief="solid")
                nameEntry.grid(row=1,column=1,pady=10)
                lastnameEntry.grid(row=2,column=1,pady=10)
                ageEntry.grid(row=3,column=1,pady=10)
                idEntry.grid(row=4,column=1,pady=10)
                doctoridEntry.grid(row=5,column=1,pady=10)
                dayEntry.grid(row=7,column=1,pady=10)
                diseaseEntry.grid(row=9,column=1,pady=10)
                var=IntVar()
                Label(master,text="Patient's gender :",bg="light sky blue").grid(row=8,column=0,pady=10)
                r1=Radiobutton(master,text="Male",variable=var,value=1,bg="light sky blue")
                r1.grid(row=8,column=1,pady=0)
                r2=Radiobutton(master,text="Female",variable=var,value=2,bg="light sky blue")
                r2.grid(row=8,column=2,pady=0)
                r3=Radiobutton(master,text="Others",variable=var,value=3,bg="light sky blue")
                r3.grid(row=8,column=3,padx=35,pady=0)


                dnameValue=StringVar()#DOCTOR'S INFO
                dlastnameValue=StringVar()
                dageValue=StringVar()
                didValue=StringVar()
                dspecialityValue=StringVar()
                dnameEntry=Entry(master,textvariable=dnameValue,relief="solid")
                dlastnameEntry=Entry(master,textvariable=dlastnameValue,relief="solid")
                dageEntry=Entry(master,textvariable=dageValue,relief="solid")
                didEntry=Entry(master,textvariable=doctoridValue,relief="solid")
                dspecialityEntry=Entry(master,textvariable=dspecialityValue,relief="solid")
                dnameEntry.grid(row=12,column=1,pady=10)
                dlastnameEntry.grid(row=13,column=1,pady=10)
                dageEntry.grid(row=14,column=1,pady=10)
                didEntry.grid(row=15,column=1,pady=10)
                dspecialityEntry.grid(row=16,column=1,pady=10)

                roomnoValue=StringVar()#Room's Data
                roomtypeValue=StringVar()
                costValue=StringVar()
                roomnoEntry=Entry(master,textvariable=roomnoValue,relief="solid")
                pidEntry=Entry(master,textvariable=idValue,relief="solid")
                roomtypeEntry=Entry(master,textvariable=roomtypeValue,relief="solid")
                costEntry=Entry(master,textvariable=costValue,relief="solid")
                roomnoEntry.grid(row=1,column=5,pady=10)
                pidEntry.grid(row=2,column=5,pady=10)
                roomtypeEntry.grid(row=3,column=5,pady=10)
                costEntry.grid(row=4,column=5,pady=10)

                surgerynoValue=StringVar()#PATIENT_IN INFO
                idateadmValue=StringVar()
                idatedisValue=StringVar()
                PhoneValue=StringVar()
                surgerynoEntry=Entry(master,textvariable=surgerynoValue,relief="solid")
                iroomnoEntry=Entry(master,textvariable=roomnoValue,relief="solid")
                idateadmEntry=Entry(master,textvariable=idateadmValue,relief="solid")
                idatedisEntry=Entry(master,textvariable=idatedisValue,relief="solid")
                PhoneEntry=Entry(master,textvariable=PhoneValue,relief="solid")
                surgerynoEntry.grid(row=7,column=5)
                iroomnoEntry.grid(row=8,column=5)
                idateadmEntry.grid(row=10,column=5,pady=10)
                idatedisEntry.grid(row=12,column=5)
                PhoneEntry.grid(row=13,column=5,pady=10)

                billnoValue=StringVar()#BILL INFO
                patidValue=StringVar()
                docidValue=StringVar()
                nodaysadValue=StringVar()
                costperdayValue=StringVar()
                billnoEntry=Entry(master,textvariable=billnoValue,relief="solid")
                patidEntry=Entry(master,textvariable=idValue,relief="solid")
                docidEntry=Entry(master,textvariable=doctoridValue,relief="solid")
                nodaysadEntry=Entry(master,textvariable=nodaysadValue,relief="solid")
                costperdayEntry=Entry(master,textvariable=costValue,relief="solid")
                billnoEntry.grid(row=1,column=7)
                patidEntry.grid(row=2,column=7)
                docidEntry.grid(row=3,column=7)
                nodaysadEntry.grid(row=4,column=7)
                costperdayEntry.grid(row=5,column=7)

                outidValue=StringVar()#PAIENT_OUT INFO
                alValue=StringVar()
                outidEntry=Entry(master,textvariable=outidValue,relief="solid")
                pfnEntry=Entry(master,textvariable=nameValue,relief="solid")
                SEntry=Entry(master,textvariable=surgerynoValue,relief="solid")
                billEntry=Entry(master,textvariable=billnoValue,relief="solid")
                alEntry=Entry(master,textvariable=alValue,relief="solid")
                outidEntry.grid(row=10,column=7)
                pfnEntry.grid(row=11,column=7)
                SEntry.grid(row=12,column=7)
                billEntry.grid(row=13,column=7)
                alEntry.grid(row=14,column=7)
                Button(master,text="Calculate Total Cost",command=cd,fg="white",bg="green").grid(row=7,column=6)
                Button(master,text="Submit",command=avsg,bg="blue",fg="white").grid(row=15,column=4)   
                Button(master,text="To Quit adding data",command=remove,fg="white",bg="red").grid(row=16,column=4)
                    
                    
            def choice3():#to delete data from the database
                def deletion():
                    q=RoomnoEntry.get()
                    if q.isdigit()==False:
                        tkinter.messagebox.showerror("Error","There must be numeric values only in Room No column")
                        sys.exit()
                    else:
                        n1=int(q)
                    t=SurgeryNoEntry.get()
                    if t.isdigit()==False:
                        tkinter.messagebox.showerror("Error","There must be numeric values only in Surgery No column")
                        sys.exit()
                    else:
                        n2=int(t)
                    w=BillnoEntry.get()
                    if w.isdigit()==False:
                        tkinter.messagebox.showerror("Error","There must be numeric values only in Bill No column")
                        sys.exit()
                    else:
                        n3=int(w)
                    p=tkinter.messagebox.askquestion("Submission","Are you sure you want to Delete this data?") 
                    if p=="yes":

                        sql="DELETE FROM patient_out_info WHERE Patients_Out_ID = %s"
                        mycursor.execute(sql,(PatientoutIDEntry.get(),))
                        mydb.commit()

                        sql="DELETE FROM billing_info WHERE Bill_Number = %s"
                        mycursor.execute(sql,(n3,))
                        mydb.commit()

                        sql="DELETE FROM patient_in_info WHERE Surgery_Number = %s"
                        mycursor.execute(sql,(n2,))
                        mydb.commit()

                        sql="DELETE FROM patients_room_info WHERE Room_Number = %s"
                        mycursor.execute(sql,(n1,))
                        mydb.commit()

                        sql="DELETE FROM doctor WHERE Doctors_ID = %s"
                        mycursor.execute(sql,(DoctorIDEntry.get(),))
                        mydb.commit()

                        sql="DELETE FROM patient WHERE Patients_ID = %s"
                        mycursor.execute(sql,(PatientIDEntry.get(),))
                        mydb.commit()
                        delete.destroy()

                delete=Toplevel()
                delete.title("Deletion of Data")
                delete.geometry("250x320")
                delete.configure(bg="light sky blue")
                Label(delete,text="Fill out the following:",fg="navy",bg="light sky blue").grid(row=0,column=0)
                Label(delete,text="Patient ID :",bg="light sky blue").grid(row=1,column=0,pady=10)
                Label(delete,text="Doctor ID :",bg="light sky blue").grid(row=2,column=0,pady=10)
                Label(delete,text="Room No :",bg="light sky blue").grid(row=3,column=0,pady=10)
                Label(delete,text="Surgery No :",bg="light sky blue").grid(row=4,column=0,pady=10)
                Label(delete,text="Bill No :",bg="light sky blue").grid(row=5,column=0,pady=10)
                Label(delete,text="Patient Out ID:",bg="light sky blue").grid(row=6,column=0,pady=10)
                PatientIDValue=StringVar()
                DoctorIDValue=StringVar()
                RoomnoValue=StringVar()
                SurgeryNoValue=StringVar()
                BillnoValue=StringVar()
                PatientoutIDvalue=StringVar()
                PatientIDEntry=Entry(delete,textvariable=PatientIDValue,relief="solid")
                DoctorIDEntry=Entry(delete,textvariable=DoctorIDValue,relief="solid")
                RoomnoEntry=Entry(delete,textvariable=RoomnoValue,relief="solid")
                SurgeryNoEntry=Entry(delete,textvariable=SurgeryNoValue,relief="solid")
                BillnoEntry=Entry(delete,textvariable=BillnoValue,relief="solid")
                PatientoutIDEntry=Entry(delete,textvariable=PatientoutIDvalue,relief="solid")
                PatientIDEntry.grid(row=1,column=1)
                DoctorIDEntry.grid(row=2,column=1)
                RoomnoEntry.grid(row=3,column=1)
                SurgeryNoEntry.grid(row=4,column=1)
                BillnoEntry.grid(row=5,column=1)
                PatientoutIDEntry.grid(row=6,column=1)
                Button(delete,text="Delete",command=deletion,fg="white",bg="blue").grid(row=7,column=1)

                
            def choice4():#To update data in the database
                def patientinfo():
                    def update1():
                        def change():
                            t=PatientIDEntry.get()
                            k=FirstcEntry.get()
                            if t=="":
                                tkinter.messagebox.showerror("Error","Patient ID column is empty!!")
                                sys.exit()
                            else:
                                n1=t
                            if k.isalpha()==False:
                                tkinter.messagebox.showerror("Error","There must be alphabets only in Changed First name of the patient column or it is empty!!")
                                sys.exit()
                            else:
                                n2=k.lower()
                            p=tkinter.messagebox.askquestion("Submission","Are you sure you want to Update this data?")
                            if p=="yes":
                                sql="SELECT Patients_First_Name FROM patient WHERE Patients_ID = %s"
                                mycursor.execute(sql,(n1,))
                                record=mycursor.fetchall()
                                n3=record[0][0]

                                sql="UPDATE patient SET Patients_First_Name = %s where Patients_ID = %s"
                                mycursor.execute(sql,(n2,n1))
                                mydb.commit()

                                sql="UPDATE patient_out_info SET Patients_First_Name = %s where Patients_First_Name = %s"
                                mycursor.execute(sql,(n2,n3))
                                mydb.commit()
                                up.destroy()
      
                        up=Toplevel()
                        up.configure(bg="light sky blue")
                        Label(up,text="Fill these below",font="Times",fg="navy",bg="light sky blue").grid(row=0,column=0)
                        Label(up,text="Patient ID of the patient :",font="Times",bg="light sky blue").grid(row=1,column=0)
                        Label(up,text="Changed First name of the patient :",font="Times",bg="light sky blue").grid(row=2,column=0)
                        PatientID=StringVar()
                        PatientIDEntry=Entry(up,textvariable=PatientID,relief="solid")
                        PatientIDEntry.grid(row=1,column=1)
                        Firstnamec=StringVar()
                        FirstcEntry=Entry(up,textvariable=Firstnamec,relief="solid")
                        FirstcEntry.grid(row=2,column=1)
                        Button(up,text="Change",command=change,bg="navy",fg="cyan").grid(row=3,column=1)
                        choose.destroy()

                    def update2():
                        def change():
                            t=PatientIDEntry.get()
                            k=LastcEntry.get()
                            if t=="":
                                tkinter.messagebox.showerror("Error","Patient ID column is empty!!")
                                sys.exit()
                            else:
                                n1=t
                            if k.isalpha()==False:
                                tkinter.messagebox.showerror("Error","There must be alphabets only in Changed Last name of the patient column or it is empty!!")
                                sys.exit()
                            else:
                                n2=k.lower()
                            p=tkinter.messagebox.askquestion("Submission","Are you sure you want to Update this data?")
                            if p=="yes":
                                sql="UPDATE patient SET Patients_Last_Name = %s where Patients_ID = %s"
                                mycursor.execute(sql,(n2,n1))
                                mydb.commit()
                                up.destroy()
                            
                        up=Toplevel()
                        up.configure(bg="light sky blue")
                        Label(up,text="Fill these below",font="Times",fg="navy",bg="light sky blue").grid(row=0,column=0)
                        Label(up,text="Patient ID of the Patient :",font="Times",bg="light sky blue").grid(row=1,column=0)
                        Label(up,text="Changed Last name of the patient :",font="Times",bg="light sky blue").grid(row=2,column=0)
                        PatientID=StringVar()
                        PatientIDEntry=Entry(up,textvariable=PatientID,relief="solid")
                        PatientIDEntry.grid(row=1,column=1)
                        Lastnamec=StringVar()
                        LastcEntry=Entry(up,textvariable=Lastnamec,relief="solid")
                        LastcEntry.grid(row=2,column=1)
                        Button(up,text="Change",command=change,bg="navy",fg="cyan").grid(row=3,column=1)
                        choose.destroy()
                        
                    def update3():
                        def change():
                            t=PatientIDEntry.get()
                            k=AgeEntry.get()
                            if t=="":
                                tkinter.messagebox.showerror("Error","Patient ID of the patient column is empty!!")
                                sys.exit()
                            else:
                                n1=t
                            if k.isdigit()==False:
                                tkinter.messagebox.showerror("Error","There must be numeric values only in Changed Age of the patient column or it is empty!!")
                                sys.exit()
                            else:
                                n2=k
                            p=tkinter.messagebox.askquestion("Submission","Are you sure you want to Update this data?")
                            if p=="yes":
                                sql="UPDATE patient SET Patients_Age = %s where Patients_ID = %s"
                                mycursor.execute(sql,(n2,n1))
                                mydb.commit()
                                up.destroy()
                            
                        up=Toplevel()
                        up.configure(bg="light sky blue")
                        Label(up,text="Fill these below",font="Times",fg="navy",bg="light sky blue").grid(row=0,column=0)
                        Label(up,text="Patient ID of the patient :",font="Times",bg="light sky blue").grid(row=1,column=0)
                        Label(up,text="Changed Age of the patient :",font="Times",bg="light sky blue").grid(row=2,column=0)
                        PatientID=StringVar()
                        PatientIDEntry=Entry(up,textvariable=PatientID,relief="solid")
                        PatientIDEntry.grid(row=1,column=1)
                        Age=StringVar()
                        AgeEntry=Entry(up,textvariable=Age,relief="solid")
                        AgeEntry.grid(row=2,column=1)
                        Button(up,text="Change",command=change,bg="navy",fg="cyan").grid(row=3,column=1)
                        choose.destroy()

                    def update4():
                        def change():
                            t=PatientIDEntry.get()
                            k=PatientIDcEntry.get()
                            if t=="":
                                tkinter.messagebox.showerror("Error","Patient ID of the patient column is empty!!")
                                sys.exit()
                            else:
                                n1=t
                            if k=="":
                                tkinter.messagebox.showerror("Error","Changed Patient ID column is empty!!")
                                sys.exit()
                            else:
                                n2=k
                            p=tkinter.messagebox.askquestion("Submission","Are you sure you want to Update this data?")
                            if p=="yes":
                                sql="UPDATE patient SET Patients_ID = %s where Patients_ID = %s"
                                mycursor.execute(sql,(n2,n1))
                                mydb.commit()
                                up.destroy()
                            
                        up=Toplevel()
                        up.configure(bg="light sky blue")
                        Label(up,text="Fill these below",font="Times",fg="navy",bg="light sky blue").grid(row=0,column=0)
                        Label(up,text="Patient ID of the patient :",font="Times",bg="light sky blue").grid(row=1,column=0)
                        Label(up,text="Changed Patient ID :",font="Times",bg="light sky blue").grid(row=2,column=0)
                        PatientID=StringVar()
                        PatientIDEntry=Entry(up,textvariable=PatientID,relief="solid")
                        PatientIDEntry.grid(row=1,column=1)
                        PatientIDc=StringVar()
                        PatientIDcEntry=Entry(up,textvariable=PatientIDc,relief="solid")
                        PatientIDcEntry.grid(row=2,column=1)
                        Button(up,text="Change",command=change,bg="navy",fg="cyan").grid(row=3,column=1)
                        choose.destroy()
                        
                    def update5():
                        def change():
                            t=PatientIDEntry.get()
                            k=DOBEntry.get()
                            if t=="":
                                tkinter.messagebox.showerror("Error","Patient ID of the patient coulmn is empty!!")
                                sys.exit()
                            else:
                                n1=t
                            if k=="":
                                tkinter.messagebox.showerror("Error","Changed Date of birth column is empty!!")
                                sys.exit()
                            else:
                                datereverse(k)
                            p=tkinter.messagebox.askquestion("Submission","Are you sure you want to Update this data?")
                            if p=="yes":
                                sql="UPDATE patient SET Date_Of_Birth = %s where Patients_ID = %s"
                                mycursor.execute(sql,(date,n1))
                                mydb.commit()
                                up.destroy()
                        
                        up=Toplevel()
                        up.configure(bg="light sky blue")
                        Label(up,text="Fill these below",font="Times",fg="navy",bg="light sky blue").grid(row=0,column=0)
                        Label(up,text="Patient ID of the patient :",font="Times",bg="light sky blue").grid(row=1,column=0)
                        Label(up,text="Changed Patient's date of birth:",font="Times",bg="light sky blue").grid(row=2,column=0)
                        Label(up,text="DD-MM-YYYY",bg="light sky blue").grid(row=2,column=1)
                        PatientID=StringVar()
                        PatientIDEntry=Entry(up,textvariable=PatientID,relief="solid")
                        PatientIDEntry.grid(row=1,column=1)
                        DOB=StringVar()
                        DOBEntry=Entry(up,textvariable=DOB,relief="solid")
                        DOBEntry.grid(row=3,column=1)
                        Button(up,text="Change",command=change,bg="navy",fg="cyan").grid(row=4,column=1)
                        choose.destroy()
                        
                    def update6():
                        def change():
                            t=PatientIDEntry.get()
                            k=GenderEntry.get()
                            if t=="":
                                tkinter.messagebox.showerror("Error","Patient ID column is empty!!")
                                sys.exit()
                            else:
                                n1=t
                            if k.lower()=="male" or k.lower()=="female" or k.lower()=="others":
                                n2=k.lower()
                            else:
                                tkinter.messagebox.showerror("Error","Invalid input in Gender column!!")
                                sys.exit()
                            p=tkinter.messagebox.askquestion("Submission","Are you sure you want to Update this data?")
                            if p=="yes":
                                sql="UPDATE patient SET Gender = %s where Patients_ID = %s"
                                mycursor.execute(sql,(n2,n1))
                                mydb.commit()
                                up.destroy()
                            
                        up=Toplevel()
                        up.configure(bg="light sky blue")
                        Label(up,text="Fill these below",font="Times",fg="navy",bg="light sky blue").grid(row=0,column=0)
                        Label(up,text="Patient ID of the Patient :",font="Times",bg="light sky blue").grid(row=1,column=0)
                        Label(up,text="Changed Gender of the patient :",font="Times",bg="light sky blue").grid(row=2,column=0)
                        PatientID=StringVar()
                        PatientIDEntry=Entry(up,textvariable=PatientID,relief="solid")
                        PatientIDEntry.grid(row=1,column=1)
                        Gender=StringVar()
                        GenderEntry=Entry(up,textvariable=Gender,relief="solid")
                        GenderEntry.grid(row=2,column=1)
                        Button(up,text="Change",command=change,bg="navy",fg="cyan").grid(row=3,column=1)
                        choose.destroy()
                        
                    def update7():
                        def change():
                            t=PatientIDEntry.get()
                            k=DiseaseEntry.get()
                            if t=="":
                                tkinter.messagebox.showerror("Error","Patient ID column is empty!!")
                                sys.exit()
                            else:
                                n1=t
                            if k.isalpha()==False:
                                tkinter.messagebox.showerror("Error","There must be alphabets only in Changed Disease/Injury of the patient column or it is empty!!")
                                sys.exit()
                            else:
                                n2=k.lower()
                            p=tkinter.messagebox.askquestion("Submission","Are you sure you want to Update this data?")
                            if p=="yes":
                                sql="UPDATE patient SET Disease_Or_Injury = %s where Patients_ID = %s"
                                mycursor.execute(sql,(n2,n1))
                                mydb.commit()
                                up.destroy()
                            
                        up=Toplevel()
                        up.configure(bg="light sky blue")
                        Label(up,text="Fill these below : ",font="Times",fg="navy",bg="light sky blue").grid(row=0,column=0)
                        Label(up,text="Patient ID of the Patient :",font="Times",bg="light sky blue").grid(row=1,column=0)
                        Label(up,text="Changed Disease/Injury of the patient :",font="Times",bg="light sky blue").grid(row=2,column=0)
                        PatientID=StringVar()
                        PatientIDEntry=Entry(up,textvariable=PatientID,relief="solid")
                        PatientIDEntry.grid(row=1,column=1)
                        Disease=StringVar()
                        DiseaseEntry=Entry(up,textvariable=Disease,relief="solid")
                        DiseaseEntry.grid(row=2,column=1)
                        Button(up,text="Change",command=change,bg="navy",fg="cyan").grid(row=3,column=1)
                        choose.destroy()
                        
                    choose=Tk()
                    choose.configure(bg="light sky blue")
                    Label(choose,text="Choose from the option below to be updated :",font="Times",fg="navy",bg="light sky blue").grid(row=0,column=0)
                    Button(choose,text="Patient's First Name",command=update1,font="times",bg="navy",fg="cyan",width=15).grid(row=1,column=0)
                    Button(choose,text="Patient's Last Name",command=update2,font="times",bg="navy",fg="cyan",width=15).grid(row=2,column=0)
                    Button(choose,text="Patient's Age",command=update3,font="times",bg="navy",fg="cyan",width=15).grid(row=3,column=0)
                    Button(choose,text="Patient ID",command=update4,font="times",bg="navy",fg="cyan",width=15).grid(row=4,column=0)
                    Button(choose,text="Patient's Date of Birth",command=update5,font="times",bg="navy",fg="cyan",width=15).grid(row=5,column=0)
                    Button(choose,text="Patient's Gender",command=update6,font="times",bg="navy",fg="cyan",width=15).grid(row=6,column=0)
                    Button(choose,text="Disease/Injury",command=update7,font="times",bg="navy",fg="cyan",width=15).grid(row=7,column=0)
                    
                def doctorinfo():
                    def update1():
                        def change():
                            t=DoctorIDEntry.get()
                            k=FirstcEntry.get()
                            if t=="":
                                tkinter.messagebox.showerror("Error","Doctor ID column is empty!!")
                                sys.exit()
                            else:
                                n1=t
                            if k.isalpha()==False:
                                tkinter.messagebox.showerror("Error","There must be alphabets only in Changed First name of the doctor column or it is empty!!")
                                sys.exit()
                            else:
                                n2=k.lower()
                            p=tkinter.messagebox.askquestion("Submission","Are you sure you want to Update this data?")
                            if p=="yes":
                                sql="UPDATE doctor SET Doctors_First_Name = %s where Doctors_ID = %s"
                                mycursor.execute(sql,(n2,n1))
                                mydb.commit()
                                up.destroy()
      
                        up=Toplevel()
                        up.configure(bg="light sky blue")
                        Label(up,text="Fill these below",font="Times",fg="navy",bg="light sky blue").grid(row=0,column=0)
                        Label(up,text="Doctor's ID of the Doctor :",font="Times",bg="light sky blue").grid(row=1,column=0)
                        Label(up,text="Changed First name of the patient :",font="Times",bg="light sky blue").grid(row=2,column=0)
                        DoctorID=StringVar()
                        DoctorIDEntry=Entry(up,textvariable=DoctorID,relief="solid")
                        DoctorIDEntry.grid(row=1,column=1)
                        Firstnamec=StringVar()
                        FirstcEntry=Entry(up,textvariable=Firstnamec,relief="solid")
                        FirstcEntry.grid(row=2,column=1)
                        Button(up,text="Change",command=change,bg="navy",fg="cyan").grid(row=3,column=1)
                        choose.destroy()
                        
                    def update2():
                        def change():
                            t=DoctorIDEntry.get()
                            k=LastcEntry.get()
                            if t=="":
                                tkinter.messagebox.showerror("Error","Doctor ID column is empty!!")
                                sys.exit()
                            else:
                                n1=t
                            if k.isalpha()==False:
                                tkinter.messagebox.showerror("Error","There must be alphabets only in Changed Last name of the doctor column or it is empty!!")
                                sys.exit()
                            else:
                                n2=k.lower()
                            p=tkinter.messagebox.askquestion("Submission","Are you sure you want to Update this data?")
                            if p=="yes":
                                sql="UPDATE doctor SET Doctors_Last_Name = %s where Doctors_ID = %s"
                                mycursor.execute(sql,(n2,n1))
                                mydb.commit()
                                up.destroy()
      
                        up=Toplevel()
                        up.configure(bg="light sky blue")
                        Label(up,text="Fill these below",font="Times",fg="navy",bg="light sky blue").grid(row=0,column=0)
                        Label(up,text="Doctor's ID of the Doctor :",font="Times",bg="light sky blue").grid(row=1,column=0)
                        Label(up,text="Changed Last name of the patient :",font="Times",bg="light sky blue").grid(row=2,column=0)
                        DoctorID=StringVar()
                        DoctorIDEntry=Entry(up,textvariable=DoctorID,relief="solid")
                        DoctorIDEntry.grid(row=1,column=1)
                        Lastnamec=StringVar()
                        LastcEntry=Entry(up,textvariable=Lastnamec,relief="solid")
                        LastcEntry.grid(row=2,column=1)
                        Button(up,text="Change",command=change,bg="navy",fg="cyan").grid(row=3,column=1)
                        choose.destroy()

                    def update3():
                        def change():
                            t=DoctorIDEntry.get()
                            k=AgeEntry.get()
                            if t=="":
                                tkinter.messagebox.showerror("Error","Doctor ID of the patient column is empty!!")
                                sys.exit()
                            else:
                                n1=t
                            if k.isdigit()==False:
                                tkinter.messagebox.showerror("Error","There must be numeric vaues only in Changed Age of the Doctor column or it is empty!!")
                                sys.exit()
                            else:
                                n2=k
                            p=tkinter.messagebox.askquestion("Submission","Are you sure you want to Update this data?")
                            if p=="yes":
                                sql="UPDATE doctor SET Doctors_Age = %s where Doctors_ID = %s"
                                mycursor.execute(sql,(n2,n1))
                                mydb.commit()
                                up.destroy()
                            
                        up=Toplevel()
                        up.configure(bg="light sky blue")
                        Label(up,text="Fill these below",font="Times",fg="navy",bg="light sky blue").grid(row=0,column=0)
                        Label(up,text="Patient ID of the doctor :",font="Times",bg="light sky blue").grid(row=1,column=0)
                        Label(up,text="Changed Age of the doctor :",font="Times",bg="light sky blue").grid(row=2,column=0)
                        DoctorID=StringVar()
                        DoctorIDEntry=Entry(up,textvariable=DoctorID,relief="solid")
                        DoctorIDEntry.grid(row=1,column=1)
                        Age=StringVar()
                        AgeEntry=Entry(up,textvariable=Age,relief="solid")
                        AgeEntry.grid(row=2,column=1)
                        Button(up,text="Change",command=change,bg="navy",fg="cyan").grid(row=3,column=1)
                        choose.destroy()

                    def update4():
                        def change():
                            t=DoctorIDEntry.get()
                            k=DoctorIDcEntry.get()
                            if t=="":
                                tkinter.messagebox.showerror("Error","Doctor ID of the patient column is empty!!")
                                sys.exit()
                            else:
                                n1=t
                            if k=="":
                                tkinter.messagebox.showerror("Error","Changed Doctor ID column is empty!!")
                                sys.exit()
                            else:
                                n2=k
                            p=tkinter.messagebox.askquestion("Submission","Are you sure you want to Update this data?")
                            if p=="yes":
                                sql="UPDATE doctor SET Doctors_ID = %s where Doctors_ID = %s"
                                mycursor.execute(sql,(n2,n1))
                                mydb.commit()
                                up.destroy()
                            
                        up=Toplevel()
                        up.configure(bg="light sky blue")
                        Label(up,text="Fill these below",font="Times",fg="navy",bg="light sky blue").grid(row=0,column=0)
                        Label(up,text="Doctor ID of the doctor :",font="Times",bg="light sky blue").grid(row=1,column=0)
                        Label(up,text="Changed Doctor ID :",font="Times",bg="light sky blue").grid(row=2,column=0)
                        DoctorID=StringVar()
                        DoctorIDEntry=Entry(up,textvariable=DoctorID,relief="solid")
                        DoctorIDEntry.grid(row=1,column=1)
                        DoctorIDc=StringVar()
                        DoctorIDcEntry=Entry(up,textvariable=DoctorIDc,relief="solid")
                        DoctorIDcEntry.grid(row=2,column=1)
                        Button(up,text="Change",command=change,bg="navy",fg="cyan").grid(row=3,column=1)
                        choose.destroy()

                    def update5():
                        def change():
                            t=DoctorIDEntry.get()
                            k=SpecialityEntry.get()
                            if t=="":
                                tkinter.messagebox.showerror("Error","Doctor ID of the patient column is empty!!")
                                sys.exit()
                            else:
                                n1=t
                            if k.isalpha()==False:
                                tkinter.messagebox.showerror("Error","Changed Speciality of doctor must have alphabets only or column is empty!!")
                                sys.exit()
                            else:
                                n2=k.lower()
                            p=tkinter.messagebox.askquestion("Submission","Are you sure you want to Update this data?")
                            if p=="yes":
                                sql="UPDATE doctor SET Speciality = %s where Doctors_ID = %s"
                                mycursor.execute(sql,(n2,n1))
                                mydb.commit()
                                up.destroy()
                                
                        up=Toplevel()
                        up.configure(bg="light sky blue")
                        Label(up,text="Fill these below",font="Times",fg="navy",bg="light sky blue").grid(row=0,column=0)
                        Label(up,text="Doctor ID of the doctor :",font="Times",bg="light sky blue").grid(row=1,column=0)
                        Label(up,text="Changed Speciality of doctor :",font="Times",bg="light sky blue").grid(row=2,column=0)
                        DoctorID=StringVar()
                        DoctorIDEntry=Entry(up,textvariable=DoctorID,relief="solid")
                        DoctorIDEntry.grid(row=1,column=1)
                        Speciality=StringVar()
                        SpecialityEntry=Entry(up,textvariable=Speciality,relief ="solid")
                        SpecialityEntry.grid(row=2,column=1)
                        Button(up,text="Change",command=change,bg="navy",fg="cyan").grid(row=3,column=1)
                        choose.destroy()
                        
                    choose=Tk()
                    choose.configure(bg="light sky blue")
                    Label(choose,text="Choose from the option below to be updated :",font="Times",fg="navy",bg="light sky blue").grid(row=0,column=0)
                    Button(choose,text="Doctor's First Name",command=update1,font="times",bg="navy",fg="cyan",width=15).grid(row=1,column=0)
                    Button(choose,text="Doctor's Last Name",command=update2,font="times",bg="navy",fg="cyan",width=15).grid(row=2,column=0)
                    Button(choose,text="Doctor's Age",command=update3,font="times",bg="navy",fg="cyan",width=15).grid(row=3,column=0)
                    Button(choose,text="Doctor's ID",command=update4,font="times",bg="navy",fg="cyan",width=15).grid(row=4,column=0)
                    Button(choose,text="Speciality of doctor",command=update5,font="times",bg="navy",fg="cyan",width=15).grid(row=5,column=0)
                   
                def roominfo():
                    def update1():
                        def change():
                            t=RoomEntry.get()
                            k=RoomcEntry.get()
                            if t.isdigit()==False:
                                tkinter.messagebox.showerror("Error","Room Number should have numeric values only or it is empty")
                                sys.exit()
                            else:
                                n1=t
                            if k.isdigit()==False:
                                tkinter.messagebox.showerror("Error","Changed Room Number should have numeric values only or it is empty")
                                sys.exit()
                            else:
                                n2=k
                            p=tkinter.messagebox.askquestion("Submission","Are you sure you want to Update this data?")
                            if p=="yes":
                                sql="UPDATE patients_room_info SET Room_Number = %s where Room_Number = %s"
                                mycursor.execute(sql,(n2,n1))
                                mydb.commit()
                                up.destroy()
                            
                        up=Toplevel()
                        up.configure(bg="light sky blue")
                        Label(up,text="Fill these below",font="Times",fg="navy",bg="light sky blue").grid(row=0,column=0)
                        Label(up,text="Room Number of the patient :",font="Times",bg="light sky blue").grid(row=1,column=0)
                        Label(up,text="Changed Room number of patient :",font="Times",bg="light sky blue").grid(row=2,column=0)
                        Room=StringVar()
                        RoomEntry=Entry(up,textvariable=Room,relief="solid")
                        RoomEntry.grid(row=1,column=1)
                        Roomc=StringVar()
                        RoomcEntry=Entry(up,textvariable=Roomc,relief="solid")
                        RoomcEntry.grid(row=2,column=1)
                        Button(up,text="Change",command=change,bg="navy",fg="cyan").grid(row=3,column=1)
                        choose.destroy()

                    def update2():
                        def change():
                            t=RoomEntry.get()
                            k=TypeEntry.get()
                            if t.isdigit()==False:
                                tkinter.messagebox.showerror("Error","Room Number should have numeric values only or it is empty")
                                sys.exit()
                            else:
                                n1=t
                            if k.isalpha()==False:
                                tkinter.messagebox.showerror("Error","Changed Type of Room should have alphabets only or the column is empty")
                                sys.exit()
                            else:
                                n2=k.lower()
                            p=tkinter.messagebox.askquestion("Submission","Are you sure you want to Update this data?")
                            if p=="yes":
                                sql="UPDATE patients_room_info SET Type_Of_Room = %s where Room_Number = %s"
                                mycursor.execute(sql,(n2,n1))
                                mydb.commit()
                                up.destroy()
                                
                        up=Toplevel()
                        up.configure(bg="light sky blue")
                        Label(up,text="Fill these below",font="Times",fg="navy",bg="light sky blue").grid(row=0,column=0)
                        Label(up,text="Room Number of the patient :",font="Times",bg="light sky blue").grid(row=1,column=0)
                        Label(up,text="Changed Type of Room :",font="Times",bg="light sky blue").grid(row=2,column=0)
                        Room=StringVar()
                        RoomEntry=Entry(up,textvariable=Room,relief="solid")
                        RoomEntry.grid(row=1,column=1)
                        Type=StringVar()
                        TypeEntry=Entry(up,textvariable=Type,relief="solid")
                        TypeEntry.grid(row=2,column=1)
                        Button(up,text="Change",command=change,bg="navy",fg="cyan").grid(row=3,column=1)
                        choose.destroy()

                    def update3():
                        def change():
                            t=RoomEntry.get()
                            k=CostEntry.get()
                            if t.isdigit()==False:
                                tkinter.messagebox.showerror("Error","Room number should only have numeric values or it is empty")
                                sys.exit()
                            else:
                                n1=t
                            if k.isdigit()==False:
                                tkinter.messagebox.showerror("Error","Changed Cost of Room should only have numeric values or it is empty")
                                sys.exit()
                            else:
                                n2=k
                            p=tkinter.messagebox.askquestion("Submission","Are you sure you want to Update this data?")
                            if p=="yes":
                                sql="SELECT Patients_ID FROM patients_room_info WHERE Room_Number = %s"
                                mycursor.execute(sql,(n1,))
                                record=mycursor.fetchall()
                                n3=record[0][0]

                                sql="UPDATE patients_room_info SET Cost_Per_Day = %s where Room_Number = %s"
                                mycursor.execute(sql,(n2,n1))
                                mydb.commit()

                                sql="UPDATE billing_info SET Cost_Per_Day = %s where Patients_ID = %s"
                                mycursor.execute(sql,(n2,n3))
                                mydb.commit()

                                sql="SELECT Number_Days_Admitted FROM billing_info WHERE Patients_ID = %s"
                                mycursor.execute(sql,(n3,))
                                record1=mycursor.fetchall()
                                n4=int(record1[0][0])
                                n2=int(n2)
                                n5=(n2*n4)+0.05*(n2*n4)
                                n5=int(n5)

                                sql="UPDATE billing_info SET Total_Cost = %s where Patients_ID = %s"
                                mycursor.execute(sql,(n5,n3))
                                mydb.commit()
                                up.destroy()
                            
                        up=Toplevel()
                        up.configure(bg="light sky blue")
                        Label(up,text="Fill these below",font="Times",fg="navy",bg="light sky blue").grid(row=0,column=0)
                        Label(up,text="Room Number of the patient :",font="Times",bg="light sky blue").grid(row=1,column=0)
                        Label(up,text="Changed cost of Room :",font="Times",bg="light sky blue").grid(row=2,column=0)
                        Room=StringVar()
                        RoomEntry=Entry(up,textvariable=Room,relief="solid")
                        RoomEntry.grid(row=1,column=1)
                        Cost=StringVar()
                        CostEntry=Entry(up,textvariable=Cost,relief="solid")
                        CostEntry.grid(row=2,column=1)
                        Button(up,text="Change",command=change,bg="navy",fg="cyan").grid(row=3,column=1)
                        choose.destroy()
                        
                    choose=Tk()
                    choose.configure(bg="light sky blue")#
                    Label(choose,text="Choose from the option below to be updated :",font="Times",fg="navy",bg="light sky blue").grid(row=0,column=0)
                    Button(choose,text="Room Number",command=update1,font="times",bg="navy",fg="cyan",width=15).grid(row=1,column=0)
                    Button(choose,text="Type of room",command=update2,font="times",bg="navy",fg="cyan",width=15).grid(row=2,column=0)
                    Button(choose,text="Cost per day",command=update3,font="times",bg="navy",fg="cyan",width=15).grid(row=3,column=0)
                    
                def patientin():
                    def update1():
                        def change():
                            t=SurgeryEntry.get()
                            k=SurgerycEntry.get()
                            if t.isdigit()==False:
                                tkinter.messagebox.showerror("Error","Surgery number of the patient should only have numeric values or it is empty")
                                sys.exit()
                            else:
                                n1=t
                            if k.isdigit==False:
                                tkinter.messagebox.showerror("Error","Changed Surgery number of the patient should only have numeric values or it is empty")
                                sys.exit()
                            else:
                                n2=k
                            p=tkinter.messagebox.askquestion("Submission","Are you sure you want to Update this data?")
                            if p=="yes":
                                sql="UPDATE patient_in_info SET Surgery_Number = %s WHERE Surgery_Number = %s"
                                mycursor.execute(sql,(n2,n1))
                                mydb.commit()
                                up.destroy()
                            
                        up=Toplevel()
                        up.configure(bg="light sky blue")
                        Label(up,text="Fill these below :",font="Times",fg="navy",bg="light sky blue").grid(row=0,column=0)
                        Label(up,text="Surgery Number of Patient :",font="Times",bg="light sky blue").grid(row=1,column=0)
                        Label(up,text="Changed Surgery Number :",font="Times",bg="light sky blue").grid(row=2,column=0)
                        Surgery=StringVar()
                        SurgeryEntry=Entry(up,textvariable=Surgery,relief="solid")
                        SurgeryEntry.grid(row=1,column=1)
                        Surgeryc=StringVar()
                        SurgerycEntry=Entry(up,textvariable=Surgeryc,relief="solid")
                        SurgerycEntry.grid(row=2,column=1)
                        Button(up,text="Change",command=change,bg="navy",fg="cyan").grid(row=3,column=1)
                        choose.destroy()

                    def update2():
                        def change():
                            t=SurgeryEntry.get()
                            k=DateEntry.get()
                            if t.isdigit()==False:
                                tkinter.messagebox.showerror("Error","Surgery number of the patient should only have numeric values or it is empty")
                                sys.exit()
                            else:
                                n1=t
                            if k=="":
                                tkinter.messagebox.showerror("Error","Changed date of admission column is empty")
                                sys.exit()
                            else:
                                datereverse(k)
                            p=tkinter.messagebox.askquestion("Submission","Are you sure you want to Update this data?")
                            if p=="yes":
                                sql="UPDATE patient_in_info SET Date_Of_Admission = %s WHERE Surgery_Number = %s"
                                mycursor.execute(sql,(date,n1))
                                mydb.commit()
                                up.destroy()
                                
                        up=Toplevel()
                        up.configure(bg="light sky blue")
                        Label(up,text="Fill these below :",font="Times",fg="navy",bg="light sky blue").grid(row=0,column=0)
                        Label(up,text="Surgery Number of Patient :",font="Times",bg="light sky blue").grid(row=1,column=0)
                        Label(up,text="DD-MM-YYYY",bg="light sky blue").grid(row=2,column=1)
                        Label(up,text="Changed Date of Admission :",font="Times",bg="light sky blue").grid(row=3,column=0)
                        Surgery=StringVar()
                        SurgeryEntry=Entry(up,textvariable=Surgery,relief="solid")
                        SurgeryEntry.grid(row=1,column=1)
                        Date=StringVar()
                        DateEntry=Entry(up,textvariable=Date,relief="solid")
                        DateEntry.grid(row=3,column=1)
                        Button(up,text="Change",command=change,bg="navy",fg="cyan").grid(row=4,column=1)
                        choose.destroy()

                    def update3():
                        def change():
                            t=SurgeryEntry.get()
                            k=DateEntry.get()
                            if t.isdigit()==False:
                                tkinter.messagebox.showerror("Error","Surgery number of the patient should only have numeric values or it is empty")
                                sys.exit()
                            else:
                                n1=t
                            if k=="":
                                tkinter.messagebox.showerror("Error","Changed date of Discharge column is empty")
                                sys.exit()
                            else:
                                datereverse(k)
                            p=tkinter.messagebox.askquestion("Submission","Are you sure you want to Update this data?")
                            if p=="yes":
                                sql="UPDATE patient_in_info SET Date_Of_Discharge = %s WHERE Surgery_Number = %s"
                                mycursor.execute(sql,(date,n1))
                                mydb.commit()
                                up.destroy()
                                
                        up=Toplevel()
                        up.configure(bg="light sky blue")
                        Label(up,text="Fill these below :",font="Times",bg="light sky blue",fg="navy").grid(row=0,column=0)
                        Label(up,text="Surgery Number of Patient :",font="Times",bg="light sky blue").grid(row=1,column=0)
                        Label(up,text="DD-MM-YYYY",bg="light sky blue").grid(row=2,column=1)
                        Label(up,text="Changed Date of Discharge :",font="Times",bg="light sky blue").grid(row=3,column=0)
                        Surgery=StringVar()
                        SurgeryEntry=Entry(up,textvariable=Surgery,relief="solid")
                        SurgeryEntry.grid(row=1,column=1)
                        Date=StringVar()
                        DateEntry=Entry(up,textvariable=Date,relief="solid")
                        DateEntry.grid(row=3,column=1)
                        Button(up,text="Change",command=change,bg="navy",fg="cyan").grid(row=4,column=1)
                        choose.destroy()

                    def update4():
                        def change():
                            t=SurgeryEntry.get()
                            k=PhoneEntry.get()
                            if t.isdigit()==False:
                                tkinter.messagebox.showerror("Error","Surgery number of the patient should only have numeric values or it is empty")
                                sys.exit()
                            else:
                                n1=t
                            if k.isdigit==False or len(k)!=10:
                                tkinter.messagebox.showerror("Error","Changed Phone number is invalid")
                                sys.exit()
                            else:
                                n2=k
                            p=tkinter.messagebox.askquestion("Submission","Are you sure you want to Update this data?")
                            if p=="yes":
                                sql="UPDATE patient_in_info SET Phone_Number = %s WHERE Surgery_Number = %s"
                                mycursor.execute(sql,(n2,n1))
                                mydb.commit()
                                up.destroy()
                        
                        up=Toplevel()
                        up.configure(bg="light sky blue")
                        Label(up,text="Fill these below :",font="Times",fg="navy",bg="light sky blue").grid(row=0,column=0)
                        Label(up,text="Surgery Number of Patient :",font="Times",bg="light sky blue").grid(row=1,column=0)
                        Label(up,text="Changed Phone Number :",font="Times",bg="light sky blue").grid(row=2,column=0)
                        Surgery=StringVar()
                        SurgeryEntry=Entry(up,textvariable=Surgery,relief="solid")
                        SurgeryEntry.grid(row=1,column=1)
                        Phone=StringVar()
                        PhoneEntry=Entry(up,textvariable=Phone,relief="solid")
                        PhoneEntry.grid(row=2,column=1)
                        Button(up,text="Change",command=change,bg="navy",fg="cyan").grid(row=3,column=1)
                        choose.destroy()
                        
                    choose=Tk()
                    choose.configure(bg="light sky blue")
                    Label(choose,text="Choose from the option below to be updated :",font="Times",fg="navy",bg="light sky blue").grid(row=0,column=0)
                    Button(choose,text="Surgery Number",command=update1,font="times",bg="navy",fg="cyan",width=17).grid(row=1,column=0)
                    Button(choose,text="Date of admission",command=update2,font="times",bg="navy",fg="cyan",width=17).grid(row=2,column=0)
                    Button(choose,text="Date of Discharge",command=update3,font="times",bg="navy",fg="cyan",width=17).grid(row=3,column=0)
                    Button(choose,text="Phone Number",command=update4,font="times",bg="navy",fg="cyan",width=17).grid(row=4,column=0)
                    
                def billinginfo():
                    def update1():
                        def change():
                            t=BillEntry.get()
                            k=BillcEntry.get()
                            if t.isdigit()==False:
                                tkinter.messagebox.showerror("Error","Bill number of the patient should only have numeric values or it is empty")
                                sys.exit()
                            else:
                                n1=t
                            if k.isdigit()==False:
                                tkinter.messagebox.showerror("Error","Changed Bill number of the patient should only have numeric values or it is empty")
                                sys.exit()
                            else:
                                n2=k
                            p=tkinter.messagebox.askquestion("Submission","Are you sure you want to Update this data?")
                            if p=="yes":
                                sql="UPDATE billing_info SET Bill_Number = %s WHERE Bill_Number = %s"
                                mycursor.execute(sql,(n2,n1))
                                mydb.commit()
                                up.destroy()
                            
                        up=Toplevel()
                        up.configure(bg="light sky blue")
                        Label(up,text="Fill these below :",font="Times",fg="navy",bg="light sky blue").grid(row=0,column=0)
                        Label(up,text="Bill Number of Patient :",font="Times",bg="light sky blue").grid(row=1,column=0)
                        Label(up,text="Changed Bill Number :",font="Times",bg="light sky blue").grid(row=2,column=0)
                        Bill=StringVar()
                        BillEntry=Entry(up,textvariable=Bill,relief="solid")
                        BillEntry.grid(row=1,column=1)
                        Billc=StringVar()
                        BillcEntry=Entry(up,textvariable=Billc,relief="solid")
                        BillcEntry.grid(row=2,column=1)
                        Button(up,text="Change",command=change,bg="navy",fg="cyan").grid(row=3,column=1)
                        choose.destroy()

                    def update2():
                        def change():
                            t=BillEntry.get()
                            k=NIDEntry.get()
                            if t.isdigit()==False:
                                tkinter.messagebox.showerror("Error","Bill number of the patient should only have numeric values or it is empty")
                                sys.exit()
                            else:
                                n1=t
                            if k.isdigit()==False:
                                tkinter.messagebox.showerror("Error","Changed Number of days admitted column is empty")
                                sys.exit()
                            else:
                                n2=k
                            p=tkinter.messagebox.askquestion("Submission","Are you sure you want to Update this data?")
                            if p=="yes":
                                sql="UPDATE billing_info SET Number_Days_Admitted = %s WHERE Bill_Number = %s"
                                mycursor.execute(sql,(n2,n1))
                                mydb.commit()

                                sql="SELECT Cost_Per_Day FROM billing_info WHERE Bill_Number = %s"
                                mycursor.execute(sql,(n1,))
                                record=mycursor.fetchall()

                                n3=int(record[0][0])
                                n2=int(n2)
                                n4=int((n2*n3)+0.05*(n2*n3))

                                sql=sql="UPDATE billing_info SET Total_Cost = %s WHERE Bill_Number = %s"
                                mycursor.execute(sql,(n4,n1))
                                mydb.commit()
                                up.destroy()
                                
                        up=Toplevel()
                        up.configure(bg="light sky blue")
                        Label(up,text="Fill these below :",font="Times",fg="navy",bg="light sky blue").grid(row=0,column=0)
                        Label(up,text="Bill Number of Patient :",font="Times",bg="light sky blue").grid(row=1,column=0)
                        Label(up,text="Changed Number of days admitted :",font="Times",bg="light sky blue").grid(row=2,column=0)
                        Bill=StringVar()
                        BillEntry=Entry(up,textvariable=Bill,relief="solid")
                        BillEntry.grid(row=1,column=1)
                        NID=StringVar()
                        NIDEntry=Entry(up,textvariable=NID,relief="solid")
                        NIDEntry.grid(row=2,column=1)
                        Button(up,text="Change",command=change,bg="navy",fg="cyan").grid(row=3,column=1)
                        choose.destroy()

                    def update3():
                        def change():
                            t=BillEntry.get()
                            k=CIDEntry.get()
                            if t.isdigit()==False:
                                tkinter.messagebox.showerror("Error","Bill number of the patient should only have numeric values or it is empty")
                                sys.exit()
                            else:
                                n1=t
                            if k.isdigit()==False:
                                tkinter.messagebox.showerror("Error","Changed Cost Per Day column should only have numeric values or it is empty")
                                sys.exit()
                            else:
                                n2=k
                            p=tkinter.messagebox.askquestion("Submission","Are you sure you want to Update this data?")
                            if p=="yes":
                                sql="SELECT Patients_Id FROM billing_info WHERE Bill_Number = %s"
                                mycursor.execute(sql,(n1,))
                                record=mycursor.fetchall()
                                n3=record[0][0]

                                sql="UPDATE patients_room_info SET Cost_Per_Day = %s WHERE Patients_ID = %s"
                                mycursor.execute(sql,(n2,n3))
                                mydb.commit()

                                sql=sql="UPDATE billing_info SET Cost_Per_Day = %s WHERE Bill_Number = %s"
                                mycursor.execute(sql,(n2,n1))
                                mydb.commit()

                                sql="SELECT Number_Days_Admitted FROM billing_info WHERE Bill_Number = %s"
                                mycursor.execute(sql,(n1,))
                                record1=mycursor.fetchall()
                                n4=int(record1[0][0])
                                n2=int(n2)
                                n5=(n4*n2)+0.05*(n4*n2)

                                sql=sql="UPDATE billing_info SET Total_Cost = %s WHERE Bill_Number = %s"
                                mycursor.execute(sql,(n5,n1))
                                mydb.commit()
                                up.destroy()
                                
                        up=Toplevel()
                        up.configure(bg="light sky blue")
                        Label(up,text="Fill these below :",font="Times",fg="navy",bg="light sky blue").grid(row=0,column=0)
                        Label(up,text="Bill Number of Patient :",font="Times",bg="light sky blue").grid(row=1,column=0)
                        Label(up,text="Changed Cost Per Day :",font="Times",bg="light sky blue").grid(row=2,column=0)
                        Bill=StringVar()
                        BillEntry=Entry(up,textvariable=Bill,relief="solid")
                        BillEntry.grid(row=1,column=1)
                        CID=StringVar()
                        CIDEntry=Entry(up,textvariable=CID,relief="solid")
                        CIDEntry.grid(row=2,column=1)
                        Button(up,text="Change",command=change,bg="navy",fg="cyan").grid(row=3,column=1)
                        choose.destroy()
                        
                    choose=Tk()
                    choose.configure(bg="light sky blue")
                    Label(choose,text="Choose from the option below to be updated :",font="Times",fg="navy",bg="light sky blue").grid(row=0,column=0)
                    Button(choose,text="Bill Number",command=update1,font="times",bg="navy",fg="cyan",width=20).grid(row=1,column=0)
                    Button(choose,text="Number of days admitted",command=update2,font="times",bg="navy",fg="cyan",width=20).grid(row=2,column=0)
                    Button(choose,text="Cost per Day",command=update3,font="times",bg="navy",fg="cyan",width=20).grid(row=3,column=0)
 
                def patientout():
                    def update1():
                        def change():
                            t=PODEntry.get()
                            k=PODCEntry.get()
                            if t=="":
                                tkinter.messagebox.showerror("Error","Patient Out ID column is empty")
                                sys.exit()
                            else:
                                n1=t
                            if k=="":
                                tkinter.messagebox.showerror("Error","Changed Patient Out ID column is empty")
                                sys.exit()
                            else:
                                n2=k
                            p=tkinter.messagebox.askquestion("Submission","Are you sure you want to Update this data?")
                            if p=="yes":
                                sql="UPDATE patient_out_info SET Patients_Out_ID = %s WHERE Patients_Out_ID = %s"
                                mycursor.execute(sql,(n2,n1))
                                mydb.commit()
                                up.destroy()
                        
                        up=Toplevel()
                        up.configure(bg="light sky blue")
                        Label(up,text="Fill these below :",font="Times",fg="navy",bg="light sky blue").grid(row=0,column=0)
                        Label(up,text="Patient Out ID of Patient :",font="Times",bg="light sky blue").grid(row=1,column=0)
                        Label(up,text="Changed Patient Out ID :",font="Times",bg="light sky blue").grid(row=2,column=0)
                        POD=StringVar()
                        PODEntry=Entry(up,textvariable=POD,relief="solid")
                        PODEntry.grid(row=1,column=1)
                        PODC=StringVar()
                        PODCEntry=Entry(up,textvariable=PODC,relief="solid")
                        PODCEntry.grid(row=2,column=1)
                        Button(up,text="Change",command=change,bg="navy",fg="cyan").grid(row=3,column=1)
                        choose.destroy()

                    def update2():
                        def change():
                            t=PODEntry.get()
                            k=DAEntry.get()
                            if t=="":
                                tkinter.messagebox.showerror("Error","Patient Out ID column is empty")
                                sys.exit()
                            else:
                                n1=t
                            if k.lower()=="dead" or k.lower()=="alive":
                                n2=k.lower()
                            else:
                                tkinter.messagebox.showerror("Error","Invalid input in Dead/Alive column")
                                sys.exit()
                            p=tkinter.messagebox.askquestion("Submission","Are you sure you want to Update this data?")
                            if p=="yes":
                                sql="UPDATE patient_out_info SET Dead_Or_Alive = %s WHERE Patients_Out_ID = %s"
                                mycursor.execute(sql,(n2,n1))
                                mydb.commit()
                                up.destroy()
                                
                        up=Toplevel()
                        up.configure(bg="light sky blue")
                        Label(up,text="Fill these below :",font="Times",fg="navy",bg="light sky blue").grid(row=0,column=0)
                        Label(up,text="Patient Out ID of Patient :",font="Times",bg="light sky blue").grid(row=1,column=0)
                        Label(up,text="Changed Dead/Alive :",font="Times",bg="light sky blue").grid(row=2,column=0)
                        POD=StringVar()
                        PODEntry=Entry(up,textvariable=POD,relief="solid")
                        PODEntry.grid(row=1,column=1)
                        DA=StringVar()
                        DAEntry=Entry(up,textvariable=DA,relief="solid")
                        DAEntry.grid(row=2,column=1)
                        Button(up,text="Change",command=change,bg="navy",fg="cyan").grid(row=3,column=1)
                        choose.destroy()
                        
                    choose=Tk()
                    choose.configure(bg="light sky blue")
                    Label(choose,text="Choose from the option below to be updated :",font="Times",fg="navy",bg="light sky blue").grid(row=0,column=0)
                    Button(choose,text="Patient Out Id",command=update1,font="times",bg="navy",fg="cyan",width=17).grid(row=1,column=0)
                    Button(choose,text="Dead/Alive",command=update2,font="times",bg="navy",fg="cyan",width=17).grid(row=2,column=0)
                    
                def quitup():
                    update.destroy()
                #    
                update=Tk()
                update.title("To Update")
                update.configure(bg="light sky blue")
                Label(update,text="Choose from the below Data table that you want to update :",font="Times",fg="navy",bg="light sky blue").grid(row=0,column=0)
                Button(update,text="Patient's Information",command=patientinfo,bg="navy",fg="cyan",font="Times",width=20).grid(row=2,column=0)
                Button(update,text="Doctor's Information",command=doctorinfo,bg="navy",fg="cyan",font="Times",width=20).grid(row=3,column=0)
                Button(update,text="Patient's Room Info",command=roominfo,bg="navy",fg="cyan",font="Times",width=20).grid(row=4,column=0)
                Button(update,text="Patient's In_Information",command=patientin,bg="navy",fg="cyan",font="Times",width=20).grid(row=5,column=0)
                Button(update,text="Billing Information",command=billinginfo,bg="navy",fg="cyan",font="Times",width=20).grid(row=6,column=0)
                Button(update,text="Patient's Out_Information",command=patientout,bg="navy",fg="cyan",font="Times",width=20).grid(row=7,column=0)
                Button(update,text="To Quit Updating Data",command=quitup,bg="red",fg="white",font="Times",width=20).grid(row=8,column=0)
                
            def choice5():# To print reports from the databse
                def report1():
                    def printreport():
                        q=RoomnoEntry.get()
                        if q.isdigit()==False:
                            tkinter.messagebox.showerror("Error","There must be numeric values only in Room No column")
                            sys.exit()
                        else:
                            n1=q
                        t=SurgeryNoEntry.get()
                        if t.isdigit()==False:
                            tkinter.messagebox.showerror("Error","There must be numeric values only in Surgery No column")
                            sys.exit()
                        else:
                            n2=t
                        w=BillnoEntry.get()
                        if w.isdigit()==False:
                            tkinter.messagebox.showerror("Error","There must be numeric values only in Bill No column")
                            sys.exit()
                        else:
                            n3=w

                        sql="SELECT * FROM patient WHERE Patients_ID = %s"
                        mycursor.execute(sql,(PatientIDEntry.get(),))
                        record1=mycursor.fetchall()

                        sql="SELECT * FROM doctor WHERE Doctors_ID = %s"
                        mycursor.execute(sql,(DoctorIDEntry.get()),)
                        record2=mycursor.fetchall()

                        sql="SELECT * FROM patients_room_info WHERE Room_Number = %s"
                        mycursor.execute(sql,(n1,))
                        record3=mycursor.fetchall()

                        sql="SELECT * FROM patient_in_info WHERE Surgery_Number = %s"
                        mycursor.execute(sql,(n2,))
                        record4=mycursor.fetchall()

                        sql="SELECT * FROM billing_info WHERE Bill_Number = %s"
                        mycursor.execute(sql,(n3,))
                        record5=mycursor.fetchall()

                        sql="SELECT * FROM patient_out_info WHERE Patients_Out_ID = %s"
                        mycursor.execute(sql,(PatientoutIDEntry.get(),))
                        record6=mycursor.fetchall()
                        report1.destroy()
                        list1=["Patients First Name : ","Patients Last Name : ","Patients Age : ","Patient's ID : ","Doctor's ID : ","Date of Birth : ","Gender : ","Disease/Injury : "]
                        list2=["Doctor's First Name : ","Doctor's Last Name : ","Doctor's Age : ","Doctor's ID : ","Speciality : "]
                        list3=["Room Number : ","Patient ID : ","Type of Room : ","Cost Per Day : "]
                        list4=["SurgeryNumber : ","Room Number : ","Date Admitted : ","Date Discharged : ","Phone Number : "]
                        list5=["Bill Number : ","Patients ID : ","Doctors ID : ","Number of Days Admitted : ","Cost Per Day : ","Total Cost : "]
                        list6=["Patient Out ID : ","Patients First Name : ","Surgery Number : ","Bill Number : ","Dead/Alive : ","Total Cost : "]
                        list7=list1+list2+list3+list4+list5+list6
                        record7=record1[0]+record2[0]+record3[0]+record4[0]+record5[0]+record6[0]
                        t=len(record7)
                        report=open("Report1.txt","w")
                        for x in range(0,t):
                            report.write(str(list7[x])+str(record7[x])+"\n")
                        report.close()

                    file.destroy()
                    report1=Toplevel()
                    report1.title("Report1")
                    report1.geometry("250x320")
                    report1.configure(bg="light sky blue")
                    Label(report1,text="Fill out the following:",fg="navy",bg="light sky blue").grid(row=0,column=0)
                    Label(report1,text="Patient ID :",bg="light sky blue").grid(row=1,column=0,pady=10)
                    Label(report1,text="Doctor ID :",bg="light sky blue").grid(row=2,column=0,pady=10)
                    Label(report1,text="Room No :",bg="light sky blue").grid(row=3,column=0,pady=10)
                    Label(report1,text="Surgery No :",bg="light sky blue").grid(row=4,column=0,pady=10)
                    Label(report1,text="Bill No :",bg="light sky blue").grid(row=5,column=0,pady=10)
                    Label(report1,text="Patient Out ID:",bg="light sky blue").grid(row=6,column=0,pady=10)
                    PatientIDValue=StringVar()
                    DoctorIDValue=StringVar()
                    RoomnoValue=StringVar()
                    SurgeryNoValue=StringVar()
                    BillnoValue=StringVar()
                    PatientoutIDvalue=StringVar()
                    PatientIDEntry=Entry(report1,textvariable=PatientIDValue,relief="solid")
                    DoctorIDEntry=Entry(report1,textvariable=DoctorIDValue,relief="solid")
                    RoomnoEntry=Entry(report1,textvariable=RoomnoValue,relief="solid")
                    SurgeryNoEntry=Entry(report1,textvariable=SurgeryNoValue,relief="solid")
                    BillnoEntry=Entry(report1,textvariable=BillnoValue,relief="solid")
                    PatientoutIDEntry=Entry(report1,textvariable=PatientoutIDvalue,relief="solid")
                    PatientIDEntry.grid(row=1,column=1)
                    DoctorIDEntry.grid(row=2,column=1)
                    RoomnoEntry.grid(row=3,column=1)
                    SurgeryNoEntry.grid(row=4,column=1)
                    BillnoEntry.grid(row=5,column=1)
                    PatientoutIDEntry.grid(row=6,column=1)
                    Button(report1,text="Print Report",command=printreport,bg="navy",fg="cyan").grid(row=7,column=1)
                    
                def report2():
                    file.destroy()
                    sql="select count(Patients_ID), Disease_Or_Injury from patient group by Disease_Or_Injury"
                    mycursor.execute(sql)
                    record=mycursor.fetchall()
                    record1=(("Number of Patients","Disease/Injury"),)
                    record=record1+record
                    t=len(record)
                    report=open("report2.txt","w")
                    for x in range(0,t):
                        report.write(str(record[x][0])+" : "+str((record[x][1]))+"\n")
                    report.close()
                    
                def report3():
                    file.destroy()
                    sql="select distinct Disease_Or_Injury from patient"
                    mycursor.execute(sql)
                    record=mycursor.fetchall()
                    t=len(record)
                    report=open("report3.txt","w")
                    for x in range(0,t):
                        sql="select count(Patients_ID) from patient where Disease_Or_Injury=%s and Gender=%s"
                        mycursor.execute(sql,(record[x][0],"female"))
                        record1=mycursor.fetchall()

                        sql="select count(Patients_ID) from patient where Disease_Or_Injury=%s and Gender=%s"
                        mycursor.execute(sql,(record[x][0],"male"))
                        record2=mycursor.fetchall()

                        sql="select count(Patients_ID) from patient where Disease_Or_Injury=%s and Gender=%s"
                        mycursor.execute(sql,(record[x][0],"others"))
                        record3=mycursor.fetchall()

                        report.write("Disease/Injury : "+str(record[x][0])+"\n"+"female : "+str(record1[0][0])+"\n"+"male : "+str(record2[0][0])+"\n"+"others : "+str(record3[0][0])+"\n")
                    report.close()                        

                def report4():
                    file.destroy()
                    sql="SELECT COUNT(Patients_ID) FROM patient"
                    mycursor.execute(sql)
                    record=mycursor.fetchall()
                    record1=(("Total Patients : ",str(record[0][0])),(" "," "),("Name of the patients :"," "))
                    sql="SELECT Patients_First_Name, Patients_Last_Name FROM patient"
                    mycursor.execute(sql)
                    record2=mycursor.fetchall()
                    record2=record1+record2
                    t=len(record2)
                    report=open("report4.txt","w")
                    for x in range(0,t):
                        report.write(record2[x][0]+" "+record2[x][1]+"\n")
                    report.close()

                def report5():
                    file.destroy()
                    sql="select Type_Of_Room, COUNT(Patients_ID) from patients_room_info group by Type_Of_Room"
                    mycursor.execute(sql)
                    record=mycursor.fetchall()
                    record=(("Type Of Room","Count"),)+record
                    report=open("report5.txt","w")
                    t=len(record)
                    for x in range(0,t):
                        report.write(str(record[x][0])+" : "+str(record[x][1])+"\n")
                    report.close()

                def report6():
                    file.destroy()
                    sql="select distinct(Speciality) from doctor"
                    mycursor.execute(sql)
                    record=mycursor.fetchall()
                    report=open("report6.txt","w")
                    for x in record:
                        sql="SELECT Doctors_First_Name, Doctors_Last_Name FROM doctor WHERE Speciality = %s"
                        mycursor.execute(sql,x)
                        record1=mycursor.fetchall()
                        t=len(record1)
                        for y in range(0,t):
                            report.write(str(record1[y][0])+" "+str(record1[y][1])+" : "+str(x[0])+"\n")
                    report.close()
    
                def report7():
                    file.destroy()
                    sql="SELECT Patients_First_Name, Bill_Number FROM patient_out_info WHERE Total_Cost>50000"
                    mycursor.execute(sql)
                    record=mycursor.fetchall()
                    record1=(("Name of Patient","Bill Number"),)
                    record=record1+record
                    report=open("report7.txt","w")
                    t=len(record)
                    for x in range(0,t):
                        report.write(str(record[x][0])+" : "+str(record[x][1])+"\n")
                    report.close()
                    
                def report8():
                    file.destroy()
                    sql="SELECT COUNT(Dead_Or_Alive) FROM patient_out_info WHERE Dead_Or_Alive= %s"
                    mycursor.execute(sql,("dead",))
                    record=mycursor.fetchall()
                    report=open("report8.txt","w")
                    report.write("Number of unsuccessful surgeries are :"+str(record[0][0]))
                    report.close()
                    
                def report9():
                    file.destroy()
                    sql="SELECT SUM(Total_Cost) FROM billing_info"
                    mycursor.execute(sql)
                    record=mycursor.fetchall()
                    report=open("report9.txt","w")
                    report.write("Total money generated till now is "+str(record[0][0]))
                    report.close()

                def report10():
                    file.destroy()
                    sql="SELECT MAX(Total_Cost),Bill_Number FROM patient_out_info"
                    mycursor.execute(sql)
                    record=mycursor.fetchall()
                    report=open("report10.txt","w")
                    report.write("Highest paid surgery is of :"+"\n"+"MAX TOTAL COST"+","+"SURGERY NUMBER"+"\n"+str(record[0][0])+","+str(record[0][1]))
                def report11():
                    file.destroy()
                    sql="SELECT AVG(Total_Cost) FROM billing_info"
                    mycursor.execute()
                    record=mycursor.fetchall()
                    report=open("report11.txt","w")
                    report.write("Average money generated by each surgery is "+str(record[0][0]))
                    report.close()
                    
                def report12():
                    def printreport():
                        datereverse(DateEntry.get())
                        sql="SELECT Surgery_Number, Phone_Number FROM patient_in_info WHERE Date_Of_Admission = %s"
                        mycursor.execute(sql,(date,))
                        record=mycursor.fetchall()
                        record1=(("Surgery number","Phone Number"),)
                        record=record1+record
                        t=len(record)
                        report=open("report12.txt","w")
                        for x in range(0,t):
                            report.write(str(record[x][0])+","+str(record[x][1])+"\n")
                        report.close()
                        report12.destroy()
                        
                    file.destroy()
                    report12=Toplevel()
                    report12.configure(bg="light sky blue")
                    Label(report12,text="DD-MM-YYYY",bg="light sky blue").grid(row=0,column=1)
                    Label(report12,text="Date Admitted : ",bg="light sky blue").grid(row=1,column=0)
                    DateValue=StringVar()
                    DateEntry=Entry(report12,textvariable=DateValue,relief="solid")
                    DateEntry.grid(row=1,column=1)
                    Button(report12,text="Print Report",command=printreport,bg="navy",fg="cyan").grid(row=3,column=1)
                    
                def report13():
                    def printreport():
                        datereverse(DateEntry.get())
                        sql="SELECT Surgery_Number, Phone_Number FROM patient_in_info WHERE Date_Of_Discharge = %s"
                        mycursor.execute(sql,(date,))
                        record=mycursor.fetchall()
                        record1=(("Surgery number","Phone Number"),)
                        record=record1+record
                        t=len(record)
                        report=open("report13.txt","w")
                        for x in range(0,t):
                            report.write(str(record[x][0])+","+str(record[x][1])+"\n")
                        report.close()
                        report13.destroy()
                        
                    file.destroy()
                    report13=Toplevel()
                    report13.configure(bg="light sky blue")
                    Label(report13,text="DD-MM-YYYY",bg="light sky blue").grid(row=0,column=1)
                    Label(report13,text="Date Discharged : ",bg="light sky blue").grid(row=1,column=0)
                    DateValue=StringVar()
                    DateEntry=Entry(report13,textvariable=DateValue,relief="solid")
                    DateEntry.grid(row=1,column=1)
                    Button(report13,text="Print Report",command=printreport,bg="navy",fg="cyan").grid(row=3,column=1)
                def report14():
                    def printreport():
                        datereverse(Date1Entry.get())
                        sql="SELECT COUNT(Room_Number) FROM patients_room_info WHERE Date_Of_Admission = %s"
                        mycursor.execute(sql,(date,))
                        record=mycursor.fetchall()
                        report=open("report14.txt","w")
                        report.write("Number of rooms occupied on "+str(Date1Entry.get())+" "+"is "+str(record[0][0]))
                        report.close()
                    
                    file.destroy()
                    report14=Toplevel()
                    report14.configure(bg="light sky blue")
                    Label(report14,text="Fill the following",bg="light sky blue").grid(row=0,column=0)
                    Label(report14,text="1st Date : ",bg="light sky blue").grid(row=1,column=0)
                    Date1Value=StringVar()
                    Date1Entry=Entry(report4,textvariable=Date1Value,relief="solid")
                    Date1Entry.grid(row=1,column=1)
                    Button(report14,text="Print Report",command=printreport,bg="navy",fg="cyan").grid(row=2,column=1)
                def report15():
                    def printreport():
                        n1=DoctorIDEntry.get()
                        sql="SELECT * FROM doctor WHERE Doctors_ID = %s"
                        mycursor.execute(sql,(n1,))
                        record=mycursor.fetchall()
                        record1=["Doctors_First_Name : ","Doctors_Last_Name : ","Doctors_Age : ","Doctors_ID : ","Speciality : "]
                        file=open("report15.txt","w")
                        for x in range(0,5):
                            y=record1[x]+str(record[0][x])+"\n"
                            file.write(y)
                        file.close()
                        report15.destroy()

                    file.destroy()
                    report15=Toplevel()
                    report15.configure(bg="light sky blue")
                    Label(report15,text="Fill the following",bg="light sky blue").grid(row=0,column=0)
                    Label(report15,text="Doctor's ID:",bg="light sky blue").grid(row=1,column=0)
                    DoctorIDValue=StringVar()
                    DoctorIDEntry=Entry(report15,textvariable=DoctorIDValue,relief="solid")
                    DoctorIDEntry.grid(row=1,column=1)
                    Button(report15,text="Print Report",command=printreport,bg="navy",fg="cyan").grid(row=3,column=1)
                    
                file=Tk()
                file.title("Reports")
                file.configure(bg="light sky blue")
                Label(file,text="Choose from the below given reports that you want to get",font="times",bg="light sky blue",fg="navy").grid(row=0,column=0)
                Button(file,text="Information about a particular patient",command=report1,bg="navy",fg="cyan",font="Times",width=60).grid(row=1,column=0)
                Button(file,text="People having same type of disease/Injury",command=report2,bg="navy",fg="cyan",font="Times",width=60).grid(row=2,column=0)
                Button(file,text="People having same type of disease/Injury segregated on the basis of gender",command=report3,bg="navy",fg="cyan",font="Times",width=60).grid(row=3,column=0)
                Button(file,text="Total Number of Patients and their Names",command=report4,bg="navy",fg="cyan",font="Times",width=60).grid(row=4,column=0)
                Button(file,text="Type of room and how many of them are being used",command=report5,bg="navy",fg="cyan",font="Times",width=60).grid(row=5,column=0)
                Button(file,text="Name of those Doctors having same field of expertise",command=report6,bg="navy",fg="cyan",font="Times",width=60).grid(row=6,column=0)
                Button(file,text="Name and bill number of those people whose total money greater than 50,000",command=report7,bg="navy",fg="cyan",font="Times",width=60).grid(row=7,column=0)
                Button(file,text="Number of unsuccessful surgeries",command=report8,bg="navy",fg="cyan",font="Times",width=60).grid(row=8,column=0)
                Button(file,text="Total Money generated by hospital till now",command=report9,bg="navy",fg="cyan",font="Times",width=60).grid(row=9,column=0)
                Button(file,text="Highest paid surgery",command=report10,bg="navy",fg="cyan",font="Times",width=60).grid(row=10,column=0)
                Button(file,text="Average Money generated by each surgery",command=report11,bg="navy",fg="cyan",font="Times",width=60).grid(row=11,column=0)
                Button(file,text="Surgery and Phone Number of people who were admitted on a specific date",command=report12,bg="navy",fg="cyan",font="Times",width=60).grid(row=12,column=0)
                Button(file,text="Surgery and Phone Number of people who were discharged on a specific date",command=report13,bg="navy",fg="cyan",font="Times",width=60).grid(row=13,column=0)
                Button(file,text="Rooms Occupied on a specific date",command=report14,bg="navy",fg="cyan",font="Times",width=60).grid(row=14,column=0)
                Button(file,text="Information about a specific doctor",command=report15,bg="navy",fg="cyan",font="Times",width=60).grid(row=15,column=0)
                
            def choice6():
                root.destroy()
            
            management_hospital=PhotoImage(file="C:/Users/dell/Desktop/se/MANAGEMENT.png")
            Label(root,image=management_hospital,font="Times 32",fg="white",bg="white").grid(row=0,column=0)
            S_pic=Image.open("C:/Users/dell/Desktop/se/S_ENTRY.png")
            resized2=S_pic.resize((200,200),Image.LANCZOS)
            S_Entry=ImageTk.PhotoImage(resized2)
            M_pic=Image.open("C:/Users/dell/Desktop/se/M_ENTRY.png")
            resized3=M_pic.resize((200,200),Image.LANCZOS)
            M_Entry=ImageTk.PhotoImage(resized3)
            D_pic=Image.open("C:/Users/dell/Desktop/se/D_ENTRY.png")
            resized4=D_pic.resize((200,200),Image.LANCZOS)
            D_Entry=ImageTk.PhotoImage(resized4)
            U_pic=Image.open("C:/Users/dell/Desktop/se/U_ENTRY.png")
            resized5=U_pic.resize((200,200),Image.LANCZOS)
            U_Entry=ImageTk.PhotoImage(resized5)
            R_pic=Image.open("C:/Users/dell/Desktop/se/R_ENTRY.png")
            resized6=R_pic.resize((200,200),Image.LANCZOS)
            R_Entry=ImageTk.PhotoImage(resized6)
            Q_pic=Image.open("C:/Users/dell/Desktop/se/Q_ENTRY.png")
            resized7=Q_pic.resize((200,200),Image.LANCZOS)
            Q_Entry=ImageTk.PhotoImage(resized7)
            Button(root,image=S_Entry,command=choice1,bg="white",borderwidth=0).grid(row=3,column=0)
            Button(root,image=M_Entry,command=choice2,bg="white",borderwidth=0).grid(row=3,column=1)
            Button(root,image=D_Entry,command=choice3,bg="white",borderwidth=0).grid(row=3,column=2,padx=100)
            Button(root,image=U_Entry,command=choice4,bg="white",borderwidth=0).grid(row=4,column=0)
            Button(root,image=R_Entry,command=choice5,bg="white",borderwidth=0).grid(row=4,column=1)
            Button(root,image=Q_Entry,command=choice6,bg="white",borderwidth=0).grid(row=4,column=2)
            root.mainloop()
            
        else:
            tkinter.messagebox.showerror("Error","The password input by you is wrong or is empty")
            sys.exit()
     
    else:
        tkinter.messagebox.showerror("Error","The username input by you is wrong or is empty")
        sys.exit()
    
plus=Tk()
plus.title("Username & Password")
plus.geometry("390x525")
plus.maxsize(390,525)
plus.minsize(390,525)
login_pic=Image.open("C:/Users/dell/Desktop/se/LOGIN.png")
resized=login_pic.resize((75,35),Image.LANCZOS)
login_btn=ImageTk.PhotoImage(resized)
da_hospital=PhotoImage(file="C:/Users/dell/Desktop/se/DA HOSPITAL.png")
L=PhotoImage(file="C:/Users/dell/Desktop/se/L.png")
L=Image.open("C:/Users/dell/Desktop/se/L.png")
resizedl=L.resize((175,175),Image.LANCZOS)
L_l=ImageTk.PhotoImage(resizedl)
plus.configure(bg="white")
Label(image=da_hospital).grid(row=1,column=1)
Label(image=L_l,bg="white").grid(row=2,column=1,pady=25)
Label(text="Username :",font="Times",bg="white").grid(row=4,column=1,pady=10)
Label(text="Password :",font="Times",bg="white").grid(row=6,column=1,pady=10)
kValue=StringVar()
kEntry=Entry(plus,textvariable=kValue,relief="solid")
kEntry.grid(row=5,column=1,pady=10)
wValue=StringVar()
wEntry=Entry(plus,textvariable=wValue,relief="solid",show="•")
wEntry.grid(row=7,column=1,pady=10)
Button(image=login_btn,command=login,borderwidth=0,bg="white",activebackground="white").grid(row=9,column=1,pady=10)#
