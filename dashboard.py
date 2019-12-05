from tkinter import *
import os
import time
#functions that we need


def destroy_screen():
    screen3.destroy()

def destroy_screen2():
    screen7.destroy()

def destroy_screen3():
    screen11.destroy()
def destroy_screen8():
    screen8.destroy()


def saved():
    global screen7
    screen7 = Toplevel(screen)
    screen7.title('saved Successful')
    screen7.geometry('150x150')
    Label(screen7, text='Saved Successfully!').pack()
    Button(screen7, text='OK', command=destroy_screen2).pack()


def read_km():
    print('km _read')


def previous_km():

    print('previous')

def milage():

    print('milage')

def track_previous_km():

    previous_km_var1= read_km.get()
    file = open(previous_km_var, 'w')
    file.write(previous_km_var1 + '\n')
    file.close()

    screen8.destroy()


def read_value_km():
    previous_km_var1 = read_km.get()
    file = open(previous_km_var, 'r')
    file.read().splitlines()


def view_note2():
    global screen11


    try:
        data = open(file_name, 'r')
        data1 = data.read()
        screen11 = Toplevel(screen)
        screen11.title('Info')
        screen11.geometry('450x450')
        Label(screen11, text=data1).pack()
        Button(screen11,text='Close',command=destroy_screen3).pack()
    except:
        screen11 = Toplevel(screen)
        screen11.title('Warning')
        screen11.geometry('450x450')
        Label(screen11, text='No file found', fg='red').pack()
        Button(screen11, text='Close', command=destroy_screen3).pack()


def generate_report_servicing():
    global details
    global file_name
    global title
    localtime = time.asctime(time.localtime(time.time()))
    title=  "NAME -----  CATEGORY  -----      DATE OF TRANSACTION   ---------- PRICE "+'\n\n\n'+'----------------------------------------------------------------------'+'\n\n\n'
    details = userx +'    SERVICING' + '           ' + localtime + '              NRS ' + servicing_var.get() + '\n\n\n'
    file_name = 'statement'
    enter_trans()


def generate_report_grandtotal():
    global details
    global file_name
    localtime = time.asctime(time.localtime(time.time()))
    title=  "NAME -----  CATEGORY  -----      DATE OF TRANSACTION   ---------- PRICE "+'\n\n\n'+'----------------------------------------------------------------------'+'\n\n\n'
    details = userx+'      PETROL' + '           ' + localtime + '              NRS ' + str(grand_total) + '\n\n\n'
    file_name = 'statement'
    enter_trans()

def enter_trans():

    try:
        file1 = open(file_name, 'r')
        verify = file1.read().splitlines()
        print(verify)
        if 'NAME -----  CATEGORY  -----      DATE OF TRANSACTION   ---------- PRICE ' in verify:
            file1 = open(file_name, 'a')
            file1.write(details)
            file1.close()
            view_note2()
    except:

        file1 = open(file_name, 'a')
        file1.write(title)
        file1.write(details)
        file1.close()
        view_note2()

def bike_service():
    global screen15
    global servicing_var
    screen15 = Toplevel(screen)
    screen15.title('EXTRA EXPENSES')
    screen15.geometry('300x500')
    servicing_var = StringVar()

    Label(screen15, text="ENTER SERVICING FEE: ").pack()
    servicing_rate = Entry(screen15, textvariable=servicing_var)
    servicing_rate.pack()
    Label(screen15, text='').pack()
    Button(screen15, text='RECORD AND VIEW', command=generate_report_servicing, relief='sunken').pack()




def fuel_cons_calc():

    global screen8
    global read_km
    global previous_km
    global final_val
    global grand_total

    screen8 = Toplevel(screen)
    screen8.title('Fuel Consumed')
    screen8.geometry('500x400')
    read_km = read_km_var.get()
    previous_km = previous_km_var.get()
    petrol_rate = petrol_price_var.get()

    list_file = os.listdir()
    if previous_km_var==NONE:
        read_value_km()

    milage= milage_var.get()
    final_val = (int(read_km)- int(previous_km))/int(milage)
    grand_total = final_val * float(petrol_rate)
    Label(screen8, text= str(final_val)+' L fuel has been consumed').pack()
    Label(screen8, text='').pack()
    Label(screen8, text= 'Generate financial report?').pack()
    Label(screen8, text='').pack()
    Button(screen8, text='OK', command = generate_report_grandtotal).pack()
    Label(screen8, text='').pack()
    Button(screen8, text='cancel', command = destroy_screen8).pack()




def fin_stmt_dash():
    global screen10
    screen10 = Toplevel(screen)
    screen10.title('FINANCIAL TRACKER')
    screen10.geometry('300x500')

    Label(screen10, text='').pack()
    Label(screen10, text='Choose an Option').pack()
    # Label(screen10, text='').pack()
    # Button(screen10, text='Create Note', command=create_note).pack()
    Label(screen10, text='').pack()
    Button(screen10, text='VIEW STATEMENT', command=view_note).pack()
    Label(screen10, text='').pack()
    Button(screen10, text='DELETE STATEMENT', command=delete_notes).pack()
    Label(screen10, text='').pack()

