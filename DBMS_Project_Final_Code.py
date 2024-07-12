# HEADER_FILES

import random
import mysql.connector
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.spinner import Spinner
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.core.window import Window

# DATABASE_INFO

DATABASE_NAME = 'wholesale'
USERS_TABLE = 'customer'

# DATABASE_CONNECTION

db = mysql.connector.connect(host='localhost', database=DATABASE_NAME, user='root', password='password',
                             autocommit=True)
c = db.cursor()

# ADMIN_INFO

ADMIN_FN = 'Admin'
ADMIN_LN = '123'
ADMIN_PASS = '123456'
ADMIN_ID = '0001'

# Global_Variables

CUSTOMER_ID = ''
text1 = ''
text2 = ''

Window.maximize()


# FUNCTION_DEFINITIONS

def text_call_1():
    global text1;
    text1 = ''


def text_call_2():
    global text2;
    text2 = ''


def Refresh():
    c.execute("select distinct OrderNo from CustTest where Status = 'Active' order by OrderNo;")
    o = c.fetchall()
    UpdCan.activeorders = tuple()
    for el in o:
        UpdCan.activeorders += (str(el[0]),)
    UpdCan.dropdown_spinner1 = Spinner(text='Active Orders',
                                       values=tuple(UpdCan.activeorders),
                                       size_hint=(0.20, 0.1),
                                       pos_hint={'center_x': 0.15,
                                                 'center_y': 0.65},
                                       font_size=15)


def pass_check(self, password1, password2):
    error = 0
    digit_present_pass = 0
    upper_case_present_pass = 0
    spaces_present_pass = 0
    sp_char_present_pass = 0

    for p in password1:
        if p.isdigit():
            digit_present_pass = 1
        elif p.isspace():
            spaces_present_pass = 1
        elif not p.isalnum():
            sp_char_present_pass = 1
        elif p.isupper():
            upper_case_present_pass = 1

    if password1 == '' or password2 == '':
        error = 1
        self.promt_password.text = 'Fill both pasword blanks'
    elif password1 != password2:
        error = 1
        self.promt_password.text = 'Password Mismatch!'
    elif len(password1) < 8:
        error = 1
        self.promt_password.text = 'Password should be longer than 8 characters'
    elif spaces_present_pass == 1:
        error = 1
        self.promt_password.text = 'Password should not include spaces.'
    elif digit_present_pass == 0 or sp_char_present_pass == 0 or upper_case_present_pass == 0:
        error = 1
        self.promt_password.text = 'Password should contain a digit, an upper case character and a special character'

    return error


# MAIN



class ScreenManagement(ScreenManager):
    def __init__(self, **kwargs):
        super(ScreenManagement, self).__init__(**kwargs)


class LoginPage(Screen):
    def __init__(self, **kwargs):
        super(LoginPage, self).__init__(**kwargs)
        self.clear_widgets()
        self.add_widget(Label(text='LOGIN',
                              font_size=30,
                              bold=True,
                              pos_hint={'center_x': .5,
                                        'center_y': .8}))

        self.add_widget(Label(text='User Name :',
                              font_size=20,
                              pos_hint={'center_x': .405,
                                        'center_y': .66}))

        self.username = TextInput(multiline=False,
                                  size_hint=(.2, .055),
                                  font_size=20,
                                  pos_hint={'center_x': .55,
                                            'center_y': .66})
        self.add_widget(self.username)

        self.promt_username = Label(text='',
                                    color=[1, 0, 0, 1],
                                    font_size=12,
                                    pos_hint={'center_x': .73,
                                              'center_y': .66})
        self.add_widget(self.promt_username)

        self.add_widget(Label(text='Customer ID :',
                              font_size=20,
                              pos_hint={'center_x': .4,
                                        'center_y': .60}))

        self.ID = TextInput(multiline=False,
                            size_hint=(.2, .055),
                            font_size=20,
                            pos_hint={'center_x': .55,
                                      'center_y': .60})
        self.add_widget(self.ID)

        self.promt_ID = Label(text='',
                              color=[1, 0, 0, 1],
                              font_size=12,
                              pos_hint={'center_x': .73,
                                        'center_y': .60})
        self.add_widget(self.promt_ID)

        self.add_widget(Label(text='Password :',
                              font_size=20,
                              pos_hint={'center_x': .41,
                                        'center_y': .54}))

        self.password = TextInput(password=True,
                                  multiline=False,
                                  font_size=20,
                                  size_hint=(.2, .055),
                                  pos_hint={'center_x': .55,
                                            'center_y': .54})
        self.add_widget(self.password)

        self.promt_password = Label(text='',
                                    color=[1, 0, 0, 1],
                                    font_size=12,
                                    pos_hint={'center_x': .73,
                                              'center_y': .54})
        self.add_widget(self.promt_password)

        self.add_widget(Label(text="Don't have an Account?",
                              font_size=10,
                              pos_hint={'center_x': .3,
                                        'center_y': .4}))

        self.Create_Acc = Button(text='Create Account', size_hint=(.17, .05),
                                 font_size=15,
                                 pos_hint={'center_x': .3,
                                           'center_y': .35},
                                 on_press=self.screen_transition_Acc)
        self.add_widget(self.Create_Acc)

        self.add_widget(Label(text="Don't remember your password?",
                              font_size=10,
                              pos_hint={'center_x': .7,
                                        'center_y': .4}))

        self.Forgot_Password = Button(text='Forgot Password', size_hint=(.17, .05),
                                      font_size=15,
                                      pos_hint={'center_x': .7,
                                                'center_y': .35},
                                      on_press=self.screen_transition_FP)
        self.add_widget(self.Forgot_Password)

        self.add_widget(Label(text="Don't remember your Customer-ID?",
                              font_size=10,
                              pos_hint={'center_x': .5,
                                        'center_y': .4}))

        self.Forgot_Cust_ID = Button(text='Forgot Customer-ID', size_hint=(.17, .05),
                                     font_size=15,
                                     pos_hint={'center_x': .5,
                                               'center_y': .35},
                                     on_press=self.screen_transition_FC)
        self.add_widget(self.Forgot_Cust_ID)

        self.add_widget(Button(text='Enter',
                               size_hint=(.1, .05),
                               font_size=15,
                               pos_hint={'center_x': .5,
                                         'center_y': .25},
                               on_press=self.Login_Check))

        lab1 = Label(text='Contact Information',
                     bold=True,
                     size_hint=(None, None),
                     pos_hint={'center_x': .5,
                               'center_y': .1})
        self.add_widget(lab1)

        lab2 = Label(text='Phone: +971 5X XXX XXXX',
                     size_hint=(None, None),
                     pos_hint={'center_x': .5,
                               'center_y': .065})
        self.add_widget(lab2)

        lab3 = Label(text='Email: warehousexxx@gmail.com',
                     size_hint=(None, None),
                     pos_hint={'center_x': .5,
                               'center_y': .032})
        self.add_widget(lab3)

    def Login_Check(self, instance):
        self.promt_username.text = ''
        self.promt_password.text = ''
        self.promt_ID.text = ''
        error = 0

        username = self.username.text
        password = self.password.text
        ID = self.ID.text

        if username == ADMIN_FN and password == ADMIN_PASS and ID == ADMIN_ID:
            self.username.text = ''
            self.password.text = ''
            self.ID.text = ''
            self.manager.current = 'Admin Page'
        else:
            if username == '':
                error = 1
                self.promt_username.text = 'Enter the Username'
            if password == '':
                error = 1
                self.promt_password.text = 'Enter the Password'
            if ID == '':
                error = 1
                self.promt_ID.text = 'Enter the Customer Id'

            if error == 0:
                c.execute("select * from %s" % (USERS_TABLE))
                user_info = c.fetchall()
                invalid_username = invalid_password = invalid_ID = 1
                together = 0
                for i in user_info:
                    if username in [i[1], i[2]]:
                        invalid_username = 0
                    if password == i[3]:
                        invalid_password = 0
                    if ID == i[0]:
                        invalid_ID = 0
                    if username in [i[1], i[2]] and password == i[3] and ID == i[0]:
                        together = 1
                if not (invalid_password == 0 and invalid_username == 0 and invalid_ID == 0):
                    if bool(invalid_username):
                        self.promt_username.text = 'Invalid Username'
                    if bool(invalid_password):
                        self.promt_password.text = 'Invalid Password'
                    if bool(invalid_ID):
                        self.promt_ID.text = 'Invalid Customer ID'
                elif invalid_password == 0 and invalid_username == 0 and invalid_ID == 0 and together == 1:
                    global CUSTOMER_ID
                    global FNAME
                    CUSTOMER_ID = ID
                    FNAME = username
                    Customer.custname = Label(text="Welcome, " + FNAME + "!",
                                              pos_hint={"center_x": 0.5,
                                                        "center_y": 0.90},
                                              size_hint=(0.05, 0.05),
                                              font_size=30)
                    self.manager.current = 'Customer'
                    self.username.text = ''
                    self.password.text = ''
                    self.ID.text = ''
                elif together == 0:
                    self.promt_username.text = 'Invalid Acc.'
                    self.promt_password.text = 'Invalid Acc.'
                    self.promt_ID.text = 'Invalid Acc.'

    def reset_page(self, *args):
        self.username.text = ''
        self.password.text = ''
        self.ID.text = ''
        self.promt_username.text = ''
        self.promt_password.text = ''
        self.promt_ID.text = ''

    def screen_transition_Acc(self, *args):
        self.reset_page()
        self.manager.current = 'Create-Acc'

    def screen_transition_FP(self, *args):
        self.reset_page()
        self.manager.current = 'FP'

    def screen_transition_FC(self, *args):
        self.reset_page()
        self.manager.current = 'FC'


class Create_Acc(Screen):
    def __init__(self, **kwargs):
        super(Create_Acc, self).__init__(**kwargs)
        self.add_widget(Label(text='Enter your First Name* :',
                              font_size=20,
                              pos_hint={'center_x': .41,
                                        'center_y': .7}))

        self.fname = TextInput(multiline=False,
                               size_hint=(.2, .055),
                               font_size=20,
                               pos_hint={'center_x': .60,
                                         'center_y': .7})
        self.add_widget(self.fname)

        self.promt_fname = Label(text='',
                                 color=[1, 0, 0, 1],
                                 font_size=12,
                                 pos_hint={'center_x': .83,
                                           'center_y': .7})
        self.add_widget(self.promt_fname)

        self.add_widget(Label(text='Enter your Last Name* :',
                              font_size=20,
                              pos_hint={'center_x': .41,
                                        'center_y': .64}))

        self.lname = TextInput(multiline=False,
                               size_hint=(.2, .055),
                               font_size=20,
                               pos_hint={'center_x': .60,
                                         'center_y': .64})
        self.add_widget(self.lname)

        self.promt_lname = Label(text='',
                                 color=[1, 0, 0, 1],
                                 font_size=12,
                                 pos_hint={'center_x': .83,
                                           'center_y': .64})
        self.add_widget(self.promt_lname)

        self.add_widget(Label(text='Create Password* :',
                              font_size=20,
                              pos_hint={'center_x': .425,
                                        'center_y': .57}))

        self.password1 = TextInput(password=True,
                                   multiline=False,
                                   font_size=20,
                                   size_hint=(.2, .055),
                                   pos_hint={'center_x': .60,
                                             'center_y': .57})
        self.add_widget(self.password1)

        self.add_widget(Label(text='Confirm Password* :',
                              font_size=20,
                              pos_hint={'center_x': .42,
                                        'center_y': .51}))

        self.password2 = TextInput(password=True,
                                   multiline=False,
                                   font_size=20,
                                   size_hint=(.2, .055),
                                   pos_hint={'center_x': .60,
                                             'center_y': .51})
        self.add_widget(self.password2)

        self.promt_password = Label(text='',
                                    color=[1, 0, 0, 1],
                                    font_size=12,
                                    pos_hint={'center_x': .60,
                                              'center_y': .46})
        self.add_widget(self.promt_password)

        self.Create_ID_Button = Button(text='Create ID',
                                       size_hint=(.1, .05),
                                       font_size=15,
                                       pos_hint={'center_x': .5,
                                                 'center_y': .40},
                                       on_press=self.ID_Creation)
        self.add_widget(self.Create_ID_Button)

        self.ID = Label(text='',
                        font_size=30,
                        pos_hint={'center_x': .50,
                                  'center_y': .33})
        self.add_widget(self.ID)

        self.Done_Back = Button(text='Back',
                                size_hint=(.1, .05),
                                font_size=15,
                                pos_hint={'center_x': .5,
                                          'center_y': .20},
                                on_press=self.screen_transition_Login)
        self.add_widget(self.Done_Back)

    def ID_Creation(self, instance):

        self.promt_fname.text = ''
        self.promt_lname.text = ''
        self.promt_password.text = ''
        error = 0

        password1 = self.password1.text
        password2 = self.password2.text
        fname = self.fname.text.capitalize()
        lname = self.lname.text.capitalize()

        # Checks for Digits, Special Characters , Spaces and Upper case letters.
        digit_present_fname = 0
        spaces_present_fname = 0
        sp_char_present_fname = 0

        digit_present_lname = 0
        spaces_present_lname = 0
        sp_char_present_lname = 0

        # Checking...
        for f in fname:
            if f.isdigit():
                digit_present_fname = 1
            elif f.isspace():
                spaces_present_fname = 1
            elif not f.isalnum():
                sp_char_present_fname = 1
        for l in lname:
            if l.isdigit():
                digit_present_lname = 1
            elif l.isspace():
                spaces_present_lname = 1
            elif not l.isalnum():
                sp_char_present_lname = 1

        if fname == '':
            error = 1
            self.promt_fname.text = 'Enter your First name.'
        elif digit_present_fname == 1 or spaces_present_fname == 1 or sp_char_present_fname == 1:
            error = 1
            self.promt_fname.text = "The name shouldn't contain spaces, digits or special chracters. "

        if lname == '':
            error = 1
            self.promt_lname.text = 'Enter your Last name.'
        elif digit_present_lname == 1 or spaces_present_lname == 1 or sp_char_present_lname == 1:
            error = 1
            self.promt_lname.text = "The name shouldn't contain spaces,\n digits or special chracters. "

        if error == 0 and pass_check(self, password1, password2) == 0:
            idc = fname[slice(2)] + lname[slice(2)] + str(random.randint(1000, 9999))
            self.ID.text = idc

            # Adding info to the database
            c.execute("insert into %s values('%s','%s','%s','%s')" % (USERS_TABLE, idc, fname, lname, password1))
            db.commit()

            # Creating the table for customer
            # Code: create table using 'Customer ID' as name.

            self.Done_Back.text = 'Done'
            self.remove_widget(self.Create_ID_Button)

    def screen_transition_Login(self, *args):
        self.promt_fname.text = ''
        self.promt_lname.text = ''
        self.promt_password.text = ''
        self.password1.text = ''
        self.password2.text = ''
        self.fname.text = ''
        self.lname.text = ''
        self.manager.current = 'Login'


