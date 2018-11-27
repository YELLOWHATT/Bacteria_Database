# -*- coding: utf-8 -*-

__author__ = "Nico Moric, Marcus Ocampo"
__copyright__ = "No Copyright Yet"
__credits__ = "Nico Moric, Marcus Ocampo, Mr.Vhyte"
__license__ = "MIT"
__version__ = "0.0.0.0.11"
__maintainer__ = "Nico David Moric, Marcus Ocampo"
__email__ = "thekoolaidmannn@gmail.com"
__status__ = "Production"
__name__ = "?"
__dates__ = "11/17/18 - 11/25/18"
__type__ = "Scientific Application"
__estimated_realease_date__ = "03/04/19"
__name__ = "Bac-Biolog"
__help__ = "Mr.Vhyte"

import wikipedia
import math
import sys
import random
import os


##### The numebrs are organized in binary

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


##### Scientific name || Gram + || Species

##### Gram Positive Bacteria || EVEN NUMBERS

#####

def g_s():  # Gram Stain

    gram_pos = [bac00000010, bac00000100, bac00000110, bac00001000, bac00001010, bac00001100,
                bac00001110, bac00010000, bac00010010, bac00010100]  # || EVEN NUMBERS

    gram_neg = [bac00000001, bac00000011, bac00000101, bac00000111, bac00001001, bac00001011,
                bac00001101, bac00001111, bac00010001, bac00010011]  # || ODD NUMBERS

    print("Welcome!")
    print("\nYou are using version " + __version__ + " of " + __name__)

    print("\nPlease enter a gram stain or enter a name\n")

    NTS = str(input())

    if (NTS == "Gram Positive" or NTS == "Gram positive" or NTS == "gram positive"):

        for gram_pos in gram_pos:
            print("\n")
            print(gram_pos)
            print("\n")
        input("Press enter to continue...")

    elif (NTS == "Gram Negative" or NTS == "Gram negative" or NTS == "gram negative"):

        for gram_neg in gram_neg:
            print("\n")
            print(gram_neg)
            print("\n")
        input("Press enter to continue...")

    else:

        print("You have entered an illegal input please try again\n")
        g_s()

g_s()