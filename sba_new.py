import os
import json
import tkinter as tk
from tkinter import ttk
from functools import partial
os.chdir(os.path.dirname(os.path.abspath(__file__)))
root=tk.Tk()
datatype=["Name","Address","Group","Age"]
catch=False
list0=[] 
find=[""]
abandon=[""]
page=0
findpage=0
nextpage=False
backpage=False
button_list=[]
l11=[]
list2=[]
list4=[["",0,"","",False,False,False],["","","","",False,False,False],["","","","",False,True,True],[125,0,"","",True,False,False]]
list5=[[],[],["a","b","c","d"],[]]
if os.path.exists("save.json"):
    if os.path.getsize("save.json")>0:
        with open("save.json","r") as f:
            loaded_save=json.load(f)
            datatype=loaded_save[0]
            list0=loaded_save[1]
            list4=loaded_save[2]
            list5=loaded_save[3]
def option(x,y):
    global l11get,b19,l11,l11c,b19c
    if y==0:
        l11get.pop(x)
        for i in l11c:
            i.destroy()
        for i in b19c:
            i.destroy()
    elif y==1:
        l11get.append(e8.get())
        e8.delete(0,tk.END)
    for i in range (0,len(l11get)):
        l11=tk.Label(window2)
        l11.grid(column=2+(i//5)*2,row=i%5)
        l11.config(text=l11get[i])
        l11c.append(l11)
        b19=tk.Button(window2,text="X",command=partial(option,i,0))
        b19.grid(column=3+(i//5)*2,row=i%5)
        b19c.append(b19)
def ckadd(x):
    global l11get,l11c,b19c
    list4[x][5]=True
    list5[x]=l11get
    if var1.get()=="1":
        list4[x][6]=True
    else:
        list4[x][6]=False
    l11c=[]
    b19c=[]
    l11get=[]
def ckcombo(x):
    global var1,l11,l11get,e8,window2,b19,l11c,b19c
    window2=tk.Toplevel()
    window2.geometry("340x135")
    if x<len(datatype):
        title=datatype[x]
    else:
        title=list2[x-len(datatype)]
    window2.title(f"{title}")
    b16=tk.Button(window2,text="change to entry",command=lambda:[window2.destroy(),check(x,0)])
    b16.grid(column=0,row=0)
    var1=tk.StringVar()
    ckb=tk.Checkbutton(window2,text="only select",variable=var1,onvalue=True,offvalue=False)
    ckb.grid(column=0,row=1)
    if list4[x][6]==False:
        ckb.deselect()
    else:
        ckb.select()
    b17=tk.Button(window2,text=" + ",command=lambda:[option(x,1)])
    b17.grid(column=1,row=2)
    e8=tk.Entry(window2)
    e8.grid(column=0,row=2)
    l11c=[]
    b19c=[]
    l11get=list5[x].copy()
    option(2,2)
    b18=tk.Button(window2,text="comfirm",command=lambda:[ckadd(x),window2.destroy()])
    b18.grid(column=0,row=3)
    b18=tk.Button(window2,text="leave",command=lambda:window2.destroy())
    b18.grid(column=0,row=4)
def word():
    if var2.get()=="1":
        l8.config(text="number little than")
        l9.config(text="number bigger than")
    else:
        l8.config(text="character less than")
        l9.config(text="character more than")
def check(x,y):
    global e4,e5,e6,e7,var2,title,l8,l9,l12,l13,window1
    if list4[x][5]==True and y==1:
        ckcombo(x)
    else:
        window1=tk.Toplevel()
        window1.geometry("340x165")
        if x<len(datatype):
            title=datatype[x]
        else:
            title=list2[x-len(datatype)]
        window1.title(f"{title}")
        b14=tk.Button(window1,text="change to combobox",command=lambda:[window1.destroy(),ckcombo(x)])
        b14.grid(column=0,row=0)
        var2=tk.StringVar()
        var2=tk.StringVar()
        ckb2=tk.Checkbutton(window1, text="only number",variable=var2, onvalue=True, offvalue=False,command=word)
        ckb2.grid(column=1,row=1)
        if list4[x][4]==True:
            ckb2.select()
        else:
            ckb2.deselect()
        l8=tk.Label(window1)
        l8.grid(column=0,row=3)
        l9=tk.Label(window1)
        l9.grid(column=0,row=4)
        e4=tk.Entry(window1)
        e4.grid(column=1,row=3)
        e4.insert(0,list4[x][0])
        e5=tk.Entry(window1)
        e5.grid(column=1,row=4)
        e5.insert(0,list4[x][1])
        l12=tk.Label(window1)
        l12.grid(column=2,row=3)
        l13=tk.Label(window1)
        l13.grid(column=2,row=4)
        l0=tk.Label(window1,text="must include:")
        l0.grid(column=0,row=5)
        e6=tk.Entry(window1)
        e6.grid(column=1,row=5)
        e6.insert(0,list4[x][2])
        l11=tk.Label(window1,text="must not include:")
        l11.grid(column=0,row=6)
        e7=tk.Entry(window1)
        e7.grid(column=1,row=6)
        e7.insert(0,list4[x][3])
        b15=tk.Button(window1,text="enter",command=lambda:[chas(x)])
        b15.grid(column=2,row=7)
        b16=tk.Button(window1,text="exit",command=lambda:window1.destroy())
        b16.grid(column=0,row=7)
        word()
def chas(x):
    global var2
    list4[x][5]=False
    try:
        if e4.get()!="":
            list4[x][0]=int(e4.get())
        else:
            list4[x][0]=""
        try:
            if e5.get()!="":
                list4[x][1]=int(e5.get())
            else:
                list4[x][1]=""
            list4[x][2]=e6.get()
            list4[x][3]=e7.get()
            YN=var2.get()=="1"
            list4[x][4]=YN
            print(list4,YN,x)
            window1.destroy()
        except ValueError:
            l13.config(text="must be int")
    except ValueError:
        l12.config(text="must be int")
def setting(x):
    global order_list,win0,dx,datatype,de,win0,l10
    win0=tk.Tk()
    dow=tk.Frame(win0)
    dow.pack()
    l4=tk.Label(dow,text="subject order:")
    l4.grid(column=1,row=0)
    order_list=[]
    de=[]
    No=["Del"]
    for i in range (0,len(datatype)+x):
        No.append(i+1)
    for i in range (0,len(datatype)+x):
        de.append(ttk.Combobox(dow,values=(No),state="readonly"))
        de[i].grid(column=1,row=(i+1))
        de[i].set(i+1)
        checking=partial(check,i,1)
        b13=tk.Button(dow,text="🔨",command=checking)
        b13.grid(column=2,row=(i+1))
    for i in range (0,len(datatype)):
        l6=tk.Label(dow,text=datatype[i])
        l6.grid(column=0,row=(i+1))
    for i in range (0,x):
        l9=tk.Label(dow,text=list2[i])
        l9.grid(column=0,row=(len(datatype)+i+1))
    height=26*len(de)+95
    win0.geometry(f"300x{height}")
    win0.title("setting")
    b7=tk.Button(dow,text=" + ",command=lambda:[addsub(x),win0.destroy()])
    b7.grid(column=0,row=(len(datatype)+x+1))
    l10=tk.Label(dow)
    l10.grid(column=1,row=(len(datatype)+x+2))
    b9=tk.Button(win0,text="cancel",command=lambda:[clear(),win0.destroy()])
    b9.pack(side="left")
    b0=tk.Button(win0,text=" finish",command=lambda:[change(),clear(),look(0)])
    b0.pack(side="right")
def change():
    global datatype,list0,de,order_list,win0,l10,list4,list5
    list3=[]
    con=True
    for k in range (0,len(de)):
        if de[k].get()=="Del" or de[k].get() not in list3:
            list3.append(de[k].get())
            print(list3)
    if con:
        print(de)
        if len(list3)==len(de):
            for i in range (0,len(list2)):
                datatype.append(list2[i])
            for i in range (0,len(datatype)):
                order_list.append(de[i])
            datacopy=datatype.copy()
            list0copy=list0.copy()
            list4copy=list4.copy()
            list5copy=list5.copy()
            list4=[]
            list5=[]
            datatype=[]
            list0=[]
            for i in range (0,len(list0copy)):
                list0.append([""]*len(datacopy))
                while len(list0copy[i])<len(list0[i]):
                    list0copy[i].append("")
            for i in range (0,len(datacopy)):
                for r in range (0,len(datacopy)):
                    if order_list[r].get()==str(i+1):
                        datatype.append(datacopy[r])
                        list4.append(list4copy[r])
                        list5.append(list5copy[r])
                        for u in range (0,len(list0copy)):
                            list0[u][i]=list0copy[u][r]
            win0.destroy()
        else:
            l10.config(text="Please enter the different number!")
        print(list4)
        print(list5)
def clear():
    global list2
    list2=[]
def addsub(x):
    global e2
    win=tk.Tk()
    win.geometry("300x80")
    win.title("information add")
    l7=tk.Label(win,text="New subject name")
    l7.grid(column=0,row=0)
    e2=tk.Entry(win)
    e2.grid(column=1,row=0)
    b8=tk.Button(win,text="Done",command=lambda:[gets(),setting(x+1),win.destroy()])
    b8.grid(column=2,row=1)
    b10=tk.Button(win,text="Back",command=lambda:[setting(x),win.destroy()])
    b10.grid(column=0,row=1)
def gets():
    list2.append(e2.get())
    list4.append(["","","","","","",""])
    list5.append([[]])
def looks(t):
    global findpage
    findpage=findpage+t
def finding(w):
    global e0,find,abandon,list1,l2,l3,button_list,page,np,bp,findpage,nextpage,backpage,u,catch
    if nextpage==True:
        np.destroy()
        nextpage=False
    if backpage==True:
        bp.destroy()
        backpage=False
    u=0
    if w!=2:
        findpage=0
    for btn in button_list:
        btn.destroy()
    button_list=[]
    if e0.get()=="!ERROR":
        find=[""]
        l2.destroy()
        l2=tk.Label(frame)
        l2.grid(column=0,row=2)
        abandon=[""]
        l3.destroy()
        l3=tk.Label(frame)
        l3.grid(column=2,row=2)
        catch=True
    else:
        catch=False
    if w==0 and catch==False:
        if find[0]=="":
            find[0]=e0.get()
        else:
            if e0.get() not in find:
                find.append(e0.get())
            else:
                find.remove(e0.get())
                if len(find)==0:
                    find=[""]
        if find!=[""]:
            l2.config(text=("+",find))
        else:
            l2.destroy()
            l2=tk.Label(frame)
            l2.grid(column=0,row=2)
    if w==1 and catch==False:
        if abandon[0]=="":
            abandon[0]=e0.get()
        else:
            if e0.get() not in abandon:
                abandon.append(e0.get())
            else:
                abandon.remove(e0.get())
                if len(abandon)==0:
                    abandon=[""]
                    if abandon[0]=="":
                        look(0)
        if abandon!=[""]:
            l3.config(text=("-",abandon))
        else:
            l3.destroy()
            l3=tk.Label(frame)
            l3.grid(column=2,row=2)
    if find[0]=="" and abandon[0]=="":
        look(0)
        return
    if w==2 or e0.get()!="":
        for x in range (0,len(list0)):
            build=1
            count=0
            for i in range (0,len(list0[x])):
                if catch:
                    if list4[i][4]==True:
                        try:
                            if list4[i][0]=="" or int(list0[x][i])<int(list4[i][0]):
                                if list4[i][1]=="" or int(list0[x][i])>int(list4[i][1]):
                                    if list4[i][2]=="" or (list0[x][i]!="" and list4[i][2] in list0[x][i]):
                                        if list4[i][3]=="" or (list0[x][i]!="" and list4[i][3] not in list0[x][i]):
                                            count+=1
                        except ValueError:
                            pass
                    elif list4[i][0]=="" or len(list0[x][i])<int(list4[i][0]):
                        if list4[i][1]=="" or len(list0[x][i])>int(list4[i][1]):
                            if list4[i][2]=="" or (list0[x][i]!="" and list4[i][2] in list0[x][i]):
                                if list4[i][3]=="" or (list0[x][i]!="" and list4[i][3] not in list0[x][i]):
                                    count+=1
                    if i==len(list0[x])-1 and count==i:
                        build=0
                else:
                    for v in range (0,len(find)):
                        count=0
                        for j in range (0,len(list0[x])):
                            if (find[v] in list0[x][j] or find[0]=="") and build!=2:
                                count=1
                            for b in range (0,len(abandon)):
                                if abandon[b] in list0[x][j] and abandon[0]!="":
                                    build=0
                        if count==0 and j==len(list0[x])-1:
                            build=0
            if (catch and w==0) or catch==False:
                if build==1:
                    u=u+1
                    if u>findpage*10 and u<=(findpage+1)*10:
                        d=tk.Button(root,text=list0[x][0],command=partial(see,x))
                        d.pack(fill='x', ipady=2)
                        button_list.append(d)
            else:
                if build==0:
                    u=u+1
                    if u>findpage*10 and u<=(findpage+1)*10:
                        d=tk.Button(root,text=list0[x][0],command=partial(see,x))
                        d.pack(fill='x', ipady=2)
                        button_list.append(d)
        if 10*(findpage+1)<u:
            np=tk.Button(root,text=" ⭢ ",command=lambda:[looks(1),finding(2)])
            np.pack(side="right")
            nextpage=True
        if findpage>0:
            bp=tk.Button(root,text=" ⭠ ",command=lambda:[looks(-1),finding(2)])
            bp.pack(side="left")
            backpage=True
    else:
        find=[""]
        l2.destroy()
        l2=tk.Label(frame)
        l2.grid(column=0,row=2)
        abandon=[""]
        l3.destroy()
        l3=tk.Label(frame)
        l3.grid(column=2,row=2)
        look(0)
        findpage=0
    printpage()
def order(x):
    if x==0:
        list0.sort(reverse=True)
    else:
        list0.sort()
def look(c):
    global button_list,np,bp,page,nextpage,backpage
    for btn in button_list:
        btn.destroy()
    button_list=[]
    if nextpage==True:
        np.destroy()
        nextpage=False
    if backpage==True:
        bp.destroy()
        backpage=False
    for v in range (len(list0)-1,-1,-1):
        blank=True
        for i in range (0,len(list0[v])):
            if list0[v][i]!="":
                blank=False
        if blank==True:
            del list0[v]
    page=page+c
    if len(list0)/10>(page+1):
        f=10*(page+1)
    else:
        f=len(list0)
    for v in range (10*page,f):
        seen=partial(see,v)
        d=tk.Button(root,text=list0[v][0],command=seen)
        d.pack(fill='x', ipady=2)
        button_list.append(d)
    if (page+1)<(len(list0))/10:
        np=tk.Button(root,text=" ⭢ ",command=lambda:look(1))
        np.pack(side="right")
        nextpage=True
    if page>0:
        bp=tk.Button(root,text=" ⭠ ",command=lambda:look(-1))
        bp.pack(side="left")
        backpage=True
    printpage()
def see(z):
    global e3
    see=tk.Tk()
    height=20*len(datatype)+30
    see.geometry(f"255x{height}")
    see.title("detail")
    e3=[]
    for i in range (0,len(datatype)):
        imf=tk.Label(see,text=(datatype[i],":"))
        imf.grid(column=0,row=i)
        e3.append(tk.Entry(see))
        e3[i].grid(column=1,row=i)
        e3[i].insert(0,list0[z][i])
    if find==[""] and abandon==[""] and catch==False:
        b11=tk.Button(see,text="delete",command=lambda:[revamp(z,0),look(0),see.destroy()])
        b12=tk.Button(see,text="change",command=lambda:[revamp(z,1),look(0),see.destroy()])
    else:
        b11=tk.Button(see,text="delete",command=lambda:[revamp(z,0),look(0),finding(2),see.destroy()])
        b12=tk.Button(see,text="change",command=lambda:[revamp(z,1),look(0),finding(2),see.destroy()])
    b11.grid(column=0,row=len(datatype))
    b12.grid(column=2,row=len(datatype))
def revamp(z,x):
    global list0
    for i in range (0,len(datatype)):
        if x==0:
            list0[z][i]=""
        else:
            list0[z][i]=e3[i].get()
def adding():
    global e1,l11,window,cho
    window=tk.Toplevel()
    wins=tk.Frame(window)
    wins.pack()
    height=20*len(datatype)+30
    window.geometry(f"500x{height}")
    window.title("adding")
    e1=[]
    l11=[]
    cho=[]
    for i in range (0,len(datatype)):
        l1=tk.Label(wins, text=(datatype[i],":"))
        l1.grid(column=0,row=i)
        if list4[i][5]==True:
            if list4[i][6]==True:
                cho.append(ttk.Combobox(wins,width=27,values=(list5[i]),state="readonly"))
                cho[i-len(e1)].grid(column=1,row=i)
            else:
                cho.append(ttk.Combobox(wins,width=27,values=(list5[i])))
                cho[i-len(e1)].grid(column=1,row=i)
        else:
            e1.append(tk.Entry(wins,width=30))
            e1[i-len(cho)].grid(column=1,row=i)
        l11.append(tk.Label(wins))
        l11[i].grid(column=2,row=i)
    b6=tk.Button(window,text="Ok",command=lambda:[get()])
    b6.pack(anchor="ne")
    printpage()
def get():
    global e1,l11,cho
    list1=[]
    p=0
    q=0
    for i in range (0,len(datatype)):
        if list4[i][5]==True:
            list1.append(cho[i-p].get())
            q+=1
        else:
            list1.append(e1[i-q].get())
            p+=1
    for i in range (0,len(datatype)):
        l11[i].config(text="")
    for i in range (0,len(datatype)):
        if list4[i][4]==True:
            try:
                if list4[i][0]!="" and int(list1[i])>=int(list4[i][0]):
                    l11[i].config(text=f"The number should be little than {list4[i][0]}")
                    break
                if list4[i][1]!="" and int(list1[i])<=int(list4[i][1]):
                    l11[i].config(text=f"The number should be bigger than {list4[i][1]}")
                    break
            except ValueError:
                if list1[i]!="":
                    l11[i].config(text="You should fill integer in the blank")
                    break
        elif list4[i][0]!="" and len(list1[i])>=int(list4[i][0]):
            l11[i].config(text=f"The character should be less than {list4[i][0]}")
            break
        elif list4[i][1]!="" and len(list1[i])<=int(list4[i][1]):
            l11[i].config(text=f"The character should be more than {list4[i][1]}")
            break
        if list4[i][2]!="" and list4[i][2] not in list1[i] and list1[i]!="":
            l11[i].config(text=f"The input should include {list4[i][2]}")
            break
        if list4[i][3]!="" and list4[i][3] in list1[i] and list4[i][3]!="":
            print("a",list4[len(list0)][3],"b",list1[i])
            l11[i].config(text=f"The input should not include {list4[i][3]}")
            break
        if i==len(datatype)-1:
            list0.append(list1)
            printpage()
            look(0)
            cho=[]
            e1=[]
            l11=[]
            window.destroy()
def printpage():
    global catch
    if find[0]=="" and abandon[0]=="" and catch==False:
        if len(list0)%10==0:
            ab.set("page:"+str(page+1)+"/"+str(len(list0)//10))
        else:
            ab.set("page:"+str(page+1)+"/"+str(1+(len(list0))//10))
    else:
        try:
            if u%10==0:
                ab.set("page:"+str(findpage+1)+"/"+str(u//10))
            else:
                ab.set("page:"+str(findpage+1)+"/"+str(1+(u//10)))
        except NameError:
            if len(list0)%10==0:
                ab.set("page:"+str(page+1)+"/"+str(len(list0)//10))
            else:
                ab.set("page:"+str(page+1)+"/"+str(1+(len(list0))//10))
def close():
    save=[datatype,list0,list4,list5]
    with open("save.json","w") as f:
        json.dump(save,f)
    root.destroy()
def goto():
    try:
        if find[0]=="" and abandon[0]=="" and catch==False:
            if e0.get()=="":
                look(-page)
            elif len(list0)%10==0:
                if (int(e0.get())-page-1)<=(len(list0)//10):
                    look(int(e0.get())-page-1)
            else:
                if (int(e0.get())-page-1)<=(1+len(list0)//10):
                    look(int(e0.get())-page-1)
        else:
            if e0.get()=="":
                looks(-findpage)
                finding(2)
            elif len(list0)%10==0:
                if (int(e0.get())-findpage)<=(len(list0)//10):
                    looks(int(e0.get())-findpage-1)
                    finding(2)
            else:
                if (int(e0.get())-findpage)<=(1+(len(list0))//10):
                    looks(int(e0.get())-findpage-1)
                    finding(2)
    except ValueError:
        pass
frame=tk.Frame(root)
frame.pack()
root.title("Address list")
root.geometry("300x430")
root.protocol("WM_DELETE_WINDOW",close)
l=tk.Label(frame, text="Search")
l.grid(column=0,row=0)
b=tk.Button(frame,text=" 🔍 ",command=lambda:finding(0))
b.grid(column=2,row=0)
b1=tk.Button(frame,text=" 🗑 ",command=lambda:finding(1))
b1.grid(column=3,row=0)
e0=tk.Entry(frame)
e0.grid(column=1,row=0)
b2=tk.Button(root,text="⚙",command=lambda:setting(0))
b2.pack(anchor="ne")
b3=tk.Button(frame, text="  ⭡  ",command=lambda:[order(0),finding(2),look(-page)])
b3.grid(column=0,row=1)
b4=tk.Button(frame, text="📞add",command=lambda:adding())
b4.grid(column=1,row=1)
b5=tk.Button(frame, text="  ⭣  ",command=lambda:[order(1),finding(2),look(-page)])
b5.grid(column=2,row=1)
b20=tk.Button(frame,text="go",command=lambda:goto())
b20.grid(column=3,row=1)
l2=tk.Label(frame)
l2.grid(column=0,row=2)
ab=tk.StringVar()
printpage()
l5=tk.Label(frame,textvariable=ab)
l5.grid(column=1,row=2)
l3=tk.Label(frame)
l3.grid(column=2,row=2)
look(0)
root.mainlo
