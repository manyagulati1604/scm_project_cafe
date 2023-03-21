from tkinter import *
from tkinter import filedialog,messagebox
import random
import time
import requests


def reset():
    textReceipt.delete(1.0,END)
    e_Expresso.set('0')
    e_DoubleExpresso.set('0')
    e_Cappacino.set('0')
    e_Americano.set('0')
    e_Latte.set('0')
    e_Mocha.set('0')
    e_Chocofrappe.set('0')
    e_Hotchocolate.set('0')
    e_Coldcoffee.set('0')

    e_Chocotruffle.set('0')
    e_Brownie.set('0')
    e_RedVelvet.set('0')
    e_Pineapple.set('0')
    e_BlackForest.set('0')
    e_Oreo.set('0')
    e_Blueberry.set('0')
    e_Vanilla.set('0')
    e_Kitkat.set('0')

    textExpresso.config(state=DISABLED)
    textDoubleExpresso.config(state=DISABLED)
    textCappacino.config(state=DISABLED)
    textAmericano.config(state=DISABLED)
    textLatte.config(state=DISABLED)
    textMocha.config(state=DISABLED)
    textChocofrappe.config(state=DISABLED)
    textHotchocolate.config(state=DISABLED)
    textChocotruffle.config(state=DISABLED)
    textBrownie.config(state=DISABLED)
    textRedVelvet.config(state=DISABLED)
    textPineapple.config(state=DISABLED)
    textBlackForest.config(state=DISABLED)
    textOreo.config(state=DISABLED)
    textBlueberry.config(state=DISABLED)
    textVanilla.config(state=DISABLED)
    textKitkat.config(state=DISABLED)
    textColdcoffee.config(state=DISABLED)

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)

    CostofCoffeevar.set('')
    CostofCakesvar.set('')
    Subtotalvar.set('')
    Servicetaxvar.set('')
    Totalcostvar.set('')


def save():
    url=filedialog.asksaveasfile(mode='w',defaultextension='.txt')

    bill_data=textReceipt.get(1.0,END)
    url.write(bill_data)
    url.close()
    messagebox.showinfo('Information','Your Bill is Successfully Saved')


def send():
    def send_msg():
        message=textarea.get(1.0,END)
        number=numberfield.get()
        auth = 'woVHAjOGldMsPhnT7gS6XRIi4cYr0ym3FZkEWfKv9Qxauq8J2DHDWus7AqZKnkeXlVzQJa3fIRrp925S'
        url = 'https://www.fast2sms.com/dev/bulk'

        params = {
            'authorization': auth,
            'message': message,
            'numbers': number,
            'sender-id': 'FSTSMS',
            'route': 'p',
            'language': 'english'
        }
        response = requests.get(url, params=params)
        dic = response.json()
        result = dic.get('return')
        if result == True:
            messagebox.showinfo('Send Successfully', 'Message sent succesfully')

        else:
            messagebox.showerror('Error', 'Something went wrong')






    root2=Toplevel()

    root2.title("SEND BILL")
    root2.config(bg='red4')
    root2.geometry('485x495+50+50')
    numberlabel=Label(root2,text='Mobile Number',font=('arial',18,'bold underline'),bg='red4',fg='white')
    numberlabel.pack(pady=5)

    numberfield=Entry(root2,font=('helvetica',22,'bold'),bd=3,width=24)
    numberfield.pack(pady=5)

    billlabel = Label(root2, text='Bill Details', font=('arial', 18, 'bold underline'), bg='red4', fg='white')
    billlabel.pack(pady=5)

    textarea=Text(root2,font=('arial',12,'bold'),bd=3,width=42,height=14)
    textarea.pack(pady=5)
    textarea.insert(END,'Receipt Ref:\t\t'+billnumber+'\t\t'+date+'\n\n')
    if CostofCoffeevar.get()!='0 Rs':
        textarea.insert(END,f'Cost of Coffee\t\t\t{priceofcoffee}Rs\n')
    if CostofCakesvar.get()!=0:
        textarea.insert(END, f'Cost of Cakes\t\t\t{priceofcakes}Rs\n')

    textarea.insert(END, f'Sub Total\t\t\t{SubtotalofItems}Rs\n')
    textarea.insert(END, f'Service Tax\t\t\t{50}Rs\n')
    textarea.insert(END, f'Total Cost\t\t\t{SubtotalofItems+50}Rs\n')


    sendbutton=Button(root2,text='SEND',font=('arial',19,'bold'),bg='white',fg='red4',bd=7,relief=GROOVE,command=send_msg)
    sendbutton.pack(pady=5)



    root2.mainloop()


