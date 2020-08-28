from tkinter import *
#importing tkinter for the qui
import os
#importing os so as to access the file, as we have to read and write usernames and passwords
def delete1():
  screen1.destroy()
  #screen1.deiconify()
  #screen1.quit()

def delete2():
  screen3.destroy()

def delete3():
  screen4.destroy()

def delete4():
  screen5.destroy()
  
def login_sucess():
  global screen3
  screen3 = Toplevel(screen)
  screen3.title("Success")
  screen3.geometry("150x100")
  import mainloop
  mainloop.my_func()
  ##os.system('python mainloop.py')
  Label(screen3, text = "Login Sucess").pack()
  Button(screen3, text = "OK", command =delete2).pack()

def password_not_recognised():
  global screen4
  screen4 = Toplevel(screen)
  screen4.title("Success")
  screen4.geometry("150x100")
  Label(screen4, text = "Password Error").pack()
  Button(screen4, text = "OK", command =delete3).pack()

def user_not_found():
  global screen5
  screen5 = Toplevel(screen)
  screen5.title("Success")
  screen5.geometry("150x100")
  Label(screen5, text = "User Not Found").pack()
  Button(screen5, text = "OK", command =delete4).pack()

  
def register_user():
  print("working")
  
  username_info = username.get()
  password_info = password.get()

  file=open(username_info, "w")  
  file.write(username_info+"\n")
  #to add a new line in the file 
  file.write(password_info)
  file.close()

  username_entry.delete(0, END)
  password_entry.delete(0, END)
  Label(screen1, text = "", bg = "#A55D35").pack()
  Label(screen1, text = "Registration Sucess", fg = "green" ,font = ("calibri", 11)).pack()
  Label(screen1, text = "", bg = "#A55D35").pack()
  Button(screen1, text = "Okay, take to login page ", command=lambda:[login(),delete1()]).pack()
  #command lamda fn is used to execute multiple fns at the same time :)
def login_verify():
  
  username1 = username_verify.get()
  password1 = password_verify.get()
  username_entry1.delete(0, END)
  password_entry1.delete(0, END)

  list_of_files = os.listdir()
  if username1 in list_of_files:
    file1 = open(username1, "r")
    verify = file1.read().splitlines()
    if password1 == verify[1]:
        login_sucess()
    else:
        password_not_recognised()

  else:
        user_not_found()
  
##get password *

def register():
  global screen1

  screen1 = Toplevel(screen)
  screen1.geometry("600x600")
  screen1['bg'] = '#A55D35'

  Label(screen1, text = "", bg = "#A55D35").pack()
  #making the variables global so that we can access them in resigter verfiy function
  #photo1 = PhotoImage(file = r"logo_new2.png")
  #labelphoto1 = Label(screen1, image = photo1)
  #labelphoto1.pack()

  global username
  global password
  global username_entry
  global password_entry
  username = StringVar()
  password = StringVar()

  Label(screen1, text = "Please enter details below").pack()
  Label(screen1, text = "", bg = "#A55D35").pack()
  Label(screen1, text = "Username * ").pack()
 
  username_entry = Entry(screen1, textvariable = username)
  username_entry.pack()
  Label(screen1, text = "", bg = "#A55D35").pack()
  Label(screen1, text = "Password * ").pack()
  password_entry =  Entry(screen1, textvariable = password)
  password_entry.pack()
  Label(screen1, text = "", bg = "#A55D35").pack()
  Button(screen1, text = "Register", width = 10, height = 1, command = register_user).pack()

def login():
  global screen2
  print('login  Working ')
  screen2 = Toplevel(screen)
  #photo2 = PhotoImage(file = r"logo_new1")
  #labelphoto = Label(screen2, image = photo2)
  #labelphoto.pack()
  screen2.title("Login")
  screen2['bg'] = '#A55D35'
  screen2.geometry("600x600")
  Label(screen2, text = "", bg = "#A55D35").pack()
  Label(screen2, text = "Please enter details below to login").pack()

  Label(screen2,text = "", bg = "#A55D35").pack()

  global username_verify
  global password_verify
  
  username_verify = StringVar()
  password_verify = StringVar()
  # user and pass are used as string var, since we are not using input fn, doing the same is conisdered a good progtamming practice 
  global username_entry1
  global password_entry1
  
  Label(screen2, text = "Username * ").pack()
  username_entry1 = Entry(screen2, textvariable = username_verify)
  username_entry1.pack()
  Label(screen2, text = "", bg = "#A55D35").pack()
  Label(screen2, text = "Password * ").pack()
  password_entry1 = Entry(screen2, textvariable = password_verify)
  password_entry1.pack()
  Label(screen2, text = "", bg = "#A55D35").pack()
  Button(screen2, text = "Login", width = 10, height = 1, command = login_verify).pack()
  Label(screen2, text = "* Means Required ",fg = "red" ,font = ("calibri", 11)).pack()
  Label(screen2, text = "", bg = "#A55D35").pack()

def main_screen():
  global screen
  print('main_screen Working')
  screen = Tk()
  photo = PhotoImage(file = r"logo_new1.png")
  labelphoto = Label(screen, image = photo)
  labelphoto.pack()
  screen.geometry("600x600")
  screen.title("Login page")
  screen['bg'] = '#A55D35'
  Label(text = "Conics with Matpltlib", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
  #photofg = PhotoImage(file = r"futured_img.png")
  #labelphoto2 = Label(screen, image = photofg)
  #labelphoto2.pack()
  Label(text = "", bg = "#A55D35").pack()
  Button(text = "Login", height = "2", width = "30", command = login).pack()
  Label(text = "", bg = "#A55D35").pack()
  Button(text = "Register",height = "2", width = "30", command = register).pack()

  screen.mainloop()

main_screen()
  
