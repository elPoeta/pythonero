import os
import time
from hagman import Hagman

def main():
    print(os.name)
    print('test clear ')
    time.sleep(1)
    os.system('clear' if os.name == 'posix' else 'cls')
    hagman = Hagman()
    hagman.print_pics(0)
    

if __name__ == '__main__':
    main()   