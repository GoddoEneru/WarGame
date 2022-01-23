import numpy as np


def compute_number_neighbors_1(paded_frame, index_line, index_column):
    """
    Cette fonction prend en entrée la matrice avec bordure et
    renvoie le nombre de cellules 1 voisines vivantes
    """
    number_neighbors_1 = 0
    for ir in range(index_line - 1, index_line + 2):
        for ic in range(index_column - 1, index_column + 2):
            if paded_frame[(ir, ic)] == 1 and (ir != index_line or ic != index_column):
                number_neighbors_1 += paded_frame[(ir, ic)]
    return number_neighbors_1


def compute_number_neighbors_2(paded_frame, index_line, index_column):
    """
    Cette fonction prend en entrée la matrice avec bordure et
    renvoie le nombre de cellules 2 voisines vivantes
    """
    number_neighbors_2 = 0
    for ir in range(index_line - 1, index_line + 2):
        for ic in range(index_column - 1, index_column + 2):
            if paded_frame[(ir, ic)] == 2 and (ir != index_line or ic != index_column):
                number_neighbors_2 += paded_frame[(ir, ic)]
    return number_neighbors_2 / 2


def compute_next_frame(frame):
    """
    cette fonction prend en entrée une frame et retourne la frame suivante
    à partir des règles du jeu de la guerre
    """
    # Etape 1 : On calcule la matrice avec bordure
    paded_frame = np.pad(frame, 1, mode="constant")

    # Etape 2 : 2 boucles for imbriquées pour parcourir la matrice avec bordure (0 padding) élément par élément.
    for ir in range(1, paded_frame.shape[0] - 1):
        for ic in range(1, paded_frame.shape[1] - 1):
            # Etape 3 : Pour chacun des éléments calculez le nombre de voisin
            # On fait appelle à la fonction compute_number_neighbors
            number_neighbors_1 = compute_number_neighbors_1(paded_frame, ir, ic)
            number_neighbors_2 = compute_number_neighbors_2(paded_frame, ir, ic)
            number_neighbors = number_neighbors_1 + number_neighbors_2
            if number_neighbors > 6:
                frame[(ir - 1, ic - 1)] = 0
            elif number_neighbors_1 > number_neighbors_2:
                # Etape 4 : Pour chacun des éléments faire les tests (état de l'élément et son nombre de voisin)
                if (paded_frame[(ir, ic)] == 0 or paded_frame[(ir, ic)] == 2) and 2 <= number_neighbors_1 <= 3:
                    frame[(ir - 1, ic - 1)] = 1
                if paded_frame[(ir, ic)] == 1 and (number_neighbors_1 < 2 or number_neighbors_1 > 3):
                    frame[(ir - 1, ic - 1)] = 0
            elif number_neighbors_2 > number_neighbors_1:
                # Etape 4 : Pour chacun des éléments faire les tests (état de l'élément et son nombre de voisin)
                if (paded_frame[(ir, ic)] == 0 or paded_frame[(ir, ic)] == 1) and 2 <= number_neighbors_2 <= 3:
                    frame[(ir - 1, ic - 1)] = 2
                if paded_frame[(ir, ic)] == 2 and (number_neighbors_2 < 2 or number_neighbors_2 > 3):
                    frame[(ir - 1, ic - 1)] = 0
    return frame
