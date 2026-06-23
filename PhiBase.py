import math

PHI = (1 + math.sqrt(5)) / 2 # Константа ФИ


class PhiBase:
    def __init__(self, x):

        s = str(x)
        allowed = '01.'  # разрешённые цифры (0, 1) и точка

        if all(ch in allowed for ch in s):

            if s.count('.') > 1:
                raise TypeError("Число может содержать только одну точку")
            
            no_dot = s.replace('.', '')

            if "11" not in no_dot:
                self.x = s
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
    res = 0.0

    if "." in s:
        whole = s.split(".")[0]
        fraction = s.split(".")[1]
    else:
        whole = s
        fraction = ""

    for i, w in enumerate(reversed(whole)):
        res += int(w)*phi_to_power_n(i)

    for i, f in enumerate(fraction, 1):
        res += int(f)*phi_to_power_n(-1*i)

    return res
    

def transfer_int_to_Phi(x: float) -> PhiBase:
    
    if x == 0:
        return PhiBase("0")

    n = 0
    while PHI ** (n + 1) <= x + 1e-12:
        n += 1

    pos_w = []
    pos_f = []
    s = x

    while s > 1e-9:
            
        while PHI**n > s + 1e-9:
            n -= 1
                
        if n >= 0:
            pos_w.append(n)
        else:
            pos_f.append(n)
                
        s -= PHI**n

    if pos_w:
        max_w = max(pos_w)  
        w = ["0"] * (max_w + 1)
        for p in pos_w:
            w[max_w - p] = "1"
    else:
        w = []

    if pos_f:
        min_f = min(pos_f)
        f = ["0"] * (-min_f)
        for p in pos_f:
            f[-p - 1] = "1"
    else:
        f = []
    

    if not f:
        phi_s = "".join(w)
    else:
        phi_s = "".join(w) + "." + "".join(f)


    while "11" in phi_s.replace('.', ''):
        if "011" in phi_s:
            phi_s = phi_s.replace("011", "100")

        if phi_s.startswith("11"):
            phi_s = "100" + phi_s[2:]

        if ".11" in phi_s:
            phi_s = phi_s.replace(".11", "1.00")

        else:
            break 

    return PhiBase(phi_s)
        
    
