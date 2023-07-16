data Lista a = No a (Lista a) | Vazio 
    deriving Show

sublist :: Lista (Lista Int)
sublist = No l1 (No l2 (No l3 Vazio))
-- sublist = No ((No 10 (No 20 (No 30 Vazio)))  (No (No (No 13 (No 31 Vazio)) (No (No 23 Vazio) Vazio))))

l1 = No 10 (No 20 (No 30 Vazio))
l2 = No 13 (No 31 Vazio)
l3 = No 23 Vazio

main = print sublist