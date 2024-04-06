#import section
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import *

# initialising login window
login = Tk()

# setting attributes of login window
login.title('Login')
login.minsize(500,500)
login.maxsize(500,500)
login.configure(background='#0096DC')

#function for handling login
correct_mail = 'abc@gmail.com'
correct_password = '123abc'
def handle_login():

    # fetching data from form
    mail=email_input.get()
    password=password_input.get()

    # when either of the field is empty
    if mail=='' or password=='':
        messagebox.showwarning('warning','Please fill out all the fields')

    # when user enters correct credentials
    elif mail==correct_mail and password==correct_password:
        messagebox.showinfo('Success','Login Successful')

        # destroy the login window
        login.destroy()
        
        # initialise the new window for dashboard
        dashboard = Tk()

        # setting attributes of 
        dashboard.title('Dashboard')
        dashboard.geometry('1366x768')
        # dashboard.resizable(False,False)
        dashboard.configure(background='#eff5f6')
        
        #------------- header section----------------------

        #creating header frame
        header = Frame(dashboard,bg='#009df4')
        header.place(x=300, y=0, width=1070, height=60)

        # logout button
        logout = Button(header, text='logout',bg="#32cf8e",font=("verdana",13,'bold'),bd=0,fg='white')
        logout.place(x=950,y=15)

        #------------- header section----------------------


        #--------------side bar----------------------------

        #creating side bar frame
        sidebar = Frame(dashboard, bg='#ffffff')
        sidebar.place(x=0,y=0,width=300,height=750)

        #logo
        logoImage = Image.open('images\hyy.png')
        photo = ImageTk.PhotoImage(logoImage)
        logo = Label(sidebar, image=photo, bg='#ffffff')
        logo.image = photo
        logo.place(x=70, y=80)

        #name 
        name = Label(sidebar,text='ABC',bg='#ffffff',font=("verdana",15,'bold'))
        name.place(x=120, y=200)

        # menu - dashboard
        #image
        dash_image = Image.open('images\dashboard-icon.png')
        photo = ImageTk.PhotoImage(dash_image)
        dash = Label(sidebar,image=photo, bg='#ffffff')
        dash.image = photo
        dash.place(x=35, y=289)
        #text
        dash_text = Label(sidebar, text='Dashboard',bg='#ffffff', cursor='hand2',activebackground='#ffffff')
        dash_text.place(x=80, y=287)


        # menu 
        # 1. dashboard
        #image
        dash_image = Image.open('images\dashboard-icon.png')
        photo = ImageTk.PhotoImage(dash_image)
        dash = Label(sidebar,image=photo, bg='#ffffff')
        dash.image = photo
        dash.place(x=35, y=289)
        #text
        dash_text = Button(sidebar, text='Dashboard',bg='#ffffff', cursor='hand2',activebackground='#ffffff',font=("verdana",13,'bold'),bd=0)
        dash_text.place(x=80, y=287)

        # 2. manage
        #image
        manage_image = Image.open('images\manage-icon.png')
        photo = ImageTk.PhotoImage(manage_image)
        manage = Label(sidebar,image=photo, bg='#ffffff')
        manage.image = photo
        manage.place(x=35, y=340)
        #text
        manage_text = Button(sidebar, text='Manage',bg='#ffffff', cursor='hand2',activebackground='#ffffff',font=("verdana",13,'bold'),bd=0)
        manage_text.place(x=80, y=345)

        # 3. settings
        #image
        setting_image = Image.open('images\settings-icon.png')
        photo = ImageTk.PhotoImage(setting_image)
        setting = Label(sidebar,image=photo, bg='#ffffff')
        setting.image = photo
        setting.place(x=35, y=402)
        #text
        setting_text = Button(sidebar, text='Settings',bg='#ffffff', cursor='hand2',activebackground='#ffffff',font=("verdana",13,'bold'),bd=0)
        setting_text.place(x=80, y=402)

        # 4. Exit
        # image
        exit_image = Image.open('images\exit-icon.png')
        photo = ImageTk.PhotoImage(exit_image)
        exit = Label(sidebar,image=photo, bg='#ffffff')
        exit.image = photo
        exit.place(x=25, y=452)
        # text
        exit_text = Button(sidebar, text='Exit',bg='#ffffff', cursor='hand2',activebackground='#ffffff',font=("verdana",13,'bold'),bd=0)
        exit_text.place(x=85, y=462)

        #--------------side bar----------------------------


        #----------------body-------------------------------
        heading = Label(dashboard,text='Dashboard',font=("verdana",13,'bold'),fg='#0064d3',bg='#eff5f6')
        heading.place(x=325, y=70)

        # body frame 1
        bframe1 = Frame(dashboard, bg='#ffffff')
        bframe1.place(x=328,y=110,width=1040,height=350)

        # body frame 2
        bframe2 = Frame(dashboard, bg='#009aa5')
        bframe2.place(x=328,y=492,width=310,height=220)

        # body frame 3
        bframe3 = Frame(dashboard, bg='#e21f26')
        bframe3.place(x=680,y=495,width=310,height=220)

        # body frame 4
        bframe4 = Frame(dashboard, bg='#ffcb1f')
        bframe4.place(x=1030,y=495,width=310,height=220)

        # Pie Chart
        piechart_image = Image.open('images\pie-graph1.png')
        photo = ImageTk.PhotoImage(piechart_image)
        piechart = Label(bframe1,image=photo, bg='#ffffff')
        piechart.image = photo
        piechart.place(x=690, y=70)

         # Graph
        graph_image = Image.open('images\graph.png')
        photo = ImageTk.PhotoImage(graph_image)
        graph = Label(bframe1,image=photo, bg='#ffffff')
        graph.image = photo
        graph.place(x=40, y=70)

        # total people
        # image
        totalpeople_image = Image.open('images\left-icon.png')
        photo = ImageTk.PhotoImage(totalpeople_image)
        totalpeople = Label(bframe2,image=photo, bg='#009aa5')
        totalpeople.image = photo
        totalpeople.place(x=220, y=0)
        # text
        totalpeople_text = Label(bframe2, text='Total People',bg='#009aa5',font=("verdana",13,'bold'))
        totalpeople_text.place(x=5, y=5)

        totalpeopleno_text = Label(bframe2, text='230',bg='#009aa5',font=("verdana",25,'bold'))
        totalpeopleno_text.place(x=120, y=100)


        # people left
        # image
        peopleleft_image = Image.open('images\left-icon.png')
        photo = ImageTk.PhotoImage(peopleleft_image)
        peopleleft = Label(bframe3,image=photo, bg='#e21f26')
        peopleleft.image = photo
        peopleleft.place(x=220, y=0)
        # text
        peopleleft_text = Label(bframe3, text='People Left',bg='#e21f26',font=("verdana",13,'bold'))
        peopleleft_text.place(x=5, y=5)

        peopleleftno_text = Label(bframe3, text='100',bg='#e21f26',font=("verdana",25,'bold'))
        peopleleftno_text.place(x=120, y=100)


        # Earnings
        # image
        Earning_image = Image.open('images\earn3.png')
        photo = ImageTk.PhotoImage(Earning_image)
        Earning = Label(bframe4,image=photo, bg='#ffcb1f')
        Earning.image = photo
        Earning.place(x=220, y=0)
        # text
        Earning_text = Label(bframe4, text='Earnings',bg='#ffcb1f',font=("verdana",13,'bold'))
        Earning_text.place(x=5, y=5)

        Earning_figure = Label(bframe4, text='$40,000.00',bg='#ffcb1f',font=("verdana",25,'bold'))
        Earning_figure.place(x=80, y=100)

        #----------------body-------------------------------
        
    
        dashboard.mainloop()
    
    # when either of the credential is wrong
    else:
        messagebox.showerror('error','Incorrect Mail or Password')



#login title
login_label = Label(login,text="Login",bg='#0096DC',fg='white')
login_label.pack(pady=30)
login_label.configure(font=('verdana',20,'bold'))

#email label and field 
email_label = Label(login, text='Enter your Email',font=('verdana',12),fg='white',bg='#0096DC')
email_label.pack(pady=(50,10))
email_input = Entry(login, width=50)
email_input.pack(pady=(10,20),ipady=5)

#email label and field 
password_label = Label(login, text='Enter your Password',font=('verdana',12),fg='white',bg='#0096DC')
password_label.pack(pady=(20,10))
password_input = Entry(login, width=50)
password_input.pack(pady=(10,50),ipady=5)

#login button
login_btn = Button(login,text='Login',font=('verdana',8,'bold'),fg='black',bg='white',width=15,command=handle_login)
login_btn.pack(pady=(5,50),ipady=10)


login.mainloop()