def Receipt():
    global billnumber,date
    textReceipt.delete(1.0,END)
    x=random.randint(100,10000)
    billnumber='BILL'+str(x)
    date=time.strftime('%d/%m/%Y')
    textReceipt.insert(END,'Receipt Ref:\t\t'+billnumber+'\t\t'+date+'\n')
    textReceipt.insert(END,'***************************************************************\n')
    textReceipt.insert(END,'Items:\t\t Cost of Items(Rs)\n')
    textReceipt.insert(END, '***************************************************************\n')
    if e_Expresso.get()!='0':
        textReceipt.insert(END,f'Expresso\t\t\t{int(e_Expresso.get())*90}\n\n')
    if e_DoubleExpresso.get()!='0':
        textReceipt.insert(END,f'DoubleExpresso\t\t\t{int(e_DoubleExpresso.get())*90}\n\n')
    if e_Cappacino.get()!='0':
        textReceipt.insert(END,f'Cappacino\t\t\t{int(e_Cappacino.get())*110}\n\n')
    if e_Americano.get()!='0':
        textReceipt.insert(END,f'Americano\t\t\t{int(e_Americano.get())*110}\n\n')
    if e_Latte.get()!='0':
        textReceipt.insert(END,f'Latte\t\t\t{int(e_Latte.get())*85}\n\n')
    if e_Mocha.get()!='0':
        textReceipt.insert(END,f'Mocha\t\t\t{int(e_Mocha.get())*95}\n\n')
    if e_Chocofrappe.get()!='0':
        textReceipt.insert(END,f'Chocofrappe\t\t\t{int(e_Chocofrappe.get())*70}\n\n')
    if e_Hotchocolate.get()!='0':
        textReceipt.insert(END,f'Hotchocolate\t\t\t{int(e_Hotchocolate.get())*100}\n\n')
    if e_Chocotruffle.get()!='0':
        textReceipt.insert(END,f'Chocotruffle\t\t\t{int(e_Chocotruffle.get())*100}\n\n')
    if e_Coldcoffee.get()!='0':
        textReceipt.insert(END,f'Coldcoffee\t\t\t{int(e_Coldcoffee.get())*60}\n\n')
    if e_Brownie.get()!='0':
        textReceipt.insert(END,f'Brownie\t\t\t{int(e_Brownie.get())*400}\n\n')
    if e_RedVelvet.get()!='0':
        textReceipt.insert(END,f'RedVelvet\t\t\t{int(e_RedVelvet.get())*575}\n\n')
    if e_Pineapple.get()!='0':
        textReceipt.insert(END,f'Pineapple\t\t\t{int(e_Pineapple.get())*500}\n\n')
    if e_BlackForest.get()!='0':
        textReceipt.insert(END,f'BlackForest\t\t\t{int(e_BlackForest.get())*900}\n\n')
    if e_Oreo.get()!='0':
        textReceipt.insert(END,f'Oreo\t\t\t{int(e_Oreo.get())*750}\n\n')
    if e_Blueberry.get()!='0':
        textReceipt.insert(END,f'Blueberry\t\t\t{int(e_Blueberry.get())*680}\n\n')
    if e_Vanilla.get()!='0':
        textReceipt.insert(END,f'Vanilla\t\t\t{int(e_Vanilla.get())*550}\n\n')
    if e_Kitkat.get()!='0':
        textReceipt.insert(END,f'Kitkat\t\t\t{int(e_Kitkat.get())*750}\n\n')
    textReceipt.insert(END, '***************************************************************\n')
    if CostofCoffeevar.get()!='0 Rs':
        textReceipt.insert(END,f'Cost of Coffee\t\t\t{priceofcoffee}Rs\n\n')
    if CostofCakesvar.get()!=0:
        textReceipt.insert(END, f'Cost of Cakes\t\t\t{priceofcakes}Rs\n\n')

    textReceipt.insert(END, f'Sub Total\t\t\t{SubtotalofItems}Rs\n\n')
    textReceipt.insert(END, f'Service Tax\t\t\t{50}Rs\n\n')
    textReceipt.insert(END, f'Total Cost\t\t\t{SubtotalofItems+50}Rs\n\n')
    textReceipt.insert(END, '***************************************************************\n')

