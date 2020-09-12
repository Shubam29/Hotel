from tkinter import*
from tkinter import ttk
import random
import tkinter.messagebox
from datetime import datetime
import hotelDatabase
import datetime
import time
from datetime import datetime, timedelta

#Frontend
#================================================================================

class Hotel:

    def __init__(self,root):
        self.root = root
        self.root.title("Hotel Management Systems")
        self.root.geometry("1350x750+0+0")


        CusID =StringVar()
        Firstname =StringVar()
        Surname =StringVar()
        Address=StringVar()
        PostCode =StringVar()
        Mobile=StringVar()
        Email=StringVar()
        Nationality=StringVar()
        DOB =StringVar()
        ProveOfID=StringVar()
        Gender =StringVar()            
        DateIn=StringVar()
        DateOut=StringVar()
        Meal=StringVar()
        RoomType=StringVar()
        RoomNo=StringVar()
        RoomExtNo=StringVar()
        TotalCost=StringVar()
        SubTotal=StringVar()
        PaidTax=StringVar()
        TotalDays=StringVar()
        global hd

        

        MainFrame =Frame(self.root)
        MainFrame.grid()

        TopFrame = Frame(MainFrame, bd=10, width=1350,height=550, padx=2, relief=RIDGE)
        TopFrame.pack(side=TOP)

        LeftFrame = Frame(TopFrame, bd=5, width=400,height=550, padx=0, relief=RIDGE)
        LeftFrame.pack(side=LEFT)

        RightFrame = Frame(TopFrame, bd=5, width=820,height=550, padx=0,pady=0, relief=RIDGE)
        RightFrame.pack(side=RIGHT)
        RightFrame1 = Frame(RightFrame, bd=5, width=800,height=50, padx=10,pady=0, relief=RIDGE)
        RightFrame1.grid(row=0,column=0)
        RightFrame2 = Frame(RightFrame, bd=5, width=800,height=100, padx=3,pady=0, relief=RIDGE)
        RightFrame2.grid(row=1,column=0)
        RightFrame3 = Frame(RightFrame, bd=5, width=800,height=400, padx=4,pady=0, relief=RIDGE)
        RightFrame3.grid(row=3,column=0)
        
        BottomFrame = Frame(MainFrame, bd=10, width=1350,height=150, padx=2, relief=RIDGE)
        BottomFrame.pack(side=BOTTOM)

        #Date1.set(time.strftime("%d/%m/%Y")) # date#datetime.date
        #time1.set(time.strftime("%H:%M:%S")) # time
        DateIn.set(time.strftime("%d/%m/%Y")) # date
        DateOut.set(time.strftime("%d/%m/%Y"))

        x = random.randint(109, 5876)
        randomRef = str(x)
        CusID.set("Hot"+ randomRef)
        #===========================================================================================================================

        #===========================================================================================================================
        def addData():
            if(len(CusID.get())!=0):
                hotelDatabase.addHotelRec(CusID.get(), Firstname.get(),  Surname.get(),Address.get(),Gender.get(),Mobile.get(),
                                     Nationality.get(),ProveOfID.get(),DateIn.get(),DateOut.get(),Email.get())
                lstHotel.delete(0,END)            
                lstHotel.insert(END,(CusID.get(), Firstname.get(),  Surname.get(),Address.get(),Gender.get(),Mobile.get(),
                                     Nationality.get(),ProveOfID.get(),DateIn.get(),DateOut.get(),Email.get()))

               

        def DisplayData():
            lstHotel.delete(0,END)
            for row in hotelDatabase.viewData():
                lstHotel.insert(END,row,str(""))

        
        def HotelRec(event):
            global hd
            searchHdb = lstHotel.curselection()[0]
            hd = lstHotel.get(searchHdb )

            self.txtCusID.delete(0,END)
            self.txtCusID.insert(END,hd[1])
            self.txtFirstname.delete(0,END)
            self.txtFirstname.insert(END,hd[2])
            self.txtSurname.delete(0,END)
            self.txtSurname.insert(END,hd[3])
            self.txtAddress.delete(0,END)
            self.txtAddress.insert(END,hd[4])
            self.cboGender.delete(0,END)
            self.cboGender.insert(END,hd[5])
            self.txtMobile.delete(0,END)
            self.txtMobile.insert(END,hd[6])            
            self.cboNationality.delete(0,END)
            self.cboNationality.insert(END,hd[7])
            self.cboProveOfID.delete(0,END)
            self.cboProveOfID.insert(END,hd[8]) 
            self.txtDateIn.delete(0,END)
            self.txtDateIn.insert(END,hd[9]) 
            self.txtDateOut.delete(0,END)
            self.txtDateOut.insert(END,hd[10])
            self.txtEmail.delete(0,END)
            self.txtEmail.insert(END,hd[11]) 
            
        def iExit():
            iExit = tkinter.messagebox.askyesno("Hotel Management Systems", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def Reset():
           
            Meal.set("")
            RoomType.set("")
            RoomNo.set("")
            RoomExtNo.set("")
            TotalCost.set("")
            Nationality.set("")         
            ProveOfID.set("")
            Gender.set("")
            TotalDays.set("")
            self.txtDOB.delete(0,END)
            self.txtEmail.delete(0,END) 
            self.txtCusID.delete(0,END) 
            self.txtFirstname.delete(0,END)
            self.txtSurname.delete(0,END)      
            self.txtAddress.delete(0,END) 
            self.txtPostCode.delete(0,END)    
            self.txtMobile.delete(0,END)            
            self.txtDateIn.delete(0,END)
            self.txtDateOut.delete(0,END)
            self.txtPaidTax.delete(0,END)
            self.txtSubTotal.delete(0,END)
            self.txtTotalCost.delete(0,END)
            DateIn.set(time.strftime("%d/%m/%Y")) # date
            DateOut.set(time.strftime("%d/%m/%Y"))

            x = random.randint(109, 5876)
            randomRef = str(x)
            CusID.set("Hot"+ randomRef)
 

        def DeleteData():
            if(len(CusID.get())!=0):
                hotelDatabase.deleteRec(hd[0])
                Reset()
                DisplayData()

        def searchDatabase():
            lstHotel.delete(0,END)
            for row in hotelDatabase.searchData(CusID.get(),Firstname.get(),Surname.get(),Address.get(),Gender.get(),Mobile.get(),
                                      Nationality.get(),ProveOfID.get(),DateIn.get(),DateOut.get(),Email.get()):
                lstHotel.insert(END,row,str(""))


        def update():
            if(len(CusID.get())!=0):
                hotelDatabase.deleteRec(hd[0])
            if(len(CusID.get())!=0):                
                hotelDatabase.addStdRec(CusID.get(),Firstname.get(),Surname.get(),Address.get(),Gender.get(),Mobile.get(),
                                      Nationality.get(),ProveOfID.get(),DateIn.get(),DateOut.get(),Email.get())           
                lstHotel.delete(0,END)            
                lstHotel.insert(END,(CusID.get(),Firstname.get(),Surname.get(),Address.get(),Gender.get(),Mobile.get(),
                                      Nationality.get(),ProveOfID.get(),DateIn.get(),DateOut.get(),Email.get()))

        def TotalCostandAddData():
            addData()

            
            InDate = DateIn.get()
            OutDate = DateOut.get()
            InDate = datetime.strptime(InDate, "%d/%m/%Y")
            OutDate = datetime.strptime(OutDate, "%d/%m/%Y")
            TotalDays.set(abs((OutDate - InDate).days))          
            
            if (Meal.get() == "Breakfast" and RoomType.get()=="Single"):

                q1 =float(17)
                q2 =float(34)
                q3 =float(TotalDays.get())
                q4 =float(q1 + q2)
                q5 = float(q3 * q4)
                Tax="£"+ str('%.2f'%((q5)*0.09))
                ST="£"+ str('%.2f'%((q5)))
                TT =  "£"+ str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif (Meal.get() == "Breakfast" and  RoomType.get() =="Double"):
                
                q1 =float(35)
                q2 =float(43)
                q3 =float(TotalDays.get())
                q4 =float(q1 + q2)
                q5 = float(q3 * q4)
                Tax="£"+ str('%.2f'%((q5)*0.09))
                ST="£"+ str('%.2f'%((q5)))
                TT =  "£"+ str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif (Meal.get() == "Breakfast" and  RoomType.get() =="Family"):
                
                q1 =float(45)
                q2 =float(63)
                q3 =float(TotalDays.get())
                q4 =float(q1 + q2)
                q5 = float(q3 * q4)
                Tax="£"+ str('%.2f'%((q5)*0.09))
                ST="£"+ str('%.2f'%((q5)))
                TT =  "£"+ str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)

            elif (Meal.get() == "Lunch" and  RoomType.get() =="Single"):
                
                q1 =float(29)
                q2 =float(37)
                q3 =float(TotalDays.get())
                q4 =float(q1 + q2)
                q5 = float(q3 * q4)
                Tax="£"+ str('%.2f'%((q5)*0.09))
                ST="£"+ str('%.2f'%((q5)))
                TT =  "£"+ str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif (Meal.get() == "Lunch" and  RoomType.get() =="Double"):
                
                q1 =float(37)
                q2 =float(43)
                q3 =float(TotalDays.get())
                q4 =float(q1 + q2)
                q5 = float(q3 * q4)
                Tax="£"+ str('%.2f'%((q5)*0.09))
                ST="£"+ str('%.2f'%((q5)))
                TT =  "£"+ str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif (Meal.get() == "Lunch" and  RoomType.get() =="Family"):
                
                q1 =float(46)
                q2 =float(63)
                q3 =float(TotalDays.get())
                q4 =float(q1 + q2)
                q5 = float(q3 * q4)
                Tax="£"+ str('%.2f'%((q5)*0.09))
                ST="£"+ str('%.2f'%((q5)))
                TT =  "£"+ str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)

            elif (Meal.get() == "Dinner" and  RoomType.get() =="Single"):
                
                q1 =float(28)
                q2 =float(37)
                q3 =float(TotalDays.get())
                q4 =float(q1 + q2)
                q5 = float(q3 * q4)
                Tax="£"+ str('%.2f'%((q5)*0.09))
                ST="£"+ str('%.2f'%((q5)))
                TT =  "£"+ str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif (Meal.get() == "Dinner" and  RoomType.get() =="Double"):
                
                q1 =float(30)
                q2 =float(43)
                q3 =float(TotalDays.get())
                q4 =float(q1 + q2)
                q5 = float(q3 * q4)
                Tax="£"+ str('%.2f'%((q5)*0.09))
                ST="£"+ str('%.2f'%((q5)))
                TT =  "£"+ str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif (Meal.get() == "Dinner" and  RoomType.get() =="Family"):
                
                q1 =float(43)
                q2 =float(63)
                q3 =float(TotalDays.get())
                q4 =float(q1 + q2)
                q5 = float(q3 * q4)
                Tax="£"+ str('%.2f'%((q5)*0.09))
                ST="£"+ str('%.2f'%((q5)))
                TT =  "£"+ str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)

            

        #=======================================Widget===========================================================
        self.lblCusID =Label(LeftFrame, font=('arial',12,'bold'),text="Customer Ref:",padx=1)
        self.lblCusID.grid(row=0,column=0, sticky =W)
        self.txtCusID =Entry(LeftFrame, font=('arial',12,'bold'),textvariable =CusID,width =18)#,state= DISABLED)
        self.txtCusID.grid(row=0,column=1,pady=3, padx=20)

        self.lblFirstname =Label(LeftFrame, font=('arial',12,'bold'),text="Firstname:",padx=1)
        self.lblFirstname.grid(row=1,column=0, sticky =W)
        self.txtFirstname =Entry(LeftFrame, font=('arial',12,'bold'),textvariable =Firstname,width =18)
        self.txtFirstname.grid(row=1,column=1,pady=3, padx=20)

        self.lblSurname =Label(LeftFrame, font=('arial',12,'bold'),text="Surname:",padx=1)
        self.lblSurname.grid(row=2,column=0, sticky =W)
        self.txtSurname =Entry(LeftFrame, font=('arial',12,'bold'),textvariable =Surname,width =18)
        self.txtSurname.grid(row=2,column=1,pady=3, padx=20)

        self.lblAddress =Label(LeftFrame, font=('arial', 12,'bold'), text="Address:",padx=1,pady=2 )
        self.lblAddress.grid(row=3, column=0,sticky=W)
        self.txtAddress=Entry(LeftFrame, font=('arial', 12,'bold'),textvariable = Address, width =18)
        self.txtAddress.grid(row=3, column=1, pady=3, padx=20)
        
        self.lblDOB =Label(LeftFrame, font=('arial', 12,'bold'), text="Date of Birth:",padx=2,pady=2)
        self.lblDOB.grid(row=4, column=0,sticky=W)
        self.txtDOB=Entry(LeftFrame, font=('arial', 12,'bold'),textvariable = DOB, width =18)
        self.txtDOB.grid(row=4, column=1, pady=3, padx=20)

        self.lblPostCode =Label(LeftFrame, font=('arial', 12,'bold'), text="PostCode:",padx=2,pady=2 )
        self.lblPostCode.grid(row=5, column=0,sticky=W)
        self.txtPostCode=Entry(LeftFrame, font=('arial', 12,'bold'),textvariable = PostCode, width =18)
        self.txtPostCode.grid(row=5, column=1, pady=3, padx=20)

        self.lblMobile =Label(LeftFrame, font=('arial', 12,'bold'), text="Mobile:",padx=2,pady=2)
        self.lblMobile.grid(row=6, column=0,sticky=W)
        self.txtMobile=Entry(LeftFrame,font=('arial', 12,'bold'),textvariable = Mobile,width =18)
        self.txtMobile.grid(row=6, column=1, pady=3, padx=20)

        self.lblEmail =Label(LeftFrame, font=('arial', 12,'bold'), text="Email:",padx=2,pady=2)
        self.lblEmail.grid(row=7, column=0,sticky=W)
        self.txtEmail=Entry(LeftFrame, font=('arial', 12,'bold'),textvariable = Email, width =18)
        self.txtEmail.grid(row=7, column=1, pady=3, padx=20)

        self.lblNationality =Label(LeftFrame,font=('arial',12,'bold'),text="Nationality:",padx=2,pady=2)
        self.lblNationality .grid(row=8, column=0,sticky=W)
        self.cboNationality=Entry(LeftFrame, font=('arial', 12,'bold'),textvariable = Nationality, width =18)
        self.cboNationality.grid(row=8, column=1, pady=3, padx=20)
        #self.cboNationality =ttk.Combobox(LeftFrame,textvariable= Nationality, state='readonly', font=('arial', 12,'bold'),width=16)                                        
        #self.cboNationality['value']=('','British','Nigeria','Kenya','India','Iran','Morocco','Canada', 'France','Norway')
        #self.cboNationality.current(0)
        #self.cboNationality.grid(row=8,column=1,pady=3,padx=2)



        self.lblGender =Label(LeftFrame, font=('arial', 12,'bold'), text="Gender:",padx=2,pady=2)
        self.lblGender.grid(row=9, column=0,sticky=W)
        self.cboGender =Entry(LeftFrame, font=('arial', 12,'bold'),textvariable = Gender, width =18)#,state= DISABLED
        self.cboGender.grid(row=9, column=1, pady=3, padx=20)
        #self.cboGender=ttk.Combobox(LeftFrame,textvariable=Gender, state='readonly',
                                        #font=('arial', 12,'bold'), width=16)
        #self.cboGender['value']=('','Male','Female')
        #self.cboGender.current(0)
        #self.cboGender.grid(row=10, column=1, pady=3, padx=2)

                                        

        self.lblDateIn =Label(LeftFrame,font=('arial', 12,'bold'),text="Check In Date:",padx=1,pady=2)                                   
        self.lblDateIn.grid(row=10, column=0,sticky=W)
        self.txtDateIn =Entry(LeftFrame, font=('arial', 12,'bold'),textvariable = DateIn, width =18)#,state= DISABLED
        self.txtDateIn.grid(row=10, column=1, pady=3, padx=20)

        self.lblDateOut=Label(LeftFrame,font=('arial',12,'bold'),text="Check Out Date:",padx=1,pady=2)                                     
        self.lblDateOut.grid(row=11, column=0,sticky=W)
        self.txtDateOut =Entry(LeftFrame,font=('arial', 12,'bold'),textvariable = DateOut,width =18)
        self.txtDateOut.grid(row=11, column=1, pady=3, padx=20)

        self.lblProveOfID =Label(LeftFrame, font=('arial', 12,'bold'),text="Type of ID:",padx=2,pady=2)
        self.lblProveOfID .grid(row=12, column=0,sticky=W)
        self.cboProveOfID =ttk.Combobox(LeftFrame,textvariable= ProveOfID, state='readonly', font=('arial', 12,'bold'),width=16)
        self.cboProveOfID['value'] = ('','Pilot Licence','Driving Licence','Student ID','Passport')
        self.cboProveOfID.current(0)
        self.cboProveOfID.grid(row=12,column=1,pady=3,padx=2)

        self.lblMeal =Label(LeftFrame, font=('arial', 12,'bold'), text="Meal:",padx=1,pady=2)
        self.lblMeal.grid(row=13, column=0,sticky=W)
        self.cboMeal=ttk.Combobox(LeftFrame,textvariable=Meal, state='readonly',font=('arial', 12,'bold'), width=16)                                        
        self.cboMeal['value']=('','Breakfast','Lunch','Dinner')
        self.cboMeal.current(0)
        self.cboMeal.grid(row=13, column=1, pady=3, padx=2)

        self.lblRoomType=Label(LeftFrame, font=('arial', 12,'bold'), text="Room Type:",padx=2,pady=2)
        self.lblRoomType.grid(row=14, column=0,sticky=W)
        self.cboRoomType=ttk.Combobox(LeftFrame,textvariable=RoomType, state='readonly',font=('arial', 12,'bold'), width=16)                                        
        self.cboRoomType['value']=('','Single','Double','Family')
        self.cboRoomType.current(0)
        self.cboRoomType.grid(row=14, column=1, pady=3, padx=2)

        self.lblRoomNo =Label(LeftFrame, font=('arial', 12,'bold'), text="Room No:",padx=2,pady=2)
        self.lblRoomNo.grid(row=15, column=0,sticky=W)
        self.cboRoomNo=ttk.Combobox(LeftFrame,textvariable=RoomNo, state='readonly',font=('arial', 12,'bold'), width=16)                                        
        self.cboRoomNo['value']=('','001','002','003','004','005','006')
        self.cboRoomNo.current(0)
        self.cboRoomNo.grid(row=15, column=1, pady=3, padx=2)

        self.lblRoomExtNo=Label(LeftFrame, font=('arial', 12,'bold'), text="Room Ext. No:",padx=2,pady=2)
        self.lblRoomExtNo.grid(row=16, column=0,sticky=W)
        self.cboRoomExtNo=ttk.Combobox(LeftFrame,textvariable=RoomExtNo, state='readonly',font=('arial', 12,'bold'), width=16)                                        
        self.cboRoomExtNo['value']=('','101','102','103','104','105','106')
        self.cboRoomExtNo.current(0)
        self.cboRoomExtNo.grid(row=16, column=1, pady=3, padx=2)  

        #======================================Receipt==================================================================
        self.lblLabel = Label(RightFrame1, font=('arial', 10, 'bold'),padx=6,pady=10,
        text="Customer Ref\tFirstname\tSurname\tAddress\tGender\tMobile\tNationality\tProveOfID\tDateIn\tDateOut\t\tEmail")
        self.lblLabel.grid(row = 0, column=0,columnspan=17)

        #=========================================Listbox and Scrollbar=======Receipt========================================
        scrollbar = Scrollbar(RightFrame2)
        scrollbar.grid(row=0, column=1, sticky ='ns')

        lstHotel = Listbox(RightFrame2, width = 103, height=14, font=('arial', 12,'bold'), yscrollcommand=scrollbar.set)#selectmode='multiple',exportselection=0,
        lstHotel.bind('<<ListboxSelect>>', HotelRec)
        lstHotel.grid(row=0, column=0, padx=7, sticky='nsew')
        scrollbar.config(command = lstHotel.xview)
     
        #========================================================================================================
        #box.bind('<<ListboxSelect>>', self.selected)
        #box.grid(row=1, column=col, sticky='nsew')
        #self.columnconfigure(col, weight=1)
        #=========================================Buttons Widget=====================================================
       
        self.lblDays= Label(RightFrame3,font=('arial', 14,'bold'), text="No. of Days", bd=7,)
        self.lblDays.grid(row=0,column=0, sticky=W)
        self.txtDays  = Entry(RightFrame3,font=('arial', 14,'bold'), textvariable=TotalDays, width=76, justify=LEFT)                               
        self.txtDays.grid(row=0,column=1)

        self.lblPaidTax = Label(RightFrame3,font=('arial', 14,'bold'), text="Paid Tax", bd=7)
        self.lblPaidTax.grid(row=1,column=0, sticky=W)
        self.txtPaidTax  = Entry(RightFrame3,font=('arial', 14,'bold'), textvariable=PaidTax,width=76, justify=LEFT)                               
        self.txtPaidTax.grid(row=1,column=1)

        self.lblSubTotal = Label(RightFrame3,font=('arial', 14,'bold'), text="Sub Total", bd=7,)
        self.lblSubTotal.grid(row=2,column=0, sticky=W)
        self.txtSubTotal= Entry(RightFrame3,font=('arial', 14,'bold'), textvariable=SubTotal,width=76, justify=LEFT)                                  
        self.txtSubTotal.grid(row=2,column=1)

        self.lblTotalCost = Label(RightFrame3,font=('arial', 14,'bold'), text="Total Cost", bd=7,)
        self.lblTotalCost.grid(row=3,column=0, sticky=W)
        self.txtTotalCost = Entry(RightFrame3,font=('arial', 14,'bold'), textvariable=TotalCost, width=76)                                  
        self.txtTotalCost.grid(row=3,column=1)
        #=================================================================================================================
        self.btnTotalandAddData=Button(BottomFrame,pady=1, bd=4, fg="black",font=('arial', 16,'bold'),
            width=13,height=2,text="AddNew/Total ",command=TotalCostandAddData).grid(row=0, column=0,padx=4)

        self.btnDisplay=Button(BottomFrame,pady=1, bd=4, fg="black",font=('arial', 16,'bold'),
                            width=13,height=2,text="Display", command=DisplayData).grid(row=0, column=1,padx=4)

        self.btnUpdate=Button(BottomFrame,pady=1, bd=4, fg="black",font=('arial', 16,'bold'),
                            width=13,height=2,text="Update",command=update).grid(row=0, column=2,padx=4)

        self.btnDelete=Button(BottomFrame,pady=1, bd=4, fg="black",font=('arial', 16,'bold'),
                    width=13,height=2, text="Delete", command=DeleteData).grid(row=0, column=3,padx=4)


        self.btnSearch=Button(BottomFrame,pady=1, bd=4, fg="black",font=('arial', 16,'bold'),
                            width=13,height=2,text="Search", command=searchDatabase).grid(row=0, column=4,padx=3)

        self.btnReset=Button(BottomFrame,pady=1, bd=4, fg="black",font=('arial', 16,'bold'),
                            width=13,height=2,text="Reset",command=Reset).grid(row=0, column=5,padx=4)

        self.btnExit=Button(BottomFrame,pady=1, bd=4, fg="black",font=('arial', 16,'bold'),
                    width=13,height=2, text="Exit", command=iExit).grid(row=0, column=6,padx=4)




if __name__=='__main__':
    root = Tk()
    application = Hotel (root)
    root.mainloop()
