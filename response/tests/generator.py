from cgitb import reset
import numpy as np
import random
import string

upper = string.ascii_uppercase

def fill(s):
    for line in s.split("\n"):
        res = ""
        for c in line:
            if c != ".": res += c.upper()
            else: res += random.choice(upper)
        print(res)

if __name__ == "__main__":
    s = """r........S
o.......o.
p......l..
a.....a...
v....r....
r...w.....
e..i......
t.n.......
ad........
w.sunspot."""
    fill(s)