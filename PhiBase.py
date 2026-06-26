from fractions import Fraction
from PhiNumber import _PhiNumber

PHI = _PhiNumber.phi()

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
        x = self.transfer_to_number(self)
        y = self.transfer_to_number(other)
        return self.transfer_to_Phi(x + y)

    # Вычитание чисел в фи-еричной системе счисления
    def __sub__(self, other: PhiBase) -> PhiBase:
        x = self.transfer_to_number(self)
        y = self.transfer_to_number(other)
        if (x > y):
            return self.transfer_to_Phi(x - y)
        else:
            raise ValueError("Отрицательный результат вычитания не поддерживается")

    # Умножение чисел в фи-еричной системе счисления
    def __mul__(self, other: PhiBase) -> PhiBase:
        x = self.transfer_to_number(self)
        y = self.transfer_to_number(other)
        return self.transfer_to_Phi(x * y)

            
    # Возведение числа ФИ в любую степень
    @staticmethod
    def phi_to_power_n(n: int) -> _PhiNumber:

        if n == 0:
            return _PhiNumber(1, 0)
        if n == 1:
            return PHI
        if n > 0:
            a, b = _PhiNumber(1, 0), PHI
            for i in range(2, n + 1):
                a, b = b, a + b
            return b
        if n < 0:
            a, b =  PHI, _PhiNumber(1, 0)
            for i in range(0, -n):
                a, b = b, a - b
            return b


    # Перевод из Фи-еричной системы счисления в 10-тичную
    @staticmethod
    def transfer_to_number(x: PhiBase) -> _PhiNumber:

        s = x.x
        res = _PhiNumber(0, 0)

        if "." in s:
            whole = s.split(".")[0]
            fraction = s.split(".")[1]
        else:
            whole = s
            fraction = ""

        for i, w in enumerate(reversed(whole)):
            res += _PhiNumber(int(w), 0) * PhiBase.phi_to_power_n(i)

        for i, f in enumerate(fraction, 1):
            res += _PhiNumber(int(f), 0) * PhiBase.phi_to_power_n(-i)

        return res
    
    # Нормализиция числа в Фи-еричной системы счисления в 10-тичную
    @staticmethod
    def normalization(x: str) -> str:
        s = x
        while "11" in s.replace('.', ''):

            if "011" in s:
                s = s.replace("011", "100")

            if (s[:2] == "11"):
                s = "100" + s[2:]

            if ".11" in s:
                s = s.replace(".11", "1.00")

            if "01.1" in s:
                s = s.replace("01.1", "10.0")

            if "0110" in s:
                s = s.replace("0110", "1000")

            if "01.10" in s:
                s = s.replace("01.10", "10.00")

        s = s.lstrip('0')
        if s.startswith('.'):
            s = '0' + s
        if s.endswith('.'):
            s = s[:-1]

        return s

    @staticmethod
    def transfer_to_Phi(x) -> PhiBase:

        if not isinstance(x, _PhiNumber):
            x = _PhiNumber(x, 0)

        if x == _PhiNumber(0, 0):
            return PhiBase("0")

        n = 0
        while PhiBase.phi_to_power_n(n + 1) <= x:
            n += 1

        pos_w = []
        pos_f = []
        s = x
        max_fr = 20

        while s > _PhiNumber(0, 0) and max_fr >= 0:
            while PhiBase.phi_to_power_n(n) > s and max_fr >= 0:
                n -= 1

            if n >= 0:
                pos_w.append(n)
            else:
                pos_f.append(n)
                max_fr -= 1

            s -= PhiBase.phi_to_power_n(n)

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