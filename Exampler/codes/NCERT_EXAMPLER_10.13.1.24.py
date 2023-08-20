import random

desired_output = 0.2


def simulate():
  list = []
  for i in range(0, 1000):
    list.append(random.randint(1, 40))
  div_5 = 0
  for i in range(0, 1000):
    if list[i] % 5 == 0:
      div_5 += 1
  prob_5 = div_5 / 1000
  return prob_5


while True:
  prob_5 = simulate()
  if prob_5 == desired_output:
    print(f"Probability of number divisible by 5 ={prob_5}")

    break
  else:
    continue

