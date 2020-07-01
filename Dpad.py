import tkinter as tk
from tkinter import ttk
from tkinter import font,colorchooser,filedialog,messagebox
import os

main_app = tk.Tk()
main_app.geometry("800x600")
main_app.title("Dpad text editor")

#main menu
main_menu= tk.Menu()
#File icons
new_icon=tk.PhotoImage(file='colors/new.png')
open_icon=tk.PhotoImage(file='colors/open.png')
save_icon=tk.PhotoImage(file='colors/save.png')
save_as_icon=tk.PhotoImage(file='colors/save_as.png')
exit_icon=tk.PhotoImage(file='colors/exit.png')


cut_icon=tk.PhotoImage(file='colors/cut.png')
copy_icon=tk.PhotoImage(file='colors/copy.png')
paste_icon=tk.PhotoImage(file='colors/paste.png')
find_icon=tk.PhotoImage(file='colors/find.png')
clear_all=tk.PhotoImage(file='colors/clear_all.png')

toolbar_icon=tk.PhotoImage(file='colors/tool_bar.png')
status_icon=tk.PhotoImage(file='colors/status_bar.png')


''' File menu description '''
File =tk.Menu(main_menu, tearoff=False)



''' Edit menu discription '''
Edit =tk.Menu(main_menu, tearoff=False)



''' View menu discription '''
View =tk.Menu(main_menu, tearoff=False)

'''color theme discription'''
Colortheme =tk.Menu(main_menu, tearoff=False)
default_col=tk.PhotoImage(file='colors/white.png')
black=tk.PhotoImage(file='colors/black.png')
Bluegray=tk.PhotoImage(file='colors/Bluegray.png')
lightgreen=tk.PhotoImage(file='colors/light_green.png')
lightsilicon=tk.PhotoImage(file='colors/light_silicon.png')
wood=tk.PhotoImage(file='colors/wood.png')


theme_choice = tk.StringVar() # variable to choose theme

color_icons=(default_col,black,Bluegray,lightgreen,lightsilicon,wood)
color_dict={
    'default_col':('#030303','#ffffff'),
    'black':('#ffffff','#030303'),
    'Bluegray':('#ffffff','#7694bf'),
    'lightgreen':('#030303','#92eeb8'),
    'lightsiliocn':('#ffffff','#828684'),
    'wood':('#030303','#f6bd72')
}

def change_theme():
    chosen_theme=theme_choice.get()
    color_tuple=color_dict.get(chosen_theme)
    fg_color,bg_color=color_tuple[0],color_tuple[1]
    text_editor.config(background=bg_color,fg=fg_color)
count=0
for i in color_dict:
    Colortheme.add_radiobutton(label=i,image=color_icons[count],variable=theme_choice,compound=tk.LEFT,command=change_theme)
    count +=1


#casecade
main_menu.add_cascade(label='File',menu=File)
main_menu.add_cascade(label='Edit',menu=Edit)
main_menu.add_cascade(label='View',menu=View)
main_menu.add_cascade(label='Colrotheme',menu=Colortheme)
#End menu

#Toolbar
tool_bar=ttk.Label(main_app)
tool_bar.pack(side=tk.TOP,fill=tk.X)

font_tuple=tk.font.families()
font_family=tk.StringVar()
font_box=ttk.Combobox(tool_bar,width=30,textvariable=font_family,state='readonly')
font_box['values']=font_tuple
font_box.grid(row=0,column=1,padx=5)

#size box
size_var=tk.IntVar()
font_size=ttk.Combobox(tool_bar,width=7,textvariable=size_var,state='readonly')
font_size['values']=tuple(range(8,81))
font_size.current(4)
font_size.grid(row=0,column=2,padx=5)
#bold Button
bold_icon=tk.PhotoImage(file='colors/Bold.png')
bold_btn=ttk.Button(tool_bar,image=bold_icon)
bold_btn.grid(row=0,column=3,padx=5)

#italic Button
italic_icon=tk.PhotoImage(file='colors/Italic.png')
italic_btn=ttk.Button(tool_bar,image=italic_icon)
italic_btn.grid(row=0,column=4,padx=5)

#underline
under_icon=tk.PhotoImage(file='colors/underline.png')
under_btn=ttk.Button(tool_bar,image=under_icon)
under_btn.grid(row=0,column=5,padx=5)

#font color button
font_color=tk.PhotoImage(file='colors/colorbtn.png')
font_color_btn=ttk.Button(tool_bar,image=font_color)
font_color_btn.grid(row=0,column=6,padx=5)

#align

aleft=tk.PhotoImage(file='colors/left.png')
aleft_icon=ttk.Button(tool_bar,image=aleft)
aleft_icon.grid(row=0,column=7,padx=5)

