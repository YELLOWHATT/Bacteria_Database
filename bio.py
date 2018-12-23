#!/usr/bin/env python3

# -*- coding: utf-8 -*-

__author__ = "SIGMA-LOGYKAL Software"
__license__ = "MIT"
__version__ = "0.0.85"
__maintainer__ = "Nico Moric"
__email__ = "thekoolaidmannn@gmail.com"
__status__ = "Production - Pre Alpha"
__dates__ = "11/17/18 - 12/23/18"
__type__ = "Scientific Application"
__estimated_release_date__ = "03/07/19"
__name__ = "Microbe-Log"

import wikipedia
import sys
import time

##### Numbers are organized in binary

#### b = bacteria || v = virus || p = protozoa || f = fungi

class virus:

    def __init__(self, namev, typev, speciesv, common_name_diseasev):
        self.namev = namev
        self.typev = typev
        self.speciesv = speciesv
        self.common_name_diseasev = common_name_diseasev

    def __str__(self):
        return (" ".join(["Name:", self.namev, "Type:", self.typev, "Species:", self.speciesv, "Common disease name:", self.common_name_diseasev]))

#### LIST SEPARATION

#### RNA || ODD NUMBERS

#### Scientific name || RNA || Species

vrs00000000 = virus("Zaire Ebola Virus", "(-ssRNA)", "Ebola Virus", "Ebola Hemorhagic Fever") # 1

#### Scientific name || RNA || Species

#### RNA || ODD NUMEBRS

#### LIST SEPARATION

class protozoa:

    def __init__(self, namep, typep, speciesp, common_name_diseasep):
        self.namep = namep
        self.typep = typep
        self.speciesp = speciesp
        self.common_name_diseasep = common_name_diseasep

    def __str__(self):
        return (" ".join(["Name:", self.namep, "Type:", self.typep, "Species:", self.speciesp, "Common disease name:", self.common_name_diseasep]))

####

####

#### Protzoa || sOMETHING HERE

#### Protozoa || SOMETHING HERE

proto00000001 = protozoa("Toxoplasma gondii", "Spore forming", "Gondii", "Toxoplasmosis") # 1
proto00000010 = protozoa("Plasmodium vivax", "Spore forming", "Vivax", "Malaria") # 2

#### Protozoa || SOMETHING HERE

#### Protozoa || SOEMTHING HERE

####

##### Class separation

class bacteria:

    def __init__(self, nameb, typeb, speciesb, common_name_diseaseb):
        self.nameb = nameb
        self.typeb = typeb
        self.speciesb = speciesb
        self.common_name_diseaseb = common_name_diseaseb

    def __str__(self):
        return (" ".join(["Name:", self.nameb, "Type:", self.typeb, "Species:", self.speciesb, "Common disease name:", self.common_name_diseaseb]))

#####

##### Gram Negative Bacteria || ODD NUMBERS

##### Scientific name || Gram - || Species

bac00000001 = bacteria("Eschericia Coli", "Gram Negative", "Coli", "Lorem ipsum")  # 1
bac00000011 = bacteria("Pseudomonas Aeruginosa", "Gram Negatove", "Aeruginosa", "Lorem ipsum")  # 3
bac00000101 = bacteria("Salmonella Enterica", "Gram Negative", "Enterica", "Lorem  ipsum")  # 5
bac00000111 = bacteria("Helicobacter Pylori", "Gram Negative", "Pylori", "Lorem ipsum")  # 7
bac00001001 = bacteria("Klebsiella Pneumoniae", "Gram Negative", "Pneumoniae", "Lorem ipsum")  # 9
bac00001011 = bacteria("Burkholderia Pseudomallei", "Gram Negative", "Pseudomallei", "Lorem ipsum")  # 11
bac00001101 = bacteria("Enterobacter Cloacae", "Gram Negative", "Cloacae", "Lorem ipsum")  # 13
bac00001111 = bacteria("Yersinia Pestis", "Gram Negative", "Pestis", "lorem ipsum")  # 15
bac00010001 = bacteria("Neisseria Meningitidis", "Gram Negative", "Meningitidis", "Lorem ipsum")  # 17
bac00010011 = bacteria("Prevotella Melaninogenica", "Gram Negative", "Melaninogenica", "Lorem ipsum")  # 19
bac00010101 = bacteria("Salmonella Bongori", "Gram Negative", "Bongori", "Lorem ipsum") # 21
bac00010111 = bacteria("Vibrio Cholerae", "Gram Negative", "Cholerae", "Lorem ipsum") # 23
bac00011001 = bacteria("Brucellosis Canis", "Gram Negative", "Canis", "Lorem ipsum") # 25

