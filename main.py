from tkinter import *

tk = Tk()
tk.title("Text Disappearing App")
tk.config(width=600, height=200, padx=100, pady=100)

count = 0
text = ""


def count_up(count):
    global top_label
    global text
    print(text)
    print(count)
    current_text = text_field.get()
    if len(text) != 0 and text == current_text:
        print(text_field.get())
        if count == 0:
            text_field.delete(0, END)
    else:
        text = current_text
        count = 5
    top_label["text"] = f"If you stop typing for {count} seconds, text will be disappear!!!"
    tk.after(1000, count_up, count - 1)


top_label = Label(text="If you stop typing for 5 seconds, text will be disappear!!!")
top_label.pack()

text_field = Entry()
text_field.pack()


count_up(count)
tk.mainloop()
