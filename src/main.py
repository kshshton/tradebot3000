import customtkinter as ctk

from table import Table
from gui import GUI


def main():
    # table = Table()
    # table.save_to_csv(file_name="data")
    gui = GUI(ctk.CTk())
    print(gui)


if __name__ == "__main__":
    main()
