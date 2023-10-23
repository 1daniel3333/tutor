#!/c/Users/Dell/AppData/Local/Microsoft/WindowsApps/python
import sys
import subprocess
def main():
    data=[]
    for line in sys.stdin:
        data.append(line.strip())
    if len(data)==0:
        raise ValueError("No Input Data.")
    data = list(filter(None, data))
    print('Hello')
    print(data)

if __name__=='__main__':
    main()