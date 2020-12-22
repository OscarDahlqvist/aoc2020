import Debug.Trace
import Data.List

d1 :: [Int]
d2 :: [Int]
--d1 = [9,2,6,3,1]
--d2 = [5,8,4,7,10]
--d1 = [43,19]
--d2 = [2,29,14]
d1 = [10,39,16,32,5,46,47,45,48,26,36,27,24,37,49,25,30,13,23,1,9,3,31,14,4]
d2 = [2,15,29,41,11,21,8,44,38,19,12,20,40,17,22,35,34,42,50,6,33,7,18,28,43]

game :: [Int] -> [Int] -> [([Int],[Int])] -> (Int,[Int],[([Int],[Int])])
game (c1:p1) (c2:p2) setups
 | (p1,p2) `elem` setups = (1,exdeck1,setups)
 | length p1 == 0 = (2,exdeck2,setups)
 | length p2 == 0 = (1,exdeck1,setups)
 | c1 <= length p2 && c2 <= length p2 
  = if reqWin == 1 then game1 else game2 
 | c1 > c2 = game1
 | c2 > c1 = game2
 where
  newSetups = (p1,p2):setups
  (reqWin,_,_) = game p1 p2 newSetups
  game1 = game exdeck1 p2 newSetups
  game2 = game p1 exdeck2 newSetups
  exdeck1 = (p1++[c1,c2])
  exdeck2 = (p2++[c2,c1])
  
g p1 p2 = (a,b)
 where
  (a,b,_) = game p1 p2 []
 
 
infix 0 >>>
(>>>) :: a -> String -> a
(>>>) a str = (trace str a)
debugged :: Show a => a -> a
debugged a = (trace (">>>"++show(a)) a)