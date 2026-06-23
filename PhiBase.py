import math

PHI = (1 + math.sqrt(5)) / 2 # Константа ФИ


class PhiBase:
    def __init__(self, x):

        allowed = '01.'  # разрешённые цифры (0, 1) и точка
        if all(ch in allowed for ch in str(x)):

            if str(x).count('.') > 1:
                raise TypeError("Число может содержать только одну точку")
            
            no_dot = str(x).replace('.', '')

            if "11" not in x:
                self.x = x
            else:
                raise TypeError("Число в фи-еричной системе счисления не может содержать 11")
            
        else:
            raise TypeError("Число в фи-еричной системе счисления содержит только 0 и 1 и точку")

# Возведение числа ФИ в любую степень
def phi_to_power_n(n: int) -> float:

    if n == 0:
        return 1.0
    if n == 1:
        return PHI
    if n > 0:
        return phi_to_power_n(n - 1) + phi_to_power_n(n - 2)  
    if n < 0:
        return phi_to_power_n(n + 2) - phi_to_power_n(n + 1) 

# Перевод из Фи-еричной системы счисления в 10-тичную
def transfer_to_int(x: PhiBase) -> float:

    s = x.x
    sum = 0.0

    if "." in x:
        whole = s.split(",")[0]
        fraction = s.split(",")[1]
    else:
        whole = s
        fraction = ""

    for i, w in enumerate(reversed(whole), len(whole)):
        sum += int(w)*phi_to_power_n(i)

    for i, f in enumerate(fraction, 1):
        sum += int(f)*phi_to_power_n(-1*i)

    return sum
    



