# От конзолата се четат 3 реда:
# 1.	Депозирана сума – реално число в интервала [100.00 … 10000.00]
# 2.	Срок на депозита (в месеци) – цяло число в интервала [1…12]
# 3.	Годишен лихвен процент – реално число в интервала [0.00 …100.00]
#
# сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)

deposit_amount = float(input())
term = int(input())
annual_interest_percentage = float(input())/100

final_amount = deposit_amount + term * ((deposit_amount * annual_interest_percentage) / 12)

print(final_amount)