#------SAVE NOTE FUNCTION------------
def save():
    file_name =  raw_filename.get()
    notes = raw_notes.get()

    file1 = open(file_name, 'w')
    file1.write(notes)
    file1.close()
    saved()



#------CREATE NOTE FUNCTION------------------

# def create_note():
#     global screen6
#
#     global raw_filename
#     raw_filename= StringVar()
#     global raw_notes
#     raw_notes =StringVar()
#
#     screen6= Toplevel(screen)
#     screen6.title('Info')
#     screen6.geometry('250x200')
#     Label(screen6, text='please enter a filename for you note').pack()
#     Entry(screen6,textvariable=raw_filename).pack()
#     Label(screen6, text='please enter a CONTENT for you note').pack()
#     Entry(screen6, textvariable=raw_notes).pack()
#     Button(screen6, text='SAVE!', command=save).pack()


#--------VIEW NOTE---------


def view_note():
    global screen10
    screen10 = Toplevel(screen)
    screen10.title('Info')
    screen10.geometry('250x200')
    all_files= os.listdir()
    Label(screen10, text='please use one of the files below:').pack()
    Label(screen10, text=all_files).pack()
    global raw_filename1
    raw_filename1=StringVar()

    Entry(screen10, textvariable=raw_filename1).pack()
    Button(screen10,command= view_note1, text='OK').pack()

def view_note1():
    global screen11
    screen10.destroy()
    file_name1 = raw_filename1.get()
    try:
        data = open(file_name1, 'r')
        data1 = data.read()
        screen11 = Toplevel(screen)
        screen11.title('Info')
        screen11.geometry('450x450')
        Label(screen11, text=data1).pack()
        Button(screen11,text='Close',command=destroy_screen3).pack()
    except:
        screen11 = Toplevel(screen)
        screen11.title('Warning')
        screen11.geometry('450x450')
        Label(screen11, text='No file found', fg='red').pack()
        Button(screen11, text='Close', command=destroy_screen3).pack()

#--------DELETE NOTES--------

def delete_notes():
    global screen14
    screen14 = Toplevel(screen)
    screen14.title('Info')
    screen14.geometry('250x200')
    all_files = os.listdir()
    Label(screen14, text='please use one of the files below to detele:').pack()
    Label(screen14, text=all_files).pack()
    global raw_filename5
    raw_filename5 = StringVar()

    Entry(screen14, textvariable=raw_filename5).pack()
    Button(screen14, command=delete_note1, text='OK').pack()


def delete_note1():
    global screen17
    screen14.destroy()
    try:
        file_name5 = raw_filename5.get()
        os.remove(file_name5)
        screen17 = Toplevel(screen)
        screen17.title('Info')
        screen17.geometry('450x450')
        Label(screen17, text='Are you sure you want to delete?',fg='red').pack()
        Button(screen17, text='YES', command=message_success).pack()
    except:
        screen17 = Toplevel(screen)
        screen17.title('Warning')
        screen17.geometry('450x450')
        Label(screen17, text='No file found', fg='red').pack()
        Button(screen17, text='Close', command=destroy_screen3).pack()

def destroy_screen18():
    screen18.destroy()
def message_success():
    global screen18
    screen17.destroy()
    screen18 = Toplevel(screen)
    screen18.title('Info')
    screen18.geometry('450x450')
    Label(screen18, text='Deleted Successfully!', fg='green').pack()
    Button(screen18, text='OK', command=destroy_screen18).pack()

#------------------- set variable ----------
# def set_var():
#
#     global screen14
#     global petrol_price_var
#     global milage_var
#     screen14 = Toplevel(screen)
#     screen14.title('SET YOURSELF')
#     screen14.geometry('300x500')
#     petrol_price_var = StringVar()
#     milage_var = StringVar()
#     Label(screen14,text='').pack()  # leaves an empty row
#     Label(screen14,text="ENTER TODAY'S PETROL RATE HERE: ").pack()
#     pertol_rate = Entry(screen14,text='petrol_price_var')
#     pertol_rate.pack()
#     Label(screen14,text='').pack() # leaves an empty row
#     Label(screen14,text='ENTER MILAGE HERE: ').pack()
#     milage = Entry(screen14, text='milage_var')
#     milage.pack()
#     Button(screen14, text='GO!',width=25, relief='ridge',command=session).pack()



def session():
    global screen5
    screen20.destroy()
    screen5 = Toplevel(screen)
    screen5.title('DASHBOARD')
    screen5.geometry('300x500')
    Label(screen5, text='Welcome '+userx, fg='green').pack()
    Label(screen5, text='').pack()
    Label(screen5, text='Choose an Option').pack()
    Label(screen5, text='').pack()
    global read_km_var
    global previous_km_var

    read_km_var= StringVar()
    previous_km_var = StringVar()

    Label(screen5,text='READ_KM').pack()
    read_km = Entry(screen5, textvariable=read_km_var)
    read_km.pack()

    Label(screen5,text='').pack()
    Label(screen5, text='PREVIOUS_KM').pack()
    previous_km = Entry(screen5, textvariable=previous_km_var)
    previous_km.pack()
    Label(screen5, text='').pack()
    Button(screen5, text='FUEL_CONSUMED', command=fuel_cons_calc).pack()


