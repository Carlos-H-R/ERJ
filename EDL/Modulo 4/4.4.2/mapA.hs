data Arvore a = Galho (Arvore a) a (Arvore a) | Folha
    deriving Show


mapA :: (a -> b) -> Arvore a -> Arvore b
mapA f Folha = Folha
mapA f (Galho l c r) = Galho (mapA f l) (f c) (mapA f r)

