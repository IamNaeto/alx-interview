#!/usr/bin/python3 
 """ 
    method that determines if all the boxes can be opened 
    if an n number of locked boxes, Each box numbered sequentially 
    0 to n - 1 and each box may contain keys to the other boxes. 
 """ 
  
  
 def canUnlockAll(boxes): 
     """ 
         Parameter: boxes 
         Return: True or False 
     """ 
     if not boxes or type(boxes) is not list: 
         return False 
     unlocked = [0] 
     for x in unlocked: 
         for y in boxes[x]: 
             if y not in unlocked and y < len(boxes): 
                 unlocked.append(y) 
     if len(unlocked) == len(boxes): 
         return True 
     return False
