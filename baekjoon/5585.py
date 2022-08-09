# https://www.acmicpc.net/problem/5585
# 거스름돈

import sys

pay = int(sys.stdin.readline().strip())
charge = 1000-pay
charge_money = [500, 100, 50, 10, 5, 1]

remain_charge_moeny = charge
count = 0
for cm in charge_money:
    count += remain_charge_moeny//cm
    remain_charge_moeny -= (remain_charge_moeny//cm * cm)
    
print(count)