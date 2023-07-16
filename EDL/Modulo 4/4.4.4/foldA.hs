data Lista a = No a (Lista a) | Vazio 
    deriving Show

foldA :: (a -> b -> b) -> b -> Lista a -> b
foldA f acc Vazio = acc
foldA f acc (No e r) = foldA f (f e acc) r

-- fold para somar
t = foldA (+) 0 l1

l1 = No 10 (No 20 (No 30 Vazio))