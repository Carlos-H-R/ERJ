data Lista a = No a (Lista a) | Vazio 
    deriving Show

filterl :: (a -> Bool) -> Lista a -> Lista a
filterl f Vazio = Vazio
filterl f (No a b) = if f a then No a (filterl f b) else filterl f b

list :: Lista  Int
list = No 10 (No 20 (No 30 Vazio))

g a = a > 22
flist = filterl g list
    
main = print flist