

from tkinter import *
from tkinter.font import BOLD
import random
import time
    
#Global variables

player1_char = 'x'
player2_char = 'o'
char = player1_char
buttons = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
        ]
clean_buttons = []

#Functions

def create_buttons_PvP():
    
    '''Created buttons and label of the playing field at the meeting
       PvP game on the main screen'''

    global player1_char, game_label

    
    for row in range(3):
        for column in range(3):                                  
            
            buttons[row][column] = Button(window, text= '',
                                          font=('consolas',40),                                          
                                          width= 3,
                                          height= 1,
                                          padx= 28,
                                          pady= 20,
                                          command= lambda row= row, column= column: next_turn(row, column))
            buttons[row][column].grid(row= row, column= column)         

    
    game_label = Label(window, text= char + ' turn',
                       bg= '#f0f0f0',
                       fg= 'black',
                       font= ('Bauhaus 93',30),
                       pady= 30,
                       bd= 3,
                       relief= 'groove',
                       background= '#f0f0f0')
    game_label.place(anchor= 'center',
                     x= 225,
                     y= 495,
                     height= 110,
                     width= 450)  
    game_label.config(text= f'put {char}')

    
    btn_restart = Button(window, image= img1,
                         height= 110,
                         width= 110,
                         relief= 'flat',
                         command= create_buttons_PvP)    
    btn_restart.place(anchor= 'center',
                     x= 395,
                     y= 495,
                     height= 100,
                     width= 100)
    
    
    btn_back = Button(window, image= img2,
                         height= 110,
                         width= 110,
                         relief= 'flat',
                         command= run)    
    btn_back.place(anchor= 'center',
                     x= 50,
                     y= 495,
                     height= 100,
                     width= 100)  



def create_buttons_VSPC():

    '''Creates buttons and playfield label when clicked
       VSPC Game on Home Screen'''

    global player1_char, game_label

    char = player1_char

    for row in range(3):
        for column in range(3):                                  
            
            buttons[row][column] = Button(window, text= '',
                                          font=('consolas',40),                                          
                                          width= 3,
                                          height= 1,
                                          padx= 28,
                                          pady= 20,
                                          command= lambda row= row, column= column: next_PCturn(row, column))
            buttons[row][column].grid(row= row, column= column)         

    
    game_label = Label(window, text= char + ' turn',
                       bg= '#f0f0f0',
                       fg= 'black',
                       font= ('Bauhaus 93',30),
                       pady= 30,
                       bd= 3,
                       relief= 'groove',
                       background= '#f0f0f0')
    game_label.place(anchor= 'center',
                     x= 225,
                     y= 495,
                     height= 110,
                     width= 450)  
    game_label.config(text= f'put {char}')

    
    btn_restart = Button(window, image= img1,
                         height= 110,
                         width= 110,
                         relief= 'flat',
                         command= create_buttons_VSPC)    
    btn_restart.place(anchor= 'center',
                     x= 395,
                     y= 495,
                     height= 100,
                     width= 100)
    
    
    btn_back = Button(window, image= img2,
                         height= 110,
                         width= 110,
                         relief= 'flat',
                         command= run)    
    btn_back.place(anchor= 'center',
                     x= 50,
                     y= 495,
                     height= 100,
                     width= 100) 



def PCturn(row, column):

    '''Computer stroke calculation in VSPC mode'''
    
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != 'x' and buttons[row][column]['text'] != 'o':
                clean_buttons.append(buttons[row][column])

    random.choice(clean_buttons).config(text= 'o')
    clean_buttons.clear()



def next_PCturn(row, column):

    '''Accepting the player's turn and proceeding to the PC's turn'''

    global char
    
    
    if buttons[row][column]['text'] == '':                   

        if check_winner() != True and empty_squares() != 'DROW!':
            char = player1_char
            change_text(row, column, char)
            
            
            if check_winner() != True and empty_squares() != 'DROW!':
                time.sleep(0.2)
                char = player2_char
                PCturn(row,column)
                
                
                if check_winner() == True:
                    find_winner() 
                
                elif empty_squares() == 'DROW!':
                    game_label.config(text= " DROW!")
                    for button in buttons:
                        for n in range(3):
                            button[n].config(state="disabled")         
            
            elif check_winner() == True:
                find_winner()            
            
            elif empty_squares() == 'DROW!':
                game_label.config(text= " DROW!")
                for button in buttons:
                    for n in range(3):
                        button[n].config(state="disabled")
        
        
        elif check_winner() == True:
            find_winner()            
        
        elif empty_squares() == 'DROW!':
            game_label.config(text= " DROW!")
            for button in buttons:
                for n in range(3):
                    button[n].config(state="disabled")                


