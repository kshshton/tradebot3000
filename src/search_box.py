import customtkinter


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")
position = {"pady": 12, "padx": 10}

def search():
    pass

frame = customtkinter.CTkFrame(master=root)
frame.pack(
    pady=20, 
    padx=60, 
    fill="both", 
    expand=True,
)

label = customtkinter.CTkLabel(
    master=frame, 
    text="tradebot3000",
)
label.pack(**position)

entry1 = customtkinter.CTkEntry(
    master=frame, 
    placeholder_text="Item name", 
    show="*",
)
entry1.pack(**position)

combobox = customtkinter.CTkComboBox(
    master=frame, 
    values=[
        "Factory new", 
        "Minimal wear", 
        "Field tested", 
        "Well worn", 
        "Battle scared",
    ],
)
combobox.pack(**position)
combobox.set("Condition")

checkbox = customtkinter.CTkCheckBox(
    master=frame, 
    text="Stattrak",
)
checkbox.pack(**position)

button = customtkinter.CTkButton(
    master=frame, 
    text="Search", 
    command=search,
)
button.pack(**position)

root.mainloop()