##### Scientific name || Gram - || Species

##### Gram Negative Bacteria || ODD NUMBERS

##### ||||| ##### SEPARATED LISTS

##### Gram Positive Bacteria || EVEN NUMBERS

##### Scientific name || Gram + || Species

bac00000010 = bacteria("Streptococcus Sanguinis", "Gram Negative", "Sanguinis", "Lorum ipsum")  # 2
bac00000100 = bacteria("Staphylococcus Aureus", "Gram Positive", "Aureus", "Lorem ipsum")  # 4
bac00000110 = bacteria("Clostridium Botulinum", "Gram Positive", "Botulinum", "Botulinum Toxin")  # 6
bac00001000 = bacteria("Clostridium Tetani", "Gram Positive", "Tetani", "Tetanus")  # 8
bac00001010 = bacteria("Bacillus Anthracis", "Gram Positive", "Anthracis", "Anthrax")  # 10
bac00001100 = bacteria("Listeria Monocytogenes", "Gram Positive", "Monocytogenes", "Lorum ipsum")  # 12
bac00001110 = bacteria("Clostridioides Difficile", "Gram Positive", "Difficile", "Lorum ipsum")  # 14
bac00010000 = bacteria("Streptococcus Mitis", "Gram Positive", "Mitis", "Lorum ipsum")  # 16
bac00010010 = bacteria("Clostridium Perfringens", "Gram Positive", "Perfringens", "Lorum ipsum")  # 18
bac00010100 = bacteria("Staphylococcus Saprophyticus", "Gram Positive", "Saprophyticus", "Lorum ipsum")  # 20
bac00010110 = bacteria("Corynebacterium Diphtheriae", "Gram Positive", "Diphtheriae", "Lorem ipsum") # 22
bac00011000 = bacteria("Streptococcus Pyogenes", "Gram Positive", "Pyogenes", "Lorem ipsum") # 24
bac00011010 = bacteria("Clostridium Perfringens", "Gram Positive", "Perfringens", "Lorum ipsum") # 26


##### Scientific name || Gram + || Species

##### Gram Positive Bacteria || EVEN NUMBERS

#####

def repeat():
    print("You have entered an incorrect input please try again")
    print("Would you like to exit or continue?")
    continue_with_program = str(input())

    if (continue_with_program == "No" or continue_with_program == "no" or continue_with_program == "NO"):

        print("Ok continuing program")
        g_s()

    else:

        print("Are you sure you would like to exit")
        yes_exit = str(input())

        if (yes_exit == "No" or yes_exit == "NO" or yes_exit == "no"):

            print("OK")
            print("Going back to repeat")
            repeat()

        elif (yes_exit != "No" or yes_exit != "NO" or yes_exit != "n"):

            print("Exitting")
            sys.exit()

####

#### Function separation

####

def v(): # Virus

    rna_based = [vrs00000000]

    print("\nPlease enter a Nucleic type, Name, or a Species\n")
    print("If you would like to find more information on a Viral species enter wikipedia\n")

    VTS = str(input())
    print("\n\n############")

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
            sys.exit()

        elif (newexit == "Menu" or newexit == "menu"):

            print("Returning to menu...")
            repeat2()
            return

        else:

            repeat()


    else:
        for rna_based in rna_based:

            if (rna_based.namev == VTS or rna_based.speciesv == VTS or rna_based.typev == VTS):

                print("\n")
                print(rna_based)
                print("\nGoing back to Main Menu\n")
                input("Press any key to continue")
                repeat2()
                return

    # include for other based viruses

        time.sleep(2)
        repeat()
####

#### Function separation

####

