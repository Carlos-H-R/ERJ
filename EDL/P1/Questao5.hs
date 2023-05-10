import Language.Haskell.TH.PprLib (float)
import Data.String (IsString)
import Text.Read (Lexeme(String))
import GHC.Exts.Heap (GenClosure(FloatClosure))
import Data.STRef (STRef)
type Aluno = (String,Integer,Integer)

alunos :: [Aluno]
alunos = [   ("Ana",80,100),
            ("Bernardo",70,96),
            ("Carlos",60,70),
            ("Danilo",30,40)
        ]

mean :: (String,Integer,Integer) -> (String,Float)
mean (a,x,y) = (a,(fromInteger x + fromInteger y) / 2)

apro :: [(String,Float)] -> [(String,Float)]
apro l = filter f l where
    f :: (String,Float) -> Bool
    f (_,v) = v >= 50

maxmin :: [(String,Float)] -> ((String,Float),(String,Float))
maxmin = foldr f (("",0),("",100)) where
    f :: (String,Float) -> ((String,Float),(String,Float)) ->  ((String,Float),(String,Float))
    f (c,z) ((a,x),(b,y))
      | z < y = ((a,x),(c,z))
      | z > x = ((c,z),(b,y))
      | otherwise = ((a,x),(b,y))


main = print $ maxmin $ apro $ map mean alunos