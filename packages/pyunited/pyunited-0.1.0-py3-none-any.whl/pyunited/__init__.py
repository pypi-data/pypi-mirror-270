import typing as T
from . import unit

m = unit.Quantity(1, unit.BaseUnit.m)
mm = unit.Quantity(1, unit.ScaledUnit("mm", unit.BaseUnit.m, 1e-3))

inch  = unit.Quantity(1, unit.ScaledUnit("inch", unit.BaseUnit.m, 0.0254))

class United:
    def __new__(self, value = 1.0, unit_ = None):
        if isinstance(value, unit.Quantity):
            return value

        # Implement parsing
        if isinstance(value, str) and unit_ is None:
            value, unit_ = value.split()
            value = float(value)
            unit_ = getattr(self, unit_).unit

        if unit_ is None:
            unit_ = unit.BaseUnit.unitless

        return unit.Quantity(value, unit_)
    
def to(*args, **kwargs):
    if len(args) == 1 and isinstance(args[0], unit.Quantity):
        return lambda x: unit.Quantity(x.value, args[0].unit)
    else:
        raise NotImplementedError("Unsupported operation")

def values(united):
    if isinstance(united, unit.Quantity):
        return united.value
    elif isinstance(united, T.Iterable):
        # Check whether all units are the same
        if not all(item.unit == united[0].unit for item in united):
            raise UnityError("All units must be the same")
        return (item.value for item in united)
    else:
        raise NotImplementedError("Unsupported operation")
    
class UnityError(Exception):
    pass