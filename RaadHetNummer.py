import tkinter as tk
import random

# Functie voor het spel 'Raad het Nummer'
class RaadHetNummer(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pogingen = 8
        self.willekeurig_getal = random.randint(1, 100)

        self.label = tk.Label(self, text="Raad het nummer tussen 1 en 100:", font=("Arial", 16))
        self.label.pack(pady=10)

        self.entry = tk.Entry(self, font=("Arial", 14))
        self.entry.pack(pady=10)

        self.result_label = tk.Label(self, text="", font=("Arial", 14), fg="blue")
        self.result_label.pack(pady=10)

        self.button = tk.Button(self, text="Raad", command=self.raad_nummer, font=("Arial", 12), bg="lightblue")
        self.button.pack(pady=10)

        self.pogingen_label = tk.Label(self, text=f"Pogingen over: {self.pogingen}", font=("Arial", 14))
        self.pogingen_label.pack(pady=10)

    def raad_nummer(self):
        try:
            gok = int(self.entry.get())
            if gok == self.willekeurig_getal:
                self.result_label.config(text=f"Goed gedaan! Het nummer was {self.willekeurig_getal}.", fg="green")
                self.button.config(state='disabled')
            elif gok < self.willekeurig_getal:
                self.result_label.config(text="Het nummer is hoger.", fg="blue")
            else:
                self.result_label.config(text="Het nummer is lager.", fg="blue")

            self.pogingen -= 1
            if self.pogingen == 0:
                self.result_label.config(text=f"Game over! Het juiste nummer was {self.willekeurig_getal}.", fg="red")
                self.button.config(state='disabled')
            self.pogingen_label.config(text=f"Pogingen over: {self.pogingen}")
        except ValueError:
            self.result_label.config(text="Vul een geldig nummer in.", fg="red")
