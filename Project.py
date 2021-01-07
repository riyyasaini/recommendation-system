import tkinter as tk
from tkinter import *
import datetime
from functools import partial
import pandas as pd
import numpy as np
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
te=TransactionEncoder()
dff=pd.read_csv("D:/COllege/Delhi/HPE/ML/database.csv")
ind=110
iiind=200
arrec=[]
mycolor = '#%02x%02x%02x' % (50, 50, 50)

iiuser=dff.iloc[:,0]
iiuser=np.array(iiuser)
iiuser=list(iiuser)
iiphone=dff.iloc[:,1]
iiphone=np.array(iiphone)
iiphone=list(iiphone)
iidate=dff.iloc[:,2]
iidate=np.array(iidate)
iidate=list(iidate)
iitime=dff.iloc[:,3]
iitime=np.array(iitime)
iitime=list(iitime)
iiname=dff.iloc[:,4]
iiname=np.array(iiname)
iiname=list(iiname)
iiprice=dff.iloc[:,5]
iiprice=np.array(iiprice)
iiprice=list(iiprice)
iiquantity=dff.iloc[:,6]
iiquantity=np.array(iiquantity)
iiquantity=list(iiquantity)
iiamount=dff.iloc[:,7]
iiamount=np.array(iiamount)
iiamount=list(iiamount)
iicno=dff.iloc[:,8]
iicno=np.array(iicno)
iicno=list(iicno)

cno=dff["Customer No"][len(iicno)-1] + 1


iuser=[]
iphone=[]
idate=[]
itime=[]
iname=[]
iprice=[]
iquantity=[]
iamount=[]
icno=[]

window1=tk.Tk()
window1.configure(background="Light blue")
window1.title("Supermarket Recommendation System")
window1.geometry('600x600')
now = datetime.datetime.now()
date=now.strftime("%Y-%m-%d")
time=now.strftime("%H:%M:%S")

timee=tk.Label(window1,text=time, bg="Light blue", fg=mycolor)
timee.place(x=200,y=15)
datee=tk.Label(window1,text=date,bg="Light blue", fg=mycolor)
datee.place(x=300,y=15)

e11=tk.Label(window1,text="Name : ",bg="Light blue", fg=mycolor)
e11.place(x=50,y=45)
e22=tk.Label(window1,text="Phone Number : ",bg="Light blue", fg=mycolor)
e22.place(x=250,y=45)
e1=tk.Entry(window1)
e1.place(x=100,y=45)
e2=tk.Entry(window1)
e2.place(x=350,y=45)



l1=tk.Label(window1,text="Item name",bg="Light blue", fg=mycolor)
l1.place(x=10, y=80)
l2=tk.Label(window1,text="Price",bg="Light blue", fg=mycolor)
l2.place(x=110, y=80)
l3=tk.Label(window1,text="Quantity",bg="Light blue", fg=mycolor)
l3.place(x=210, y=80)
l3=tk.Label(window1,text="Amount",bg="Light blue", fg=mycolor)
l3.place(x=310, y=80)


def store() :
    global e1,e2
    usern=e1.get()
    phno=e2.get()
    x=entry1.get()
    y=entry2.get()
    z=entry3.get()
    y=int(y)
    z=int(z)
    w=z*y
    l4=tk.Label(window1,text=(str(w)+"Rs."),bg="Light blue", fg=mycolor)
    l4.place(x=310,y=ind)
    l5=tk.Label(window1,text="Added.",bg="Light blue", fg=mycolor)
    l5.place(x=410,y=ind)
    iuser.append(usern)
    iphone.append(phno)
    idate.append(date)
    itime.append(time)
    iname.append(x)
    iprice.append(y)
    iquantity.append(z)
    iamount.append(w)
    icno.append(cno)
    
    
    
def newent() :
    global ind
    ind=ind+20
    global entry1,entry2,entry3
    entry1=tk.Entry(window1)
    entry1.place(x=10,y=ind)
    entry2=tk.Entry(window1)
    entry2.place(x=110,y=ind)
    entry3=tk.Entry(window1)
    entry3.place(x=210,y=ind)
    button1=tk.Button(window1,text="Add",command=store,fg="White", bg=mycolor)
    button1.place(x=400,y=430)

    
button1=tk.Button(window1,text="New item",command=newent, fg="White", bg=mycolor)
button1.place(x=400,y=400)
#print(entry.get())


