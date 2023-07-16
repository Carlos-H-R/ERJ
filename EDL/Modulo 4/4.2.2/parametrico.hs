data Arvore a = Galho (Arvore a) a (Arvore a) | Folha
    deriving Show

data Lista a = No a (Lista a) | Vazio 
    deriving Show

binTree :: Arvore Bool
binTree = Galho  (Galho (Galho Folha True Folha) True (Galho Folha False Folha)) True (Galho (Galho Folha False Folha) False (Galho Folha True Folha))

lintTree :: Arvore [Int]
lintTree = Galho  (Galho (Galho Folha l4 Folha) l2 (Galho Folha l5 Folha)) l1 (Galho (Galho Folha l6 Folha) l3 (Galho Folha l7 Folha))
l1 = [2,4,8,16]
l2 = [3,5,15]
l3 = [12]
l4 = [1,2,3]
l5 = [10,50,66]
l6 = [3,4,5]
l7 = [31,13]

main = do
    print binTree
    print lintTree