def protozoan():

    protozoan_list = [proto00000001, proto00000010]

    print("\nPlease enter a Protozoan name, Species, or Causative agent")

    PTS = str(input())
    print("\n\n############\n\n")

    if (PTS == "Sporeforming" or PTS == "sporeforming" or PTS == "SPOREFORMING"):

        for protozoan_list in protozoan_list:
            print("\n")
            print(protozoan_list)
            print("\n")
        input("This is the end of the program press enter to exit...")
        repeat2()
        return

    elif (PTS == "Wikipedia" or PTS == "WIKIPEDIA" or PTS == "wikipedia"):

        print("\nEnter the name of a bacteria to find more about it\n")
        wiki_protozoa = str(input())
        print("\n")
        print(wikipedia.summary(wiki_protozoa, sentences = 7))
        print("\nWould you like to return  to the menu or exit?")

        nexit = str(input())

        if (nexit == "Exit" or nexit == "exit"):

            print("Exitting...")
            sys.exit()

        elif (nexit == "Menu" or nexit == "menu"):

            print("Returning to menu...")
            repeat2()
            return

        else:

            repeat()

    else:

        for protozoan_list in protozoan_list:

            if (protozoan_list.namep == PTS or protozoan_list.speciesp == PTS or protozoan_list.typep == PTS or protozoan_list.common_name_diseasep == PTS):

                print(protozoan_list)
                print("\nGoing back to Main Menu\n")
                input("Press any key to continue\n")
                repeat2()
                return

#### Function separation

def g_s():  # Gram Stain this is done

    gram_pos = [bac00000010, bac00000100, bac00000110, bac00001000, bac00001010, bac00001100,
                bac00001110, bac00010000, bac00010010, bac00010100, bac00010110, bac00011000,
                bac00011010]  # || EVEN NUMBERS

    gram_neg = [bac00000001, bac00000011, bac00000101, bac00000111, bac00001001, bac00001011,
                bac00001101, bac00001111, bac00010001, bac00010011, bac00010101, bac00010111,
                bac00011001]  # || ODD NUMBERS

    print("\nPlease enter a Gram stain, Name, Species or a Common name / disease\n")
    print("If you would like to find more information on a bacterial species enter wikipedia\n")

    NTS = str(input())
    print("\n\n############\n\n")

    if (NTS == "Gram Positive" or NTS == "Gram positive" or NTS == "gram positive"): # Grams stains

        for gram_pos in gram_pos:
            print("\n")
            print(gram_pos)
            print("\n")
        input("This is the end of the program press enter to exit...")

    elif (NTS == "Gram Negative" or NTS == "Gram negative" or NTS == "gram negative"): # Grams stains

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
            sys.exit()

        elif (nexit == "Menu" or nexit == "menu"):

            print("Returning to menu...")
            repeat2()
            return

        else:

            repeat()


    else:
        for gram_pos in gram_pos:

            if (gram_pos.nameb == NTS or gram_pos.speciesb == NTS or gram_pos.common_name_diseaseb == NTS):

                print(gram_pos)
                print("\nGoing back to Main Menu\n")
                input("Press any key to continue\n")
                repeat2()
                return

        for gram_neg in gram_neg:

            if (gram_neg.nameb == NTS or gram_neg.speciesb == NTS or gram_pos.common_name_diseaseb == NTS):

                print(gram_neg)
                print("\nGoing back to Main Menu\n")
                input("Press any key to continue\n")
                repeat2()
                return

        time.sleep(2)
        repeat()

microbes = "Bacteria, Virus or Protozoa (IN TEST FAZE) (Fungi coming soon!!!!!)"

print("Welcome!")
print("\nYou are using version " + __version__ + " of " + __name__ + " made by " + __author__)

def repeat2():

    print("\nPlease select if you would like to view, " + microbes + "\n")
    view = str(input())

    if (view == "Virus" or view == "virus" or view == "VIRUS"):

        print("\nGoing to Virus menu")
        v()

    elif (view == "Protozoa" or view == "PROTOZOA" or view == "protozoa"):

        print("\nGoing to Protozoa menu")
        protozoan()

    elif (view == "Bacteria" or view == "bacteria" or view == "BACTERIA"):

        print("\nGoing to Bacteria menu")
        g_s()

    else:

        print("\nYou have entered an incorrect input please try again...\n")
        time.sleep(2)
        input("Press enter when you are ready...")
        repeat2()

repeat2()