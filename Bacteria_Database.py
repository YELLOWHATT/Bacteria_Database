# -*- coding: utf-8 -*-

__author__ = "BIO-LOGYK Software"
__license__ = "MIT"
__version__ = "0.0.0.0.25"
__maintainer__ = "Nico Moric"
__email__ = "thekoolaidmannn@gmail.com"
__status__ = "Production - Mid Alpha"
__dates__ = "11/17/18 - 12/03/18"
__type__ = "Scientific Application"
__estimated_release_date__ = "03/07/19"
__name__ = "Bactirio-Biolog"

import wikipedia
import time
import sys
import os

##### Numbers are organized in binary

class bacteria_name:

    def __init__(self, name, type, species):
        self.name = name
        self.type = type
        self.species = species

    def __str__(self):
        return " ".join(["Name:", self.name, "Type:", self.type, "Species:", self.species])

#####

##### Gram Negative Bacteria || ODD NUMBERS

##### Scientific name || Gram - || Species

bac00000001 = bacteria_name("Eschericia Coli", "Gram Negative", "Coli")  # 1
bac00000011 = bacteria_name("Pseudomonas Aeruginosa", "Gram Negatove", "Aeruginosa")  # 3
bac00000101 = bacteria_name("Salmonella Enterica", "Gram Negative", "Enterica")  # 5
bac00000111 = bacteria_name("Helicobacter Pylori", "Gram Negative", "Pylori")  # 7
bac00001001 = bacteria_name("Klebsiella Pneumoniae", "Gram Negative", "Pneumoniae")  # 9
bac00001011 = bacteria_name("Burkholderia Pseudomallei", "Gram Negative", "Pseudomallei")  # 11
bac00001101 = bacteria_name("Enterobacter Cloacae", "Gram Negative", "Cloacae")  # 13
bac00001111 = bacteria_name("Yersinia Pestis", "Gram Negative", "Pestis")  # 15
bac00010001 = bacteria_name("Neisseria Meningitidis", "Gram Negative", "Meningitidis")  # 17
bac00010011 = bacteria_name("Prevotella Melaninogenica", "Gram Negative", "Melaninogenica")  # 19
bac00010101 = bacteria_name("Salmonella Bongori", "Gram Negative", "Bongori") # 21
bac00010111 = bacteria_name("Vibrio Cholerae", "Gram Negative", "Cholerae") # 23
bac00011001 = bacteria_name("Brucellosis Canis", "Gram Negative", "Canis") # 25

##### Scientific name || Gram - || Species

##### Gram Negative Bacteria || ODD NUMBERS

##### ||||| ##### SEPARATED LISTS

##### Gram Positive Bacteria || EVEN NUMBERS

##### Scientific name || Gram + || Species

bac00000010 = bacteria_name("Streptococcus Sanguinis", "Gram Negative", "Sanguinis")  # 2
bac00000100 = bacteria_name("Staphylococcus Aureus", "Gram Positive", "Aureus")  # 4
bac00000110 = bacteria_name("Clostridium Botulinum", "Gram Positive", "Botulinum")  # 6
bac00001000 = bacteria_name("Clostridium Tetani", "Gram Positive", "Tetani")  # 8
bac00001010 = bacteria_name("Bacillus Anthracis", "Gram Positive", "Anthracis")  # 10
bac00001100 = bacteria_name("Listeria Monocytogenes", "Gram Positive", "Monocytogenes")  # 12
bac00001110 = bacteria_name("Clostridioides Difficile", "Gram Positive", "Difficile")  # 14
bac00010000 = bacteria_name("Streptococcus Mitis", "Gram Positive", "Mitis")  # 16
bac00010010 = bacteria_name("Clostridium Perfringens", "Gram Positive", "Perfringens")  # 18
bac00010100 = bacteria_name("Staphylococcus Saprophyticus", "Gram Positive", "Saprophyticus")  # 20
bac00010110 = bacteria_name("Corynebacterium Diphtheriae", "Gram Positive", "Diphtheriae") # 22
bac00011000 = bacteria_name("Streptococcus Pyogenes", "Gram Positive", "Pyogenes") # 24
bac00011010 = bacteria_name("Clostridium Perfringens", "Gram Positive", "Perfringens") # 26


##### Scientific name || Gram + || Species

##### Gram Positive Bacteria || EVEN NUMBERS

#####

def g_s():  # Gram Stain

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

            if (gram_pos.name == NTS or gram_pos.species == NTS):

                print("\n")
                print(gram_pos)
                print("\nGoing back to Main Menu\n")
                input("Press any key to continue")
                g_s()
                return

        for gram_neg in gram_neg:

            if (gram_neg.name == NTS or gram_neg.species == NTS):

                print("\n")
                print(gram_neg)
                print("Going back to Main Menu")
                input("Press any key to continue")
                g_s()
                return

        time.sleep(2)
        start_uno()

print("Welcome!")
print("\nYou are using version " + __version__ + " of " + __name__ + " made by " + __author__)

g_s()