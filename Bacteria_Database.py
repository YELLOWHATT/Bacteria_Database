# -*- coding: utf-8 -*-

__author__ = "BIO-LOGYK Software"
__license__ = "MIT"
__version__ = "0.0.0.0.37"
__maintainer__ = "Nico Moric"
__email__ = "thekoolaidmannn@gmail.com"
__status__ = "Production - Mid Alpha"
__dates__ = "11/17/18 - 12/03/18"
__type__ = "Scientific Application"
__estimated_release_date__ = "03/07/19"
__name__ = "Microbe-Log"

import wikipedia
import time
import sys
import os

##### Numbers are organized in binary

#### Add what deasease everything causes

#### b = bacteria || v = virus || p = protozoa

class virus:

    def __init__(self, namev, typev, speciesv):
        self.namev = namev
        self.typev = typev
        self.speciesv = speciesv

    def __str__(self):
        return (" ".join(["Name:", self.namev, "Type:", self.typev, "Species:", self.speciesv]))

####

#### RNA || ODD NUMBERS

#### Scientific name || RNA || Species

vrs = virus("Zaire Ebola Virus", "(-ssRNA)", "Ebola Virus")

#### Scientific name || RNA || Species

#### RNA || ODD NUMEBRS

#### LIST SEPARATION

class protozoa:

    def __init__(self, namep, typep, speciesp):
        self.namep = namep
        self.typep = typep
        self.speciesp = speciesp

    def __str__(self):
        return (" ".join(["Name:", self.namep, "Type:", self.typep, "Species:", self.speciesp]))

####

#### Protzoa || sOMETHING HERE

#### Protozoa || SOMETHING HERE

# Insert Protozoa objects here

#### Protozoa || SOMETHING HERE

#### Protozoa || SOEMTHING HERE

####


##### Class separation

class bacteria:

    def __init__(self, nameb, typeb, speciesb):
        self.nameb = nameb
        self.typeb = typeb
        self.speciesb = speciesb

    def __str__(self):
        return (" ".join(["Name:", self.nameb, "Type:", self.typeb, "Species:", self.speciesb]))

#####

##### Gram Negative Bacteria || ODD NUMBERS

##### Scientific name || Gram - || Species

bac00000001 = bacteria("Eschericia Coli", "Gram Negative", "Coli")  # 1
bac00000011 = bacteria("Pseudomonas Aeruginosa", "Gram Negatove", "Aeruginosa")  # 3
bac00000101 = bacteria("Salmonella Enterica", "Gram Negative", "Enterica")  # 5
bac00000111 = bacteria("Helicobacter Pylori", "Gram Negative", "Pylori")  # 7
bac00001001 = bacteria("Klebsiella Pneumoniae", "Gram Negative", "Pneumoniae")  # 9
bac00001011 = bacteria("Burkholderia Pseudomallei", "Gram Negative", "Pseudomallei")  # 11
bac00001101 = bacteria("Enterobacter Cloacae", "Gram Negative", "Cloacae")  # 13
bac00001111 = bacteria("Yersinia Pestis", "Gram Negative", "Pestis")  # 15
bac00010001 = bacteria("Neisseria Meningitidis", "Gram Negative", "Meningitidis")  # 17
bac00010011 = bacteria("Prevotella Melaninogenica", "Gram Negative", "Melaninogenica")  # 19
bac00010101 = bacteria("Salmonella Bongori", "Gram Negative", "Bongori") # 21
bac00010111 = bacteria("Vibrio Cholerae", "Gram Negative", "Cholerae") # 23
bac00011001 = bacteria("Brucellosis Canis", "Gram Negative", "Canis") # 25

##### Scientific name || Gram - || Species

##### Gram Negative Bacteria || ODD NUMBERS

##### ||||| ##### SEPARATED LISTS

##### Gram Positive Bacteria || EVEN NUMBERS

##### Scientific name || Gram + || Species

