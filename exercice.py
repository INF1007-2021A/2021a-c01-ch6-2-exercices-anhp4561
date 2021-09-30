#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib
from matplotlib.colors import cnames


def list_to_dict(some_list: list) -> dict:
    # TODO: Transformer la liste en dictionnaire, les éléments de la liste deviennent les clés et leur index deviennent les valeurs
    dictionnaire = {}
    for items in some_list:
        index = some_list.index(items)
        dictionnaire[items] = index

    return dictionnaire

def color_name_to_hex(colors: list) -> list:
    # TODO: Trouver la valeur hex de chaque couleur dans la liste et créer une liste de tupple où le premier élément est le nom de la couleur et le deuxième est la valeur hex
    """for cname, hex in matplotlib.colors.cnames.items():
        print(cname, hex)
        """
    col_and_hex = []
    for color in colors :
        col = matplotlib.colors.cnames.get(color)
        tup = (color,col)
        col_and_hex.append(tup)

    return col_and_hex


def create_list() -> list:
    # TODO: Créer une liste des 10 000 premiers entiers positif, sauf pour les entiers de 15 à 350
    #utiliser une comprehension de liste
    # ex de comprehension de liste : str_value = [value for value in values if not value.isdigit()]
    max_val = 350
    min_val = 15
    longueur = 10000
    liste_entier = [entier for entier in range(longueur) if entier < min_val or entier > max_val]
    return liste_entier


def compute_mse(model_dict: dict) -> dict:
    # TODO: Calculer l'erreur quadratique moyen pour chaque modèle. Retourner un dictionnaire contenant les MSE.
    for cle in model_dict: # for chaque cle dans le dict
        calcul2 = 0
        for i in model_dict[cle]: # pour chaque tuple dans la liste
            calcul = (i[0]-i[1])**2
            calcul2 += calcul
        mse = (1/len(model_dict[cle]))*calcul2
        model_dict[cle]= round(mse,1)

    return model_dict


def main() -> None:
    some_list = ["a", "b", "z", "patate"]
    print(f"La liste suivante {some_list} est transformée en dictionnaire: {list_to_dict(some_list)}")

    colors = ["blue", "red", "green", "yellow", "black", "white"]
    print(f"La valeur hex associée aux couleurs est: {color_name_to_hex(colors)}")

    print(f"La liste des 10000 entiers est: {create_list()}")

    model_dict = {"LR": [(90, 92), (96, 100), (20, 25), (21, -2), (3, -20)],
                  "DNN": [(100, 101), (50, 50), (1,2), (-10, -12), (-1, 7)],
                  "RF": [(10, 19), (56, 70), (1, 9), (-100, -12), (-11, 7)]}
    print(f"Le mse des différents modèles est: {compute_mse(model_dict)}")


if __name__ == '__main__':
    main()