class Forgot_Password(Screen):
    def __init__(self, **kwargs):
        super(Forgot_Password, self).__init__(**kwargs)
        self.add_widget(Label(text='Forgot Password',
                              font_size=30,
                              pos_hint={'center_x': .5,
                                        'center_y': .8}))

        self.add_widget(Label(text='First Name :',
                              font_size=20,
                              pos_hint={'center_x': .4,
                                        'center_y': .6}))

        self.fname = TextInput(multiline=False,
                               size_hint=(.2, .055),
                               font_size=20,
                               pos_hint={'center_x': .55,
                                         'center_y': .6})
        self.add_widget(self.fname)

        self.promt_fname = Label(text='',
                                 color=[1, 0, 0, 1],
                                 font_size=12,
                                 pos_hint={'center_x': .83,
                                           'center_y': .6})
        self.add_widget(self.promt_fname)

        self.add_widget(Label(text='Last Name :',
                              font_size=20,
                              pos_hint={'center_x': .4,
                                        'center_y': .5}))

        self.lname = TextInput(multiline=False,
                               size_hint=(.2, .055),
                               font_size=20,
                               pos_hint={'center_x': .55,
                                         'center_y': .5})
        self.add_widget(self.lname)

        self.promt_lname = Label(text='',
                                 color=[1, 0, 0, 1],
                                 font_size=12,
                                 pos_hint={'center_x': .83,
                                           'center_y': .5})
        self.add_widget(self.promt_lname)

        self.add_widget(Label(text='Customer ID :',
                              font_size=20,
                              pos_hint={'center_x': .395,
                                        'center_y': .4}))

        self.ID = TextInput(multiline=False,
                            font_size=20,
                            size_hint=(.2, .055),
                            pos_hint={'center_x': .55,
                                      'center_y': .4})
        self.add_widget(self.ID)

        self.promt_ID = Label(text='',
                              color=[1, 0, 0, 1],
                              font_size=12,
                              pos_hint={'center_x': .83,
                                        'center_y': .4})
        self.add_widget(self.promt_ID)

        self.add_widget(Button(text='Enter',
                               size_hint=(.1, .05),
                               font_size=15,
                               pos_hint={'center_x': .5,
                                         'center_y': .3},
                               on_press=self.Pass_Check))

        self.passw = Label(text='',
                           font_size=30,
                           pos_hint={'center_x': .50,
                                     'center_y': .23})
        self.add_widget(self.passw)

        self.Create_Acc = Button(text='Create_Acc',
                                 size_hint=(.17, .05),
                                 font_size=15,
                                 pos_hint={'center_x': .5,
                                           'center_y': .1},
                                 on_press=self.screen_transition_Acc)

    def Pass_Check(self, instance):
        self.promt_fname.text = ''
        self.promt_lname.text = ''
        self.promt_ID.text = ''
        error = 0

        fname = self.fname.text
        lname = self.lname.text
        ID = self.ID.text
        self.remove_widget(self.Create_Acc)

        if fname == '':
            error = 1
            self.promt_fname.text = 'Enter the First Name'
        if lname == '':
            error = 1
            self.promt_lname.text = 'Enter the Last Name'
        if ID == '':
            error = 1
            self.promt_ID.text = 'Enter the Customer Id'

        if error == 0:
            c.execute("select * from %s" % (USERS_TABLE))
            user_info = c.fetchall()
            invalid_fname = invalid_lname = invalid_ID = 1
            together = 0
            for i in user_info:
                if fname == i[1]:
                    invalid_fname = 0
                if lname == i[2]:
                    invalid_lname = 0
                if ID == i[0]:
                    invalid_ID = 0
                if (ID, fname, lname) == i[:3]:
                    together = 1
            if bool(invalid_fname):
                self.promt_username.text = 'Invalid First Name'
            if bool(invalid_lname):
                self.promt_lname.text = 'Invalid Last Name'
            if bool(invalid_ID):
                self.promt_ID.text = 'Invalid Customer ID'

            if invalid_fname == 0 and invalid_lname == 0 and invalid_ID == 0 and together == 1:
                global CUSTOMER_ID
                CUSTOMER_ID = ID
                self.manager.current = 'UP'
            else:
                self.promt_fname.text = 'No such account found!'
                self.promt_lname.text = 'No such account found!'
                self.promt_ID.text = 'No such account found!'
                self.add_widget(self.Create_Acc)

    def screen_transition_Acc(self, *args):
        self.promt_fname.text = ''
        self.promt_lname.text = ''
        self.promt_ID.text = ''
        self.fname.text = ''
        self.lname.text = ''
        self.ID.text = ''
        self.manager.current = 'Create-Acc'


class Update_Pass(Screen):
    def __init__(self, **kwargs):
        super(Update_Pass, self).__init__(**kwargs)

        self.add_widget(Label(text='Update Password* :',
                              font_size=20,
                              pos_hint={'center_x': .425,
                                        'center_y': .57}))

        self.password1 = TextInput(password=True,
                                   multiline=False,
                                   font_size=20,
                                   size_hint=(.2, .055),
                                   pos_hint={'center_x': .60,
                                             'center_y': .57})
        self.add_widget(self.password1)

        self.add_widget(Label(text='Confirm Password* :',
                              font_size=20,
                              pos_hint={'center_x': .42,
                                        'center_y': .51}))

        self.password2 = TextInput(password=True,
                                   multiline=False,
                                   font_size=20,
                                   size_hint=(.2, .055),
                                   pos_hint={'center_x': .60,
                                             'center_y': .51})
        self.add_widget(self.password2)

        self.promt_password = Label(text='',
                                    color=[1, 0, 0, 1],
                                    font_size=12,
                                    pos_hint={'center_x': .60,
                                              'center_y': .46})
        self.add_widget(self.promt_password)

        self.add_widget(Button(text='Update',
                               size_hint=(.1, .05),
                               font_size=15,
                               pos_hint={'center_x': .5,
                                         'center_y': .40},
                               on_press=self.Update))

        self.Promt = Label(text='',
                           font_size=30,
                           pos_hint={'center_x': .50,
                                     'center_y': .33})
        self.add_widget(self.Promt)

        self.Done_Back = Button(text='Back',
                                size_hint=(.1, .05),
                                font_size=15,
                                pos_hint={'center_x': .5,
                                          'center_y': .20},
                                on_press=self.screen_transition_Login)
        self.add_widget(self.Done_Back)

    def Update(self, instance):
        self.promt_password.text = ''

        password1 = self.password1.text
        password2 = self.password2.text
        global CUSTOMER_ID

        if pass_check(self, password1, password2) == 0:
            c.execute("UPDATE %s SET Password = '%s' where CustomerID = '%s';" % (USERS_TABLE, password1, CUSTOMER_ID))
            db.commit()
            self.password1.text = ''
            self.password2.text = ''
            self.Promt.text = 'Password Updated'
            self.Done_Back.text = 'Done'

    def screen_transition_Login(self, *args):
        self.promt_password.text = ''
        self.manager.current = 'Login'


class Forgot_Cust_ID(Screen):
    def __init__(self, **kwargs):
        super(Forgot_Cust_ID, self).__init__(**kwargs)
        self.add_widget(Label(text='Forgot Customer_ID',
                              font_size=30,
                              pos_hint={'center_x': .5,
                                        'center_y': .8}))

        self.add_widget(Label(text='First Name :',
                              font_size=20,
                              pos_hint={'center_x': .4,
                                        'center_y': .6}))

        self.fname = TextInput(multiline=False,
                               size_hint=(.2, .055),
                               font_size=20,
                               pos_hint={'center_x': .55,
                                         'center_y': .6})
        self.add_widget(self.fname)

        self.promt_fname = Label(text='',
                                 color=[1, 0, 0, 1],
                                 font_size=12,
                                 pos_hint={'center_x': .83,
                                           'center_y': .6})
        self.add_widget(self.promt_fname)

        self.add_widget(Label(text='Last Name :',
                              font_size=20,
                              pos_hint={'center_x': .4,
                                        'center_y': .5}))

        self.lname = TextInput(multiline=False,
                               size_hint=(.2, .055),
                               font_size=20,
                               pos_hint={'center_x': .55,
                                         'center_y': .5})
        self.add_widget(self.lname)

        self.promt_lname = Label(text='',
                                 color=[1, 0, 0, 1],
                                 font_size=12,
                                 pos_hint={'center_x': .83,
                                           'center_y': .5})
        self.add_widget(self.promt_lname)

        self.add_widget(Label(text='Password :',
                              font_size=20,
                              pos_hint={'center_x': .395,
                                        'center_y': .4}))

        self.Pass = TextInput(multiline=False,
                              password=True,
                              font_size=20,
                              size_hint=(.2, .055),
                              pos_hint={'center_x': .55,
                                        'center_y': .4})
        self.add_widget(self.Pass)

        self.promt_password = Label(text='',
                                    color=[1, 0, 0, 1],
                                    font_size=12,
                                    pos_hint={'center_x': .83,
                                              'center_y': .4})
        self.add_widget(self.promt_password)

        self.add_widget(Button(text='Enter',
                               size_hint=(.1, .05),
                               font_size=15,
                               pos_hint={'center_x': .5,
                                         'center_y': .3},
                               on_press=self.ID_Check))

        self.ID = Label(text='',
                        font_size=30,
                        pos_hint={'center_x': .50,
                                  'center_y': .23})
        self.add_widget(self.ID)

        self.Back = Button(text='Back',
                           size_hint=(.17, .05),
                           font_size=15,
                           pos_hint={'center_x': .5,
                                     'center_y': .1},
                           on_press=self.screen_transition_Login)
        self.add_widget(self.Back)

    def ID_Check(self, instance):

        self.promt_fname.text = ''
        self.promt_lname.text = ''
        self.promt_password.text = ''
        self.ID.text = ''

        fname = self.fname.text.capitalize()
        lname = self.lname.text.capitalize()
        password = self.Pass.text

        self.Back.text = 'Back'
        self.Back.on_press = self.screen_transition_Login

        if fname == '':
            self.promt_fname.text = 'Enter your First name.'
        if lname == '':
            self.promt_lname.text = 'Enter your Last name.'
        if password == '':
            self.promt_password.text = 'Fill the password blank.'

        if fname != '' and lname != '' and password != '':
            c.execute("select * from %s" % (USERS_TABLE))
            user_info = c.fetchall()
            invalid_fname = invalid_lname = invalid_password = 1
            together = 0
            for i in user_info:
                if fname == i[1]:
                    invalid_fname = 0
                if lname == i[2]:
                    invalid_lname = 0
                if password == i[3]:
                    invalid_password = 0
                if (fname, lname, password) == i[1:]:
                    together = 1
                    CUSTOMER_ID = i[0]
            if bool(invalid_fname):
                self.promt_username.text = 'Invalid First Name'
            if bool(invalid_lname):
                self.promt_lname.text = 'Invalid Last Name'
            if bool(invalid_password):
                self.promt_password.text = 'Invalid Password'
            if invalid_fname == 0 and invalid_lname == 0 and invalid_password == 0:
                if together == 1:
                    self.ID.text = CUSTOMER_ID
                    self.Back.text = 'Done'
                else:
                    self.ID.text = 'No such account found!'
                    self.Back.text = 'Create_Acc'
                    self.Back.on_press = self.screen_transition_Acc

    def reset_page(self, *args):
        self.promt_fname.text = ''
        self.promt_lname.text = ''
        self.promt_password.text = ''
        self.ID.text = ''
        self.fname.text = ''
        self.lname.text = ''
        self.Pass.text = ''

    def screen_transition_Acc(self, *args):
        self.reset_page()
        self.manager.current = 'Create-Acc'

    def screen_transition_Login(self, *args):
        self.reset_page()
        self.manager.current = 'Login'


## ADMIN_PAGES - CHANDAN

class MainPage(Screen):
    def __init__(self, **kwargs):
        super(MainPage, self).__init__(**kwargs)

        self.Item = Label(text='ITEM: ',
                          font_size=20,
                          pos_hint={'center_x': .2,
                                    'center_y': .9})
        self.Price = Label(text='PRICE: ',
                           font_size=20,
                           pos_hint={'center_x': .45,
                                     'center_y': .9})
        self.Quantity = Label(text='QUANTITY: ',
                              font_size=20,
                              pos_hint={'center_x': .6,
                                        'center_y': .9})
        self.add_widget(self.Item)
        self.add_widget(self.Price)
        self.add_widget(self.Quantity)

        c.execute('select ItemName from admin')
        k = list(c.fetchall())
        p = 0
        c.execute('select count(*) from admin')
        b = c.fetchall()
        b1 = b[0][0]
        y = .8
        for index in range(b1):
            l = k[p][0]
            self.add_widget(Label(text=str(l),
                                  font_size=15,
                                  pos_hint={'center_x': .2,
                                            'center_y': y}))
            p += 1
            y -= .05

        c.execute('select Price from admin')
        k = list(c.fetchall())
        p = 0
        c.execute('select count(*) from admin')
        b = c.fetchall()
        b1 = b[0][0]
        y = .8
        for index in range(b1):
            l = k[p][0]
            self.add_widget(Label(text=str(l),
                                  font_size=15,
                                  pos_hint={'center_x': .45,
                                            'center_y': y}))
            p += 1
            y -= .05

        c.execute('select Quantity from admin')
        k = list(c.fetchall())
        p = 0
        c.execute('select count(*) from admin')
        b = c.fetchall()
        b1 = b[0][0]
        y = .8
        for index in range(b1):
            l = k[p][0]
            self.add_widget(Label(text=str(l),
                                  font_size=15,
                                  pos_hint={'center_x': .6,
                                            'center_y': y}))
            p += 1
            y -= .05

        # Return Buttons
        self.Add = Button(text='Add-Items',
                          size_hint=(.17, .05),
                          font_size=15,
                          pos_hint={'center_x': .85,
                                    'center_y': .7},
                          on_press=self.BackToAdd)

        self.Update = Button(text='Update-Items',
                             size_hint=(.17, .05),
                             font_size=15,
                             pos_hint={'center_x': .85,
                                       'center_y': .6},
                             on_press=self.BackToUpdate)

        self.Delete = Button(text='Delete-Items',
                             size_hint=(.17, .05),
                             font_size=15,
                             pos_hint={'center_x': .85,
                                       'center_y': .5},
                             on_press=self.BackToDelete)

        self.Review = Button(text='Review-Feedback',
                             size_hint=(.17, .05),
                             font_size=15,
                             pos_hint={'center_x': .85,
                                       'center_y': .4},
                             on_press=self.BackToReview)
        # Refresh Button
        self.Refresh = Button(text='Refresh',
                              size_hint=(.15, .05),
                              font_size=15,
                              pos_hint={'center_x': .45,
                                        'center_y': .2},
                              on_press=self.ItemView)

        self.btn4 = Button(text='Log Out',
                           size_hint=(.1, .05),
                           pos_hint={'x': .87, 'y': .9},
                           on_press=self.Exit)

        self.add_widget(self.Add)
        self.add_widget(self.Update)
        self.add_widget(self.Delete)
        self.add_widget(self.Review)
        self.add_widget(self.Refresh)
        self.add_widget(self.btn4)

    def Exit(self, *args):
        layout = FloatLayout()  # Pop-Up Part
        noButton = Button(text="CANCEL",
                          size_hint=(.15, .12),
                          pos_hint={'center_x': .6,
                                    'center_y': .6},
                          font_size=15)
        yesButton = Button(text="YES",
                           size_hint=(.15, .12),
                           pos_hint={'center_x': .4,
                                     'center_y': .6},
                           font_size=15)
        popupLabel = Label(text="Are you sure you want to exit?",
                           font_size=20,
                           pos_hint={'center_x': .5,
                                     'center_y': .4})
        layout.add_widget(popupLabel)
        layout.add_widget(noButton)
        layout.add_widget(yesButton)
        popup = Popup(title='EXIT',  # Instantiate the popup and display
                      content=layout,
                      size_hint=(.4, .4))
        popup.open()
        # Attach close button press with popup.dismiss action
        noButton.bind(on_press=popup.dismiss)
        yesButton.bind(on_press=self.Closing)
        yesButton.bind(on_press=popup.dismiss) 

    def Closing(self, *args):
        self.manager.current = 'Login'

    def ItemView(self, instance):
        self.clear_widgets()
        self.add_widget(self.Item)
        self.add_widget(self.Price)
        self.add_widget(self.Quantity)

        c.execute('select ItemName from admin')
        k = list(c.fetchall())
        p = 0
        c.execute('select count(*) from admin')
        b = c.fetchall()
        b1 = b[0][0]
        y = .8
        for index in range(b1):
            l = k[p][0]
            self.add_widget(Label(text=str(l),
                                  font_size=15,
                                  pos_hint={'center_x': .2,
                                            'center_y': y}))
            p += 1
            y -= .05

        c.execute('select Price from admin')
        k = list(c.fetchall())
        p = 0
        c.execute('select count(*) from admin')
        b = c.fetchall()
        b1 = b[0][0]
        y = .8
        for index in range(b1):
            l = k[p][0]
            self.add_widget(Label(text=str(l),
                                  font_size=15,
                                  pos_hint={'center_x': .45,
                                            'center_y': y}))
            p += 1
            y -= .05

        c.execute('select Quantity from admin')
        k = list(c.fetchall())
        p = 0
        c.execute('select count(*) from admin')
        b = c.fetchall()
        b1 = b[0][0]
        y = .8
        for index in range(b1):
            l = k[p][0]
            self.add_widget(Label(text=str(l),
                                  font_size=15,
                                  pos_hint={'center_x': .6,
                                            'center_y': y}))
            p += 1
            y -= .05

        # Return Buttons
        self.add_widget(self.Add)
        self.add_widget(self.Update)
        self.add_widget(self.Delete)
        self.add_widget(self.Review)
        self.add_widget(self.Refresh)
        self.add_widget(self.btn4)

    def BackToAdd(self, instance):
        self.manager.current = 'Add-Items'

    def BackToUpdate(self, instance):
        self.manager.current = 'Update-Items'

    def BackToDelete(self, instance):
        self.manager.current = 'Delete-Items'

    def BackToReview(self, *args):
        self.manager.current = 'Review-Feedback'


