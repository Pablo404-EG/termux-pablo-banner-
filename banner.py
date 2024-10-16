import os
import time
import sys

def print_banner():
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
    print(art)
    print("[GitHub : https://github.com/Pablo404-EG\n")

if __name__ == "__main__":
    
    username = input("Enter your name, hacker: ")
    
    os.system("clear")
    
    print_banner()
    
    time.sleep(3)

    os.system("clear")
   
    print("[INFO] You can now continue using Termux normally.\n")
    
