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
        x = str(self.x)
        y = str(other.x)

        sum = ""

        if "." in x:
            whole_x = x.split(".")[0]
            fraction_x = x.split(".")[1]
        else:
            whole_x = x
            fraction_x = ""

        if "." in y:
            whole_y = y.split(".")[0]
            fraction_y = y.split(".")[1]
        else:
            whole_y = y
            fraction_y = ""
        
        if len(whole_x) > len(whole_y):
            whole_y = "0"*(len(whole_x) - len(whole_y)) + whole_y
        else:
            whole_x = "0"*(len(whole_y) - len(whole_x)) + whole_x

        if len(fraction_x) > len(fraction_y):
            fraction_y = fraction_y + "0"*(len(fraction_x) - len(fraction_y))
        else:
            fraction_x = fraction_x + "0"*(len(fraction_y) - len(fraction_x))
        
        x = whole_x + fraction_x
        y = whole_y + fraction_y

        result = []
        for i in range(len(x) - 1, -1, -1):
            d_sum = int(x[i]) + int(y[i])
            result.append(str(d_sum))

        res = "".join(reversed(result))

        point = len(whole_x)
        result_str = res[:-point] + "." + res[-point:]
        
        result_str = PhiBase.normalization(result_str)

        return PhiBase(result_str)

    # Вычитание чисел в фи-еричной системе счисления
    def __sub__(self, other: PhiBase) -> PhiBase:
        x = self.transfer_to_number(self)
        y = self.transfer_to_number(other)

        if x > y:
            return self.transfer_to_Phi(x - y)
        
        raise ValueError("Отрицательный результат вычитания не поддержижается")

    # Умножение чисел в фи-еричной системе счисления
    def __mul__(self, other: PhiBase) -> PhiBase:
        x = self.x
        y = other.x

        if "." in x:
            whole_x = x.split(".")[0]
            fraction_x = x.split(".")[1]
        else:
            whole_x = x
            fraction_x = ""

        pos_x = []

        for i, ch in enumerate(reversed(whole_x)):
            if ch == '1':
                pos_x.append(i)

        for i, ch in enumerate(fraction_x):
            if ch == '1':
                pos_x.append(-(i + 1))
   
        if "." in y:
            whole_y = y.split(".")[0]
            fraction_y = y.split(".")[1]
        else:
            whole_y = y
            fraction_y = ""

        pos_y = []

        for i, ch in enumerate(reversed(whole_y)):
            if ch == '1':
                pos_y.append(i)
    
        for i, ch in enumerate(fraction_y):
            if ch == '1':
                pos_y.append(-(i + 1))

        coeff = {}
        for p_x in pos_x:
            for p_y in pos_y:
                d = p_x + p_y
                coeff[d] = coeff.get(d, 0) + 1

        if not coeff:
            return PhiBase("0")

        min_deg = min(coeff.keys())
        max_deg = max(coeff.keys())


        digits = []
        for deg in range(max_deg, min_deg - 1, -1):
            digits.append(str(coeff.get(deg, 0)))

        point = max_deg + 1

        if point < 0:
            point = 0
        if point > len(digits):
            point = len(digits)

        res = ''.join(digits[:point]) + '.' + ''.join(digits[point:])

        res = PhiBase.normalization(res)

        return PhiBase(res)

            
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
        while "11" in s.replace('.', '') or "2" in s or "3" in s or "4" in s or "5" in s or "6" in s or "7" in s or "8" in s or "9" in s:
            
            if "9" in s:
                s = s.replace("9", "1101")
            if "8" in s:
                s = s.replace("8", "1100")
            if "7" in s:
                s = s.replace("7", "1011")
            if "6" in s:
                s = s.replace("6", "1010")
            if "5" in s:
                s = s.replace("5", "1001")
            if "4" in s:
                s = s.replace("4", "1000")
            if "3" in s:
                s = s.replace("3", "101")
            if "2" in s:
                s = s.replace("2", "100")
            if "011" in s:
                s = s.replace("011", "100")
            if s[:2] == "11":
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
        if s[:1] == ".":
            s = '0' + s
        if s[-1:] == '.':
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