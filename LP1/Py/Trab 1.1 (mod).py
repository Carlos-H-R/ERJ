import calendar

def prevmon(y,m):
    days = 0
    for i in range(1,m):
        x = calendar.monthrange(y,i)
        days += x[1]
    return days

def yearday(y,m,d):
    day = prevmon(y,m) + d
    return day

dia,mes,ano = map(int,input('Para saber qual o dia do ano, digite a data (dd mm aaaa): ').split())
dn = yearday(ano,mes,dia)
print(f'{dia}/{mes}/{ano} é o dia {dn} do ano')
