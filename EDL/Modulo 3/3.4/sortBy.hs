import Data.List (sortBy)

-- cliente :: [(Nome, Idade, Tempo de contrato, VIP)]

compareClient :: (String,Int,Int,Bool) -> (String,Int,Int,Bool) -> Ordering
compareClient (_,_,a_date,a_vip) (_,_,b_date,b_vip) = do
    if a_vip == b_vip
        then compare b_date a_date

    else if a_vip then LT
    else GT

sortPriority = sortBy compareClient

main :: IO ()
main = do
    let clientes = [("Augusto", 47, 3238, True), ("Pedro", 25, 890, False), ("Jorge", 62, 7920, True), ("Maria", 28, 2602, False)]
    let sorted = sortPriority clientes
    print sorted
