import tkinter as tk
from tkinter import ttk
from RaadHetNummer import RaadHetNummer  # Importeer de klasse RaadHetNummer
from Galgje import Galgje  # Importeer de klasse Galgje



# Functie voor het starttabblad met 'PlayNation'
class StartScherm(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.label = tk.Label(self, text="PlayNation", font=("Arial", 48, "bold"), fg="blue")
        self.label.pack(pady=100)

        self.instructies = tk.Label(self, text="Welkom bij PlayNation! Kies een spel hierboven.", font=("Arial", 24))
        self.instructies.pack(pady=20)


# Hoofdprogramma met drie tabbladen (voor de startpagina en de twee spellen)
class GameApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PlayNation")
        self.geometry("600x500")

        # Zet de achtergrondkleur
        self.configure(bg='lightblue')

        tab_control = ttk.Notebook(self)

        start_tab = StartScherm(tab_control)
        tab1 = RaadHetNummer(tab_control)
        tab2 = Galgje(tab_control)

        tab_control.add(start_tab, text="PlayNation")
        tab_control.add(tab1, text="Raad het Nummer")
        tab_control.add(tab2, text="Galgje")

        tab_control.pack(expand=1, fill="both")


# Start de applicatie
if __name__ == "__main__":
    app = GameApp()
    app.mainloop()
