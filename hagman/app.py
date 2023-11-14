import os
import time


def main():
    print(os.name)
    print('test clear ')
    time.sleep(3)
    os.system('clear' if os.name == 'posix' else 'cls')
    

if __name__ == 'main':
    main()   