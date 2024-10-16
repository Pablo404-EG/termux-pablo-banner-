import os
import time
import sys

def print_art(username):
    art = f'''
      ██████╗  █████╗ ██████╗ ██╗      ██████╗ 
      ██╔══██╗██╔══██╗██╔══██╗██║     ██╔═══██╗
      ██████╔╝███████║██████╔╝██║     ██║   ██║
      ██╔═══╝ ██╔══██║██╔═══╝ ██║     ██║   ██║
      ██║     ██║  ██║██║     ███████╗╚██████╔╝
      ╚═╝     ╚═╝  ╚═╝╚═╝     ╚══════╝ ╚═════╝ 
                                            
    ░▒▓█  WELCOME TO THE SYSTEM  █▓▒░
    ░▒▓█      {username}     █▓▒░
    -----------------------------------
    ░▒▓█  ACCESS LEVEL: HACKER █▓▒░
    -----------------------------------
     '''
    for line in art.split("\n"):
        sys.stdout.write(line + "\n")
        sys.stdout.flush()
        time.sleep(0.05)

def keep_terminal_active():
    print("\n[INFO] Terminal active. You can continue using it with the banner displayed.\n")
    while True:
        try:
            cmd = input("$ ")
            os.system(cmd)
        except KeyboardInterrupt:
            print("\nExiting... Goodbye.")
            break

if __name__ == "__main__":
  
    username = input("Enter your name, hacker: ")
  
    os.system('clear')
  
    print_art(username)
  
    keep_terminal_active()
  