class AddItems(Screen):
    def __init__(self, **kwargs):
        super(AddItems, self).__init__(**kwargs)

        self.clear_widgets()
        self.add_widget(Label(text='Add Items',
                              font_size=30,
                              pos_hint={'center_x': .51,
                                        'center_y': .8}))
        # Button 1
        self.add_widget(Label(text='Item Name: ',
                              font_size=20,
                              pos_hint={'center_x': .4,
                                        'center_y': .6}))

        self.itemname = TextInput(multiline=False,
                                  size_hint=(.2, .055),
                                  font_size=20,
                                  pos_hint={'center_x': .6,
                                            'center_y': .6})
        self.add_widget(self.itemname)
        # Button 2
        self.add_widget(Label(text='Quantity: ',
                              font_size=20,
                              pos_hint={'center_x': .4,
                                        'center_y': .5}))

        self.quantity = TextInput(multiline=False,
                                  size_hint=(.2, .055),
                                  font_size=20,
                                  pos_hint={'center_x': .6,
                                            'center_y': .5})
        self.add_widget(self.quantity)
        # Button 3
        self.add_widget(Label(text='Price: ',
                              font_size=20,
                              pos_hint={'center_x': .4,
                                        'center_y': .4}))

        self.price = TextInput(multiline=False,
                               font_size=20,
                               size_hint=(.2, .055),
                               pos_hint={'center_x': .6,
                                         'center_y': .4})
        self.add_widget(self.price)
        # Enter Button
        self.add_widget(Button(text='Enter',
                               size_hint=(.1, .05),
                               font_size=15,
                               pos_hint={'center_x': .5,
                                         'center_y': .2},
                               on_press=self.Enter))
        # Back Button
        self.add_widget(Button(text='Back',
                               size_hint=(.1, .05),
                               font_size=15,
                               pos_hint={'center_x': .1,
                                         'center_y': .9},
                               on_press=self.Back))

    def Enter(self, instance):
        l = str(self.itemname.text)
        m = str(self.quantity.text)
        n = str(self.price.text)

        if l == '' or m == '' or n == '':
            layout = FloatLayout()  # Pop-Up Part
            closeButton = Button(text="CLOSE",
                                 size_hint=(.2, .1),
                                 pos_hint={'center_x': .5,
                                           'center_y': .15},
                                 font_size=15)
            popupLabel = Label(text="ERROR: Empty Fields Not Permisisble",
                               font_size=20,
                               pos_hint={'center_x': .5,
                                         'center_y': .5})
            layout.add_widget(popupLabel)
            layout.add_widget(closeButton)
            popup = Popup(title='ERROR: FIELD(S) EMPTY',  # Instantiate the popup and display
                          content=layout,
                          size_hint=(.4, .4))
            popup.open()
            # Attach close button press with popup.dismiss action
            closeButton.bind(on_press=popup.dismiss)
        else:
            n = "{:.2f}".format(float(n))
            c.execute("insert into admin values('%s','%s','%s')" % (str(l), n, int(m)))
            db.commit()
            self.itemname.text = ''
            self.quantity.text = ''
            self.price.text = ''
            layout = FloatLayout()  # Pop-Up Part
            closeButton = Button(text="CLOSE",
                                 size_hint=(.2, .1),
                                 pos_hint={'center_x': .5,
                                           'center_y': .15},
                                 font_size=15)
            popupLabel = Label(text=str(l) + " IS ADDED",
                               font_size=20,
                               pos_hint={'center_x': .5,
                                         'center_y': .5})
            layout.add_widget(popupLabel)
            layout.add_widget(closeButton)
            popup = Popup(title='Add Item Pop-Up',  # Instantiate the popup and display
                          content=layout,
                          size_hint=(.4, .4))
            popup.open()
            # Attach close button press with popup.dismiss action
            closeButton.bind(on_press=popup.dismiss)

    def Back(self, instance):
        self.manager.current = 'Admin Page'


class UpdateItems(Screen):
    def __init__(self, **kwargs):
        super(UpdateItems, self).__init__(**kwargs)
        self.clear_widgets()

        self.add_widget(Label(text='Update Items',
                              font_size=30,
                              pos_hint={'center_x': .51,
                                        'center_y': .8}))
        # Button 1
        self.add_widget(Label(text='Item Name: ',
                              font_size=20,
                              pos_hint={'center_x': .4,
                                        'center_y': .6}))
        t = []
        c.execute('select ItemName from admin')
        k = list(c.fetchall())
        p = 0
        c.execute('select count(*) from admin')
        b = c.fetchall()
        b1 = b[0][0]
        for index in range(b1):
            l = k[p][0]
            text = 'value %d' % index

            def transfer():
                return text

            t.append(l)
            p += 1
        # DropDown 1 - Type Spinner
        itemname = Spinner(text='ITEM',
                           values=tuple(t),
                           size_hint=(.22, .06),
                           pos_hint={'center_x': .6,
                                     'center_y': .6})
        self.add_widget(itemname)

        def show(itemname, text):
            transfer();
            txt = text;
            global text1;
            text1 = txt

        itemname.bind(text=show)
        # Button 2
        self.add_widget(Label(text='New Quantity: ',
                              font_size=20,
                              pos_hint={'center_x': .4,
                                        'center_y': .5}))

        self.quantity = TextInput(multiline=False,
                                  size_hint=(.2, .055),
                                  font_size=20,
                                  pos_hint={'center_x': .6,
                                            'center_y': .5})
        self.add_widget(self.quantity)
        # Button 3
        self.add_widget(Label(text='New Price: ',
                              font_size=20,
                              pos_hint={'center_x': .4,
                                        'center_y': .4}))

        self.price = TextInput(multiline=False,
                               font_size=20,
                               size_hint=(.2, .055),
                               pos_hint={'center_x': .6,
                                         'center_y': .4})
        self.add_widget(self.price)
        # Enter Button
        self.add_widget(Button(text='Enter',
                               size_hint=(.1, .05),
                               font_size=15,
                               pos_hint={'center_x': .5,
                                         'center_y': .2},
                               on_press=self.Enter))
        # Back Button
        self.add_widget(Button(text='Back',
                               size_hint=(.1, .05),
                               font_size=15,
                               pos_hint={'center_x': .1,
                                         'center_y': .9},
                               on_press=self.Back))

        self.add_widget(Button(text='Refresh',
                               size_hint=(.13, .05),
                               font_size=15,
                               pos_hint={'center_x': .8,
                                         'center_y': .5},
                               on_press=self.Refresh))

    def Refresh(self, instance):
        self.clear_widgets()
        self.add_widget(Label(text='Update Items',
                              font_size=30,
                              pos_hint={'center_x': .51,
                                        'center_y': .8}))
        # Button 1
        self.add_widget(Label(text='Item Name: ',
                              font_size=20,
                              pos_hint={'center_x': .4,
                                        'center_y': .6}))
        t = []
        c.execute('select ItemName from admin')
        k = list(c.fetchall())
        p = 0
        c.execute('select count(*) from admin')
        b = c.fetchall()
        b1 = b[0][0]
        for index in range(b1):
            l = k[p][0]
            text = 'value %d' % index

            def transfer():
                return text

            t.append(l)
            p += 1
        # DropDown 1 - Type Spinner
        itemname = Spinner(text='ITEM',
                           values=tuple(t),
                           size_hint=(.22, .06),
                           pos_hint={'center_x': .6,
                                     'center_y': .6})
        self.add_widget(itemname)

        def show(itemname, text):
            transfer();
            txt = text;
            global text1;
            text1 = txt;

        itemname.bind(text=show)
        # Button 2
        self.add_widget(Label(text='New Quantity: ',
                              font_size=20,
                              pos_hint={'center_x': .4,
                                        'center_y': .5}))

        self.quantity = TextInput(multiline=False,
                                  size_hint=(.2, .055),
                                  font_size=20,
                                  pos_hint={'center_x': .6,
                                            'center_y': .5})
        self.add_widget(self.quantity)
        # Button 3
        self.add_widget(Label(text='New Price: ',
                              font_size=20,
                              pos_hint={'center_x': .4,
                                        'center_y': .4}))

        self.price = TextInput(multiline=False,
                               font_size=20,
                               size_hint=(.2, .055),
                               pos_hint={'center_x': .6,
                                         'center_y': .4})
        self.add_widget(self.price)
        # Enter Button
        self.add_widget(Button(text='Enter',
                               size_hint=(.1, .05),
                               font_size=15,
                               pos_hint={'center_x': .5,
                                         'center_y': .2},
                               on_press=self.Enter))
        # Back Button
        self.add_widget(Button(text='Back',
                               size_hint=(.1, .05),
                               font_size=15,
                               pos_hint={'center_x': .1,
                                         'center_y': .9},
                               on_press=self.Back))

        self.add_widget(Button(text='Refresh',
                               size_hint=(.13, .05),
                               font_size=15,
                               pos_hint={'center_x': .8,
                                         'center_y': .5},
                               on_press=self.Refresh))

    def Enter(self, instance):
        l = str(text1)
        m = str(self.quantity.text)
        n1 = str(self.price.text)
        if l == '':
            layout = FloatLayout()  # Pop-Up Part
            closeButton = Button(text="CLOSE",
                                 size_hint=(.2, .1),
                                 pos_hint={'center_x': .5,
                                           'center_y': .15},
                                 font_size=15)
            popupLabel = Label(text="ERROR: NO ITEM SELECTED",
                               font_size=20,
                               pos_hint={'center_x': .5,
                                         'center_y': .5})
            layout.add_widget(popupLabel)
            layout.add_widget(closeButton)
            popup = Popup(title='ERROR',  # Instantiate the popup and display
                          content=layout,
                          size_hint=(.4, .4))
            popup.open()
            # Attach close button press with popup.dismiss action
            closeButton.bind(on_press=popup.dismiss)
            text_call_1()
        elif l != '':
            if m == '' and n1 == '':
                layout = FloatLayout()  # Pop-Up Part
                closeButton = Button(text="CLOSE",
                                     size_hint=(.2, .1),
                                     pos_hint={'center_x': .5,
                                               'center_y': .15},
                                     font_size=15)
                popupLabel = Label(text="ERROR: NO UPDATE(S) SPECIFIED",
                                   font_size=20,
                                   pos_hint={'center_x': .5,
                                             'center_y': .5})
                layout.add_widget(popupLabel)
                layout.add_widget(closeButton)
                popup = Popup(title='ERROR',  # Instantiate the popup and display
                              content=layout,
                              size_hint=(.4, .4))
                popup.open()
                # Attach close button press with popup.dismiss action
                closeButton.bind(on_press=popup.dismiss)
            elif m == '' and n1 != '':
                n = "{:.2f}".format(float(n1))
                c.execute("update admin set Price='%s' where ItemName='%s'" % (n, l))
                db.commit()
                self.quantity.text = ''
                self.price.text = ''
                layout = FloatLayout()  # Pop-Up Part
                closeButton = Button(text="CLOSE",
                                     size_hint=(.2, .1),
                                     pos_hint={'center_x': .5,
                                               'center_y': .15},
                                     font_size=15)
                popupLabel = Label(text=str(l) + " IS UPDATED",
                                   font_size=20,
                                   pos_hint={'center_x': .5,
                                             'center_y': .5})
                layout.add_widget(popupLabel)
                layout.add_widget(closeButton)
                popup = Popup(title='Update Item Pop-Up',  # Instantiate the popup and display
                              content=layout,
                              size_hint=(.4, .4))
                popup.open()
                # Attach close button press with popup.dismiss action
                closeButton.bind(on_press=popup.dismiss)
                text_call_1()
            elif m != '' and n1 == '':
                c.execute("update admin set Quantity = '%s' where ItemName = '%s'" % (int(m), l))
                db.commit()
                self.quantity.text = ''
                self.price.text = ''
                layout = FloatLayout()  # Pop-Up Part
                closeButton = Button(text="CLOSE",
                                     size_hint=(.2, .1),
                                     pos_hint={'center_x': .5,
                                               'center_y': .15},
                                     font_size=15)
                popupLabel = Label(text=str(l) + " IS UPDATED",
                                   font_size=20,
                                   pos_hint={'center_x': .5,
                                             'center_y': .5})
                layout.add_widget(popupLabel)
                layout.add_widget(closeButton)
                popup = Popup(title='Update Item Pop-Up',  # Instantiate the popup and display
                              content=layout,
                              size_hint=(.4, .4))
                popup.open()
                # Attach close button press with popup.dismiss action
                closeButton.bind(on_press=popup.dismiss)
                text_call_1()
            elif m != '' and n1 != '':
                n = "{:.2f}".format(float(n1))
                c.execute("update admin set Price='%s', Quantity='%s' where ItemName='%s'" % (n, m, l))
                db.commit()
                self.quantity.text = ''
                self.price.text = ''
                layout = FloatLayout()  # Pop-Up Part
                closeButton = Button(text="CLOSE",
                                     size_hint=(.2, .1),
                                     pos_hint={'center_x': .5,
                                               'center_y': .15},
                                     font_size=15)
                popupLabel = Label(text=str(l) + " IS UPDATED",
                                   font_size=20,
                                   pos_hint={'center_x': .5,
                                             'center_y': .5})
                layout.add_widget(popupLabel)
                layout.add_widget(closeButton)
                popup = Popup(title='Update Item Pop-Up',  # Instantiate the popup and display
                              content=layout,
                              size_hint=(.4, .4))
                popup.open()
                # Attach close button press with popup.dismiss action
                closeButton.bind(on_press=popup.dismiss)
                text_call_1()

    def Back(self, instance):
        self.manager.current = 'Admin Page'