bac00000010 = bacteria("Streptococcus Sanguinis", "Gram Negative", "Sanguinis")  # 2
bac00000100 = bacteria("Staphylococcus Aureus", "Gram Positive", "Aureus")  # 4
bac00000110 = bacteria("Clostridium Botulinum", "Gram Positive", "Botulinum")  # 6
bac00001000 = bacteria("Clostridium Tetani", "Gram Positive", "Tetani")  # 8
bac00001010 = bacteria("Bacillus Anthracis", "Gram Positive", "Anthracis")  # 10
bac00001100 = bacteria("Listeria Monocytogenes", "Gram Positive", "Monocytogenes")  # 12
bac00001110 = bacteria("Clostridioides Difficile", "Gram Positive", "Difficile")  # 14
bac00010000 = bacteria("Streptococcus Mitis", "Gram Positive", "Mitis")  # 16
bac00010010 = bacteria("Clostridium Perfringens", "Gram Positive", "Perfringens")  # 18
bac00010100 = bacteria("Staphylococcus Saprophyticus", "Gram Positive", "Saprophyticus")  # 20
bac00010110 = bacteria("Corynebacterium Diphtheriae", "Gram Positive", "Diphtheriae") # 22
bac00011000 = bacteria("Streptococcus Pyogenes", "Gram Positive", "Pyogenes") # 24
bac00011010 = bacteria("Clostridium Perfringens", "Gram Positive", "Perfringens") # 26


##### Scientific name || Gram + || Species

##### Gram Positive Bacteria || EVEN NUMBERS

#####

def v(): # Virus

    def start_tres():

        print("\n")
        print("Please enter either 0 or 1 ( 0 - to exit the program || 1 - to continue the program )\n")

        strt_dos = str(input())

        if (strt_dos == "1"):

            print("Ok continuing program\n")
            v()

        elif (strt_dos == "0"):

            print("Ok exitting program\n")
            raise SystemExit()

        else:

            print("You have not entered a legal input try again\n")
            time.sleep(2)
            start_tres()

    def start_quatro():

        print("\n")
        print("You have entered an illegal input please try again\n")
        print("Or do you wish to exit?\n")

        ext_dos = str(input())

        if (ext_dos == "Yes" or ext_dos == "yes"):

            print("Ok exitting...")
            raise SystemExit()

        elif (ext_dos == "No" or ext_dos == "no"):

            print("Ok going back to the program")
            time.sleep(2)
            v()

        else:

            print("You have not entered a legal input please try again\n")
            start_tres()

    rna_based = [vrs]

    print("\nPlease enter a Nucleic type, Name, or a Species\n")
    print("If you would like to find more information on a Viral species enter wikipedia\n")

    VTS = str(input())

    if (VTS == "Rna" or VTS == "RNA" or VTS == "rna"):  # Virus

        for rna_based in rna_based:
            print("\n")
            print(rna_based)
            print("\n")
        input("This is the end of the program press enter to exit...")

    # Include one for other based viruses

    elif (VTS == "Wikipedia" or VTS == "WIKIPEDIA" or VTS == "wikipedia"):

        print("\nEnter the name of a bacteria to find more about it\n")
        wiki_virus = str(input())
        print("\n")
        print(wikipedia.summary(wiki_virus, sentences = 7))
        print("\nWould you like to return  to the menu or exit?")

        newexit = str(input())

        if (newexit == "Exit" or newexit == "exit"):

            print("Exitting...")
            raise SystemExit()

        elif (newexit == "Menu" or newexit == "menu"):

            print("Returning to menu...")
            v()

        else:

            start_tres()


    else:
        for rna_based in rna_based:

            if (rna_based.namev == VTS or rna_based.speciesv == VTS):
                print("\n")
                print(rna_based)
                print("\nGoing back to Main Menu\n")
                input("Press any key to continue")
                v()
                return

    # include for other based viruses

        time.sleep(2)
        start_tres()

####

#### Function separation

####

