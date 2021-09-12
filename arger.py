import argparse
import sys
def cal(a):
    if a.o=="add":
        return a.x + a.y
if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument("--x",type=float,default=1.0,help="enter the first number. If you encounter any problem please contact me.")
    parser.add_argument("--y",type=float,default=2.0,help="enter the second number. If you encounter any problem please contact me.")
    parser.add_argument("--o",type=str,default=3.0,help="enter the operation. If you encounter any problem please conta\ct me.")
    a=parser.parse_args()
    sys.stdout.write(str(cal(a)))