class DeleteItems(Screen):
    def __init__(self, **kwargs):
        super(DeleteItems, self).__init__(**kwargs)
        self.clear_widgets()
        self.add_widget(Label(text='Delete Items',
                              font_size=30,
                              pos_hint={'center_x': .51,
                                        'center_y': .8}))
        # Button 1
        self.add_widget(Label(text='Item Name: ',
                              font_size=20,
                              pos_hint={'center_x': .4,
                                        'center_y': .6}))
        t = []
        c.execute('select ItemName from admin')
        k = list(c.fetchall())
        p = 0
        c.execute('select count(*) from admin')
        b = c.fetchall()
        b1 = b[0][0]
        for index in range(b1):
            l = k[p][0]
            text = 'value %d' % index

            def transfer():
                return text

            t.append(l)
            p += 1
        # DropDown 1 - Type Spinner
        itemname = Spinner(text='ITEM',
                           values=tuple(t),
                           size_hint=(.2, .06),
                           pos_hint={'center_x': .6,
                                     'center_y': .6})
        self.add_widget(itemname)

        def show(itemname, text):
            transfer();
            txt = text;
            global text2;
            text2 = txt;

        itemname.bind(text=show)

        self.add_widget(Button(text='Delete',
                               size_hint=(.1, .05),
                               font_size=15,
                               pos_hint={'center_x': .5,
                                         'center_y': .2},
                               on_press=self.pressed))
        # Back Button
        self.add_widget(Button(text='Back',
                               size_hint=(.1, .05),
                               font_size=15,
                               pos_hint={'center_x': .1,
                                         'center_y': .9},
                               on_press=self.Back))

        self.add_widget(Button(text='Refresh',
                               size_hint=(.13, .05),
                               font_size=15,
                               pos_hint={'center_x': .8,
                                         'center_y': .6},
                               on_press=self.Refresh))

    def Refresh(self, instance):
        self.clear_widgets()
        self.add_widget(Label(text='Delete Items',
                              font_size=30,
                              pos_hint={'center_x': .51,
                                        'center_y': .8}))

        # Button 1
        self.add_widget(Label(text='Item Name: ',
                              font_size=20,
                              pos_hint={'center_x': .4,
                                        'center_y': .6}))
        t = []
        c.execute('select ItemName from admin')
        k = list(c.fetchall())
        p = 0
        c.execute('select count(*) from admin')
        b = c.fetchall()
        b1 = b[0][0]
        for index in range(b1):
            l = k[p][0]
            text = 'value %d' % index

            def transfer():
                return text

            t.append(l)
            p += 1
        # DropDown 1 - Type Spinner
        itemname = Spinner(text='ITEM',
                           values=tuple(t),
                           size_hint=(.2, .06),
                           pos_hint={'center_x': .6,
                                     'center_y': .6})
        self.add_widget(itemname)

        def show(itemname, text):
            transfer();
            txt = text;
            global text2;
            text2 = txt;

        itemname.bind(text=show)

        self.add_widget(Button(text='Delete',
                               size_hint=(.1, .05),
                               font_size=15,
                               pos_hint={'center_x': .5,
                                         'center_y': .2},
                               on_press=self.pressed))
        # Back Button
        self.add_widget(Button(text='Back',
                               size_hint=(.1, .05),
                               font_size=15,
                               pos_hint={'center_x': .1,
                                         'center_y': .9},
                               on_press=self.Back))

        self.add_widget(Button(text='Refresh',
                               size_hint=(.13, .05),
                               font_size=15,
                               pos_hint={'center_x': .8,
                                         'center_y': .6},
                               on_press=self.Refresh))

    def pressed(self, instance):
        global text2
        if text2 == '':
            layout = FloatLayout()  # Pop-Up Part
            closeButton = Button(text="CLOSE",
                                 size_hint=(.2, .1),
                                 pos_hint={'center_x': .5,
                                           'center_y': .15},
                                 font_size=15)
            popupLabel = Label(text=str('ERROR: NO ITEM HAS BEEN SELECTED'),
                               font_size=20,
                               pos_hint={'center_x': .5,
                                         'center_y': .5})
            layout.add_widget(popupLabel)
            layout.add_widget(closeButton)
            popup = Popup(title='ERROR',  # Instantiate the popup and display
                          content=layout,
                          size_hint=(.4, .4))
            popup.open()
            # Attach close button press with popup.dismiss action
            closeButton.bind(on_press=popup.dismiss)
            text_call_2()
        elif text2 != '':
            deleted_item = text2
            c.execute("delete from admin where ItemName = ('%s')" % (deleted_item))
            db.commit()
            layout = FloatLayout()  # Pop-Up Part
            closeButton = Button(text="CLOSE",
                                 size_hint=(.2, .1),
                                 pos_hint={'center_x': .5,
                                           'center_y': .15},
                                 font_size=15)
            popupLabel = Label(text=str(deleted_item) + " IS DELETED",
                               font_size=20,
                               pos_hint={'center_x': .5,
                                         'center_y': .5})
            layout.add_widget(popupLabel)
            layout.add_widget(closeButton)
            popup = Popup(title='Deleted Item Pop-Up',  # Instantiate the popup and display
                          content=layout,
                          size_hint=(.4, .4))
            popup.open()
            # Attach close button press with popup.dismiss action
            closeButton.bind(on_press=popup.dismiss)
            text_call_2()

    def Back(self, instance):
        self.manager.current = 'Admin Page'


class ReviewFeedback(Screen):
    def __init__(self, **kwargs):
        super(ReviewFeedback, self).__init__(**kwargs)
        self.clear_widgets()
        self.add_widget(Label(text='Feedback: ',
                              font_size=20,
                              pos_hint={'center_x': .51,
                                        'center_y': .9}))
        # Back Button
        self.add_widget(Button(text='Back',
                               size_hint=(.1, .05),
                               font_size=15,
                               pos_hint={'center_x': .1,
                                         'center_y': .9},
                               on_press=self.Back))
        # CustomerID Dislpay
        self.add_widget(Label(text='CustomerID: ',
                              font_size=20,
                              pos_hint={'center_x': .31,
                                        'center_y': .8}))
        c.execute('select CustomerID from feedback')
        k = list(c.fetchall())
        p = 0
        y = .7
        c.execute('select count(*) from feedback')
        b = c.fetchall()
        b1 = b[0][0]
        for index in range(b1):
            l = k[p][0]
            self.add_widget(Label(text=str(l),
                                  font_size=15,
                                  pos_hint={'center_x': .31,
                                            'center_y': y}))
            p += 1
            y -= .1
        Refresh = (Button(text='Refresh',
                          font_size=20,
                          size_hint=(.1, .05),
                          pos_hint={'center_x': .5,
                                    'center_y': .1},
                          on_press=self.Refresh))
        self.add_widget(Refresh)
        # Comment Display
        self.add_widget(Label(text='Comment: ',
                              font_size=20,
                              pos_hint={'center_x': .71,
                                        'center_y': .8}))

        c.execute('select Comment from feedback')
        k = list(c.fetchall())
        p = 0
        y = .7
        c.execute('select count(*) from feedback')
        b = c.fetchall()
        b1 = b[0][0]
        for index in range(b1):
            l = k[p][0]
            self.add_widget(Label(text=str(l),
                                  font_size=15,
                                  pos_hint={'center_x': .71,
                                            'center_y': y}))
            p += 1
            y -= .1

    def Refresh(self, instance):
        self.clear_widgets()
        self.add_widget(Label(text='Feedback: ',
                              font_size=20,
                              pos_hint={'center_x': .51,
                                        'center_y': .9}))
        # Back Button
        self.add_widget(Button(text='Back',
                               size_hint=(.1, .05),
                               font_size=15,
                               pos_hint={'center_x': .1,
                                         'center_y': .9},
                               on_press=self.Back))
        # CustomerID Dislpay
        self.add_widget(Label(text='CustomerID: ',
                              font_size=20,
                              pos_hint={'center_x': .31,
                                        'center_y': .8}))
        c.execute('select CustomerID from feedback')
        k = list(c.fetchall())
        p = 0
        y = .7
        c.execute('select count(*) from feedback')
        b = c.fetchall()
        b1 = b[0][0]
        for index in range(b1):
            l = k[p][0]
            self.add_widget(Label(text=str(l),
                                  font_size=15,
                                  pos_hint={'center_x': .31,
                                            'center_y': y}))
            p += 1
            y -= .1
        Refresh = Button(text='Refresh',
                         font_size=20,
                         size_hint=(.1, .05),
                         pos_hint={'center_x': .5,
                                   'center_y': .1},
                         on_press=self.Refresh)
        self.add_widget(Refresh)
        # Comment Display
        self.add_widget(Label(text='Comment: ',
                              font_size=20,
                              pos_hint={'center_x': .71,
                                        'center_y': .8}))
        c.execute('select Comment from feedback')
        k = list(c.fetchall())
        p = 0
        y = .7
        c.execute('select count(*) from feedback')
        b = c.fetchall()
        b1 = b[0][0]
        for index in range(b1):
            l = k[p][0]
            self.add_widget(Label(text=str(l),
                                  font_size=15,
                                  pos_hint={'center_x': .71,
                                            'center_y': y}))
            p += 1
            y -= .1

    def Back(self, instance):
        self.manager.current = 'Admin Page'


## CUSTOMER_PAGES - HARI

c.execute("select * from admin")
items_sql = list(c.fetchall())

sm = ScreenManager()



