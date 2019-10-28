"""Case-study #3 Investment report
Developers:
Silkachev (35%), Vinnikov (45%), Popov (28%).

"""
import local as lc
month = 0
years = int(input(lc.years_capital))
initial_capital = float(input(lc.initial_capital))
percent = float(input(lc.rate))
investment_infusion = float(input(lc.additive))
sum_ = (percent / 100) * initial_capital
for year in range(1, years + 1):
    print(year, lc.year)
    print("-----------------------------------------------------")
    print(lc.first_str)
    print(lc.second_str)
    print("-----------------------------------------------------")
    c = initial_capital + sum_
    for month in range(1, 13):
        print("|   {0:2}   | {1:10.2f}   |   {2:8.2f}  | {3:10.2f}  |".format(month, initial_capital, sum_, c))
        initial_capital += (sum_ + investment_infusion)
        sum_ = (initial_capital / 100) * percent
        c = initial_capital + sum_
    print("-----------------------------------------------------")
