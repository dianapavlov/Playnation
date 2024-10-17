import tkinter as tk
from tkinter import ttk
import random
import os
# Functie voor het spel 'Galgje' met moeilijkheidsgraden
class Galgje(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pogingen = 8
        self.geraden_letters = []
        self.woord = ""

        self.label = tk.Label(self, text="Welkom bij Galgje!", font=("Arial", 16))
        self.label.pack(pady=10)

        # Moeilijkheidsgraad kiezen
        self.moeilijkheidsgraad_label = tk.Label(self, text="Kies de moeilijkheidsgraad:", font=("Arial", 14))
        self.moeilijkheidsgraad_label.pack(pady=5)

        self.moeilijkheidsgraad = ttk.Combobox(self, values=["makkelijk", "gemiddeld", "moeilijk"], font=("Arial", 12))
        self.moeilijkheidsgraad.pack(pady=10)

        self.start_button = tk.Button(self, text="Start Spel", command=self.start_galgje, font=("Arial", 12),
                                      bg="lightgreen")
        self.start_button.pack(pady=10)

        self.woord_label = tk.Label(self, text="_", font=("Arial", 18))
        self.woord_label.pack(pady=10)

        self.result_label = tk.Label(self, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

        self.entry = tk.Entry(self, font=("Arial", 14))
        self.entry.pack(pady=10)

        self.button = tk.Button(self, text="Raad de letter", command=self.raad_letter, font=("Arial", 12),
                                bg="lightblue", state="disabled")
        self.button.pack(pady=10)

        self.pogingen_label = tk.Label(self, text=f"Pogingen over: {self.pogingen}", font=("Arial", 14))
        self.pogingen_label.pack(pady=10)

    # Functie om het spel te starten
    def start_galgje(self):
        moeilijkheidsgraad = self.moeilijkheidsgraad.get()

        # Gebruik os.path.join om ervoor te zorgen dat het bestand in dezelfde directory staat
        base_path = os.path.dirname(os.path.abspath(__file__))  # Krijg de directory van het script

        # Bestand kiezen op basis van moeilijkheidsgraad
        if moeilijkheidsgraad == "makkelijk":
            bestandsnaam = os.path.join(base_path, "galgjemakkelijk.txt")
        elif moeilijkheidsgraad == "gemiddeld":
            bestandsnaam = os.path.join(base_path, "galgjegemiddeld.txt")
        elif moeilijkheidsgraad == "moeilijk":
            bestandsnaam = os.path.join(base_path, "galgjemoeilijk.txt")
        else:
            self.result_label.config(text="Kies een geldige moeilijkheidsgraad", fg="red")
            return

        if os.path.exists(bestandsnaam):
            with open(bestandsnaam) as file:
                woorden = file.readlines()
            self.woord = random.choice(woorden).strip()
            self.geraden_letters = []
            self.pogingen = 8
            self.update_woord_label()
            self.button.config(state="normal")
            self.start_button.config(state="disabled")
            self.result_label.config(text="")
            self.pogingen_label.config(text=f"Pogingen over: {self.pogingen}")
        else:
            self.result_label.config(text=f"Kan bestand {bestandsnaam} niet vinden.", fg="red")

    # Update het label van het woord met geraden letters
    def update_woord_label(self):
        beeldscherm_woord = [letter if letter in self.geraden_letters else "_" for letter in self.woord]
        self.woord_label.config(text=" ".join(beeldscherm_woord))

    # Functie voor het raden van een letter
    def raad_letter(self):
        letter = self.entry.get().lower()
        if len(letter) == 1 and letter.isalpha():
            if letter in self.geraden_letters:
                self.result_label.config(text=f"Je hebt de letter '{letter}' al geraden.", fg="orange")
            elif letter in self.woord:
                self.geraden_letters.append(letter)
                self.result_label.config(text=f"Goed bezig! De letter '{letter}' zit in het woord.", fg="green")
            else:
                self.pogingen -= 1
                self.result_label.config(text=f"Jammer! De letter '{letter}' zit niet in het woord.", fg="red")

            self.pogingen_label.config(text=f"Pogingen over: {self.pogingen}")
            self.update_woord_label()
            self.entry.delete(0, tk.END)

            if "_" not in self.woord_label.cget("text"):
                self.result_label.config(text=f"Gefeliciteerd! Je hebt het woord '{self.woord}' geraden.", fg="green")
                self.button.config(state="disabled")

            if self.pogingen == 0:
                self.result_label.config(text=f"Game over! Het woord was '{self.woord}'.", fg="red")
                self.button.config(state="disabled")
        else:
            self.result_label.config(text="Voer een geldige letter in.", fg="red")
