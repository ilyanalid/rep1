import cmath
import math

class MyMath:  #инкапсуляция
    pi = math.pi
    _complex = False

    @classmethod
    def name(cls):
        return cls.__name__

    @staticmethod
    def sin(x):
        return math.sin(x)

    @classmethod
    def complex(cls):
        return cls._complex

    @classmethod
    def sqrt(cls, x):
        if cls.complex(): #полиморфизм
            result = cmath.sqrt(x)
            return result.real, result.imag
        else:
            if x < 0:
                raise ValueError("Нет корня из отрицательного числа!")
            else:
                return math.sqrt(x)

class MyComplexMath(MyMath): #наследование
    _complex = True
