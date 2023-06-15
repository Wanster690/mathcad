import time 
start = time.time()
def pal(mult):
    return str(mult) == str(mult)[::-1]
def cycle(max, min):
  max_pal = 0
  for i in range(max, min, -1):
    for j in range(max, min, -1):
      mult = i * j
      if pal(mult) and mult > max_pal:
        max_pal = mult
  return max_pal
  
for i in range(0, 10):
  print(cycle(999-i*100,900-i*100)," От", 999-i*100, "до", 900-i*100)
end = time.time() - start
print(end)