acenter=tk.PhotoImage(file='colors/center.png')
acenter_icon=ttk.Button(tool_bar,image=acenter)
acenter_icon.grid(row=0,column=8,padx=5)

aright=tk.PhotoImage(file='colors/right.png')
aright_icon=ttk.Button(tool_bar,image=aright)
aright_icon.grid(row=0,column=9,padx=5)
# end menu

#text editor

text_editor=tk.Text(main_app)
text_editor.config(wrap='word',relief=tk.FLAT)
scroll_bar=tk.Scrollbar(main_app)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

# end texteditor

#status bar

status_bar=ttk.Label(main_app,text='status bar')
status_bar.pack(side=tk.BOTTOM)
# end status

# functionality of texteditior

current_font='Arial'
current_font_size=12

def change_font(main_app):
    global current_font
    current_font=font_family.get()
    text_editor.config(font=(current_font,current_font_size))
font_box.bind('<<ComboboxSelected>>',change_font)

def change_font_size(main_app):
    global current_font_size
    current_font_size=size_var.get()
    text_editor.configure(font=(current_font,current_font_size))

font_size.bind("<<ComboboxSelected>>",change_font_size)

##############Button functionalities###########################
#Bold
def changebold():
    text_property = tk.font.Font(font=text_editor['font'])
    print(text_property)
    if text_property.actual()['weight']=='normal':
        text_editor.config(font=(current_font,current_font_size,'bold'))
    if text_property.actual()['weight']=='bold':
        text_editor.config(font=(current_font,current_font_size,'normal'))

bold_btn.configure(command=changebold)

#italic Button

def changeitalic():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant']=='roman':
        text_editor.config(font=(current_font, current_font_size, 'italic'))
    if text_property.actual()['slant']=='italic':
        text_editor.config(font=(current_font, current_font_size, 'roman'))

italic_btn.configure(command=changeitalic)

def change_underline():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline'] == 0:
        text_editor.config(font=(current_font, current_font_size, 'underline'))
    if text_property.actual()['underline'] == 1:
        text_editor.config(font=(current_font, current_font_size, 'normal'))
under_btn.configure(command=change_underline)

#Font's color funcitonality
def change_color():
    color_var= tk.colorchooser.askcolor()
    text_editor.configure()
    print(color_var)

font_color_btn.configure(command=change_color)

# align funciton
def align_left():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('lfet',justify=tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'left')
aleft_icon.configure(command=align_left)


def align_center():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('center',justify=tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'center')
acenter_icon.configure(command=align_center)

def align_right():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('right',justify=tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'right')
aright_icon.configure(command=align_right)

# status bar funciton
text_changed=False
def Change(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed=True
        words=len(text_editor.get(1.0,'end-1c').split())
        characters=len(text_editor.get(1.0,'end-1c'))
        status_bar.config(text=f'characters:{characters} words:{words}')
    text_editor.edit_modified(False)

text_editor.bind("<<Modified>>",Change)





text_property = tk.font.Font(font=text_editor['font']).actual()

text_editor.config(font=('Arial',12))

url=""
## file menu New functionallity
def new_file(event=None):
    global url
    url=""
    text_editor.delete(1.0,tk.END)

# file menu open functionality
def open_file(event=None):
    global url
    url=filedialog.askopenfilename(initialdir=os.getcwd(),title='select file',filetypes=(('Text File',".txt"),('All files',"*_*")))
    try:
        with open(url,'r') as fr:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,fr.read())
    except FileNotFoundError:
        return
    except:
        return
    main_app.title(os.path.basename(url))

# save file method
def save_file(event=None):
    global url
    try:
        if url:
            content=str(text_editor.get(1.0,tk.END))
            with open(url,'w',encoding='utf-8') as wf:
                wf.write(content)
        else:
            url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File',".txt"),('All files',".*_*")))
            content2=text_editor.get(1.0,tk.END)
            url.write(content2)
            url.close()
    except:
        return

# save as functionality
def save_as_file(event=None):
    global url
    try:
        content=str(text_editor.get(1.0,tk.END))
        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File', ".txt"),('All files', ".*_*")))
        url.write(content)
        url.close()
    except:
        return

def exit_fun(event=None):
    global url,text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel('Warning','Do you want to save file')
            if mbox is True:
                if url:
                    content =text_editor.get(1.0,tk.END)
                    with open(url,'w',encoding='utf-8') as fw:
                        fw.write(content)
                        main_app.destroy()
                else:
                    content2=text_editor.get(1.0,tk.END)
                    url = filedialog.asksaveasfile(mode='w', defaultextension='.txt',filetypes=(('Text File', ".txt"), ('All files', ".*_*")))
                    url.write(content2)
                    url.close()
                    main_app.destroy()
            elif mbox is False:
                main_app.destroy()
        else:
            main_app.destroy()
    except:
        return

