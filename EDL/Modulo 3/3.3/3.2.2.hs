import Control.Monad.RWS (Any)
-- exemplos de map

-- aplicar juros a uma lista de valores (todos os itens do mercado sofreram um aumento de 1%)
a = [1.15,1.75,5.99,12.36,3.45,5.60,7.40,6.90]

f :: Float -> Float -> Float
f adj old = newer where
    newer = old * adj

b = map (f 1.01) a


-- Lista de itens, cada um possui os atributos (Nome, Nível, Ataque, Defesa)
itens :: [(String,Int,Int,Int)]
itens = [("Espada",3,15,5),("Escudo",2,2,20),("Lanca",5,21,7)]

g (n,x,y,z) = item where
    item = (n,x+1,y+2,z+2)

update = map g itens


-- Lista de clientes com o saldo deles
clientes :: [(String,Float)]
clientes = [("Carlos",0),("Fulano",-123.34),("Ciclano",302.10)]

h (_,v) = v < 0

neg = filter h clientes

-- Pesquisa em um banco de dados

-- Nome, cpf, endereco, idade
dados :: [(String,Int,String,Int)]
dados = [("Carlos",227,"Rio",24),("Maria",087,"Rio",25),("Joao",112,"SP",20)]

j idade (_,_,_,x) = x == idade

busca = filter (j 24) dados

func = [("Carlos",42),("Pedro",35),("Juliana",40),("Marcos",29)]

s :: Int -> (String,Int) -> Int -> Int
s limite (_,carga) acc = if carga > limite then acc+1 else acc

exc = foldr (s 40) 0 func