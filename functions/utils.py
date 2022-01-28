import numpy as np

def transform_alignement_file(file):
    """ 
        Input : fichier .txt contenant les alignements entre chaque phrase
        Output : matrice des alignements entre chaque mot de chaque phrase
    """
    file_clean = []
    for l in file:
        l = l.split(' ')
        l[-1]=l[-1][-2]
        file_clean.append([int(e) for e in l[:-1]]+[l[-1]])
    return file_clean

def transform_sentence_file(file):
    """ 
        Input : fichier .txt où chaque ligne est une phrase
        Output : liste des phrases du fichier
    """
    file_clean = []
    for sentence in file:
        sentence = sentence.split(' ')[2:-1]
        file_clean.append(sentence)
    return file_clean

def lines_to_tab(lines):
    """ 
        Input : liste des phrases sous forme chaine de charctères
        Output : matrice des phrases pures
    """
    tab = [[] for i in range(100)]
    sentence_id = lines[0][0]
    for line in lines:
        if line[0]!=sentence_id:
            sentence_id = line[0]
        tab[sentence_id-1].append(line[1:])
    return tab


def extract_al(matrix):
    """ 
        Input : matrice binaire (0 : non aligné ; 1 : aligné)
        Output : liste des alignements
    """
    indexes = np.where(matrix==1)
    return list(zip(indexes[0],indexes[1]))


def matrix_to_alignments(M):
    """ 
        Input : matrice binaire (0 : non aligné ; 1 : aligné)
        Output : liste des alignements
    """
    al = []
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            if M[i][j]==1:
                al.append([i,j])
    return al  