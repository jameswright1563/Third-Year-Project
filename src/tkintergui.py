from tkinter import *
import pyautogui
from Matrix_solve_module import cofactor  # imported module for calculations

#test.cofactor([[-1,0,1],[2,-1,2],[-1,2,1]])

root = Tk()
root.title("Inverse of Matrix")
root.geometry("550x550")
root.configure(bg = "aquamarine")


def openweb():
	Label(bg = "aquamarine").grid(row=6,columnspan= 5)
	Label(root,text = "Solution :",font=("Helvetica", 15),bg = "aquamarine").grid(row=7,columnspan= 5)
	lst = [[int(a.get("1.0",END)),int(b.get("1.0",END)),int(c.get("1.0",END))],[int(d.get("1.0",END)),int(e.get("1.0",END)),int(f.get("1.0",END))],[int(g.get("1.0",END)),int(h.get("1.0",END)),int(i.get("1.0",END))]]
	det,answer = cofactor(lst)
	s = "1/"
	s+=str(det)
	Label(bg = "aquamarine").grid()
	Label(root,text = "[",font=("Helvetica", 20),bg = "aquamarine").grid(row=9,column= 1)
	Label(root,text = answer[0],font=("Helvetica", 20),bg = "aquamarine").grid(row=9,column= 2)
	Label(root,text = answer[4],font=("Helvetica", 20),bg = "aquamarine").grid(row=9,column= 3)
	Label(root,text = answer[2],font=("Helvetica", 20),bg = "aquamarine").grid(row=9,column= 4)
	Label(root,text = "]",font=("Helvetica", 20),bg = "aquamarine").grid(row=9,column= 5)
	Label(root,text = s,font=("Helvetica", 20),bg = "aquamarine").grid(row=10,column= 0)
	Label(root,text = "[",font=("Helvetica", 20),bg = "aquamarine").grid(row=10,column= 1)
	Label(root,text = answer[3],font=("Helvetica", 20),bg = "aquamarine").grid(row=10,column= 2)
	Label(root,text = answer[1],font=("Helvetica", 20),bg = "aquamarine").grid(row=10,column= 3)
	Label(root,text = answer[5],font=("Helvetica", 20),bg = "aquamarine").grid(row=10,column= 4)
	Label(root,text = "]",font=("Helvetica", 20),bg = "aquamarine").grid(row=10,column= 5)
	Label(root,text = "[",font=("Helvetica", 20),bg = "aquamarine").grid(row=11,column= 1)
	Label(root,text = answer[6],font=("Helvetica", 20),bg = "aquamarine").grid(row=11,column= 2)
	Label(root,text = answer[7],font=("Helvetica", 20),bg = "aquamarine").grid(row=11,column= 3)
	Label(root,text = answer[8],font=("Helvetica", 20),bg = "aquamarine").grid(row=11,column= 4)
	Label(root,text = "]",font=("Helvetica", 20),bg = "aquamarine").grid(row=11,column= 5)


Label(text= "Type the numbers in specific boxes:",bg= "aquamarine",font=("Helvetica", 20)).grid(row=0,columnspan = 9)
a = Text(root, height=1, width=2,bd = 3,font=("Helvetica", 30))
a.grid(row = 1,column = 0)
b = Text(root, height=1, width=2,bd = 3,font=("Helvetica", 30))
b.grid(row = 1,column = 1)
c = Text(root, height=1, width=2,bd = 3,font=("Helvetica", 30))
c.grid(row = 1,column = 2) 

Label(bg= "aquamarine").grid()
d = Text(root, height=1, width=2,bd = 3,font=("Helvetica", 30))
d.grid(row = 3,column = 0)
e = Text(root, height=1, width=2,bd = 3,font=("Helvetica", 30))
e.grid(row = 3,column = 1)
f = Text(root, height=1, width=2,bd = 3,font=("Helvetica", 30))
f.grid(row = 3,column = 2)

solve =  Button(text = "Solve" , command = openweb)
solve.grid(row = 3,column = 5)

Label(bg= "aquamarine").grid()
g = Text(root, height=1, width=2,bd = 3,font=("Helvetica", 30))
g.grid(row = 5,column = 0)
h = Text(root, height=1, width=2,bd = 3,font=("Helvetica", 30))
h.grid(row = 5,column = 1)
i = Text(root, height=1, width=2,bd = 3,font=("Helvetica", 30))
i.grid(row = 5,column = 2)

root.mainloop()