def find_winner():

    '''Operations required to be performed after finding the winner'''
 
    game_label.config(text= char.capitalize() + " WINNER!")
    
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(state="disabled")


def change_text(row, column, char):

    '''Change button text after player's turn'''

    buttons[row][column]['text'] = char
                      

def next_turn(row, column):

    '''Accepting player1's turn and proceeding to player2's turn'''
    
    global char
    
    
    if buttons[row][column]['text'] == '':
        
        
        if char == player1_char:        

            
            if check_winner() != True and empty_squares() != 'DROW!':
                change_text(row, column, char)
            
                if check_winner() != True and empty_squares() != 'DROW!':
                    char = player2_char
                    game_label.config(text= char + " turn")            
                
                elif check_winner() == True:
                    find_winner()            
                
                elif empty_squares() == 'DROW!':
                    game_label.config(text= " DROW!")
                    for button in buttons:
                        for n in range(3):
                            button[n].config(state="disabled")
                
        
        else:
        
            if check_winner() != True and empty_squares() != 'DROW!':
                change_text(row, column, char)
        
                
                if check_winner() != True and empty_squares() != 'DROW!':
                    char = player1_char
                    game_label.config(text= char + " turn")
                
                elif check_winner() == True:
                    find_winner()            
                
                elif empty_squares() == 'DROW!':
                    game_label.config(text= " DROW!")
                    for button in buttons:
                        for n in range(3):
                            button[n].config(state="disabled")


def empty_squares():

    '''Calculation of empty buttons for PC move'''
    
    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        for button in buttons:
            for n in range(3):
                button[n].config(state="disabled")
        
        return 'DROW!'

    else:
        return True


def check_winner():

    '''Checking the winning conditions'''

    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="#ababab")
            buttons[row][1].config(bg="#ababab")
            buttons[row][2].config(bg="#ababab")
            return True


    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="#ababab")
            buttons[1][column].config(bg="#ababab")
            buttons[2][column].config(bg="#ababab")
            return True

    
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="#ababab")
        buttons[1][1].config(bg="#ababab")
        buttons[2][2].config(bg="#ababab")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="#ababab")
        buttons[1][1].config(bg="#ababab")
        buttons[2][0].config(bg="#ababab")
        return True

    else:
        return False


# Window initialization
window = Tk()
window.title('Tic-Tac-Toe')
window.geometry("450x550+200+100")
icon = PhotoImage(file='icon.png')
window.iconphoto(False, icon)
window.resizable(False, False)


img1 = PhotoImage(file = r"G:/Python/gui_project/restart.png")
img2 = PhotoImage(file = r"G:/Python/gui_project/backbtn.png")

def run():

    '''Main game launch function'''
    
    # Adding a background
    canvas = Canvas(window, height=550, width=450)
    img = PhotoImage(file = 'G:/Python/gui_project/backg.png') 
    image = canvas.create_image(0, 0, anchor='nw',image=img)
    canvas.place(anchor= 'center', x= 225, y= 275)


    # Labels
    label_1 = Label(window, text= 'Tic Tac Toe',    
                       bg= '#f0f0f0',
                       fg= 'black',
                       font= ('Bauhaus 93',30),
                       pady= 30)
    label_2 = Label(window, text= 'by kudras3r',
                       bg= '#f0f0f0',
                       fg= '#2c3e50',
                       font= ('Calibri',14))

    label_1.place(anchor= 'center',x= 225, y= 50)
    label_2.place(anchor= 'center', x= 225, y= 75, height= 20)


    # Buttons
    button_play_PvP = Button(window, text= 'PvP Game',
                                activebackground= '#e8e8e8',
                                relief= 'groove',
                                font= ('Calibri',20,BOLD),
                                width= 15,
                                height= 2,
                                background= '#f0f0f0',
                                command= create_buttons_PvP)
    button_play_VSPC = Button(window, text= 'VS PC Game',
                                activebackground= '#e8e8e8',
                                relief= 'groove',	
                                font= ('Calibri',20,BOLD),
                                width= 15,
                                height= 2,
                                background= '#f0f0f0',
                                command= create_buttons_VSPC) 
    button_QUIT = Button(window, text= 'QUIT',
                                activebackground= '#e8e8e8',
                                relief= 'groove',	
                                font= ('Calibri',20,BOLD),
                                width= 15,
                                height= 2,
                                background= '#f0f0f0',
                                command= quit)
    
    button_play_PvP.place(anchor= 'center',x= 225, y= 150)
    button_play_VSPC.place(anchor= 'center',x= 225, y= 250)
    button_QUIT.place(anchor= 'center',x= 225, y= 350)



    window.mainloop()

run()