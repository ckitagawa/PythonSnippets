import random
import matplotlib
import matplotlib.pyplot as plt
import time


def rollDice():
  roll = random.randint(1,100)

  if roll == 100 or roll <= 50:
    return False
  else:
    return True

def bettor(funds, init_wager, wager_number, double_up, color=None):
  funds_arr = [funds]
  wager_num = [0]
  init_wager_storage = init_wager
  for i in range(wager_number):
    if rollDice():
      funds_arr.append(funds_arr[i]+init_wager)
      wager_num.append(i)
      if double_up:
        init_wager = init_wager_storage
        if (funds_arr[i+1] - init_wager) < 0:
          init_wager = funds_arr[i+1]
    else:
      funds_arr.append(funds_arr[i]-init_wager)
      wager_num.append(i)
      if double_up:
        init_wager = init_wager * 2
        if (funds_arr[i+1]- init_wager) < 0:
          init_wager = funds_arr[i+1]
    if funds_arr[i+1] <= 0:
      if color == None:
        plt.plot(wager_num,funds_arr,'r')
      else:
        plt.plot(wager_num,funds_arr,color)
      return funds_arr[i+1]
  if color == None:
    if funds_arr[0] > funds_arr[i]:
      plt.plot(wager_num,funds_arr,'y')
    else:
      plt.plot(wager_num,funds_arr,'g')
  else:
    plt.plot(wager_num,funds_arr,color)
  return funds_arr[i]


# for j in [True, False]:
#   earned = 0
#   broke = 0
#   init_funds = 10000
#   indivs = 10000
#   if j:
#     color = 'k'
#   else:
#     color = 'c'
#   for i in range(indivs):
#     final_funds = bettor(init_funds,100,100,j,color)
#     if final_funds >= init_funds:
#       earned += 1
#     elif final_funds <= 0:
#       broke += 1
#   if j:
#     print('Doubler Odds:')
#   else:
#     print('Simple Odds:')
#   print('In the positive: ', earned, ' or ', earned/indivs * 100, '%')
#   print('Broke individuals: ', broke, ' or ', broke/indivs * 100, '%')
#   print('In debt: ', indivs - broke - earned, ' or ', (indivs - broke - earned)/indivs * 100, '%')

# plt.ylabel('Account Value')
# plt.xlabel('Wager Count')
# plt.axhline(0, color = 'r')
# plt.show()



#Single Case:
#bettor(init_funds,100,100,True)
#plt.show()
