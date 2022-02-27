import sys
import select

def process():
    print("e")
    
while True:
    input = select.select([sys.stdin], [], [], 0.1)[0]
    if input:
        value = sys.stdin.readline().rstrip()
        
        if value == "q":
            sys.exit(0)
        else:
            print(value)
    else:
        process()