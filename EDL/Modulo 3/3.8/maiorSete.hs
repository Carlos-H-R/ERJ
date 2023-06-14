data Aluno = Aluno
    {
    nome :: String,
    p1 :: Float,
    p2 :: Float
    }deriving Show

alunos :: [Aluno]
alunos =
    [ Aluno {nome = "Alice"   , p1 = 8.5, p2 = 7.0}
    , Aluno {nome = "Bob"     , p1 = 6.0, p2 = 6.5}
    , Aluno {nome = "Carol"   , p1 = 7.5, p2 = 8.0}
    , Aluno {nome = "David"   , p1 = 9.0, p2 = 7.5}
    , Aluno {nome = "Eduardo" , p1 = 5.5, p2 = 6.0}
    , Aluno {nome = "Elen"    , p1 = 7.0, p2 = 7.5}
    , Aluno {nome = "Gloria"  , p1 = 8.0, p2 = 8.5}
    , Aluno {nome = "Henrique", p1 = 6.5, p2 = 7.0}
    , Aluno {nome = "Isabele" , p1 = 9.5, p2 = 9.0}
    , Aluno {nome = "Joao"    , p1 = 7.0, p2 = 6.5}
    , Aluno {nome = "Kevin"   , p1 = 6.0, p2 = 7.0}
    , Aluno {nome = "Luan"    , p1 = 8.5, p2 = 8.0}
    , Aluno {nome = "Mia"     , p1 = 7.0, p2 = 6.0}
    , Aluno {nome = "Natalia" , p1 = 8.0, p2 = 7.5}
    , Aluno {nome = "Pedro"   , p1 = 9.0, p2 = 9.5}
    ]


-- listMedias = map f alunos where
--     f :: Aluno -> (String, Float)
--     f x = (nome x, (p1 x + p2 x) / 2)

aprovados = filter f alunos where
    f x = (p1 x + p2 x) / 2 >= 7

listNome = map nome aprovados

main = print listNome
