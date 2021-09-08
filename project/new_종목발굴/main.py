from model import stock
from method import *

li = initialize()
for idx, elem in enumerate(li):
    print(f"{idx+1}. ", end="")
    elem.print()