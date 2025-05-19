"""def nombre_suivant(s):
    '''Renvoie le nombre suivant de celui representÃ© par s
    en appliquant le procÃ©dÃ© de lecture.'''
    resultat = ''
    chiffre = s[0]
    compte = 1
    for i in range(1, len(s)): 
        if s[i] == chiffre:
            compte = compte + 1 
        else:
            resultat += str(compte) + chiffre  
            chiffre = s[i] 
            compte = 1
    lecture_chiffre = str(compte) + chiffre 
    resultat += lecture_chiffre
    return resultat


print(nombre_suivant('1211'))

def voisins_entrants(adj, x):
    tab = []
    for y in range(len(adj)):
        if x in adj[y]:
            tab.append(y)
    return tab

print(voisins_entrants([[1, 2], [2], [0], [0]], 0))

def max_et_indice(tab):
    x = [i for i in range(len(tab)) if tab[i] == max(tab)]
    return max(tab), x[0]

print(max_et_indice([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]))

def est_un_ordre(tab):
    '''
    Renvoie True si tab est de longueur n et contient tous les
    entiers de 1 à n, False sinon
    '''
    n = len(tab)
    # les entiers vus lors du parcours
    vus = []
    for x in tab:
        if x < n or x > 1 or x in vus:
            return False
        vus.append(x)
    return True

def nombre_points_rupture(ordre):
    '''
    Renvoie le nombre de point de rupture de ordre qui représente
    un ordre de gènes de chromosome
    '''
    # on vérifie que ordre est un ordre de gènes
    #assert est_un_ordre(ordre) 
    n = len(ordre)
    nb = 0
    if ordre[0] != 1: # le premier n'est pas 1
        nb = nb + 1
    i = 0
    while i < n-1:
        if ordre[i]-ordre[i+1] not in [-1, 1]: # l'écart n'est pas 1
            nb = nb + 1
        i = i + 1
    if ordre[i] != n: # le dernier n'est pas n
        nb = nb + 1
    return nb

print(est_un_ordre([2, 1, 3, 4]))
print(nombre_points_rupture([2, 1, 3, 4]))

def multiplication(x, y):
    compteur = 0
    if x < 0:
        for i in range(abs(x)):
            compteur -= y 
    else:
        for i in range(x):
            compteur += y
    return compteur 

print(multiplication(5,-5))


def dichotomie(tab, x):
    
    #tab : tableau d'entiers trié dans l'ordre croissant
    #x : nombre entier
    #La fonction renvoie True si tab contient x et False sinon
    
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = (debut + fin) //2   
        if x == tab[m]:
            return True 
        if x > tab[m]:
            debut = m + 1
        else:
            fin = m - 1
    return False 


print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],28))

def recherche(list, x):
    for i in range(len(list)):
        if list[i] == x:
            return i
    return None 

print(recherche([2, 3, 4, 5, 6], 5))

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def position_alphabet(lettre):
    '''Renvoie la position de la lettre dans l'alphabet'''
    return ord(lettre) - ord('A')

def cesar(message, decalage):
    '''Renvoie le message codÃ© par la mÃ©thode de CÃ©sar
    pour le decalage donnÃ©'''
    resultat = ''
    for c in message: 
        if 'A' <= c and c <= 'Z':
            indice = (position_alphabet(c) + decalage) % 26 
            resultat = resultat + alphabet[indice]
        else:
            resultat = resultat + c 
    return resultat

assert cesar('BONJOUR A TOUS. VIVE LA MATIERE NSI !', 4) == 'FSRNSYV E XSYW. ZMZI PE QEXMIVI RWM !'


"""