# Customer Screen
class Customer(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(Customer, self).__init__(**kwargs)

        # Initializing the buttons
        self.orderbtn = Button(text="Order Items",
                               font_size=30,
                               size_hint=(.4, .2),
                               pos_hint={'center_x': .27,
                                         'center_y': .60},
                               on_press=self.gotoOrder)
        self.updcanbtn = Button(text="Update/Cancel Order",
                                font_size=30,
                                size_hint=(.4, .2),
                                pos_hint={'center_x': .73,
                                          'center_y': .60},
                                on_press=self.gotoUpdCan)
        self.feedbackbtn = Button(text="Feedback",
                                  font_size=30,
                                  size_hint=(.4, .2),
                                  pos_hint={'center_x': .5,
                                            'center_y': .30},
                                  on_press=self.gotoFeedback)
        self.logoutbtn = Button(text="Logout",
                                size_hint=(0.1, 0.05),
                                pos_hint={"center_x": 0.95,
                                          "center_y": 0.98},
                                on_press=self.gotoLogin)
        self.custname = Label(text="",
                              pos_hint={"center_x": 0.5,
                                        "center_y": 0.90},
                              size_hint=(0.05, 0.05),
                              font_size=30)
        self.refreshbtn = Button(text="Refresh",
                                 size_hint=(0.1, 0.05),
                                 pos_hint={"center_x": 0.05,
                                           "center_y": 0.98},
                                 on_press=self.refreshName)
        self.refreshlbl = Label(text="Please refresh the page.",
                                pos_hint={"center_x": 0.5,
                                          "center_y": 0.90},
                                size_hint=(0.05, 0.05),
                                font_size=30)
        # Adding the Buttons
        self.add_widget(self.orderbtn)
        self.add_widget(self.updcanbtn)
        self.add_widget(self.feedbackbtn)
        self.add_widget(self.logoutbtn)
        self.add_widget(self.refreshbtn)
        self.add_widget(self.refreshlbl)

    def gotoOrder(self, instance):
        self.manager.current = "Order"

    def gotoUpdCan(self, instance):
        self.manager.current = "Updcan"

    def gotoCheckord(self, instance):
        self.manager.current = "Checkord"

    def gotoFeedback(self, instance):
        self.manager.current = "Feedback"

    def gotoCustomer(self, instance):
        self.manager.current = "Customer"

    def gotoLogin(self, instance):
        self.float_layout = FloatLayout(size_hint=(0.5, 0.4),
                                        pos_hint={"center_x": 0.5,
                                                  "center_y": 0.4})

        self.logoutlbl = Label(text="Are you sure you want to log out?",
                               font_size=20,
                               pos_hint={"center_x": 0.5,
                                         "center_y": 1},
                               size_hint=(0.5, 0.5))
        self.yesbtn = Button(text="Yes",
                             font_size=20,
                             size_hint=(0.2, 0.4),
                             pos_hint={"center_x": 0.7,
                                       "center_y": 0.01},
                             on_press=self.backtoLogin)
        self.nobtn = Button(text="No",
                            font_size=20,
                            size_hint=(0.2, 0.4),
                            pos_hint={"center_x": 0.3,
                                      "center_y": 0.01},
                            on_press=self.backtoOrder)

        self.popup = Popup(title="",
                           content=self.float_layout,
                           size_hint=(0.5, 0.4),
                           pos_hint={"center_x": 0.5,
                                     "center_y": 0.5},
                           auto_dismiss=False)
        self.popup.open()
        self.float_layout.add_widget(self.logoutlbl)
        self.float_layout.add_widget(self.yesbtn)
        self.float_layout.add_widget(self.nobtn)


    def backtoLogin(self, instance):
        self.popup.dismiss()
        self.custname.text = ""
        self.manager.current = "Login"
        self.add_widget(self.refreshlbl)


    def backtoOrder(self, instance):
        self.popup.dismiss()


    def refreshName(self, instance):
        self.NAME = FNAME
        self.custname = Label(text="Welcome, " + self.NAME + "!",
                              pos_hint={"center_x": 0.5,
                                        "center_y": 0.90},
                              size_hint=(0.05, 0.05),
                              font_size=30)
        self.remove_widget(self.refreshlbl)
        self.remove_widget(self.custname)
        self.add_widget(self.custname)


# Initializing the Order Screen
class Order(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(Order, self).__init__(**kwargs)

        # Order Part
        self.item_names = []
        self.items = {}
        for el in items_sql:
            self.items[el[0]] = [el[1], el[2]]
            self.item_names.append(el[0])

        # Initializing buttons
        self.dropdown_spinner1 = Spinner(text='Items',
                                         values=tuple(self.item_names),
                                         size_hint=(0.20, 0.1),
                                         pos_hint={'center_x': 0.28,
                                                   'center_y': 0.9},
                                         font_size=15)
        self.itemslbl = Label(text="Items : ",
                              pos_hint={"center_x": 0.138,
                                        "center_y": 0.9},
                              size_hint=(0.1, 0.1),
                              font_size=25)
        self.unitpricelbl = Label(text="Unit Price : ",
                                  pos_hint={"center_x": 0.1225,  # to make it precisely ahead to match the ' : '
                                            "center_y": 0.8},
                                  size_hint=(0.1, 0.1),
                                  font_size=25)
        self.dispunitpricelbl = Label(text="",
                                      pos_hint={"center_x": 0.21,
                                                "center_y": 0.8},
                                      size_hint=(0.1, 0.1),
                                      font_size=25)
        self.dispstocklbl = Label(text="Available Stock : ",
                                  pos_hint={"center_x": 0.1,
                                            "center_y": 0.7},
                                  size_hint=(0.1, 0.1),
                                  font_size=25)
        self.stocklbl = Label(text="",
                              pos_hint={"center_x": 0.2,
                                        "center_y": 0.7},
                              size_hint=(0.05, 0.05),
                              font_size=25)
        self.qtylbl = Label(text="Qty : ",
                            pos_hint={"center_x": 0.1485,
                                      "center_y": 0.6},
                            size_hint=(0.1, 0.1),
                            font_size=25)
        self.qty = TextInput(text="",
                             multiline=False,
                             pos_hint={"center_x": 0.20,
                                       "center_y": 0.6},
                             size_hint=(0.04, 0.05),
                             font_size=20)
        self.additems = Button(text="Add Item",
                               pos_hint={"center_x": 0.47,
                                         "center_y": 0.75},
                               size_hint=(0.1, 0.1),
                               font_size=15,
                               on_press=self.AddItemToOrder)
        self.itemqty0 = Label(text="Please enter the Qty field",
                              pos_hint={"center_x": 0.16,
                                        "center_y": 0.5},
                              size_hint=(0.1, 0.1),
                              font_size=25)
        self.itemremovelbl = Label(text="Item to remove : ",
                                   pos_hint={"center_x": 0.103,
                                             "center_y": 0.4},
                                   size_hint=(0.1, 0.1),
                                   font_size=25)
        self.dropdown_spinner2 = Spinner(text='Items',
                                         values=tuple(self.item_names),
                                         size_hint=(0.20, 0.1),
                                         pos_hint={'center_x': 0.28,
                                                   'center_y': 0.4},
                                         font_size=15)
        self.deleteitem = Button(text="Delete Item",
                                 pos_hint={"center_x": 0.47,
                                           "center_y": 0.4},
                                 size_hint=(0.1, 0.1),
                                 font_size=15,
                                 on_press=self.DeleteItem)
        self.notinorder = Label(text="Item not in order",
                                pos_hint={"center_x": 0.28,
                                          "center_y": 0.275},
                                size_hint=(0.1, 0.1),
                                font_size=25)
        self.itemremoved = Label(text="",
                                 pos_hint={"center_x": 0.28,
                                           "center_y": 0.275},
                                 size_hint=(0.1, 0.1),
                                 font_size=25)
        self.disptotalprice = Label(text="Total Price : ",
                                    pos_hint={"center_x": 0.12,
                                              "center_y": 0.15},
                                    size_hint=(0.1, 0.1),
                                    font_size=25)
        self.totalpricelbl = Label(text="0",
                                   pos_hint={"center_x": 0.22,
                                             "center_y": 0.15},
                                   size_hint=(0.05, 0.05),
                                   font_size=25)
        self.paybtn = Button(text="Pay",
                             pos_hint={"center_x": 0.47,
                                       "center_y": 0.15},
                             size_hint=(0.1, 0.1),
                             font_size=15,
                             on_press=self.PayOrder)
        self.max8itemlbl = Label(text="Maximum number of items is 8.",
                                 pos_hint={"center_x": 0.85,
                                           "center_y": 0.05},
                                 size_hint=(0.1, 0.9),
                                 font_size=15)

        # Table Part

        self.itemtable = Label(text="Item",
                               size_hint=(0.5, 0.5),
                               pos_hint={"center_x": 0.65,
                                         "center_y": 0.9},
                               font_size=25)
        self.qtytable = Label(text="Qty",
                              size_hint=(0.5, 0.5),
                              pos_hint={"center_x": 0.85,
                                        "center_y": 0.9},
                              font_size=25)
        self.pricetable = Label(text="Price",
                                size_hint=(0.5, 0.5),
                                pos_hint={"center_x": 0.95,
                                          "center_y": 0.9},
                                font_size=25)
        self.additemycoor = 0.8
        self.totalprice = 0
        # all the items of order in dict format
        self.order = {}

        # The total price label

        self.add_widget(self.dropdown_spinner1)
        self.add_widget(self.itemslbl)
        self.add_widget(self.unitpricelbl)
        self.add_widget(self.dispunitpricelbl)
        self.add_widget(self.qtylbl)
        self.add_widget(self.qty)
        self.add_widget(self.additems)
        self.add_widget(self.dispstocklbl)
        self.add_widget(self.stocklbl)
        self.add_widget(self.itemremovelbl)
        self.add_widget(self.deleteitem)
        self.add_widget(self.dropdown_spinner2)
        self.add_widget(Button(text="Back",
                               size_hint=(0.1, 0.05),
                               pos_hint={"center_x": 0.05,
                                         "center_y": 0.98},
                               on_press=self.BackToCustomer))
        self.add_widget(self.disptotalprice)
        self.add_widget(self.totalpricelbl)
        self.add_widget(self.paybtn)
        self.add_widget(self.max8itemlbl)

        self.add_widget(self.itemtable)
        self.add_widget(self.qtytable)
        self.add_widget(self.pricetable)

        self.itemnameinorder = Label()
        self.qtyorder = Label()
        self.priceorder = Label()

        def show1(dropdown_spinner1, text1):
            self.dispunitpricelbl.text = str(self.items[text1][0])
            self.stocklbl.text = str(self.items[text1][1])
            self.itemname1 = text1

        self.dropdown_spinner1.bind(text=show1)

        def show2(dropdown_spinner2, text2):
            self.itemname2 = text2

        self.dropdown_spinner2.bind(text=show2)
        self.deleteitemerr = Label(text="Choose an Item",
                                   pos_hint={"center_x": 0.28,
                                             "center_y": 0.275},
                                   size_hint=(0.1, 0.1),
                                   font_size=25)

    def AddItemToOrder(self, instance):
        itemqty = self.qty.text
        if itemqty == "":
            self.itemqty0.text = "Please enter the Qty field"
            self.remove_widget(self.itemqty0)
            self.add_widget(self.itemqty0)
        elif itemqty == "0":
            self.itemqty0.text = "Please check your Qty"
            self.remove_widget(self.itemqty0)
            self.add_widget(self.itemqty0)
        elif int(itemqty) > self.items[self.itemname1][1]:
            self.itemqty0.text = "Qty is more than Available Stock"
            self.remove_widget(self.itemqty0)
            self.add_widget(self.itemqty0)
        elif itemqty != "":
            self.remove_widget(self.itemqty0)
            self.qty.text = ""
            itemprice = int(itemqty) * self.items[self.itemname1][0]

            if self.itemname1 in self.order:
                self.order[self.itemname1][0] += int(itemqty)
                self.order[self.itemname1][1] += itemprice
            else:
                # here x is the index of the item name in item names list
                self.order[self.itemname1] = [int(itemqty), itemprice]
            # because of the overlapping
            self.clear_widgets()
            self.add_widget(self.dropdown_spinner1)
            self.add_widget(self.itemslbl)
            self.add_widget(self.unitpricelbl)
            self.add_widget(self.dispunitpricelbl)
            self.add_widget(self.qtylbl)
            self.add_widget(self.qty)
            self.add_widget(self.additems)
            self.add_widget(self.dispstocklbl)
            self.add_widget(self.stocklbl)
            self.add_widget(self.itemremovelbl)
            self.add_widget(self.deleteitem)
            self.add_widget(self.dropdown_spinner2)
            self.add_widget(Button(text="Back",
                                   size_hint=(0.1, 0.05),
                                   pos_hint={"center_x": 0.05,
                                             "center_y": 0.98},
                                   on_press=self.BackToCustomer))
            self.add_widget(self.disptotalprice)
            self.add_widget(self.totalpricelbl)
            self.add_widget(self.paybtn)
            self.add_widget(self.max8itemlbl)

            self.add_widget(self.itemtable)
            self.add_widget(self.qtytable)
            self.add_widget(self.pricetable)
            self.totalprice += itemprice
            for el in self.order:
                self.itemnameinorder = Label(text=str(el),
                                             size_hint=(0.1, 0.1),
                                             pos_hint={"center_x": 0.65,
                                                       "center_y": self.additemycoor},
                                             font_size=20)
                self.add_widget(self.itemnameinorder)
                self.qtyorder = Label(text=str(self.order[el][0]),
                                      size_hint=(0.1, 0.1),
                                      pos_hint={"center_x": 0.85,
                                                "center_y": self.additemycoor},
                                      font_size=20)
                self.add_widget(self.qtyorder)
                self.priceorder = Label(text=str(self.order[el][1]),
                                        size_hint=(0.1, 0.1),
                                        pos_hint={"center_x": 0.95,
                                                  "center_y": self.additemycoor},
                                        font_size=20)
                self.add_widget(self.priceorder)
                self.additemycoor -= 0.1
            print("Total Order", self.order)
            print("Total price after adding", self.totalprice)
            self.totalpricelbl.text = str(self.totalprice)
            self.additemycoor = 0.8
            for item in self.order:
                for items in items_sql:
                    if item == items[0]:
                        if self.order[item][0] > items[2]:
                            print("Because qty > stock")
                            self.order[item][0] -= int(itemqty)
                            self.order[item][1] -= itemprice
                            self.totalprice -= itemprice
                            # because of the overlapping
                            self.clear_widgets()
                            self.add_widget(self.dropdown_spinner1)
                            self.add_widget(self.itemslbl)
                            self.add_widget(self.unitpricelbl)
                            self.add_widget(self.dispunitpricelbl)
                            self.add_widget(self.qtylbl)
                            self.add_widget(self.qty)
                            self.add_widget(self.additems)
                            self.add_widget(self.dispstocklbl)
                            self.add_widget(self.stocklbl)
                            self.add_widget(self.itemremovelbl)
                            self.add_widget(self.deleteitem)
                            self.add_widget(self.dropdown_spinner2)
                            self.add_widget(Button(text="Back",
                                                   size_hint=(0.1, 0.05),
                                                   pos_hint={"center_x": 0.05,
                                                             "center_y": 0.98},
                                                   on_press=self.BackToCustomer))
                            self.add_widget(self.disptotalprice)
                            self.add_widget(self.totalpricelbl)
                            self.add_widget(self.paybtn)
                            self.add_widget(self.max8itemlbl)

                            self.add_widget(self.itemtable)
                            self.add_widget(self.qtytable)
                            self.add_widget(self.pricetable)
                            for el in self.order:
                                self.itemnameinorder = Label(text=str(el),
                                                             size_hint=(0.1, 0.1),
                                                             pos_hint={"center_x": 0.65,
                                                                       "center_y": self.additemycoor},
                                                             font_size=20)
                                self.add_widget(self.itemnameinorder)
                                self.qtyorder = Label(text=str(self.order[el][0]),
                                                      size_hint=(0.1, 0.1),
                                                      pos_hint={"center_x": 0.85,
                                                                "center_y": self.additemycoor},
                                                      font_size=20)
                                self.add_widget(self.qtyorder)
                                self.priceorder = Label(text=str(self.order[el][1]),
                                                        size_hint=(0.1, 0.1),
                                                        pos_hint={"center_x": 0.95,
                                                                  "center_y": self.additemycoor},
                                                        font_size=20)
                                self.add_widget(self.priceorder)
                                self.additemycoor -= 0.1
                            print("Total Order", self.order)
                            print("Total price after adding", self.totalprice)
                            self.totalpricelbl.text = str(self.totalprice)
                            self.additemycoor = 0.8

                            self.itemqty0.text = "Qty exceeds Available Stock"
                            self.remove_widget(self.itemqty0)
                            self.add_widget(self.itemqty0)

    def DeleteItem(self, instance):
        self.totalprice = 0
        self.remove_widget(self.itemremoved)
        try:
            if self.itemname2 not in self.order:
                self.remove_widget(self.deleteitemerr)
                self.remove_widget(self.notinorder)
                self.add_widget(self.notinorder)
            else:
                del self.order[self.itemname2]
                self.remove_widget(self.notinorder)
                self.remove_widget(self.itemremoved)
                self.itemremoved.text = self.itemname2 + " is removed"
                # because of the overlapping
                self.clear_widgets()
                self.add_widget(self.dropdown_spinner1)
                self.add_widget(self.itemslbl)
                self.add_widget(self.unitpricelbl)
                self.add_widget(self.dispunitpricelbl)
                self.add_widget(self.qtylbl)
                self.add_widget(self.qty)
                self.add_widget(self.additems)
                self.add_widget(self.dispstocklbl)
                self.add_widget(self.stocklbl)
                self.add_widget(self.itemremovelbl)
                self.add_widget(self.deleteitem)
                self.add_widget(self.dropdown_spinner2)
                self.add_widget(self.itemremoved)
                self.add_widget(Button(text="Back",
                                       size_hint=(0.1, 0.05),
                                       pos_hint={"center_x": 0.05,
                                                 "center_y": 0.98},
                                       on_press=self.BackToCustomer))
                self.add_widget(self.disptotalprice)
                self.add_widget(self.totalpricelbl)
                self.add_widget(self.paybtn)
                self.add_widget(self.max8itemlbl)

                self.add_widget(self.itemtable)
                self.add_widget(self.qtytable)
                self.add_widget(self.pricetable)
                for el in self.order:
                    self.itemnameinorder = Label(text=str(el),
                                                 size_hint=(0.1, 0.1),
                                                 pos_hint={"center_x": 0.65,
                                                           "center_y": self.additemycoor},
                                                 font_size=20)
                    self.add_widget(self.itemnameinorder)

                    self.qtyorder = Label(text=str(self.order[el][0]),
                                          size_hint=(0.1, 0.1),
                                          pos_hint={"center_x": 0.85,
                                                    "center_y": self.additemycoor},
                                          font_size=20)
                    self.add_widget(self.qtyorder)

                    self.priceorder = Label(text=str(self.order[el][1]),
                                            size_hint=(0.1, 0.1),
                                            pos_hint={"center_x": 0.95,
                                                      "center_y": self.additemycoor},
                                            font_size=20)
                    self.add_widget(self.priceorder)
                    self.additemycoor -= 0.1
                    self.totalprice += round(float(self.order[el][1]), 3)
                self.additemycoor = 0.8
                print("Order after deleting", self.order)
                print("Total price after Deleting", self.totalprice)
                self.totalpricelbl.text = str(self.totalprice)

        except AttributeError:
            self.remove_widget(self.deleteitemerr)
            self.add_widget(self.deleteitemerr)

    def PayOrder(self, instance):
        print("Paying over", self.order)
        # Remember to change the size_hint of float_layout and popup before executing
        self.float_layout = FloatLayout(size_hint=(0.5, 0.4),
                                        pos_hint={"center_x": 0.5,
                                                  "center_y": 0.7})
        self.billlbl = Label(text="Total Bill : " + str(
            self.totalprice) + "\n \nPlease click the exit button to exit the page." + "\nThank You!",
                             font_size=20,
                             pos_hint={"center_x": 0.6,
                                       "center_y": 0.03},
                             size_hint=(0.5, 0.5))
        self.exitbtn = Button(text="Exit",
                              font_size=20,
                              size_hint=(0.2, 0.4),
                              pos_hint={"center_x": 0.1,
                                        "center_y": 0.92},
                              on_press=self.BackToCustomerPay)
        if self.totalprice != 0:
            self.popup = Popup(title="Order Successfully Paid",
                               content=self.float_layout,
                               size_hint=(0.5, 0.4),
                               pos_hint={"center_x": 0.5,
                                         "center_y": 0.5},
                               auto_dismiss=False)
            # After Paying adding to SQL
            c.execute("select DISTINCT OrderNo from CustTest order by OrderNo;")
            allorderno = c.fetchall()
            self.allorderno = []
            for num in allorderno:
                self.allorderno.append(num[0])
            while True:
                randordnum = random.randint(10000, 99999)
                if randordnum not in self.allorderno:
                    break
                else:
                    randordnum = random.randint(10000, 99999)
            for el in self.order:
                c.execute("insert into CustTest values (%s, %s, %s, %s, %s, %s, %s)",
                          (CUSTOMER_ID, randordnum, el, self.order[el][0], self.order[el][1], self.totalprice,
                           "Active"))
                db.commit()
            print("Added values in  SQL")
            self.popup.open()
            for item in self.order:
                c.execute("UPDATE admin set Quantity = Quantity - %s where ItemName = %s", (self.order[item][0], item))
                db.commit()
        self.float_layout.add_widget(self.billlbl)
        self.float_layout.add_widget(self.exitbtn)

        # after adding as test order
        # c.execute("Delete from CustTest")
        # db.commit()

    def BackToCustomerPay(self, instance):
        self.clear_widgets()
        # To reset the spinners
        self.dropdown_spinner1 = Spinner(text='Items',
                                         values=tuple(self.item_names),
                                         size_hint=(0.20, 0.1),
                                         pos_hint={'center_x': 0.28,
                                                   'center_y': 0.9},
                                         font_size=15)

        def show1(dropdown_spinner1, text1):
            self.dispunitpricelbl.text = str(self.items[text1][0])
            self.stocklbl.text = str(self.items[text1][1])
            self.itemname1 = text1

        self.dropdown_spinner1.bind(text=show1)

        self.dropdown_spinner2 = Spinner(text='Items',
                                         values=tuple(self.item_names),
                                         size_hint=(0.20, 0.1),
                                         pos_hint={'center_x': 0.28,
                                                   'center_y': 0.4},
                                         font_size=15)

        def show2(dropdown_spinner2, text2):
            self.itemname2 = text2

        self.dropdown_spinner2.bind(text=show2)

        self.order = {}
        self.add_widget(self.dropdown_spinner1)
        self.add_widget(self.itemslbl)
        self.add_widget(self.unitpricelbl)
        self.add_widget(self.dispunitpricelbl)
        self.add_widget(self.qtylbl)
        self.add_widget(self.qty)
        self.add_widget(self.additems)
        self.add_widget(self.dispstocklbl)
        self.add_widget(self.stocklbl)
        self.add_widget(self.itemremovelbl)
        self.add_widget(self.deleteitem)
        self.add_widget(self.dropdown_spinner2)
        self.add_widget(Button(text="Back",
                               size_hint=(0.1, 0.05),
                               pos_hint={"center_x": 0.05,
                                         "center_y": 0.98},
                               on_press=self.gotoCustomer))
        self.add_widget(self.disptotalprice)
        self.add_widget(self.totalpricelbl)
        self.add_widget(self.paybtn)
        self.add_widget(self.max8itemlbl)

        self.add_widget(self.itemtable)
        self.add_widget(self.qtytable)
        self.add_widget(self.pricetable)
        self.dispunitpricelbl.text = ""
        self.stocklbl.text = ""
        self.totalpricelbl.text = ""
        self.order = {}
        self.totalprice = 0
        self.manager.current = "Customer"
        self.popup.dismiss()
        Refresh()

        c.execute("select * from admin")
        items_sql = list(c.fetchall())
        self.item_names = []
        self.items = {}
        for el in items_sql:
            self.items[el[0]] = [el[1], el[2]]
            self.item_names.append(el[0])

    def BackToCustomer(self, instance):
        self.clear_widgets()
        # To reset the spinners
        self.dropdown_spinner1 = Spinner(text='Items',
                                         values=tuple(self.item_names),
                                         size_hint=(0.20, 0.1),
                                         pos_hint={'center_x': 0.28,
                                                   'center_y': 0.9},
                                         font_size=15)

        def show1(dropdown_spinner1, text1):
            self.dispunitpricelbl.text = str(self.items[text1][0])
            self.stocklbl.text = str(self.items[text1][1])
            self.itemname1 = text1

        self.dropdown_spinner1.bind(text=show1)

        self.dropdown_spinner2 = Spinner(text='Items',
                                         values=tuple(self.item_names),
                                         size_hint=(0.20, 0.1),
                                         pos_hint={'center_x': 0.28,
                                                   'center_y': 0.4},
                                         font_size=15)

        def show2(dropdown_spinner2, text2):
            self.itemname2 = text2

        self.dropdown_spinner2.bind(text=show2)
        self.order = {}
        self.add_widget(self.dropdown_spinner1)
        self.add_widget(self.itemslbl)
        self.add_widget(self.unitpricelbl)
        self.add_widget(self.dispunitpricelbl)
        self.add_widget(self.qtylbl)
        self.qty.text = ""
        self.add_widget(self.qty)
        self.add_widget(self.additems)
        self.add_widget(self.dispstocklbl)
        self.add_widget(self.stocklbl)
        self.add_widget(self.itemremovelbl)
        self.add_widget(self.deleteitem)
        self.add_widget(self.dropdown_spinner2)
        self.add_widget(Button(text="Back",
                               size_hint=(0.1, 0.05),
                               pos_hint={"center_x": 0.05,
                                         "center_y": 0.98},
                               on_press=self.gotoCustomer))
        self.add_widget(self.disptotalprice)
        self.add_widget(self.totalpricelbl)
        self.add_widget(self.paybtn)
        self.add_widget(self.max8itemlbl)

        self.add_widget(self.itemtable)
        self.add_widget(self.qtytable)
        self.add_widget(self.pricetable)
        self.manager.current = "Customer"
        self.dispunitpricelbl.text = ""
        self.stocklbl.text = ""
        self.totalpricelbl.text = ""
        self.order = {}
        self.totalprice = 0

    def gotoCustomer(self, instance):
        self.manager.current = "Customer"


ordertoupdord = {}


class UpdCan(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(UpdCan, self).__init__(**kwargs)

        self.backbtn = Button(text="Back",
                              size_hint=(0.1, 0.05),
                              pos_hint={"center_x": 0.05,
                                        "center_y": 0.98},
                              on_press=self.BackToCustomer)
        # Getting all the orders from the Customer Table
        self.activeordersdisp = Label(text="Active Orders",
                                      size_hint=(0.5, 0.5),
                                      pos_hint={"center_x": 0.15,
                                                "center_y": 0.75},
                                      font_size=25)
        c.execute("select distinct OrderNo from CustTest where Status = 'Active' and CustID = '%s' order by OrderNo ;" % (CUSTOMER_ID))
        o = c.fetchall()
        self.activeorders = tuple()
        for el in o:
            self.activeorders += (str(el[0]),)

        if len(self.activeorders) == 0:
            self.dropdown_spinner1 = Spinner(text="Active Orders",
                                             values=tuple(["No Active Orders"]),
                                             size_hint=(0.20, 0.1),
                                             pos_hint={'center_x': 0.15,
                                                       'center_y': 0.65},
                                             font_size=15)
        else:
            self.dropdown_spinner1 = Spinner(text="Active Orders",
                                             values=tuple(self.activeorders),
                                             size_hint=(0.20, 0.1),
                                             pos_hint={'center_x': 0.15,
                                                       'center_y': 0.65},
                                             font_size=15)
        self.showorderbtn = Button(text="Show Order",
                                   size_hint=(0.1, 0.1),
                                   pos_hint={"center_x": 0.4,
                                             "center_y": 0.65},
                                   font_size=15,
                                   on_press=self.DisplayOrder)
        self.deleteorder = Button(text="Delete Order",
                                  size_hint=(0.1, 0.1),
                                  pos_hint={"center_x": 0.15,
                                            "center_y": 0.45},
                                  font_size=15,
                                  on_press=self.DeleteOrder)
        self.updateorder = Button(text="Update Order",
                                  size_hint=(0.1, 0.1),
                                  pos_hint={"center_x": 0.4,
                                            "center_y": 0.45},
                                  font_size=15,
                                  on_press=self.UpdateOrder)
        self.refreshbtn = Button(text="Refresh",
                                 size_hint=(0.1, 0.05),
                                 pos_hint={"center_x": 0.95,
                                           "center_y": 0.98},
                                 on_press=self.RefreshUpdCan)
        self.chooseorderlbl = Label(text="Choose an Order",
                                    pos_hint={"center_x": 0.15,
                                              "center_y": 0.3},
                                    size_hint=(0.1, 0.1),
                                    font_size=25)
        self.refreshwarninglbl = Label(text="Refresh the page to view recently added Orders.",
                                       pos_hint={"center_x": 0.25,
                                                 "center_y": 0.05},
                                       size_hint=(0.1, 0.9),
                                       font_size=15)
        self.orderdeletedlbl = Label(text="",
                                     pos_hint={"center_x": 0.15,
                                               "center_y": 0.3},
                                     size_hint=(0.1, 0.1),
                                     font_size=25)
        self.pricedisplbl = Label(text="Total Price : ",
                                  pos_hint={"center_x": 0.15,
                                            "center_y": 0.2},
                                  size_hint=(0.1, 0.1),
                                  font_size=25)
        self.pricelbl = Label(text="",
                              pos_hint={"center_x": 0.25,
                                        "center_y": 0.2},
                              size_hint=(0.1, 0.1),
                              font_size=25)

        # Table Part

        self.itemtable = Label(text="Item",
                               size_hint=(0.5, 0.5),
                               pos_hint={"center_x": 0.65,
                                         "center_y": 0.9},
                               font_size=25)
        self.qtytable = Label(text="Qty",
                              size_hint=(0.5, 0.5),
                              pos_hint={"center_x": 0.85,
                                        "center_y": 0.9},
                              font_size=25)
        self.pricetable = Label(text="Price",
                                size_hint=(0.5, 0.5),
                                pos_hint={"center_x": 0.95,
                                          "center_y": 0.9},
                                font_size=25)

        self.add_widget(self.activeordersdisp)
        self.add_widget(self.dropdown_spinner1)
        self.add_widget(self.showorderbtn)
        self.add_widget(self.backbtn)
        self.add_widget(self.deleteorder)
        self.add_widget(self.updateorder)
        self.add_widget(self.refreshbtn)
        self.add_widget(self.refreshwarninglbl)
        self.add_widget(self.pricedisplbl)
        self.add_widget(self.pricelbl)

        # Table Part
        self.add_widget(self.itemtable)
        self.add_widget(self.qtytable)
        self.add_widget(self.pricetable)

        def show1(dropdown_spinner1, text1):
            self.ordernoselected = text1

        self.dropdown_spinner1.bind(text=show1)
        self.additemycoor = 0.8

    def RefreshUpdCan(self, instance):
        c.execute("select distinct OrderNo from CustTest where Status = 'Active' and CustID = '%s' order by OrderNo;" % (CUSTOMER_ID))
        o = c.fetchall()
        self.activeorders = tuple()
        for el in o:
            self.activeorders += (str(el[0]),)
        # Re Initializing dropdown spinner
        if len(self.activeorders) == 0:
            self.dropdown_spinner1 = Spinner(text="Active Orders",
                                             values=tuple(["No Active Orders"]),
                                             size_hint=(0.20, 0.1),
                                             pos_hint={'center_x': 0.15,
                                                       'center_y': 0.65},
                                             font_size=15)
        else:
            self.dropdown_spinner1 = Spinner(text="Active Orders",
                                             values=tuple(self.activeorders),
                                             size_hint=(0.20, 0.1),
                                             pos_hint={'center_x': 0.15,
                                                       'center_y': 0.65},
                                             font_size=15)

        def show1(dropdown_spinner1, text1):
            self.ordernoselected = text1

        self.dropdown_spinner1.bind(text=show1)
        self.remove_widget(self.dropdown_spinner1)
        self.add_widget(self.dropdown_spinner1)

        # For overlapping
        self.clear_widgets()
        self.add_widget(self.activeordersdisp)
        self.add_widget(self.dropdown_spinner1)
        self.add_widget(self.showorderbtn)
        self.add_widget(self.backbtn)
        self.add_widget(self.deleteorder)
        self.add_widget(self.updateorder)
        self.add_widget(self.refreshbtn)
        self.add_widget(self.refreshwarninglbl)
        self.add_widget(self.pricedisplbl)
        self.pricelbl.text = ""
        self.add_widget(self.pricelbl)

        # Table Part
        self.add_widget(self.itemtable)
        self.add_widget(self.qtytable)
        self.add_widget(self.pricetable)

    def DisplayOrder(self, instance):
        try:
            print("ordered selected", self.ordernoselected)
            c.execute("select * from CustTest where CustID = '%s' and OrderNo = '%s'" % (CUSTOMER_ID, self.ordernoselected))
            o = c.fetchall()
            print("Order Selected to Display", o)
            self.orderselected = {self.ordernoselected: [], "Total Price": o[0][5]}
            for el in o:
                self.orderselected[self.ordernoselected].append([el[2], el[3], el[4]])
            # For overlapping
            self.clear_widgets()
            self.add_widget(self.activeordersdisp)
            self.add_widget(self.dropdown_spinner1)
            self.add_widget(self.showorderbtn)
            self.add_widget(self.backbtn)
            self.add_widget(self.deleteorder)
            self.add_widget(self.updateorder)
            self.add_widget(self.refreshbtn)
            self.add_widget(self.refreshwarninglbl)
            self.add_widget(self.pricedisplbl)
            self.add_widget(self.pricelbl)

            # Table Part
            self.add_widget(self.itemtable)
            self.add_widget(self.qtytable)
            self.add_widget(self.pricetable)
            for el in self.orderselected:
                if el == "Total Price":
                    continue
                for ele in self.orderselected[el]:
                    self.itemnameinorder = Label(text=str(ele[0]),
                                                 size_hint=(0.1, 0.1),
                                                 pos_hint={"center_x": 0.65,
                                                           "center_y": self.additemycoor},
                                                 font_size=20)
                    self.add_widget(self.itemnameinorder)

                    self.qtyorder = Label(text=str(ele[1]),
                                          size_hint=(0.1, 0.1),
                                          pos_hint={"center_x": 0.85,
                                                    "center_y": self.additemycoor},
                                          font_size=20)
                    self.add_widget(self.qtyorder)

                    self.priceorder = Label(text=str(ele[2]),
                                            size_hint=(0.1, 0.1),
                                            pos_hint={"center_x": 0.95,
                                                      "center_y": self.additemycoor},
                                            font_size=20)
                    self.add_widget(self.priceorder)
                    self.additemycoor -= 0.1
            self.additemycoor = 0.8
            self.pricelbl.text = str(o[0][5])
        except AttributeError:
            self.chooseorderlbl.text = "Choose Order"
            self.remove_widget(self.chooseorderlbl)
            self.add_widget(self.chooseorderlbl)

    def DeleteOrder(self, instance):
        try:
            print("OrderNo selected to delete", self.ordernoselected)
            c.execute(("select ItemName, Qty from custtest where CustID = '%s' and OrderNo = '%s'") %(CUSTOMER_ID,self.ordernoselected))
            o = c.fetchall()
            print(o)
            for el in o:
                c.execute("Update admin set Quantity = Quantity + '%s' where ItemName = '%s'" % (el[1], el[0]))
                db.commit()  # only thing is the above thing and upord thing which i have to ask maam other than that nothing is left

            c.execute(("Delete from CustTest where CustID = '%s' and OrderNo = '%s'") %(CUSTOMER_ID,str(self.ordernoselected))) 
            db.commit()

            # Order deleted
            self.orderdeletedlbl.text = "Order " + str(self.ordernoselected) + " Deleted"

            c.execute(("select distinct OrderNo from CustTest where CustID = '%s' and Status = 'Active' order by OrderNo") %(CUSTOMER_ID)) 
            o = c.fetchall()
            self.activeorders = tuple()
            for el in o:
                self.activeorders += (str(el[0]),)
            # Re Initializing dropdown spinner
            if len(self.activeorders) == 0:
                self.dropdown_spinner1 = Spinner(text="Active Orders",
                                                 values=tuple(["No Active Orders"]),
                                                 size_hint=(0.20, 0.1),
                                                 pos_hint={'center_x': 0.15,
                                                           'center_y': 0.65},
                                                 font_size=15)
            else:
                self.dropdown_spinner1 = Spinner(text="Active Orders",
                                                 values=tuple(self.activeorders),
                                                 size_hint=(0.20, 0.1),
                                                 pos_hint={'center_x': 0.15,
                                                           'center_y': 0.65},
                                                 font_size=15)

            def show1(dropdown_spinner1, text1):
                self.ordernoselected = text1

            self.dropdown_spinner1.bind(text=show1)
            self.remove_widget(self.dropdown_spinner1)
            self.add_widget(self.dropdown_spinner1)

            self.clear_widgets()
            self.add_widget(self.activeordersdisp)
            self.add_widget(self.dropdown_spinner1)
            self.add_widget(self.showorderbtn)
            self.add_widget(self.backbtn)
            self.add_widget(self.deleteorder)
            self.add_widget(self.updateorder)
            self.add_widget(self.refreshbtn)
            self.add_widget(self.refreshwarninglbl)
            self.add_widget(self.pricedisplbl)
            self.add_widget(self.pricelbl)

            # Table Part
            self.add_widget(self.itemtable)
            self.add_widget(self.qtytable)
            self.add_widget(self.pricetable)

            self.add_widget(self.orderdeletedlbl)
            self.pricelbl.text = ""

        except AttributeError:
            self.chooseorderlbl.text = "Choose an Order"
            self.remove_widget(self.chooseorderlbl)
            self.add_widget(self.chooseorderlbl)

    def BackToCustomer(self, instance):
        c.execute("select distinct OrderNo from CustTest where Status = 'Active' and CustID = '%s' order by OrderNo;" % (CUSTOMER_ID))
        o = c.fetchall()
        self.activeorders = tuple()
        for el in o:
            self.activeorders += (str(el[0]),)
        # Re Initializing dropdown spinner
        if len(self.activeorders) == 0:
            self.dropdown_spinner1 = Spinner(text="Active Orders",
                                             values=tuple(["No Active Orders"]),
                                             size_hint=(0.20, 0.1),
                                             pos_hint={'center_x': 0.15,
                                                       'center_y': 0.65},
                                             font_size=15)
        else:
            self.dropdown_spinner1 = Spinner(text="Active Orders",
                                             values=tuple(self.activeorders),
                                             size_hint=(0.20, 0.1),
                                             pos_hint={'center_x': 0.15,
                                                       'center_y': 0.65},
                                             font_size=15)

        def show1(dropdown_spinner1, text1):
            self.ordernoselected = text1

        self.dropdown_spinner1.bind(text=show1)
        self.remove_widget(self.dropdown_spinner1)
        self.add_widget(self.dropdown_spinner1)

        self.clear_widgets()

        self.add_widget(self.activeordersdisp)
        self.add_widget(self.dropdown_spinner1)
        self.add_widget(self.showorderbtn)
        self.add_widget(self.backbtn)
        self.add_widget(self.deleteorder)
        self.add_widget(self.updateorder)
        self.add_widget(self.refreshbtn)
        self.add_widget(self.refreshwarninglbl)
        self.add_widget(self.pricedisplbl)
        self.pricelbl.text = ""
        self.add_widget(self.pricelbl)

        # Table Part
        self.add_widget(self.itemtable)
        self.add_widget(self.qtytable)
        self.add_widget(self.pricetable)

        self.manager.current = "Customer"

    def UpdateOrder(self, instance):
        global ordertoupdord
        try:
            self.clear_widgets()

            c.execute("select distinct OrderNo from CustTest where Status = 'Active' and CustID = '%s' order by OrderNo;" % (CUSTOMER_ID))
            o = c.fetchall()
            self.activeorders = tuple()
            for el in o:
                self.activeorders += (str(el[0]),)
            # Re Initializing dropdown spinner
            self.dropdown_spinner1 = Spinner(text='Active Orders',
                                             values=tuple(self.activeorders),
                                             size_hint=(0.20, 0.1),
                                             pos_hint={'center_x': 0.15,
                                                       'center_y': 0.65},
                                             font_size=15)

            def show1(dropdown_spinner1, text1):
                self.ordernoselected = text1

            self.dropdown_spinner1.bind(text=show1)

            self.add_widget(self.activeordersdisp)
            self.add_widget(self.dropdown_spinner1)
            self.add_widget(self.showorderbtn)
            self.add_widget(self.backbtn)
            self.add_widget(self.deleteorder)
            self.add_widget(self.updateorder)
            self.add_widget(self.refreshbtn)
            self.add_widget(self.refreshwarninglbl)
            self.add_widget(self.pricedisplbl)
            self.add_widget(self.pricelbl)

            # Table Part
            self.add_widget(self.itemtable)
            self.add_widget(self.qtytable)
            self.add_widget(self.pricetable)

            self.pricelbl.text = ""

            ordertoupdord = self.orderselected
            self.manager.current = "UpdOrd"

        except AttributeError:
            self.chooseorderlbl.text = "Display the Order first"
            self.remove_widget(self.chooseorderlbl)
            self.add_widget(self.chooseorderlbl)


# Initializing the Update Order Screen
class UpdOrd(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(UpdOrd, self).__init__(**kwargs)

        # Starting Updating Order
        self.ordtoupdate = ordertoupdord

        # Order Part
        self.item_names = []
        self.items = {}
        for el in items_sql:
            self.items[el[0]] = [el[1], el[2]]
            self.item_names.append(el[0])

        # Initializing buttons
        self.dropdown_spinner1 = Spinner(text='Items',
                                         values=tuple(self.item_names),
                                         size_hint=(0.20, 0.1),
                                         pos_hint={'center_x': 0.28,
                                                   'center_y': 0.9},
                                         font_size=15)
        self.itemslbl = Label(text="Items : ",
                              pos_hint={"center_x": 0.138,
                                        "center_y": 0.9},
                              size_hint=(0.1, 0.1),
                              font_size=25)
        self.unitpricelbl = Label(text="Unit Price : ",
                                  pos_hint={"center_x": 0.1225,  # to make it precisely ahead to match the ' : '
                                            "center_y": 0.8},
                                  size_hint=(0.1, 0.1),
                                  font_size=25)
        self.dispunitpricelbl = Label(text="",
                                      pos_hint={"center_x": 0.21,
                                                "center_y": 0.8},
                                      size_hint=(0.1, 0.1),
                                      font_size=25)
        self.dispstocklbl = Label(text="Available Stock : ",
                                  pos_hint={"center_x": 0.1,
                                            "center_y": 0.7},
                                  size_hint=(0.1, 0.1),
                                  font_size=25)
        self.stocklbl = Label(text="",
                              pos_hint={"center_x": 0.2,
                                        "center_y": 0.7},
                              size_hint=(0.05, 0.05),
                              font_size=25)
        self.qtylbl = Label(text="Qty : ",
                            pos_hint={"center_x": 0.1485,
                                      "center_y": 0.6},
                            size_hint=(0.1, 0.1),
                            font_size=25)
        self.qty = TextInput(text="",
                             multiline=False,
                             pos_hint={"center_x": 0.20,
                                       "center_y": 0.6},
                             size_hint=(0.04, 0.05),
                             font_size=20)
        self.additems = Button(text="Add Item",
                               pos_hint={"center_x": 0.47,
                                         "center_y": 0.75},
                               size_hint=(0.1, 0.1),
                               font_size=15,
                               on_press=self.AddItemToOrder)
        self.itemqty0 = Label(text="Please enter the Qty field",
                              pos_hint={"center_x": 0.17,
                                        "center_y": 0.5},
                              size_hint=(0.1, 0.1),
                              font_size=25)
        self.itemremovelbl = Label(text="Item to remove : ",
                                   pos_hint={"center_x": 0.103,
                                             "center_y": 0.4},
                                   size_hint=(0.1, 0.1),
                                   font_size=25)
        self.dropdown_spinner2 = Spinner(text='Items',
                                         values=tuple(self.item_names),
                                         size_hint=(0.20, 0.1),
                                         pos_hint={'center_x': 0.28,
                                                   'center_y': 0.4},
                                         font_size=15)
        self.deleteitem = Button(text="Delete Item",
                                 pos_hint={"center_x": 0.47,
                                           "center_y": 0.4},
                                 size_hint=(0.1, 0.1),
                                 font_size=15,
                                 on_press=self.DeleteItem)
        self.notinorder = Label(text="Item not in order",
                                pos_hint={"center_x": 0.28,
                                          "center_y": 0.275},
                                size_hint=(0.1, 0.1),
                                font_size=25)
        self.itemremoved = Label(text="",
                                 pos_hint={"center_x": 0.28,
                                           "center_y": 0.275},
                                 size_hint=(0.1, 0.1),
                                 font_size=25)
        self.disptotalprice = Label(text="Total Price : ",
                                    pos_hint={"center_x": 0.12,
                                              "center_y": 0.15},
                                    size_hint=(0.1, 0.1),
                                    font_size=25)
        self.totalpricelbl = Label(text="0",
                                   pos_hint={"center_x": 0.22,
                                             "center_y": 0.15},
                                   size_hint=(0.05, 0.05),
                                   font_size=25)
        self.paybtn = Button(text="Pay",
                             pos_hint={"center_x": 0.47,
                                       "center_y": 0.15},
                             size_hint=(0.1, 0.1),
                             font_size=15,
                             on_press=self.PayOrder)
        self.refreshwarninglbl = Label(text="Refresh the page to Update Order.",
                                       pos_hint={"center_x": 0.25,
                                                 "center_y": 0.05},
                                       size_hint=(0.1, 0.9),
                                       font_size=15)
        self.refreshbtn = Button(text="Refresh",
                                 size_hint=(0.1, 0.05),
                                 pos_hint={"center_x": 0.95,
                                           "center_y": 0.98},
                                 on_press=self.DisplayOrderToUpdate)
        self.ordernoontop = Label(text="",
                                  pos_hint={"center_x": 0.5,
                                            "center_y": 0.97},
                                  size_hint=(0.05, 0.05),
                                  font_size=25)
        self.max8itemslbl = Label(text="Maximum number of items is 8.",
                                  pos_hint={"center_x": 0.85,
                                            "center_y": 0.05},
                                  size_hint=(0.1, 0.9),
                                  font_size=15)

        self.deleteitemerr = Label(text="Choose an Item",
                                   pos_hint={"center_x": 0.28,
                                             "center_y": 0.275},
                                   size_hint=(0.1, 0.1),
                                   font_size=25)

        # Table Part

        self.itemtable = Label(text="Item",
                               size_hint=(0.5, 0.5),
                               pos_hint={"center_x": 0.65,
                                         "center_y": 0.9},
                               font_size=25)
        self.qtytable = Label(text="Qty",
                              size_hint=(0.5, 0.5),
                              pos_hint={"center_x": 0.85,
                                        "center_y": 0.9},
                              font_size=25)
        self.pricetable = Label(text="Price",
                                size_hint=(0.5, 0.5),
                                pos_hint={"center_x": 0.95,
                                          "center_y": 0.9},
                                font_size=25)
        self.additemycoor = 0.8
        self.totalprice = 0

        self.add_widget(self.dropdown_spinner1)
        self.add_widget(self.itemslbl)
        self.add_widget(self.unitpricelbl)
        self.add_widget(self.dispunitpricelbl)
        self.add_widget(self.qtylbl)
        self.add_widget(self.qty)
        self.add_widget(self.additems)
        self.add_widget(self.dispstocklbl)
        self.add_widget(self.stocklbl)
        self.add_widget(self.itemremovelbl)
        self.add_widget(self.deleteitem)
        self.add_widget(self.dropdown_spinner2)
        self.add_widget(Button(text="Back",
                               size_hint=(0.1, 0.05),
                               pos_hint={"center_x": 0.05,
                                         "center_y": 0.98},
                               on_press=self.BackToUpdCan))
        self.add_widget(self.disptotalprice)
        self.add_widget(self.totalpricelbl)
        self.add_widget(self.paybtn)
        self.add_widget(self.refreshwarninglbl)
        self.add_widget(self.refreshbtn)
        self.add_widget(self.ordernoontop)
        self.add_widget(self.max8itemslbl)

        self.add_widget(self.itemtable)
        self.add_widget(self.qtytable)
        self.add_widget(self.pricetable)

        self.itemnameinorder = Label()
        self.qtyorder = Label()
        self.priceorder = Label()

        def show1(dropdown_spinner1, text1):
            self.dispunitpricelbl.text = str(self.items[text1][0])
            self.stocklbl.text = str(self.items[text1][1])
            self.itemname1 = text1

        self.dropdown_spinner1.bind(text=show1)

        def show2(dropdown_spinner2, text2):
            self.itemname2 = text2

        self.dropdown_spinner2.bind(text=show2)

    def DisplayOrderToUpdate(self, instance):
        c.execute("select * from admin")
        items_sql = list(c.fetchall())

        # Order Part
        self.item_names = []
        self.items = {}
        for el in items_sql:
            self.items[el[0]] = [el[1], el[2]]
            self.item_names.append(el[0])

        self.dropdown_spinner1 = Spinner(text='Items',
                                         values=tuple(self.item_names),
                                         size_hint=(0.20, 0.1),
                                         pos_hint={'center_x': 0.28,
                                                   'center_y': 0.9},
                                         font_size=15)

        def show1(dropdown_spinner1, text1):
            self.dispunitpricelbl.text = str(self.items[text1][0])
            self.stocklbl.text = str(self.items[text1][1])
            self.itemname1 = text1

        self.dropdown_spinner1.bind(text=show1)

        self.ordtoupdate = ordertoupdord
        for el in self.ordtoupdate:
            if el == "Total Price":
                self.totalprice = self.ordtoupdate[el]
        print("Display Order Function  Executing and value", self.ordtoupdate)
        for el in self.ordtoupdate:
            if el != "Total Price":
                self.updordnum = el
                self.ordernoontop.text = "Order No. : " + str(el)
        self.totalpricelbl.text = str(self.totalprice)
        self.clear_widgets()
        self.add_widget(self.dropdown_spinner1)
        self.add_widget(self.itemslbl)
        self.add_widget(self.unitpricelbl)
        self.add_widget(self.dispunitpricelbl)
        self.add_widget(self.qtylbl)
        self.add_widget(self.qty)
        self.add_widget(self.additems)
        self.add_widget(self.dispstocklbl)
        self.add_widget(self.stocklbl)
        self.add_widget(self.itemremovelbl)
        self.add_widget(self.deleteitem)
        self.add_widget(self.dropdown_spinner2)
        self.add_widget(Button(text="Back",
                               size_hint=(0.1, 0.05),
                               pos_hint={"center_x": 0.05,
                                         "center_y": 0.98},
                               on_press=self.BackToUpdCan))
        self.add_widget(self.disptotalprice)
        self.add_widget(self.totalpricelbl)
        self.add_widget(self.paybtn)
        self.add_widget(self.refreshwarninglbl)
        self.add_widget(self.refreshbtn)
        self.add_widget(self.ordernoontop)
        self.add_widget(self.max8itemslbl)

        self.add_widget(self.itemtable)
        self.add_widget(self.qtytable)
        self.add_widget(self.pricetable)

        for el in self.ordtoupdate:
            if el == "Total Price":
                continue
            for ele in self.ordtoupdate[el]:
                self.itemnameinorder = Label(text=str(ele[0]),
                                             size_hint=(0.1, 0.1),
                                             pos_hint={"center_x": 0.65,
                                                       "center_y": self.additemycoor},
                                             font_size=20)
                self.add_widget(self.itemnameinorder)

                self.qtyorder = Label(text=str(ele[1]),
                                      size_hint=(0.1, 0.1),
                                      pos_hint={"center_x": 0.85,
                                                "center_y": self.additemycoor},
                                      font_size=20)
                self.add_widget(self.qtyorder)

                self.priceorder = Label(text=str(ele[2]),
                                        size_hint=(0.1, 0.1),
                                        pos_hint={"center_x": 0.95,
                                                  "center_y": self.additemycoor},
                                        font_size=20)
                self.add_widget(self.priceorder)
                self.additemycoor -= 0.1
            self.additemycoor = 0.8

    def AddItemToOrder(self, instance):
        try:
            itemqty = self.qty.text
            if itemqty == "":
                self.itemqty0.text = "Please enter the Qty field"
                self.remove_widget(self.itemqty0)
                self.add_widget(self.itemqty0)
            elif itemqty == "0":
                self.itemqty0.text = "Please check your Qty"
                self.remove_widget(self.itemqty0)
                self.add_widget(self.itemqty0)
            elif int(itemqty) > self.items[self.itemname1][1]:
                self.itemqty0.text = "Qty is more than Available Stock"
                self.remove_widget(self.itemqty0)
                self.add_widget(self.itemqty0)
            elif itemqty != "":
                self.remove_widget(self.itemqty0)
                self.qty.text = ""
                itemprice = int(itemqty) * self.items[self.itemname1][0]
                # to check for a condition
                x = 0
                for el in self.ordtoupdate[self.updordnum]:
                    if el[0] == self.itemname1:
                        el[1] += int(itemqty)
                        el[2] += itemprice
                        x = 1
                if x != 1:
                    # here x is the index of the item name in item names list
                    self.ordtoupdate[self.updordnum].append([self.itemname1, int(itemqty), itemprice])
                # because of the overlapping
                self.clear_widgets()
                self.add_widget(self.dropdown_spinner1)
                self.add_widget(self.itemslbl)
                self.add_widget(self.unitpricelbl)
                self.add_widget(self.dispunitpricelbl)
                self.add_widget(self.qtylbl)
                self.add_widget(self.qty)
                self.add_widget(self.additems)
                self.add_widget(self.dispstocklbl)
                self.add_widget(self.stocklbl)
                self.add_widget(self.itemremovelbl)
                self.add_widget(self.deleteitem)
                self.add_widget(self.dropdown_spinner2)
                self.add_widget(Button(text="Back",
                                       size_hint=(0.1, 0.05),
                                       pos_hint={"center_x": 0.05,
                                                 "center_y": 0.98},
                                       on_press=self.BackToUpdCan))
                self.add_widget(self.disptotalprice)
                self.add_widget(self.totalpricelbl)
                self.add_widget(self.paybtn)
                self.add_widget(self.refreshwarninglbl)
                self.add_widget(self.refreshbtn)
                self.add_widget(self.ordernoontop)
                self.add_widget(self.max8itemslbl)

                self.add_widget(self.itemtable)
                self.add_widget(self.qtytable)
                self.add_widget(self.pricetable)
                # Adding to Total Price over here
                self.totalprice += itemprice
                self.ordtoupdate["Total Price"] = self.totalprice
                for el in self.ordtoupdate:
                    if el == "Total Price":
                        continue
                    for ele in self.ordtoupdate[el]:
                        self.itemnameinorder = Label(text=str(ele[0]),
                                                     size_hint=(0.1, 0.1),
                                                     pos_hint={"center_x": 0.65,
                                                               "center_y": self.additemycoor},
                                                     font_size=20)
                        self.add_widget(self.itemnameinorder)

                        self.qtyorder = Label(text=str(ele[1]),
                                              size_hint=(0.1, 0.1),
                                              pos_hint={"center_x": 0.85,
                                                        "center_y": self.additemycoor},
                                              font_size=20)
                        self.add_widget(self.qtyorder)

                        self.priceorder = Label(text=str(ele[2]),
                                                size_hint=(0.1, 0.1),
                                                pos_hint={"center_x": 0.95,
                                                          "center_y": self.additemycoor},
                                                font_size=20)
                        self.add_widget(self.priceorder)
                        self.additemycoor -= 0.1
                    self.additemycoor = 0.8
                print("Total Order", self.ordtoupdate)
                print("Total price after adding", self.totalprice)
                self.totalpricelbl.text = str(self.totalprice)
        except AttributeError:
            self.itemqty0.text = "Please refresh the page"
            self.remove_widget(self.itemqty0)
            self.add_widget(self.itemqty0)
            print("Error")

    def DeleteItem(self, instance):
        self.remove_widget(self.itemremoved)
        try:
            x = 0
            for item in self.ordtoupdate[self.updordnum]:
                if item[0] != self.itemname2:
                    x += 1
                if x == len(self.ordtoupdate[self.updordnum]):
                    # to prevent overlapping
                    self.clear_widgets()
                    self.add_widget(self.dropdown_spinner1)
                    self.add_widget(self.itemslbl)
                    self.add_widget(self.unitpricelbl)
                    self.add_widget(self.dispunitpricelbl)
                    self.add_widget(self.qtylbl)
                    self.add_widget(self.qty)
                    self.add_widget(self.additems)
                    self.add_widget(self.dispstocklbl)
                    self.add_widget(self.stocklbl)
                    self.add_widget(self.itemremovelbl)
                    self.add_widget(self.deleteitem)
                    self.add_widget(self.dropdown_spinner2)
                    self.add_widget(Button(text="Back",
                                           size_hint=(0.1, 0.05),
                                           pos_hint={"center_x": 0.05,
                                                     "center_y": 0.98},
                                           on_press=self.BackToUpdCan))
                    self.add_widget(self.disptotalprice)
                    self.add_widget(self.totalpricelbl)
                    self.add_widget(self.paybtn)
                    self.add_widget(self.refreshwarninglbl)
                    self.add_widget(self.refreshbtn)
                    self.add_widget(self.ordernoontop)
                    self.add_widget(self.max8itemslbl)

                    self.add_widget(self.itemtable)
                    self.add_widget(self.qtytable)
                    self.add_widget(self.pricetable)

                    for el in self.ordtoupdate:
                        if el == "Total Price":
                            continue
                        for ele in self.ordtoupdate[el]:
                            self.itemnameinorder = Label(text=str(ele[0]),
                                                         size_hint=(0.1, 0.1),
                                                         pos_hint={"center_x": 0.65,
                                                                   "center_y": self.additemycoor},
                                                         font_size=20)
                            self.add_widget(self.itemnameinorder)

                            self.qtyorder = Label(text=str(ele[1]),
                                                  size_hint=(0.1, 0.1),
                                                  pos_hint={"center_x": 0.85,
                                                            "center_y": self.additemycoor},
                                                  font_size=20)
                            self.add_widget(self.qtyorder)

                            self.priceorder = Label(text=str(ele[2]),
                                                    size_hint=(0.1, 0.1),
                                                    pos_hint={"center_x": 0.95,
                                                              "center_y": self.additemycoor},
                                                    font_size=20)
                            self.add_widget(self.priceorder)
                            self.additemycoor -= 0.1
                        self.additemycoor = 0.8
                    self.remove_widget(self.notinorder)
                    self.add_widget(self.notinorder)
                if item[0] == self.itemname2:
                    self.ordtoupdate[self.updordnum].remove(item)
                    # because of the overlapping
                    self.clear_widgets()
                    self.add_widget(self.dropdown_spinner1)
                    self.add_widget(self.itemslbl)
                    self.add_widget(self.unitpricelbl)
                    self.add_widget(self.dispunitpricelbl)
                    self.add_widget(self.qtylbl)
                    self.add_widget(self.qty)
                    self.add_widget(self.additems)
                    self.add_widget(self.dispstocklbl)
                    self.add_widget(self.stocklbl)
                    self.add_widget(self.itemremovelbl)
                    self.add_widget(self.deleteitem)
                    self.add_widget(self.dropdown_spinner2)
                    self.add_widget(Button(text="Back",
                                           size_hint=(0.1, 0.05),
                                           pos_hint={"center_x": 0.05,
                                                     "center_y": 0.98},
                                           on_press=self.BackToUpdCan))
                    self.add_widget(self.disptotalprice)
                    self.add_widget(self.totalpricelbl)
                    self.add_widget(self.paybtn)
                    self.add_widget(self.refreshwarninglbl)
                    self.add_widget(self.refreshbtn)
                    self.add_widget(self.ordernoontop)
                    self.add_widget(self.max8itemslbl)

                    self.add_widget(self.itemtable)
                    self.add_widget(self.qtytable)
                    self.add_widget(self.pricetable)
                    self.totalprice = 0
                    self.add_widget(self.itemremoved)
                    self.itemremoved.text = str(self.itemname2) + " is removed"
                    for el in self.ordtoupdate:
                        if el == "Total Price":
                            continue
                        for ele in self.ordtoupdate[el]:
                            self.itemnameinorder = Label(text=str(ele[0]),
                                                         size_hint=(0.1, 0.1),
                                                         pos_hint={"center_x": 0.65,
                                                                   "center_y": self.additemycoor},
                                                         font_size=20)
                            self.add_widget(self.itemnameinorder)

                            self.qtyorder = Label(text=str(ele[1]),
                                                  size_hint=(0.1, 0.1),
                                                  pos_hint={"center_x": 0.85,
                                                            "center_y": self.additemycoor},
                                                  font_size=20)
                            self.add_widget(self.qtyorder)

                            self.priceorder = Label(text=str(ele[2]),
                                                    size_hint=(0.1, 0.1),
                                                    pos_hint={"center_x": 0.95,
                                                              "center_y": self.additemycoor},
                                                    font_size=20)
                            self.add_widget(self.priceorder)
                            self.totalprice += ele[2]
                            self.additemycoor -= 0.1
                        self.additemycoor = 0.8
            print("Order after deleting", self.ordtoupdate)
            print("Total price after Deleting", self.totalprice)
            self.totalpricelbl.text = str(self.totalprice)
        except AttributeError:
            self.deleteitemerr.text = "Choose an Item"
            self.remove_widget(self.deleteitemerr)
            self.add_widget(self.deleteitemerr)
            try:
                if self.itemname2 != "":
                    self.deleteitemerr.text = "Please refresh the page."
                    self.remove_widget(self.deleteitemerr)
                    self.add_widget(self.deleteitemerr)
            except AttributeError:
                pass

    # Delete Order done proper now PayOrder is left

    def PayOrder(self, instance):
        # Remember to change the size_hint of float_layout and popup before executing
        self.float_layout = FloatLayout(size_hint=(0.5, 0.4),
                                        pos_hint={"center_x": 0.5,
                                                  "center_y": 0.7})
        self.billlbl = Label(text="Total Bill : " + str(
            self.totalprice) + "\n \nPlease click the back button to exit the page." + "\nThank You!",
                             font_size=20,
                             pos_hint={"center_x": 0.6,
                                       "center_y": 0.03},
                             size_hint=(0.5, 0.5))
        self.exitbtn = Button(text="Exit",
                              font_size=20,
                              size_hint=(0.2, 0.4),
                              pos_hint={"center_x": 0.1,
                                        "center_y": 0.92},
                              on_press=self.BackToCustomerPay)
        if self.totalprice != 0:
            self.popup = Popup(title="Order Successfully Paid",
                               content=self.float_layout,
                               size_hint=(0.5, 0.4),
                               pos_hint={"center_x": 0.5,
                                         "center_y": 0.5},
                               auto_dismiss=False)
            # After Paying adding to SQL
            # Removing stock
            c.execute("select Itemname, Qty, Price from custtest where OrderNo = '%s' and CustID = '%s';" % (self.updordnum, CUSTOMER_ID))
            o = c.fetchall()
            oldorder = []
            for el in o:
                oldorder.append(list(el))
            c.execute("select * from admin;")
            adminstock = c.fetchall()
            for el in adminstock:
                for ele in oldorder:
                    if el[0] == ele[0]:
                        ele[1] += el[2]
            print("1", oldorder)
            print("2", self.ordtoupdate[self.updordnum])
            for item in self.ordtoupdate[self.updordnum]:
                for olditem in oldorder:
                    if item[0] == olditem[0]:
                        print("Content removed from", item[0], olditem[1] - item[1])
                        c.execute("UPDATE admin set Quantity = '%s' where ItemName = '%s';" % (
                            abs(olditem[1] - item[1]), olditem[0]))
                        db.commit()
                    else:
                        print("Content added extra", olditem[1], olditem[0])
                        c.execute("UPDATE admin set Quantity = '%s' where ItemName = '%s';" % (olditem[1], olditem[0]))
                        db.commit()

            # good part
            c.execute("delete from CustTest where OrderNo = %s and CustID = '%s';" % (self.updordnum, CUSTOMER_ID))
            db.commit()
            for el in self.ordtoupdate[self.updordnum]:
                    c.execute("insert into CustTest values (%s, %s, %s, %s, %s, %s, %s)",
                              (CUSTOMER_ID, self.updordnum, el[0], el[1], el[2], self.totalprice, "Active"))
                    db.commit()
            print("Added values in  SQL")
            self.popup.open()
        self.float_layout.add_widget(self.billlbl)
        self.float_layout.add_widget(self.exitbtn)

        # after adding as test order
        # c.execute("Delete from CustTest")
        # db.commit()

    def BackToCustomerPay(self, instance):
        self.clear_widgets()
        # To reset the spinners
        self.dropdown_spinner1 = Spinner(text='Items',
                                         values=tuple(self.item_names),
                                         size_hint=(0.20, 0.1),
                                         pos_hint={'center_x': 0.28,
                                                   'center_y': 0.9},
                                         font_size=15)

        def show1(dropdown_spinner1, text1):
            self.dispunitpricelbl.text = str(self.items[text1][0])
            self.stocklbl.text = str(self.items[text1][1])
            self.itemname1 = text1

        self.dropdown_spinner1.bind(text=show1)

        self.dropdown_spinner2 = Spinner(text='Items',
                                         values=tuple(self.item_names),
                                         size_hint=(0.20, 0.1),
                                         pos_hint={'center_x': 0.28,
                                                   'center_y': 0.4},
                                         font_size=15)

        def show2(dropdown_spinner2, text2):
            self.itemname2 = text2

        self.dropdown_spinner2.bind(text=show2)

        self.order = {}
        self.add_widget(self.dropdown_spinner1)
        self.add_widget(self.itemslbl)
        self.add_widget(self.unitpricelbl)
        self.add_widget(self.dispunitpricelbl)
        self.add_widget(self.qtylbl)
        self.add_widget(self.qty)
        self.add_widget(self.additems)
        self.add_widget(self.dispstocklbl)
        self.add_widget(self.stocklbl)
        self.add_widget(self.itemremovelbl)
        self.add_widget(self.deleteitem)
        self.add_widget(self.dropdown_spinner2)
        self.add_widget(Button(text="Back",
                               size_hint=(0.1, 0.05),
                               pos_hint={"center_x": 0.05,
                                         "center_y": 0.98},
                               on_press=self.gotoCustomer))
        self.add_widget(self.disptotalprice)
        self.add_widget(self.totalpricelbl)
        self.add_widget(self.paybtn)
        self.add_widget(self.refreshwarninglbl)
        self.add_widget(self.refreshbtn)
        self.add_widget(self.max8itemslbl)

        self.add_widget(self.itemtable)
        self.add_widget(self.qtytable)
        self.add_widget(self.pricetable)
        self.dispunitpricelbl.text = ""
        self.stocklbl.text = ""
        self.totalpricelbl.text = ""
        self.order = {}
        self.totalprice = 0
        self.manager.current = "Customer"
        self.popup.dismiss()

    def BackToUpdCan(self, instance):
        self.clear_widgets()
        # To reset the spinners
        self.dropdown_spinner1 = Spinner(text='Items',
                                         values=tuple(self.item_names),
                                         size_hint=(0.20, 0.1),
                                         pos_hint={'center_x': 0.28,
                                                   'center_y': 0.9},
                                         font_size=15)

        def show1(dropdown_spinner1, text1):
            self.dispunitpricelbl.text = str(self.items[text1][0])
            self.stocklbl.text = str(self.items[text1][1])
            self.itemname1 = text1

        self.dropdown_spinner1.bind(text=show1)

        self.dropdown_spinner2 = Spinner(text='Items',
                                         values=tuple(self.item_names),
                                         size_hint=(0.20, 0.1),
                                         pos_hint={'center_x': 0.28,
                                                   'center_y': 0.4},
                                         font_size=15)

        def show2(dropdown_spinner2, text2):
            self.itemname2 = text2

        self.dropdown_spinner2.bind(text=show2)

        self.add_widget(self.dropdown_spinner1)
        self.add_widget(self.itemslbl)
        self.add_widget(self.unitpricelbl)
        self.add_widget(self.dispunitpricelbl)
        self.add_widget(self.qtylbl)
        self.add_widget(self.qty)
        self.add_widget(self.additems)
        self.add_widget(self.dispstocklbl)
        self.add_widget(self.stocklbl)
        self.add_widget(self.itemremovelbl)
        self.add_widget(self.deleteitem)
        self.add_widget(self.dropdown_spinner2)
        self.add_widget(Button(text="Back",
                               size_hint=(0.1, 0.05),
                               pos_hint={"center_x": 0.05,
                                         "center_y": 0.98},
                               on_press=self.BackToUpdCan))
        self.add_widget(self.disptotalprice)
        self.add_widget(self.totalpricelbl)
        self.add_widget(self.paybtn)
        self.add_widget(self.refreshwarninglbl)
        self.add_widget(self.refreshbtn)
        self.ordernoontop.text = ""
        self.add_widget(self.ordernoontop)
        self.add_widget(self.max8itemslbl)

        self.add_widget(self.itemtable)
        self.add_widget(self.qtytable)
        self.add_widget(self.pricetable)
        self.manager.current = "Updcan"
        self.dispunitpricelbl.text = ""
        self.stocklbl.text = ""
        self.totalpricelbl.text = ""
        self.totalprice = 0

    def gotoCustomer(self, instance):
        self.manager.current = "Customer"


class Checkord(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(Checkord, self).__init__(**kwargs)
        self.add_widget(Button(text="Back",
                               size_hint=(0.1, 0.05),
                               pos_hint={"center_x": 0.05,
                                         "center_y": 0.98},
                               on_press=self.gotoCustomer))

    def gotoCustomer(self, instance):
        self.manager.current = "Customer"

class Feedback(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(Feedback, self).__init__(**kwargs)
        self.add_widget(Button(text="Back",
                               size_hint=(0.1, 0.05),
                               pos_hint={"center_x": 0.05,
                                         "center_y": 0.98},
                               on_press=self.gotoCustomerfeed))

        self.add_widget(Label(text="Enter your feedback here: (30 Characters Maximum)",
                              font_size=25,
                              size_hint=(0.5, 0.1),
                              pos_hint={"center_x": 0.5,
                                        "center_y": 0.67}))

        self.text = TextInput(size_hint=(0.5, 0.3),
                              font_size=25,
                              pos_hint={"center_x": 0.5,
                                        "center_y": 0.47})
        self.add_widget(self.text)

        self.thank = Label(text="Thank you for your Feedback!",
                           font_size=30,
                           size_hint=(0.1, 0.05),
                           pos_hint={"center_x": 0.5,
                                     "center_y": 0.17})

        self.add_widget(Button(text="Enter",
                               font_size=25,
                               size_hint=(0.1, 0.05),
                               pos_hint={"center_x": 0.5,
                                         "center_y": 0.27},
                               on_press=self.getFeed))
        self.onpressenterbtn = False

    def gotoCustomerfeed(self, instance):
        self.manager.current = "Customer"
        self.text.text = ""
        self.remove_widget(self.thank)

    def getFeed(self, instance):
        if self.onpressenterbtn == True:
            self.remove_widget(self.thank)
        custfeed = self.text.text
        self.add_widget(self.thank)
        print("Customer Feedback", custfeed)
        self.onpressenterbtn = True
        c.execute("insert into feedback values('%s','%s')" %(CUSTOMER_ID,custfeed))
        self.text.text = ""

## PAGE_LIST:

class Application(App):
    def build(self):
        sm = ScreenManagement(transition=SlideTransition())
        sm.add_widget(LoginPage(name='Login'))
        sm.add_widget(Create_Acc(name='Create-Acc'))
        sm.add_widget(Forgot_Password(name='FP'))
        sm.add_widget(Update_Pass(name='UP'))
        sm.add_widget(Forgot_Cust_ID(name='FC'))
        sm.add_widget(MainPage(name='Admin Page'))
        sm.add_widget(AddItems(name='Add-Items'))
        sm.add_widget(UpdateItems(name='Update-Items'))
        sm.add_widget(DeleteItems(name='Delete-Items'))
        sm.add_widget(ReviewFeedback(name='Review-Feedback'))
        sm.add_widget(Customer(name="Customer"))
        sm.add_widget(Order(name="Order"))
        sm.add_widget(UpdCan(name="Updcan"))
        sm.add_widget(UpdOrd(name="UpdOrd"))
        sm.add_widget(Checkord(name="Checkord"))
        sm.add_widget(Feedback(name="Feedback"))
        return sm

if __name__ == "__main__":
    Application().run()

c.close()
db.close() 
