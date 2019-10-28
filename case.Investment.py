"""Case-study #3 Investment report
Developers:
Silkachev (35%), Vinnikov (45%), Popov (35%).

"""
month = 0
years = int(input("Срок размещения капитала (лет):"))
initial_capital = float(input("Начальный капитал ($):"))
percent = float(input("Процентная ставка (%/мес.):"))
investment_infusion = float(input("Инвестиционные вливания ($/мес.):"))
sum_ = (percent / 100) * initial_capital
for year in range(1, years + 1):
    print(year, "год")
    print("-----------------------------------------------------")
    print("|         |    основа    |   сумма %    |           |")
    print("|  месяц  |  инвестиций  |   за месяц   |  капитал  |")
    print("-----------------------------------------------------")
    c = initial_capital + sum_
    for month in range(1, 13):
        print("|   {0:2}   | {1:10.2f}   |   {2:8.2f}  | {3:10.2f}  |".format(month, initial_capital, sum_, c))
        initial_capital += (sum_ + investment_infusion)
        sum_ = (initial_capital / 100) * percent
        c = initial_capital + sum_
    print("-----------------------------------------------------")
