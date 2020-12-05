banknotes = [10, 20, 50, 100, 200, 500, 1000]
amount = int(input("Please enter the amount: "))
limit = 10
final_banknote = False

for index, nominal in enumerate(banknotes):
 
 current_limit = limit
 test_sum = current_limit * nominal

 if(test_sum <= amount) and (index + 1) < len(banknotes):
  while ((amount - test_sum) % banknotes[index + 1]):
   test_sum = test_sum - nominal
   current_limit -= 1
  amount -= test_sum
  print(" Take ", current_limit, " of ", nominal)
  if amount == 0:
   break
 else:
  current_limit = amount // nominal
  if not (amount % nominal):
   print(" Take ", current_limit, " of ", nominal)
   break