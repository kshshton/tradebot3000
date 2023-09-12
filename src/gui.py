import customtkinter as ctk


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


class GUI:
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x350")
        self.position = {"pady": 12, "padx": 10}

        self.name = ctk.StringVar(self.root)
        self.condition = ctk.StringVar(self.root)
        self.is_stattrak = ctk.BooleanVar(self.root)

        self.create_widgets()

    def create_widgets(self) -> None:
        frame = ctk.CTkFrame(master=self.root)
        frame.pack(
            pady=20,
            padx=60,
            fill="both",
            expand=True,
        )

        label = ctk.CTkLabel(
            master=frame,
            text="tradebot3000",
        )
        label.pack(**self.position)

        entry = ctk.CTkEntry(
            master=frame,
            textvariable=self.name,
        )
        entry.insert(0, "Item name")
        entry.pack(**self.position)

        combobox = ctk.CTkComboBox(
            master=frame,
            values=[
                "Factory new",
                "Minimal wear",
                "Field tested",
                "Well worn",
                "Battle scared",
            ],
            variable=self.condition,
        )
        combobox.pack(**self.position)
        combobox.set("Condition")

        checkbox = ctk.CTkCheckBox(
            master=frame,
            text="Stattrak",
            variable=self.is_stattrak,
        )
        checkbox.pack(**self.position)

        button = ctk.CTkButton(
            master=frame,
            text="Search",
            command=self.close,
        )
        button.pack(**self.position)

        self.root.bind("<Return>", self.close)
        self.root.mainloop()

    def close(self, *args: any) -> None:
        self.root.destroy()

    def __str__(self) -> str:
        name = "" if self.name.get() == "Item name" else self.name.get()
        condition = "" if self.condition.get() == "Condition" else self.condition.get()
        is_stattrak = "Stattrak" if self.is_stattrak.get() else ""
        return f"{name} {condition} {is_stattrak}".strip()
