import Data.List (sortBy, partition)

divideAge :: (String,Int) -> Bool
divideAge (_,age) = age < 18

sortByAge :: [(String,Int)] -> [(String,Int)]
sortByAge lista = x where
    (minor,adult) = partition divideAge lista
    a = sortByLexicographic minor
    b = sortByLexicographic adult
    x = a ++ b


compareName :: (String,Int) -> (String,Int) -> Ordering
compareName (a,_) (b,_) = compare a b

sortByLexicographic :: [(String,Int)] -> [(String,Int)]
sortByLexicographic = sortBy compareName

main :: IO ()
main = do
  let people = [("Carlos",24), ("Ana",18), ("Gustavo",13), ("Vitor",22), ("Joao",17), ("Bruno",31), ("Bernardo",26)]
  let sortedPeople = sortByAge people
  print sortedPeople