'''Edit menu functionality'''
#Edit Menu
# Find function
def find_func(event=None):
    def find():
        word=find_input.get()
        text_editor.tag_remove('match','1.0',tk.END)
        matches=0
        if word:
            start_pos='1.0'
            while True:
                start_pos=text_editor.search(word,start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match',start_pos,end_pos)
                matches+=1
                start_pos=end_pos
                text_editor.tag_config('match',foreground='red',background='yellow')


    def Replace():
        word=find_input.get()
        replace_text=replace_input.get()
        content=text_editor.get(1.0,tk.END)
        new_content=content.replace(word,replace_text)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,new_content)

    find_dialog=tk.Toplevel()
    find_dialog.geometry('400x200')
    find_dialog.title('Find/Replace')
    find_dialog.resizable(0,0)
    # find frame
    find_frame=ttk.LabelFrame(find_dialog,text='Find/replace')
    find_frame.pack(pady=20)
    #level
    text_find_label=ttk.Label(find_frame,text='Find :')
    text_replace_label=ttk.Label(find_frame,text='Replace :')
    #entry
    find_input=ttk.Entry(find_frame, width=30)
    replace_input=ttk.Entry(find_frame,width=30)

    #button
    find_button=ttk.Button(find_frame,text="Find",command=find)
    replace_button=ttk.Button(find_frame,text='Replace',command=Replace)

    #label grid
    text_find_label.grid(row=0,column=0,pady=4,padx=4)
    text_replace_label.grid(row=1,column=0,pady=4,padx=4)
    find_input.grid(row=0,column=1,pady=4,padx=4)
    replace_input.grid(row=1,column=1,pady=4,padx=4)
    find_button.grid(row=2,column=0,pady=4,padx=4)
    replace_button.grid(row=2,column=1,pady=4,padx=4)
    find_dialog.mainloop()

# main menu function

File.add_command(label='New',image=new_icon,compound=tk.LEFT,accelerator='ctrl+N',command=new_file)
File.add_command(label='Open',image=open_icon,compound=tk.LEFT,accelerator='ctrl+O',command=open_file)
File.add_command(label='Save',image=save_icon,compound=tk.LEFT,accelerator='ctrl+S',command=save_file)
File.add_command(label='Save as',image=save_as_icon,compound=tk.LEFT,accelerator='ctrl+shift+s',command=save_as_file)
File.add_command(label='Exit',image=exit_icon,compound=tk.LEFT,accelerator='ctrl+q',command=exit_fun)

Edit.add_command(label='Cut',image=cut_icon,compound=tk.LEFT,accelerator='ctrl+x',command=lambda :text_editor.event_generate("<Control x>"))
Edit.add_command(label='Copy',image=copy_icon,compound=tk.LEFT,accelerator='ctrl+c',command=lambda :text_editor.event_generate("<Control c>"))
Edit.add_command(label='Paste',image=paste_icon,compound=tk.LEFT,accelerator='ctrl+v',command=lambda :text_editor.event_generate("<Control v>"))
Edit.add_command(label='Find',image=find_icon,compound=tk.LEFT,accelerator='ctrl+f',command=find_func)
Edit.add_command(label='Clear all',image=clear_all,compound=tk.LEFT,accelerator='ctrl+shift+x',command=lambda :text_editor.delete(1.0,tk.END))

#view functionality
show_status_bar =tk.BooleanVar()
show_status_bar.set(True)
show_tool_bar =tk.BooleanVar()
show_tool_bar.set(True)

def show_toolbar():
    global show_tool_bar
    if show_tool_bar:
        tool_bar.pack_forget()
        show_tool_bar=False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP,fill=tk.X)
        text_editor.pack(fill=tk.BOTH,expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_tool_bar=True

def hide_statusbar():
    global  show_status_bar
    if show_status_bar:
        status_bar.pack_forget()
        show_status_bar=False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_status_bar=True

View.add_checkbutton(label='Tool bar',image=toolbar_icon,onvalue=True ,offvalue=0,variable = show_toolbar,compound=tk.LEFT,command=show_toolbar)
View.add_checkbutton(label='Status bar',image=status_icon,onvalue=1, offvalue=False  ,compound=tk.LEFT,command=hide_statusbar)



# end menu funciton

main_app.config(menu=main_menu)
# shortcut key
main_app.bind("<Control-n>",new_file)
main_app.bind("<Control-o>",open_file)
main_app.bind("<Control-s>",save_file)
main_app.bind("<Control-Shift-s>",save_as_file)
main_app.bind("<Control-q>",exit_fun)
main_app.bind("<Control-f>",find_func)

main_app.mainloop()