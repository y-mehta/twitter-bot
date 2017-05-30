# Author : Yash Mehta <https://github.com/y-mehta/twitter-bot>
# Import the modules needed to run the script.
import sys, os

# Main definition - constants
menu_actions  = {}  

# =======================
#     MENUS FUNCTIONS
# =======================

# Main menu
def main_menu():
    os.system('clear')
    
    print "Welcome to Twitter-bot,\nDeveloped by Yash Mehta <https://github.com/y-mehta/twitter-bot>"
    print "What would you like to do ?"
    print "1. Tweet From a File"
    print "2. Follow users using a hashtag"
    print "3. Retweet using a hashtag"
    print "4. Like Tweets"
    print "\n0. Quit"
    choice = raw_input(" >>  ")
    exec_menu(choice)

    return

# Execute menu
def exec_menu(choice):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print "Invalid selection, please try again.\n"
            menu_actions['main_menu']()
    return

# Menu 1
def menu1():
    print "Welcome,Tweet From a File!\n"
    os.system('python tweet-from-file.py')
    print "9. Back"
    print "0. Quit"
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return


# Menu 2
def menu2():
    print "Welcome,Follow users using a hashtag!\n"
    os.system('python follow-script.py')
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

# Menu 3
def menu3():
    print "Welcome, Retweet using a hashtag!\n"
    os.system('python retweet-script.py')
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

# Menu 4
def menu4():
    print "Welcome,Like Tweets!\n"
    os.system('python like-script.py')
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return


# Back to main menu
def back():
    menu_actions['main_menu']()

# Exit program
def exit():
    sys.exit()

# =======================
#    MENUS DEFINITIONS
# =======================

# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '1': menu1,
    '2': menu2,
    '3': menu3,
    '4': menu4,
    '9': back,
    '0': exit,
}

# =======================
#      MAIN PROGRAM
# =======================

# Main Program
if __name__ == "__main__":
    # Launch main menu
    main_menu()
