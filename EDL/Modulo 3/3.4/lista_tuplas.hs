-- Acrescenta um bonus de 30% na conta se o cliente for vip e 10% caso contrário
-- Caso o cliente não seja vip e o valor de sua conta for superior a 2500 ele passa a ser vip (sem bonus)
mapeia :: [(String,Int,Float,Bool)] -> [(String,Int,Float,Bool)]
mapeia = map f where
    f (n,i,x,v) = if v then (n,i,x*1.3,v)
        else do
            if x > 2500 then (n,i,x*1.1,True) else (n,i,x*1.1,v)


-- Filtra os clientes que possuem saldo superior a 3000 e idade inferior a 30 anos
filtra = filter f where
    f (_,i,s,_) = i < 30 && s > 3000

-- Calcula a arrecadacao com taxa de 1,2% para clientes vip e 5% para clientes comuns
dobra :: [(String,Int,Float,Bool)] -> Float
dobra = foldr f 0 where
    f :: (String,Int,Float,Bool) -> Float -> Float 
    f (_,_,x,v) acc = if v then 0.012*x + acc else 0.05*x + acc

main :: IO ()
main = do
    let dados = [("Augusto", 47, 3238, True), ("Pedro", 25, 890, False), ("Jorge", 62, 7920, True), ("Maria", 28, 4602, False)]
    print $ mapeia dados
    print $ filtra dados
    print $ dobra dados