def Expresso():
    if var1.get()==1:
        textExpresso.config(state=NORMAL)
        textExpresso.delete(0,END)
        textExpresso.focus()
    else:
        textExpresso.config(state=DISABLED)
        e_Expresso.set('0')

def DoubleExpresso():
    if var2.get()==1:
        textDoubleExpresso.config(state=NORMAL)
        textDoubleExpresso.delete(0,END)
        textDoubleExpresso.focus()
    else:
        textDoubleExpresso.config(state=DISABLED)
        e_DoubleExpresso.set('0')

def Cappacino():
    if var3.get()==1:
        textCappacino.config(state=NORMAL)
        textCappacino.delete(0,END)
        textCappacino.focus()
    else:
        textCappacino.config(state=DISABLED)
        e_Cappacino.set('0')

def Americano():
    if var4.get()==1:
        textAmericano.config(state=NORMAL)
        textAmericano.delete(0,END)
        textAmericano.focus()
    else:
        textAmericano.config(state=DISABLED)
        e_Americano.set('0')

def Latte():
    if var5.get()==1:
        textLatte.config(state=NORMAL)
        textLatte.delete(0,END)
        textLatte.focus()
    else:
        textLatte.config(state=DISABLED)
        e_Latte.set('0')

def Mocha():
    if var6.get()==1:
        textMocha.config(state=NORMAL)
        textMocha.delete(0,END)
        textMocha.focus()
    else:
        textMocha.config(state=DISABLED)
        e_Mocha.set('0')

def Chocofrappe():
    if var7.get()==1:
        textChocofrappe.config(state=NORMAL)
        textChocofrappe.delete(0,END)
        textChocofrappe.focus()
    else:
        textChocofrappe.config(state=DISABLED)
        e_Chocofrappe.set('0')

def Hotchocolate():
    if var8.get()==1:
        textHotchocolate.config(state=NORMAL)
        textHotchocolate.delete(0,END)
        textHotchocolate.focus()
    else:
        textHotchocolate.config(state=DISABLED)
        e_Hotchocolate.set('0')

def Chocotruffle():
    if var9.get()==1:
        textChocotruffle.config(state=NORMAL)
        textChocotruffle.delete(0,END)
        textChocotruffle.focus()
    else:
        textChocotruffle.config(state=DISABLED)
        e_Chocotruffle.set('0')

def Brownie():
    if var10.get()==1:
        textBrownie.config(state=NORMAL)
        textBrownie.delete(0,END)
        textBrownie.focus()
    else:
        textBrownie.config(state=DISABLED)
        e_Brownie.set('0')

def RedVelvet():
    if var11.get()==1:
        textRedVelvet.config(state=NORMAL)
        textRedVelvet.delete(0,END)
        textRedVelvet.focus()
    else:
        textRedVelvet.config(state=DISABLED)
        e_RedVelvet.set('0')

