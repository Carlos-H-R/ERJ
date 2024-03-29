import Data.List (intercalate)

bandas :: [[String]]
bandas = [   ["Gilberto Gil"]
            ,["Victor","Leo"]
            ,["Gonzagao"]
            ,["Claudinho","Bochecha"] ]

type Musica = (String, Int, Int)
musicas :: [Musica]
musicas =   [("Aquele Abraco",        0, 100)
            ,("Esperando na Janela",  0, 150)
            ,("Borboletas",           1, 120)
            ,("Asa Branca",           2, 120)
            ,("Assum Preto",          2, 140)
            ,("Vem Morena",           2, 200)
            ,("Nosso Sonho",          3, 150)
            ,("Quero te Encontrar",   3, 100)]

nomes :: [String] -> String
nomes = intercalate ","

pprint :: Musica -> [String]
pprint (nome,banda,durac) =
    ["Nome: " ++ nome ++
    "\nAutores: " ++ nomes (bandas!!banda) ++
    "\nDuracao: " ++ show durac ++ "\n\n"]

percorre = foldr f [] musicas where
    f :: Musica -> [String] -> [String] 
    f m l = l ++ pprint m

main = putStr $ intercalate "\n" percorre