salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

def solve(salary, spend, increase, months):
    money_capital = 0
    for i in range(months):
        money_capital -= salary - spend
        spend += spend * increase
    return round(money_capital)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", solve(salary, spend, increase, months))