def Pineapple():
    if var12.get()==1:
        textPineapple.config(state=NORMAL)
        textPineapple.delete(0,END)
        textPineapple.focus()
    else:
        textPineapple.config(state=DISABLED)
        e_Pineapple.set('0')

def BlackForest():
    if var13.get()==1:
        textBlackForest.config(state=NORMAL)
        textBlackForest.delete(0,END)
        textBlackForest.focus()
    else:
        textBlackForest.config(state=DISABLED)
        e_BlackForest.set('0')

def Oreo():
    if var14.get()==1:
        textOreo.config(state=NORMAL)
        textOreo.delete(0,END)
        textOreo.focus()
    else:
        textOreo.config(state=DISABLED)
        e_Oreo.set('0')

def Blueberry():
    if var15.get()==1:
        textBlueberry.config(state=NORMAL)
        textBlueberry.delete(0,END)
        textBlueberry.focus()
    else:
        textBlueberry.config(state=DISABLED)
        e_Blueberry.set('0')


def Vanilla():
    if var16.get()==1:
        textVanilla.config(state=NORMAL)
        textVanilla.delete(0,END)
        textVanilla.focus()
    else:
        textVanilla.config(state=DISABLED)
        e_Vanilla.set('0')

def Kitkat():
    if var17.get()==1:
        textKitkat.config(state=NORMAL)
        textKitkat.delete(0,END)
        textKitkat.focus()
    else:
        textKitkat.config(state=DISABLED)
        e_Kitkat.set('0')

def Coldcoffee():
    if var18.get()==1:
        textColdcoffee.config(state=NORMAL)
        textColdcoffee.delete(0,END)
        textColdcoffee.focus()
    else:
        textColdcoffee.config(state=DISABLED)
        e_Coldcoffee.set('0')

def totalcost():
    global priceofcoffee,priceofcakes,SubtotalofItems


    item1=int(e_Expresso.get())
    item2=int(e_DoubleExpresso.get())
    item3=int(e_Cappacino.get())
    item4=int(e_Americano.get())
    item5=int(e_Latte.get())
    item6=int(e_Mocha.get())
    item7=int(e_Chocofrappe.get())
    item8=int(e_Hotchocolate.get())
    item9=int(e_Chocotruffle.get())
    item10=int(e_Brownie.get())
    item11=int(e_RedVelvet.get())
    item12=int(e_Pineapple.get())
    item13=int(e_BlackForest.get())
    item14=int(e_Oreo.get())
    item15=int(e_Blueberry.get())
    item16=int(e_Vanilla.get())
    item17=int(e_Kitkat.get())
    item18=int(e_Coldcoffee.get())

    priceofcoffee=(item1*90)+(item2*90)+(item3*110)+(item4*110)+(item5*85)+(item6*95)+(item7*70)+(item8*100)+(item9*100)+(item18*60)
    priceofcakes=(item10*400)+(item11*575)+(item12*500)+(item13*900)+(item14*750)+(item15*680)+(item16*550)+(item17*750)

    CostofCoffeevar.set(str(priceofcoffee)+' Rs')
    CostofCakesvar.set(str(priceofcakes)+' Rs')

    SubtotalofItems=priceofcoffee+priceofcakes
    Subtotalvar.set(str(SubtotalofItems)+' Rs')

    Servicetaxvar.set('50 Rs')

    Totalcost=SubtotalofItems+50
    Totalcostvar.set(str(Totalcost)+' Rs')



root= Tk()

root.geometry('1350x750+0+0')



root.title('Cafe Management System')

root.config(bg='firebrick4')

topFrame=Frame(root,bd=10,relief=RIDGE,bg='firebrick4')
topFrame.pack(side=TOP)
labelTitle=Label(topFrame,text='Cafe Management System',font=('arial',30,'bold'),fg='yellow',bg='red4',width=51,bd=9)
labelTitle.grid(row=0,column=0)

menuFrame=Frame(root,bd=10,relief=RIDGE,bg='firebrick4')
menuFrame.pack(side=LEFT)

