def isleap(y):
    if (y%4 == 0) or ((y%100 == 0) and (y%400 == 0)):
        return(True)
    else:
        return (False)
    
def prevmon(y,m):
    days = 0
    if isleap(y):
        x = [31,29,31,30,31,30,31,31,30,31,30,31]
    else:
        x = [31,28,31,30,31,30,31,31,30,31,30,31]
    for i in range(m-1):
        days += x[i]
    return days

def numday(y,m,d):
    day = prevmon(y,m) + d
    return day

dia,mes,ano = map(int,input("Para saber qual o dia do ano digite a data (dd mm aaaa): ").split())
day = numday(ano,mes,dia)
print(f"{dia}/{mes}/{ano} é o dia {day} do ano.")