def dash_board():
    global screen20
    screen20 = Toplevel(screen)
    screen20.title('You are logged in')
    screen20.geometry('300x500')
    Label(screen20, text='SET PARAMETERS BEFORE YOU GO!').pack()
    Label(screen20, text='').pack()

    global milage_var
    global petrol_price_var

    petrol_price_var = StringVar()
    milage_var = StringVar()
    Label(screen20, text='').pack()
    Label(screen20, text='MILAGE').pack()
    milage = Entry(screen20, textvariable=milage_var)
    milage.pack()
    Label(screen20, text='').pack()
    Label(screen20, text='PETROL_PRICE/L').pack()
    petrol_price = Entry(screen20, textvariable=petrol_price_var)
    petrol_price.pack()
    Button(screen20, text='CONTINUE', relief='sunken',command=session).pack()
#------------mode for financial statement--------------------------

    menubar = Menu(screen, font=('arial', 25), tearoff=0)

    mode = Menu(menubar)

    mode.add_checkbutton(label="fin_statement", command=fin_stmt_dash)

    mode.add_checkbutton(label="extras", command=bike_service)

    menubar.add_cascade(label='Mode', menu=mode)
    screen.config(menu=menubar)





def login_success():
    dash_board()


def password_not_match():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title('password error!')
    screen3.geometry('190x100')
    Label(screen3, text='password error!', fg='red').pack()
    Button(screen3, text='OK', command=destroy_screen).pack()

def user_not_found():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title('User Not Found')
    screen3.geometry('190x100')
    Label(screen3, text='User Not Found', fg='red').pack()
    Button(screen3, text='OK', command=destroy_screen).pack()



def login_verify():
    global userx
    userx = user_verify.get()
    passx = password_verify.get()
    user2.delete(0,END)
    pass2.delete(0,END)
    screen_login.destroy()
    list_of_file = os.listdir()




    if userx in list_of_file:
        file1 = open(userx,'r')
        verify = file1.read().splitlines()

        print(verify)

        if passx in verify:
            login_success()
        else:
            password_not_match()
    else:
        user_not_found()


def register_fun():
    user_info= username.get()
    password_info = password.get()
    screen_reg.destroy()
    file=open(user_info,'w')
    file.write(user_info+'\n')
    file.write(password_info)
    file.close()


    user_entry.delete(0,END)
    password_entry.delete(0,END)

    Label(screen_reg, text='registration_successful', fg='green', bg='white').pack()




def login():
    global screen_login

    screen_login= Toplevel(screen)
    screen_login.title('Login')
    screen_login.geometry('300x500')
    Label(screen_login, text='Please enter your details to login',bg='pink').pack()
    Label(screen_login,text='').pack()



    global user_verify
    global password_verify

    user_verify = StringVar()
    password_verify = StringVar()

    global user2
    global pass2

    Label(screen_login, text='Username *').pack()
    user2 = Entry(screen_login, textvariable=user_verify)
    user2.pack()
    Label(screen_login, text='').pack()
    Label(screen_login, text='password*').pack()
    pass2= Entry(screen_login, textvariable=password_verify)
    pass2.pack()
    Button(screen_login, text='LOGIN', width=25, height=2, fg='pink',command=login_verify).pack()

#funtion for pic_label
def pic_label(screen_name):
    pic = PhotoImage(file='image/dash.gif')
    imglabel = Label(screen_name, image=pic)
    imglabel.pack(side=TOP)




def registration():
    global screen_reg
    screen_reg = Toplevel(screen)
    screen_reg.title('Registration ')
    screen_reg.geometry('300x500')




    global username
    global password
    global user_entry
    global password_entry

    username =StringVar()
    password=StringVar()

    Label(screen_reg, text='PLEASE ENTER YOU DETAILS', font=('Calibri',20), bg='pink').pack()

    Label(screen_reg,text='').pack()

    Label(screen_reg,text='username*').pack()
    user_entry=Entry(screen_reg,textvariable=username)
    user_entry.pack()
    Label(screen_reg,text='Password*').pack()
    password_entry= Entry(screen_reg,textvariable=password)
    password_entry.pack()
    Label(screen_reg, text='').pack()
    Button(screen_reg,text='REGISTER', width='30', height=2, command=register_fun).pack()









def main_screen():
    global screen
    screen = Tk()
    screen.geometry('300x500')
    screen.title('FUEL_CONSUMPTION')
    Label(text='2 WHEEL TRACKER', bg='grey', width= '300', height='3', font=('Calibri',25)).pack()


    #----------------- calling PICTURE LABEL ---------------------------------

    pic = PhotoImage(file='image/dash.gif')
    imglabel = Label(screen, image=pic)
    imglabel.pack(side=TOP)

    Label(text='') #leaves an empty row
    Button(text='login',width= '30', height='3',command=login).pack()
    Label(text='') #leaves an empty row

    Button(text='Register',width= '30', height='3',command=registration).pack()

    #-------------------menu----------------------------



    screen.mainloop()

main_screen()


