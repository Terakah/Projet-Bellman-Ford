# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 11:48:38 2022

@author: TeRaKa
"""

import List
from math import *




# Importation de toutes les classes qui peuvent être utilisées. Si elles ne le sont pas, ce n'est pas grave.


class Frame:
    '''
    attributes :
    - data :  
    - next : next Frame or None
    - prev : previous Frame or None
    
    Dependencies : none
    '''
    def __init__(self,x):
        self.data=x
        self.next=None
        self.prev=None

class Queue:
    
    
    
    '''
    class for a queue
    
    attributes :
    - head : Frame or None
    - tail : Frame or None
    
    methods :
    - is_empty() : return true is the queue is empty, false otherwise
    - enqueue(x) : enqueue the data x  
    - dequeue() : if the queue is not empty, dequeue the head, else do nothing and return None
    - print() : print the queue

    Dependencies : class Frame
    '''
    def __init__(self):
        self.head=None
        self.tail=None
        
    def is_empty(self):
        return self.head is None
    
    def enqueue(self,x):
        new_tail=Frame(x)
        # écriture du chainage aller : 2 cas
        new_tail.next=None
        if self.tail is None:
        # si la file est vide, self.head doit pointer sur new_tail
            self.head= new_tail
        else:
        # Sinon, self.tail.next est valide et doit pointer sur new_tail
            self.tail.next=new_tail
        # écriture du chainage retour : 1 cas
        new_tail.prev=self.tail 
        self.tail=new_tail 

    def dequeue(self):
        #si la liste est vide, on ne fait rien
        if self.head is None:
            return None    
        # sinon sauvegarde de l'élément défiler
        x=self.head.data
        # écriture du chainage aller : 1 cas
        self.head=self.head.next 
        # écriture du chainage retour : 2 cas
        if self.head is None:
        # si la liste devient vide
            self.tail=None
        # sinon self.head.prev est valide
        else:
            self.head.prev=None
        return x
        
    def print(self):  # fonction d'affichage de la file
        print('File= ',end='')
        current=self.head
        while current:
            print(current.data,end=' ')
            current=current.next
        print()          
        
class Linked_list:
    '''
    class for a linked list
    
    attributes :
    - head : Frame or None
    
    methods :
    - is_empty() : return true is the list is empty, false otherwise
    - append(x) : add the data x at the head 
    - pop() : if the linked list is not empty, pop the head, else do nothing and return None
    - print() : print the list
    
    Dependencies : class Frame
    '''
    def __init__(self):
        self.head=None

    def is_empty(self):
        return self.head is None
        
    def append(self,x):
        new_head = Frame(x)
        new_head.next = self.head
        self.head = new_head

    def pop(self):
        if self.head is None:
            return None
        x=self.head.data
        self.head=self.head.next
        return x
       
class Adj_list(List.Linked_list): 
    '''
    class for a adjacency list
    
    attributes inherited from Linked_list :
    - head : Frame1 or None
    
    methods inherited from Linked_list :
    - is_empty() : return true is the queue is empty, false otherwise
    - append(x) : add the data x at the head 
    - pop() : if the linked list is not empty, pop the head, else do nothing and return None
    
    new method
    - print() : print the list of node name
    
    Dependencies : class Linked_list
'''

    def print(self):  # surcharge la methode print des listes pour afficher les noms des noeuds
        print("Liste d'adjacence = ",end='')
        current=self.head
        while current:
            edge=current.data
            print(edge.head.name,',',edge.w, end=' ; ')
            current=current.next
        print()    
        
class Node: 
    '''
    Class for nodes of a graph
    
    Attributes :
    - index : index of the node in the graph list
    - name : string (default '')
    - adj : Adj_list of Edge

    Dependencies : class Adj_list
    '''
    def __init__(self,index=0,name=''):
        self.index = index
        self.name = name
        self.adj = Adj_list()

class Edge: 
    '''
    Class for edges of a graph
        
    @attributes :
        - head : Node   # dans l'arc (x,y), y est nommé head en anglais (tete de la fleche), et x tail (queue de la fleche)
        - w : weight
    
    @requires : None
    '''
    def __init__(self,n,w=1):
        self.head = n  
        self.w = w

class Graph:
    '''
    Class for graph
    
    @attributes :
    - nodes : list of Node  (default empty list)
    
    @methods :
    - add_edge(i,j,w=1) : if i and j are not out of range, add an edge between i and j with the weight w (default edge = 1), do nothing otherwise
    
    @requires : classes Node, Edge and Adj_list
    '''
    def __init__(self,l=[]):  # l est optionnel : liste ne noms de noeuds
        self.nodes=list()
        for i in range(len(l)):
            n=Node(i,l[i])
            self.nodes.append(n)
 
    def add_edge(self,i,j,w=1):
        if i<len(self.nodes) and j<len(self.nodes):
            e=Edge(self.nodes[j],w)
            self.nodes[i].adj.append(e)
            
    def print_adj_list(self):
        for n in self.nodes:
            print('Noeud :', n.index,n.name )
            n.adj.print()
    
    def add_edge_list(self,E):
        for e in E:
            if len(e)==2:
                self.add_edge(e[0],e[1])
            if len(e)>2:
                self.add_edge(e[0],e[1],e[2])

    def edges_list(self):
        l = []
        for n in self.nodes:
            objet = n.adj.head
            while current != None:
                frame = objet.data
                l.append([n.index, frame.head.index, frame.w])
                objet=objet.next  
        return l
            



E = [[0, 1, 16.0],
  [1, 0, 0.0],
  [0, 2, 13.0],
  [2, 0, 0.0],
  [1, 2, 10.0],
  [1, 3, 12.0],
  [3, 1, 0.0],
  [2, 1, 4.0],
  [2, 4, 14.0],
  [4, 2, 0.0],
  [3, 2, 9.0],
  [2, 3, 0.0],
  [3, 5, 20.0],
  [5, 3, 0.0],
  [4, 3, 7.0],
  [3, 4, 0.0],
  [4, 5, 4.0],
  [5, 4, 0.0]]




"---------------------------------------------------------------GRAPHE-------------------------------------------------------------"


def bellman_ford(G, src): #G est ici un objet de la classe Graph, src est la source de type int
    distances = list(inf for h in range(len(G.nodes)))
    predecesseurs = list(None for h in range(len(G.nodes)))
    distances[src] = 0

    edges = G.edges_list() #On récupère une liste de toutes les arêtes du graphe G
    for _ in range(len(G.nodes)-1): #On fait n-1 itérations avec n le nombre de sommets
        for e in edges:
            if distances[e[0]] != inf and (distances[e[0]] + e[2] < distances[e[1]]): #On relaxe dans le cas où on peut optimiser
                distances[e[1]] = distances[e[0]] + e[2]
                predecesseurs[e[1]] = e[0]

    for e in edges: #On vérifie qu'il n y ait pas de cycle négatif (la condition n'étant supposée par satisfaisable après algorithme)
        if (distances[e[0]] + e[2] < distances[e[1]]):
            raise TypeError("Graphe à cycle négatif.")

    return distances, predecesseurs




#Pour l'amélioration de Moore, on essaie de compter une seule fois une optimisation qui ne change plus. De ce fait, l'une des façons de le faire
#est d'introduire une variable dit ''drapeau'' afin de ne pas refaire les même actions plusieurs fois.
#Afin d'assurer un return "correct" (car on peut avoir le cas où on a 2 arètes + et - optimales évalués en même temps sans avoir l'optimalité des autres arètes)
#On va tout de même faire n-1 itérations, n étant le nombre de sommets


def bellman_ford_moore(G, src):
    distances = list(inf for h in range(len(G.nodes)))
    predecesseurs = list(None for h in range(len(G.nodes)))
    distances[src] = 0

    edges = G.edges_list()
    for _ in range(len(G.nodes)-1):
        drapeau = False
        for e in edges:
            if distances[e[0]] != inf and (distances[e[0]] + e[2] < distances[e[1]]):
                distances[e[1]] = distances[e[0]] + e[2]
                predecesseurs[e[1]] = e[0]
                drapeau = True
                
            if drapeau == False:
                break
    for e in edges:
        if distances[e[1]]> distances[e[0]]+ e[2] :
            raise TypeError("Graphe à cycle négatif.")
            
    return distances, predecesseurs
    
    





#Il est important de diviser le graphe en 2 pour l'amélioration de Yen: On doit aller avoir deux listes qui représenteraient respectivement
#la liste des arètes + et la liste des arète -. Ainsi, on va introduire une nouvelle fonction, la fonction "tri"
#On va alors faire l'amélioration de Moore sur les listes d'arêtes + et -



def tri_list(edges):
    edgesPLUS  = []
    edgesMOINS = []
    for e in edges:
        if e[0] <= e[1]:  #Cas où pour une arète (i,j), on a i <= j
            edgesPLUS.append(e)
        else:
            edgesMOINS.append(e)
    return edgesPLUS, edgesMOINS
    

    

def bellman_ford_yen(G, src):
    distances = list(inf for h in range(len(G.nodes)))     
    predecesseurs = list(None for h in range(len(G.nodes)))
    distances[src] = 0

    edges = G.edges_list()
    edgesPLUS, edgesMOINS = tri_list(edges)

    for _ in range(len(G.nodes)-1):
        drapeau = False
        for plus in edgesPLUS:
            if distances[plus[0]] != inf and  (distances[plus[0]] + plus[2] < distances[plus[1]]):
                distances[plus[1]] = distances[plus[0]] + plus[2]
                predecesseurs[plus[1]] = plus[0]
                drapeau = True

        for moins in edgesMOINS:
            if distances[moins[0]] != inf and (distances[plus[0]] + plus[2] < distances[plus[1]]):
                distances[moins[1]] = distances[moins[0]] + moins[2]
                predecesseurs[moins[1]] = moins[0]
                drapeau = True

        if drapeau == False:
            break
    
    
    for e in edges:
        if distances[e[1]]> distances[e[0]]+ e[2] :
            raise TypeError("Graphe à cycle négatif.")

    return distances, predecesseurs


 










# Tout cela est vrai pour un G graphe. Pour un fichier texte on peut faire de nouvelles fonctions.
"-----------------------------------------------------FICHIER TXT----------------------------------------------------------"

def graphfromfic():
    E=list()
    Y = input("Fichier: ")
    with open(Y, mode='r', encoding='utf-8-sig') as fp:
        # ouverture en lecture d'un fichier codé en utf-8 avec BOM
        for i,line in enumerate(fp): # line est un string qui contient une ligne du fichier
            line.strip() # la méthode strip() retire les caractères non imprimable
            if i==0:
                if line:  # teste si line est vide
                    n=int(line) # int() convertit un string en entier
                else:
                    raise SystemExit(1)  # provoque la sortie du programme  
            else:        
                L=line.split(';') # decoupe line selon le séparateur ';'
                if len(L)==3:  # elimine les lignes mal formees
                    E.append([int(L[0]), int(L[1]),float(L[2])])
    fp.close()

    
    return E, n






def bellman_fordfic(src): #Pas besoin ici de G en argument car on n'a pas de graphe au début
    G, n = graphfromfic() #On transforme le fichier voulu en liste d'arêtes et on récupère le nombre de sommets grâce à n
    distances = list(inf for h in range(n))
    predecesseurs = list(None for h in range(n))
    distances[src] = 0

    edges = G #Cette étape n'est pas primordiale, c'est pour facilité la compréhension, on aurait pu le faire plus haut
    for _ in range(n-1): #On fait n-1 itérations avec n le nombre de sommets
        for e in edges:
            if distances[e[0]] != inf and (distances[e[0]] + e[2] < distances[e[1]]): #On relaxe dans le cas où on peut optimiser
                distances[e[1]] = distances[e[0]] + e[2]
                predecesseurs[e[1]] = e[0]

    for e in edges: #On vérifie qu'il n y ait pas de cycle négatif (la condition n'étant supposée par satisfaisable après algorithme)
        if (distances[e[0]] + e[2] < distances[e[1]]):
            raise TypeError("Graphe à cycle négatif.")

    return distances, predecesseurs


def bellman_ford_moorefic(src): #Les deux fonctions suivantes sont les même que précédemment en prenant en compte les modification dans le cas d'un fichier txt
    G, n = graphfromfic()
    distances = list(inf for h in range(n))
    predecesseurs = list(None for h in range(n))
    distances[src] = 0

    edges = G
    for _ in range(n-1):
        drapeau = False
        for e in edges:
            if distances[e[0]] != inf and (distances[e[0]] + e[2] < distances[e[1]]):
                distances[e[1]] = distances[e[0]] + e[2]
                predecesseurs[e[1]] = e[0]
                drapeau = True
                
            if drapeau == False:
                break
    for e in edges:
        if distances[e[1]]> distances[e[0]]+ e[2] :
            raise TypeError("Graphe à cycle négatif.")
            
    return distances, predecesseurs
    

def bellman_ford_yenfic(src):
    G, n = graphfromfic()
    distances = list(inf for h in range(n))     
    predecesseurs = list(None for h in range(n))
    distances[src] = 0

    edges = G
    edgesPLUS, edgesMOINS = tri_list(edges)

    for _ in range(n-1):
        drapeau = False
        for plus in edgesPLUS:
            if distances[plus[0]] != inf and  (distances[plus[0]] + plus[2] < distances[plus[1]]):
                distances[plus[1]] = distances[plus[0]] + plus[2]
                predecesseurs[plus[1]] = plus[0]
                drapeau = True

        for moins in edgesMOINS:
            if distances[moins[0]] != inf and (distances[plus[0]] + plus[2] < distances[plus[1]]):
                distances[moins[1]] = distances[moins[0]] + moins[2]
                predecesseurs[moins[1]] = moins[0]
                drapeau = True

        if drapeau == False:
            break
    
    
    for e in edges:
        if distances[e[1]]> distances[e[0]]+ e[2] :
            raise TypeError("Graphe à cycle négatif.")

    return distances, predecesseurs













#Dans le cas où nous avons une liste en guise de graphe comme dans le fichier txt exemple2_graphe, on pourra introduire:
"---------------------------------------------------------LISTE----------------------------------------------------------"

    
def bellman_fordlist(G, src): #G est ici un objet de la classe List, src est la source de type int
    C = []
    for i in G:              #On compte ici le nombre de sommets
        if not(i[0] in C):
            C.append(i[0])
        if not(i[1] in C):
            C.append(i[1])
    n = len(C)
    distances = list(inf for h in range(n))
    predecesseurs = list(None for h in range(n))
    distances[src] = 0
    
    for _ in range(n-1): #On fait n-1 itérations avec n le nombre de sommets
        for e in G:
            if distances[e[0]] != inf and (distances[e[0]] + e[2] < distances[e[1]]): #On relaxe dans le cas où on peut optimiser
                distances[e[1]] = distances[e[0]] + e[2]
                predecesseurs[e[1]] = e[0]

    for e in G: #On vérifie qu'il n y ait pas de cycle négatif (la condition n'étant supposée par satisfaisable après algorithme)
        if (distances[e[0]] + e[2] < distances[e[1]]):
            raise TypeError("Graphe à cycle négatif.")

    return distances, predecesseurs


def bellman_ford_moorelist(src): #Les deux fonctions suivantes sont les même que précédemment en prenant en compte les modification dans le cas d'une liste
    distances = list(inf for h in range(n))
    predecesseurs = list(None for h in range(n))
    distances[src] = 0
    C = []
    for i in G:              
        if not(i[0] in C):
            C.append(i[0])
        if not(i[1] in C):
            C.append(i[1])
    edges = G
    for _ in range(n-1):
        drapeau = False
        for e in edges:
            if distances[e[0]] != inf and (distances[e[0]] + e[2] < distances[e[1]]):
                distances[e[1]] = distances[e[0]] + e[2]
                predecesseurs[e[1]] = e[0]
                drapeau = True
                
            if drapeau == False:
                break
    for e in edges:
        if distances[e[1]]> distances[e[0]]+ e[2] :
            raise TypeError("Graphe à cycle négatif.")
            
    return distances, predecesseurs




def bellman_ford_moorelist(G, src):
    
    
    distances = list(inf for h in range(n))
    predecesseurs = list(None for h in range(n))
    distances[src] = 0
    C = []
    for i in G:
        if not(i[0] in C):
            C.append(i[0])
        if not(i[1] in C):
            C.append(i[1])
    n = len(C)
    for _ in range(n-1):
        drapeau = False
        for e in G:
            if distances[e[0]] != inf and (distances[e[0]] + e[2] < distances[e[1]]):
                distances[e[1]] = distances[e[0]] + e[2]
                predecesseurs[e[1]] = e[0]
                drapeau = True
                
            if drapeau == False:
                break
    for e in G:
        if distances[e[1]]> distances[e[0]]+ e[2] :
            raise TypeError("Graphe à cycle négatif.")
            
    return distances, predecesseurs  
def bellman_ford_yenlist(G, src):
    distances = list(inf for h in range(n))     
    predecesseurs = list(None for h in range(n))
    distances[src] = 0
    C = []
    for i in G:
        if not(i[0] in C):
            C.append(i[0])
        if not(i[1] in C):
            C.append(i[1])
    n = len(C)
    edgesPLUS, edgesMOINS = tri_list(G)

    for _ in range(n-1):
        drapeau = False
        for plus in edgesPLUS:
            if distances[plus[0]] != inf and  (distances[plus[0]] + plus[2] < distances[plus[1]]):
                distances[plus[1]] = distances[plus[0]] + plus[2]
                predecesseurs[plus[1]] = plus[0]
                drapeau = True

        for moins in edgesMOINS:
            if distances[moins[0]] != inf and (distances[plus[0]] + plus[2] < distances[plus[1]]):
                distances[moins[1]] = distances[moins[0]] + moins[2]
                predecesseurs[moins[1]] = moins[0]
                drapeau = True

        if drapeau == False:
            break
    
    
    for e in G:
        if distances[e[1]]> distances[e[0]]+ e[2] :
            raise TypeError("Graphe à cycle négatif.")

    return distances, predecesseurs













"---------------------------------------------------------DANS TOUS LES CAS------------------------------------------------------------"


# Ainsi, dans le cas général où on ne fait pas la distinction entre graphe, liste et fichier txt, on peut faire un appel de fonctions avec
#les fonctions précédemment définies
    



def bellman_ford2(G, src): 
    X = input("txt, liste ou graphe: ")
    if X == "txt":
        return(bellman_fordfic(src))
    elif X == "liste":
        return(bellman_fordlist(G,src))
    else:
        return(bellman_ford(G,src))
     
    
def bellman_ford_moore2(G,src): 
    X = input("txt, liste ou graphe: ")
    if X == "txt":
        return(bellman_ford_moorefic(src))
    elif X == "liste":
        return(bellman_ford_moorelist(G,src))
    else:
        return(bellman_ford_moore(G,src))
      
    
def bellman_ford_yen2(G,src):
    X = input("txt, liste ou graphe: ")
    if X == "txt":
        return(bellman_ford_yenfic(src))
    elif X == "liste":
        return(bellman_ford_yenlist(G,src))
    else:
        return(bellman_ford_yen(G,src))    