from tkinter import *
from population import *

selected_countries = []

def append_country(event):
    cs = event.widget.curselection()
    i = cs[0]
    selected_countries.append(countries_index[i])

def delete_country(event):
    cs = event.widget.curselection()
    i = cs[0]
    selected_countries.remove(countries_index[i])

def open_window():
    new_window = Toplevel(root)
    new_window.title('Choose Countries')
    new_window.geometry('300x200')

    listb = Listbox(new_window)
    for country in countries_index:
        listb.insert(END, country)
    listb.bind('<Double-1>', append_country)
    listb.bind('<Key>', delete_country)
    listb.pack(side = 'top')

    done_btn = Button(new_window, text = 'Done', bd = '5', command = lambda : plot_countries(selected_countries))
    done_btn.pack(side = 'top')

root = Tk()

root.title('Population Tools')
root.geometry('200x200')

regions_btn = Button(root, text = 'Plot Regions', bd = '5', command = lambda : plot_regions())
top_btn = Button(root, text = 'Plot Top Countries', bd = '5', command = lambda : plot_top_countries())
slct_btn = Button(root, text = 'Plot Selected Countries', bd = '5', command = lambda : open_window())

regions_btn.pack(side = 'top')
top_btn.pack(side = 'top')
slct_btn.pack(side = 'top')

root.mainloop()
