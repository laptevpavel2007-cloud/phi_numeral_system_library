import math

PHI = (1 + math.sqrt(5)) / 2 # Константа ФИ

# Класс числа в фи-еричной системе счисления
class PhiBase:

    # Инициализация числа в фи-еричной системе счисления
    def __init__(self, x):

        s = str(x)

        true_symbols = '01.'  # разрешённые цифры (0, 1) и точка

        for i in range(len(s)):
            if s[i] not in true_symbols:
                raise TypeError("Число в фи-еричной системе счисления содержит только 0 и 1 и точку")

        if s.count('.') > 1:
            raise TypeError("Число может содержать только одну точку")
            
        no_dot = s.replace('.', '')

        if "11" not in no_dot:
            self.x = s
        else:
            raise TypeError("Число в фи-еричной системе счисления не может содержать 11")
    
    # Вывод числа в фи-еричной системе счисления
    def __str__(self):
        return self.x
    
    # Сумма чисел в фи-еричной системе счисления
    def __add__(self, other: PhiBase) -> PhiBase:
        x = self.transfer_to_int(self)
        y = self.transfer_to_int(other)
        return self.transfer_int_to_Phi(x + y)

    # Вычитание чисел в фи-еричной системе счисления
    def __sub__(self, other: PhiBase) -> PhiBase:
        x = self.transfer_to_int(self)
        y = self.transfer_to_int(other)
        if (x - y >= 0):
            return self.transfer_int_to_Phi(x + (-y))
        else:
            raise ValueError("Отрицательный результат вычитания не поддерживается")

    # Умножение чисел в фи-еричной системе счисления
    def __mul__(self, other: PhiBase) -> PhiBase:
        x = self.transfer_to_int(self)
        y = self.transfer_to_int(other)
        return self.transfer_int_to_Phi(x * y)

            
    # Возведение числа ФИ в любую степень
    @staticmethod
    def phi_to_power_n(n: int) -> float:

        if n == 0:
            return 1.0
        if n == 1:
            return PHI
        if n > 0:
            return PhiBase.phi_to_power_n(n - 1) + PhiBase.phi_to_power_n(n - 2)  
        if n < 0:
            return PhiBase.phi_to_power_n(n + 2) - PhiBase.phi_to_power_n(n + 1) 


    # Перевод из Фи-еричной системы счисления в 10-тичную
    @staticmethod
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
            res += int(w) * PhiBase.phi_to_power_n(i)

        for i, f in enumerate(fraction, 1):
            res += int(f) * PhiBase.phi_to_power_n(-i)

        return res
    
    # Нормализиция числа в Фи-еричной системы счисления в 10-тичную
    @staticmethod
    def normalization(x: str) -> PhiBase:
        while "11" in x.replace('.', ''):
            if "011" in x:
                x = x.replace("011", "100")

            if x.startswith("11"):
                x = "100" + x[2:]

            if ".11" in x:
                x = x.replace(".11", "1.00")

            else:
                break 

        return x

    @staticmethod
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
                
            while PHI ** n > s + 1e-9:
                n -= 1
                    
            if n >= 0:
                pos_w.append(n)
            else:
                pos_f.append(n)
                    
            s -= PHI**n


        if len(pos_w) > 0:
            max_w = max(pos_w)  
            w = ["0"] * (max_w + 1)

            for p in pos_w:
                w[max_w - p] = "1"
        else:
            w = []

        if len(pos_f) > 0:
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


        phi_s = PhiBase.normalization(phi_s)

        return PhiBase(phi_s)

print(PhiBase.transfer_int_to_Phi(1984))
print(PhiBase.transfer_to_int(PhiBase.transfer_int_to_Phi(1984)))