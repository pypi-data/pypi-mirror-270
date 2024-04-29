from enum import Enum
from dataclasses import dataclass
from typing import Any

    

class Unit:
    def __init__(self):
        pass
    
    def __mul__(self, other):
        if self == BaseUnit.unitless:
            return other
        else:
            raise NotImplementedError("Multiplication of units is not yet implemented")
    
    
class BaseUnit(Enum):
    unitless = ""
    s = "s"
    kg = "kg"
    m = "m"
    A = "A"
    K = "K"
    mol = "mol"
    cd = "cd"
    
@dataclass
class ScaledUnit:
    name: str
    base_unit: BaseUnit
    factor: float

@dataclass
class Quantity:
    value: Any
    unit: Unit
    
    # Overload multiplication for LHS and RHS multiplication
    def __mul__(self, other):
        if isinstance(other, Quantity):
            return Quantity(self.value * other.value, self.unit * other.unit)
        elif isinstance(other, (int, float)):
            return Quantity(self.value * other, self.unit)
        else:
            raise NotImplementedError("Unsupported operation")

    def __rmul__(self, other):
        return self.__mul__(other)
    
    # Overload comparison for equality
    def __eq__(self, other: Any):
        print(self, other)
        if self.unit == BaseUnit.unitless:
            return self.value == other
        elif isinstance(other, Quantity):
            return self.value == other.value and self.unit == other.unit
        else:
            return False
        
    def to(self, target):
        if isinstance(self.unit, ScaledUnit) and isinstance(target, Quantity) and isinstance(target.unit, BaseUnit) and self.unit.base_unit == target.unit:
            return Quantity(self.value * self.unit.factor, target.unit)
        else:
            raise NotImplementedError("Conversion to unit is not yet implemented")
