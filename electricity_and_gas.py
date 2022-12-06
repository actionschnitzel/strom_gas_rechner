#!/usr/bin/python3


import tkinter as tk
from tkinter import *
from tkinter import ttk
from datetime import date


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title("Strompreis Calculator")
        #self.geometry("300x50")

        def berechnen():
            self.ergebnis_label.config(text="")
            # Berechnung
            d0 = date(int(self.yearchoosen.get()), int(self.monthchoosen.get()), int(self.daychoosen.get()))
            d1 = date(int(self.new_yearchoosen.get()), int(self.new_monthchoosen.get()), int(self.new_daychoosen.get()))#2022, 12, 6)#
            delta = d1 - d0
            print(f"Zeitraum: {delta.days} Tage")

            #Stromwerte
            strom_alt = int(self.strom_alt_entry.get())#(68445)
            strom_neu = int(self.strom_neu_entry.get())#(70644)
            strom_preis = self.strom_preis_entry.get()
            gas_preis = self.gas_preis_entry.get()

            #Gaswerte
            gas_alt= int(self.gas_alt_entry.get())
            gas_neu= int(self.gas_neu_entry.get())

            Stromverbrauch = strom_neu - strom_alt
            Gasverbrauch = gas_neu - gas_alt

            Strom_365 = Stromverbrauch / delta.days * 365
            Gas_365 = Gasverbrauch / delta.days * 365

            Strom_Kosten_365 = float(Strom_365) * float(strom_preis)
            Gas_Kosten_365 = float(Gas_365) * float(gas_preis)


            gesamst_kosten= Strom_Kosten_365 + Gas_Kosten_365

            abschlag_preis = int(self.abschlag_entry.get()) * 12

            Evtl_Rückzahlung = abschlag_preis - gesamst_kosten


            done_done = f"Stromverbauch in {delta.days} Tage: {Stromverbrauch} KwH\nGasverbauch in {delta.days} Tage: {Gasverbrauch} KwH\n_________________________________________\n\nStromverbauch überschlagen auf 365 Tage:\n{Strom_365} KwH\nGasverbauch überschlagen auf 365 Tage:\n{Gas_365} KwH\n_________________________________________\n\nStromkosten überschlagen auf 365 Tage:\n{Strom_Kosten_365} €\nGaskosten überschlagen auf 365 Tage:\n{Gas_Kosten_365} €\n_________________________________________\n\nGesamtkosten für 12 Monate: {gesamst_kosten} €\n_________________________________________\n\nUnser Abschlag für 12 Monate:{abschlag_preis} €\nEvtl. Rückzahlung: {Evtl_Rückzahlung} €"







            self.ergebnis_label.config(text=done_done)



            print(f"Stromverbauch in {delta.days} Tage: {Stromverbrauch} KwH")
            print(f"Gasverbauch in {delta.days} Tage: {Gasverbrauch} KwH\n\n")


            print(f"Stromverbauch überschlagen auf 365 Tage: {Strom_365} KwH")
            print(f"Gasverbauch überschlagen auf 365 Tage: {Gas_365} KwH\n\n")

            print(f"Stromkosten überschlagen auf 365 Tage: {Strom_Kosten_365} €")
            print(f"Gasverbauch überschlagen auf 365 Tage: {Gas_Kosten_365} €\n\n")

        self.inputs = Frame(self)
        self.inputs.pack(pady=20,padx=20,side=LEFT)
        

        # Letzte Ablesung
        self.alter_werte = LabelFrame(self.inputs,text="Letzte Ablesung",pady=10,padx=10)
        self.alter_werte.pack()

        self.datum_alt_label= Label(self.alter_werte,text="Letztes Ablesedatum:",justify="left",anchor="w",width=20)
        self.datum_alt_label.grid(column=0,row=0)


        # Tage Combo
        n1 = tk.IntVar()
        self.daychoosen = ttk.Combobox(self.alter_werte, width = 3, textvariable = n1)
        # Adding combobox drop down list
        self.daychoosen['values'] = (1,2,3,4,5,6,7,
                                8,
                                9,
                                10,
                                11,
                                12,
                                13,
                                14,
                                15,
                                16,
                                17,
                                18,
                                19,
                                20, 
                                21, 
                                22,
                                23,
                                24,
                                25,
                                26,
                                27,
                                28,
                                29,
                                30,
                                31)
        
        self.daychoosen.grid(column = 1, row = 0)


        # Monat Combo
        n2 = tk.IntVar()
        self.monthchoosen = ttk.Combobox(self.alter_werte, width = 3, textvariable = n2)
        # Adding combobox drop down list
        self.monthchoosen['values'] = (1, 
                                2,
                                3,
                                4,
                                5,
                                6,
                                7,
                                8,
                                9,
                                10,
                                11,
                                12)
        
        self.monthchoosen.grid(column = 2, row = 0)

        n3 = tk.IntVar()
        self.yearchoosen = ttk.Combobox(self.alter_werte, width = 5, textvariable = n3)
        # Adding combobox drop down list
        self.yearchoosen['values'] = (2022, 
                                2023,
                                2024,
                                2025,
                                2026,
                                2027,
                                2028,
                                2029,
                                2030,
                                2031,
                                2032,
                                2033)
        
        self.yearchoosen.grid(column = 3, row = 0)


        # Eingabe
        self.strom_alt_label= Label(self.alter_werte,text="Strom:",justify="left",anchor="w",width=20)
        self.strom_alt_label.grid(column=0,row=1)

        self.strom_alt_entry= Entry(self.alter_werte,width=20)
        self.strom_alt_entry.grid(column=1,row=1,columnspan=4)
        

        self.gas_alt_label= Label(self.alter_werte,text="Gas:",justify="left",anchor="w",width=20)
        self.gas_alt_label.grid(column=0,row=2)

        self.gas_alt_entry= Entry(self.alter_werte,width=20)
        self.gas_alt_entry.grid(column=1,row=2,columnspan=4)
               


        # Aktuelle Preis
        self.preis_werte = LabelFrame(self.inputs,text="Aktueller Strom- & Gaspreis",pady=10,padx=10)
        self.preis_werte.pack(pady=20)

        # Eingabe Preis
        self.strom_preis_label= Label(self.preis_werte,text="Strompreis is €:",justify="left",anchor="w",width=20)
        self.strom_preis_label.grid(column=0,row=1)

        self.strom_preis_entry= Entry(self.preis_werte,width=20)
        self.strom_preis_entry.grid(column=1,row=1)
        self.strom_preis_entry.insert(0,0.3905)

        self.gas_preis_label= Label(self.preis_werte,text="Gaspreis is €:",justify="left",anchor="w",width=20)
        self.gas_preis_label.grid(column=0,row=2)

        self.gas_preis_entry= Entry(self.preis_werte,width=20)
        self.gas_preis_entry.grid(column=1,row=2)     
        self.gas_preis_entry.insert(0,0.1216)

        self.abschlag_label= Label(self.preis_werte,text="Abschlag is €:",justify="left",anchor="w",width=20)
        self.abschlag_label.grid(column=0,row=3)

        self.abschlag_entry= Entry(self.preis_werte,width=20)
        self.abschlag_entry.grid(column=1,row=3)     
        


        # Aktuelle Ablesung
        self.neu_werte = LabelFrame(self.inputs,text="Aktuelle Ablesung",pady=10,padx=10)
        self.neu_werte.pack()

        self.datum_neu_label= Label(self.neu_werte,text="Aktuelles Ablesedatum:",justify="left",anchor="w",width=20)
        self.datum_neu_label.grid(column=0,row=0)


        # Tage Combo
        n4 = tk.IntVar()
        self.new_daychoosen = ttk.Combobox(self.neu_werte, width = 3, textvariable = n4)
        # Adding combobox drop down list
        self.new_daychoosen['values'] = (1,2,3,4,5,6,7,
                                8,
                                9,
                                10,
                                11,
                                12,
                                13,
                                14,
                                15,
                                16,
                                17,
                                18,
                                19,
                                20, 
                                21, 
                                22,
                                23,
                                24,
                                25,
                                26,
                                27,
                                28,
                                29,
                                30,
                                31)
        
        self.new_daychoosen.grid(column = 1, row = 0)


        # Monat Combo
        n5 = tk.IntVar()
        self.new_monthchoosen = ttk.Combobox(self.neu_werte, width = 3, textvariable = n5)
        # Adding combobox drop down list
        self.new_monthchoosen['values'] = (1, 
                                2,
                                3,
                                4,
                                5,
                                6,
                                7,
                                8,
                                9,
                                10,
                                11,
                                12)
        
        self.new_monthchoosen.grid(column = 2, row = 0)

        n6 = tk.IntVar()
        self.new_yearchoosen = ttk.Combobox(self.neu_werte, width = 5, textvariable = n6)
        # Adding combobox drop down list
        self.new_yearchoosen['values'] = (2022, 
                                2023,
                                2024,
                                2025,
                                2026,
                                2027,
                                2028,
                                2029,
                                2030,
                                2031,
                                2032,
                                2033)
        
        self.new_yearchoosen.grid(column = 3, row = 0)





        # Eingabe
        self.strom_neu_label= Label(self.neu_werte,text="Strom:",justify="left",anchor="w",width=20)
        self.strom_neu_label.grid(column=0,row=1)

        self.strom_neu_entry= Entry(self.neu_werte,width=20)
        self.strom_neu_entry.grid(column=1,row=1,columnspan=4)

        self.gas_neu_label= Label(self.neu_werte,text="Gas:",justify="left",anchor="w",width=20)
        self.gas_neu_label.grid(column=0,row=2)

        self.gas_neu_entry= Entry(self.neu_werte,width=20)
        self.gas_neu_entry.grid(column=1,row=2,columnspan=4)  

        self.gogo = Button(self.inputs,text="Berechnen",command=berechnen)
        self.gogo.pack(pady=10)



        self.ergebnis_werte = LabelFrame(self,text="Ergebnis",pady=10,padx=10)
        self.ergebnis_werte.pack(pady=20,padx=20,side=LEFT,fill=BOTH)

        self.ergebnis_label= Label(self.ergebnis_werte,text=" ",justify="left",anchor="w",width=50)
        self.ergebnis_label.pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()