#count = 0
#for number in range(1,101):
  # if number % 3 == 0:
  #  print(number ,end= " ")
 #    count=count+1
#print(f"we have {count}numbers divisible by 3 from 1 t0 100")

count = 0
for number in range (3,101,3):
  count = count+1
  print(number , end= ",")
print(f"\n\nwe have to {count} numbers divisible by 3 from 1 to 100")