data Arvore a = Galho (Arvore a) a (Arvore a) | Folha
    deriving Show


folhas :: Arvore a -> Int
folhas Folha = 1
folhas (Galho l c r) = folhas l + folhas r
