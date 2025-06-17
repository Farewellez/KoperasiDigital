import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def clearTerminal():
    if os.name == 'nt':
        os.system('cls')  
    else:
        os.system('clear')