def subm() :
    global ind
    iiuser.extend(iuser)
    iiphone.extend(iphone)
    iidate.extend(idate)
    iitime.extend(itime)
    iiname.extend(iname)
    iiprice.extend(iprice)
    iiquantity.extend(iquantity)
    iiamount.extend(iamount)
    iicno.extend(icno)
    df=pd.DataFrame({"UserName":iiuser,"Phone":iiphone,"Date":iidate,"Time":iitime,"Name":iiname,"Price":iiprice,"Quantity":iiquantity,"Amount":iiamount,"Customer No" : iicno })
    df.to_csv("D:/Delhi/HPE/ML/database.csv",index=False)
    ans=0
    for k in iamount :
        ans=ans+k
    op=tk.Label(window1,text="Submission successful. Thank you for shopping!",bg="Light blue", fg=mycolor)
    op.place(x=50,y=ind+50)
    op1=tk.Label(window1,text=("Total amount : "+ str(ans) + "Rs."),bg="Light blue", fg=mycolor)
    op1.place(x=50,y=ind+80)
    
button3=tk.Button(window1,text="Submit",command=subm, fg="White", bg=mycolor)
button3.place(x=400,y=460)
lg=[]


def recm() :
    df_new=pd.read_csv("D:/College/Delhi/HPE/ML/database.csv")
    for i in range(cno+1) :
        lg=[]
        for z in df_new.index :
            if df_new.iloc[z][8]==i :
                lg.append(df_new.iloc[z][4])
        arrec.append(lg)
    booldata=te.fit(arrec).transform(arrec)
    dff_new=pd.DataFrame(booldata,columns=te.columns_)
    freq_items=apriori(dff_new,min_support=0.05,use_colnames=True)
    freq_items['Length']=freq_items['itemsets'].apply(lambda x: len(x))
    
    recc=freq_items[(freq_items['Length']>=2) & (freq_items['support']>=0.02)]

    op=(recc.iloc[:,1].to_string(index=False)).split('\n')
    window_rec=tk.Tk()
    window_rec.title("Recommendations")
    window_rec.configure(background=mycolor)
    window_rec.geometry('300x300')
    for zz in op :
        l1=tk.Label(window_rec,text=zz,fg="White", bg=mycolor)
        l1.pack()
    

button4=tk.Button(window1,text="Recommend",command=recm,fg="White", bg=mycolor)
button4.place(x=400,y=490)
f=0


def det() :
    
    w11=tk.Tk()
    w11.title("Find Details")
    w11.configure(background=mycolor)
    w11.geometry('600x600')
    l12=tk.Label(w11,text="Username",fg="White", bg=mycolor)
    l12.place(x=100,y=50)
    e12=tk.Entry(w11)
    e12.place(x=160,y=50)
    l22=tk.Label(w11,text="Phone",fg="White", bg=mycolor)
    l22.place(x=100,y=80)
    e22=tk.Entry(w11)
    e22.place(x=160,y=80)
    
    
    def det2() :
        df_d=pd.read_csv("D:/College/Delhi/HPE/ML/database.csv")
        global iiind
        zzz=e12.get()
        yyy=e22.get()
        laa1=tk.Label(w11,text="Date",fg="White", bg=mycolor)
        laa2=tk.Label(w11,text="Time",fg="White", bg=mycolor)
        laa3=tk.Label(w11,text="Product",fg="White", bg=mycolor)
        laa4=tk.Label(w11,text="Price",fg="White", bg=mycolor)
        laa5=tk.Label(w11,text="Quantity",fg="White", bg=mycolor)
        laa6=tk.Label(w11,text="Amount",fg="White", bg=mycolor)
        laa1.place(x=30,y=160)
        laa2.place(x=100,y=160)
        laa3.place(x=170,y=160)
        laa4.place(x=240,y=160)
        laa5.place(x=310,y=160)
        laa6.place(x=380,y=160)
        global f
        for j in df_d.index :
            if (df_d.iloc[j][0]==zzz) & (df_d.iloc[j][1]==int(yyy)) :
                f=1
                la1=tk.Label(w11,text=df_d.iloc[j][2],fg="White", bg=mycolor)
                la2=tk.Label(w11,text=df_d.iloc[j][3],fg="White", bg=mycolor)
                la3=tk.Label(w11,text=df_d.iloc[j][4],fg="White", bg=mycolor)
                la4=tk.Label(w11,text=df_d.iloc[j][5],fg="White", bg=mycolor)
                la5=tk.Label(w11,text=df_d.iloc[j][6],fg="White", bg=mycolor)
                la6=tk.Label(w11,text=df_d.iloc[j][7],fg="White", bg=mycolor)
                la1.place(x=30,y=iiind)
                la2.place(x=100,y=iiind)
                la3.place(x=170,y=iiind)
                la4.place(x=240,y=iiind)
                la5.place(x=310,y=iiind)
                la6.place(x=380,y=iiind)
                iiind=iiind+30

        if f==0 :
            la7=tk.Label(w11,text="Not Found!",bg="White", fg=mycolor)
            la7.place(x=170,y=400)
               
    button6=tk.Button(w11,text="Submit",command=det2,fg="White", bg=mycolor)
    button6.place(x=170,y=115)

    
button5=tk.Button(window1,text="Find Customer Details",command=det,fg="White", bg=mycolor)
button5.place(x=400,y=520)
    
window1.mainloop()