costFrame=Frame(menuFrame,bd=4,relief=RIDGE,bg='firebrick4',pady=10)
costFrame.pack(side=BOTTOM)

coffeeFrame=LabelFrame(menuFrame,text='Coffee',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4')
coffeeFrame.pack(side=LEFT)

cakeFrame=LabelFrame(menuFrame,text='Cakes',font=('arial',19,'bold'),bd=10,relief=RIDGE)
cakeFrame.pack(side=LEFT)

rightFrame=Frame(root,bd=15,relief=RIDGE,bg='red4')
rightFrame.pack(side=RIGHT)

calculatorFrame=Frame(rightFrame,bd=1,relief=RIDGE,bg='red4')
calculatorFrame.pack()

recieptFrame=Frame(rightFrame,bd=4,relief=RIDGE,bg='red4')
recieptFrame.pack()

buttonFrame=Frame(rightFrame,bd=3,relief=RIDGE,bg='red4')
buttonFrame.pack()

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()

e_Expresso=StringVar()
e_DoubleExpresso=StringVar()
e_Cappacino=StringVar()
e_Americano=StringVar()
e_Latte=StringVar()
e_Mocha=StringVar()
e_Chocofrappe=StringVar()
e_Hotchocolate=StringVar()
e_Chocotruffle=StringVar()
e_Brownie=StringVar()
e_RedVelvet=StringVar()
e_Pineapple=StringVar()
e_BlackForest=StringVar()
e_Oreo=StringVar()
e_Blueberry=StringVar()
e_Vanilla=StringVar()
e_Kitkat=StringVar()
e_Coldcoffee=StringVar()
CostofCoffeevar=StringVar()
CostofCakesvar=StringVar()
Subtotalvar=StringVar()
Servicetaxvar=StringVar()
Totalcostvar=StringVar()



e_Expresso.set('0')
e_DoubleExpresso.set('0')
e_Cappacino.set('0')
e_Americano.set('0')
e_Latte.set('0')
e_Mocha.set('0')
e_Chocofrappe.set('0')
e_Hotchocolate.set('0')
e_Coldcoffee.set('0')

e_Chocotruffle.set('0')
e_Brownie.set('0')
e_RedVelvet.set('0')
e_Pineapple.set('0')
e_BlackForest.set('0')
e_Oreo.set('0')
e_Blueberry.set('0')
e_Vanilla.set('0')
e_Kitkat.set('0')

Expresso=Checkbutton(coffeeFrame,text='Expresso',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var1,command=Expresso)
Expresso.grid(row=0,column=0,sticky=W)

DoubleExpresso=Checkbutton(coffeeFrame,text='DoubleExpresso',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var2,command=DoubleExpresso)
DoubleExpresso.grid(row=1,column=0,sticky=W)

Cappacino=Checkbutton(coffeeFrame,text='Cappacino',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var3,command=Cappacino)
Cappacino.grid(row=2,column=0,sticky=W)

Americano=Checkbutton(coffeeFrame,text='Americano',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var4,command=Americano)
Americano.grid(row=3,column=0,sticky=W)

Latte=Checkbutton(coffeeFrame,text='Latte',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var5,command=Latte)
Latte.grid(row=4,column=0,sticky=W)

Mocha=Checkbutton(coffeeFrame,text='Mocha',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var6,command=Mocha)
Mocha.grid(row=5,column=0,sticky=W)

Chocofrappe=Checkbutton(coffeeFrame,text='Chocofrappe',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var7,command=Chocofrappe)
Chocofrappe.grid(row=6,column=0,sticky=W)

Hotchocolate=Checkbutton(coffeeFrame,text='Hotchocolate',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var8,command=Hotchocolate)
Hotchocolate.grid(row=7,column=0,sticky=W)

Coldcoffee=Checkbutton(coffeeFrame,text='Coldcoffee',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var18,command=Coldcoffee)
Coldcoffee.grid(row=8,column=0,sticky=W)

textExpresso=Entry(coffeeFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_Expresso)
textExpresso.grid(row=0,column=1)

textDoubleExpresso=Entry(coffeeFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_DoubleExpresso)
textDoubleExpresso.grid(row=1,column=1)

textCappacino=Entry(coffeeFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_Cappacino)
textCappacino.grid(row=2,column=1)

textAmericano=Entry(coffeeFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_Americano)
textAmericano.grid(row=3,column=1)

textLatte=Entry(coffeeFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_Latte)
textLatte.grid(row=4,column=1)

textMocha=Entry(coffeeFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_Mocha)
textMocha.grid(row=5,column=1)

textChocofrappe=Entry(coffeeFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_Chocofrappe)
textChocofrappe.grid(row=6,column=1)

textHotchocolate=Entry(coffeeFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_Hotchocolate)
textHotchocolate.grid(row=7,column=1)

textColdcoffee=Entry(coffeeFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_Coldcoffee)
textColdcoffee.grid(row=8,column=1)

Chocotruffle= Checkbutton(cakeFrame,text='Chocotruffle',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var9,command=Chocotruffle)
Chocotruffle.grid(row=0,column=0,sticky=W)

Brownie= Checkbutton(cakeFrame,text='Brownie',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var10,command=Brownie)
Brownie.grid(row=1,column=0,sticky=W)

RedVelvet= Checkbutton(cakeFrame,text='RedVelvet',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var11,command=RedVelvet)
RedVelvet.grid(row=2,column=0,sticky=W)

Pineapple= Checkbutton(cakeFrame,text='Pineapple',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var12,command=Pineapple)
Pineapple.grid(row=3,column=0,sticky=W)

BlackForest= Checkbutton(cakeFrame,text='BlackForest',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var13,command=BlackForest)
BlackForest.grid(row=4,column=0,sticky=W)

Oreo= Checkbutton(cakeFrame,text='Oreo',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var14,command=Oreo)
Oreo.grid(row=5,column=0,sticky=W)

Blueberry= Checkbutton(cakeFrame,text='Blueberry',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var15,command=Blueberry)
Blueberry.grid(row=6,column=0,sticky=W)

Vanilla= Checkbutton(cakeFrame,text='Vanilla',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var16,command=Vanilla)
Vanilla.grid(row=7,column=0,sticky=W)

Kitkat= Checkbutton(cakeFrame,text='Kitkat',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var17,command=Kitkat)
Kitkat.grid(row=8,column=0,sticky=W)

textChocotruffle=Entry(cakeFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_Chocotruffle)
textChocotruffle.grid(row=0,column=1)

textBrownie=Entry(cakeFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_Brownie)
textBrownie.grid(row=1,column=1)

textRedVelvet=Entry(cakeFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_RedVelvet)
textRedVelvet.grid(row=2,column=1)

textPineapple=Entry(cakeFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_Pineapple)
textPineapple.grid(row=3,column=1)

textBlackForest=Entry(cakeFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_BlackForest)
textBlackForest.grid(row=4,column=1)

textOreo=Entry(cakeFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_Oreo)
textOreo.grid(row=5,column=1)

textBlueberry=Entry(cakeFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_Blueberry)
textBlueberry.grid(row=6,column=1)

textVanilla=Entry(cakeFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_Vanilla)
textVanilla.grid(row=7,column=1)

textKitkat=Entry(cakeFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_Kitkat)
textKitkat.grid(row=8,column=1)

labelCostofCoffee=Label(costFrame,text='Cost of Coffee',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelCostofCoffee.grid(row=0,column=0)

textCostofCoffee=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=CostofCoffeevar)
textCostofCoffee.grid(row=0,column=1,padx=41)

labelCostofCakes=Label(costFrame,text='Cost of Cakes',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelCostofCakes.grid(row=1 ,column=0)

textCostofCakes=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=CostofCakesvar)
textCostofCakes.grid(row=1,column=1,padx=41)

labelSubtotal=Label(costFrame,text='Subtotal',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelSubtotal.grid(row=0 ,column=2)

textSubtotal=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=Subtotalvar)
textSubtotal.grid(row=0,column=3,padx=41)

labelServicetax=Label(costFrame,text='Service Tax',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelServicetax.grid(row=1 ,column=2)

textServicetax=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=Servicetaxvar)
textServicetax.grid(row=1,column=3,padx=41)

labelTotalcost=Label(costFrame,text='Total cost',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelTotalcost.grid(row=2 ,column=2)

textTotalcost=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=Totalcostvar)
textTotalcost.grid(row=2,column=3,padx=41)

buttonTotal=Button(buttonFrame,text='Total',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5,command=totalcost)
buttonTotal.grid(row=0,column=0)

buttonReceipt=Button(buttonFrame,text='Receipt',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5,command=Receipt)
buttonReceipt.grid(row=0,column=1)

buttonSave=Button(buttonFrame,text='Save',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5,command=save)
buttonSave.grid(row=0,column=2)

buttonSend=Button(buttonFrame,text='Send',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5,command=send)
buttonSend.grid(row=0,column=3)

buttonReset=Button(buttonFrame,text='Reset',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5,command=reset)
buttonReset.grid(row=0,column=4)

textReceipt=Text(recieptFrame,font=('arial',12,'bold'),bd=3,width=42,height=14)
textReceipt.grid(row=0,column=0)

operator=''
def buttonClick(numbers):
    global operator
    operator=operator+numbers
    calculatorField.delete(0,END)
    calculatorField.insert(END,operator)

def clear():
    global operator
    operator=''
    calculatorField.delete(0,END)

def answer():
    global operator
    result=str(eval(operator))
    calculatorField.delete(0,END)
    calculatorField.insert(0,result)
    operator=''

calculatorField=Entry(calculatorFrame,font=('arial',16,'bold'),width=32,bd=4)
calculatorField.grid(row=0,column=0,columnspan=4)

button7=Button(calculatorFrame,text='7',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('7'))
button7.grid(row=1,column=0)

button8=Button(calculatorFrame,text='8',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('8'))
button8.grid(row=1,column=1)

button9=Button(calculatorFrame,text='9',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('9'))
button9.grid(row=1,column=2)

buttonPlus=Button(calculatorFrame,text='+',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('+'))
buttonPlus.grid(row=1,column=3)

button4=Button(calculatorFrame,text='4',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('4'))
button4.grid(row=2,column=0)

button5=Button(calculatorFrame,text='5',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=6,command=lambda:buttonClick('5'))
button5.grid(row=2,column=1)

button6=Button(calculatorFrame,text='6',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=6,command=lambda:buttonClick('6'))
button6.grid(row=2,column=2)

buttonMinus=Button(calculatorFrame,text='-',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('-'))
buttonMinus.grid(row=2,column=3)

button1=Button(calculatorFrame,text='1',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('1'))
button1.grid(row=3,column=0)

button2=Button(calculatorFrame,text='2',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=6,command=lambda:buttonClick('2'))
button2.grid(row=3,column=1)

button3=Button(calculatorFrame,text='3',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=6,command=lambda:buttonClick('3'))
button3.grid(row=3,column=2)

buttonMult=Button(calculatorFrame,text='*',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('*'))
buttonMult.grid(row=3,column=3)

buttonAns=Button(calculatorFrame,text='Ans',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=answer)
buttonAns.grid(row=4,column=0)

buttonClear=Button(calculatorFrame,text='Clear',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=clear)
buttonClear.grid(row=4,column=1)

button0=Button(calculatorFrame,text='0',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('0'))
button0.grid(row=4,column=2)

buttonDiv=Button(calculatorFrame,text='/',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('/'))
buttonDiv.grid(row=4,column=3)

root.mainloop()





