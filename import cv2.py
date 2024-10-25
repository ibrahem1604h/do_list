import tkinter as tk
app=tk.Tk()
app.title("DO LIST")
app.geometry("600x300")


fram=tk.Frame(app)
fram.pack(pady=10)

rame=tk.Frame(app)
rame.pack(pady=20)

def add_mission(Event=None):
  input_list=text.get()
  if input_list:
      list.insert(0,input_list)
      text.delete(0,tk.END)

def delet_mission(Event):
  item=list.curselection()
  if item:
      list.delete(item)

labl=tk.Label(rame,text="your missions:",font=("Arial",14), )
lable=tk.Label(fram,text="ENTER YOUR MISSION",font=("Arial",14),)      
text=tk.Entry(fram,width=50)
text.bind("<Return>",add_mission)     
list=tk.Listbox(rame,width=90,)
boutom=tk.Button(fram,text="enter",command=add_mission)

lable.pack(pady=1,padx=1)
text.pack(side=tk.LEFT,padx=5)  
boutom.pack(side=tk.LEFT,padx=5) 
labl.pack(anchor="w", padx=1)  
list.pack(pady=1,padx=2)
list.bind("<Double-1>",delet_mission)


app.configure()
fram.configure()
rame.configure()

app.mainloop()