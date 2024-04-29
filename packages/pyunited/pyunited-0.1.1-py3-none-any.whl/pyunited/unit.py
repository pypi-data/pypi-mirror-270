from enum import Enum
from dataclasses import dataclass
from typing import Any

    

class Unit:
    def __init__(self, *args):
        pass
    
    def __mul__(self, other):
        return Quantity(1, self) * other
        
    def __rmul__(self, other):
        return self.__mul__(other)
    
    
class BaseUnit(Unit, Enum):
    unitless = ""
    s = "s"
    kg = "kg"
    m = "m"
    A = "A"
    K = "K"
    mol = "mol"
    cd = "cd"
    
@dataclass
class ScaledUnit(Unit):
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
        target_unit = None
        if hasattr(target, "unit"):
            target_unit = target.unit
        elif isinstance(target, BaseUnit) or isinstance(target, ScaledUnit):
            target_unit = target

        if self.unit == target_unit:
            return self

        if isinstance(self.unit, ScaledUnit) and self.unit.base_unit == target_unit:
            return Quantity(self.value * self.unit.factor, target_unit)
        else:
            raise NotImplementedError("Conversion to unit is not yet implemented")
