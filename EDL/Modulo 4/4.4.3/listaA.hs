data Arvore a = Galho (Arvore a) a (Arvore a) | Folha
    deriving Show

data Lista a = No a (Lista a) | Vazio 
    deriving Show

ccat :: Lista a -> Lista a -> Lista a
ccat Vazio b = b
ccat (No a ra) b = No a (ccat ra b)

lista :: Arvore a -> Lista a
lista Folha = Vazio
lista (Galho l c r) = No c (ccat (lista l) (lista r))

lintTree :: Arvore [Int]
lintTree = Galho  (Galho (Galho Folha l4 Folha) l2 (Galho Folha l5 Folha)) l1 (Galho (Galho Folha l6 Folha) l3 (Galho Folha l7 Folha))
l1 = [2,4,8,16]
l2 = [3,5,15]
l3 = [12]
l4 = [1,2,3]
l5 = [10,50,66]
l6 = [3,4,5]
l7 = [31,13]

r = lista lintTree

main = print r