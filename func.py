from tkinter import *

win= Tk()
win.title('原膜重量计算器')
win.geometry('260x300+1200+230')
win.config(bg='skyblue')

sa = {12:45.8,15:37.2,18:27.6,20:24.61,25:21.14}
def add():
    # sa= [num3_ent]
    m2= int(num1_ent.get())* int(num2_ent.get())/sa[int(num3_ent.get())]*0.001
    return kg_lab.config(text=m2)

def clear():
    cl= kg_lab.config(text=0)
    return cl
    

num1_lab= Label(text='宽度（mm）',bg='skyblue')
num1_lab.pack(side=TOP)

num1_ent= Entry()
num1_ent.pack()

num2_lab= Label(text='长度（ m）',bg='skyblue')
num2_lab.pack(side=TOP)

num2_ent= Entry()
num2_ent.pack()

num3_lab= Label(text='厚度（um）',bg='skyblue')
num3_lab.pack(side=TOP)

num3_ent= Entry()
num3_ent.pack()

kg_lab1= Label(text='重量（KG）',width=20,bg='skyblue')
kg_lab1.pack()

kg_lab= Label(text='00.0'+'kg',width=20,bg='pink')
kg_lab.pack(side=TOP)


num1_btn= Button(text='计算',width=20)
num1_btn.config(command=add)
num1_btn.pack(side=BOTTOM)
num1_btn= Button(text='清零',width=20)
num1_btn.config(command=clear)
num1_btn.pack(side=BOTTOM)



win.mainloop()