def g_s():  # Gram Stain this is done

    def start_dos():

        print("\n")
        print("Please enter either 0 or 1 ( 0 - to exit the program || 1 - to continue the program )\n")

        strt = str(input())

        if (strt == "1"):

            print("Ok continuing program\n")
            g_s()

        elif (strt == "0"):

            print("Ok exitting program\n")
            raise SystemExit()

        else:

            print("You have not entered a legal input try again\n")
            time.sleep(2)
            start_dos()

    def start_uno():

        print("\n")
        print("You have entered an illegal input please try again\n")
        print("Or do you wish to exit?\n")

        ext = str(input())

        if (ext == "Yes" or ext == "yes"):

            print("Ok exitting...")
            raise SystemExit()

        elif (ext == "No" or ext == "no"):

            print("Ok going back to the program")
            time.sleep(2)
            g_s()

        else:

            print("You have not entered a legal input please try again\n")
            start_dos()

    gram_pos = [bac00000010, bac00000100, bac00000110, bac00001000, bac00001010, bac00001100,
                bac00001110, bac00010000, bac00010010, bac00010100, bac00010110, bac00011000,
                bac00011010]  # || EVEN NUMBERS

    gram_neg = [bac00000001, bac00000011, bac00000101, bac00000111, bac00001001, bac00001011,
                bac00001101, bac00001111, bac00010001, bac00010011, bac00010101, bac00010111,
                bac00011001]  # || ODD NUMBERS

    print("\nPlease enter a Gram stain, Name, or a Species\n")
    print("If you would like to find more information on a bacterial species enter wikipedia\n")

    NTS = str(input())

    if (NTS == "Gram Positive" or NTS == "Gram positive" or NTS == "gram positive"): # Grams

        for gram_pos in gram_pos:
            print("\n")
            print(gram_pos)
            print("\n")
        input("This is the end of the program press enter to exit...")

    elif (NTS == "Gram Negative" or NTS == "Gram negative" or NTS == "gram negative"): # Grams

        for gram_neg in gram_neg:
            print("\n")
            print(gram_neg)
            print("\n")
        input("This is the end of the program press enter to exit...")

    elif (NTS == "Wikipedia" or NTS == "WIKIPEDIA" or NTS == "wikipedia"):

        print("\nEnter the name of a bacteria to find more about it\n")
        wiki_bacteria = str(input())
        print("\n")
        print(wikipedia.summary(wiki_bacteria, sentences = 7))
        print("\nWould you like to return  to the menu or exit?")

        nexit = str(input())

        if (nexit == "Exit" or nexit == "exit"):

            print("Exitting...")
            raise SystemExit()

        elif (nexit == "Menu" or nexit == "menu"):

            print("Returning to menu...")
            g_s()

        else:

            start_uno()


    else:
        for gram_pos in gram_pos:

            if (gram_pos.nameb == NTS or gram_pos.speciesb == NTS):

                print("\n")
                print(gram_pos)
                print("\nGoing back to Main Menu\n")
                input("Press any key to continue")
                g_s()
                return

        for gram_neg in gram_neg:

            if (gram_neg.nameb == NTS or gram_neg.speciesb == NTS):

                print("\n")
                print(gram_neg)
                print("Going back to Main Menu")
                input("Press any key to continue")
                g_s()
                return

        time.sleep(2)
        start_uno()

microbes = "Bacteria or Virus"

print("Welcome!")
print("\nYou are using version " + __version__ + " of " + __name__ + " made by " + __author__)
print("\nPlease select if you would like to view, " + microbes+ "\n")

view = str(input())

if (view == "Virus" or view == "virus" or view == "VIRUS"):

    print("\nGoing to Virus menu")
    v()

elif (view == "Bacteria" or view == "bacteria" or view == "BACTERIA"):

    print("\nGoing to Bacteria menu")
    g_s()

else:

    print("\nYou have entered an incorrect input please try again...\n")
    time.sleep(2)
    input("Press enter when you are ready...")