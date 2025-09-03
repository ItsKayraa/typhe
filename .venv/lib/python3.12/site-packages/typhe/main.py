__all__ = [
    'usbit_sinfo', 'sbit_sinfo',
    'usinfo8', 'sinfo8', 'usinfo16', 'sinfo16', 'usinfo32', 'sinfo32', 'usinfo64', 'sinfo64',
    'mint', 'mstr',
    'uint8', 'sint8', 'uint16', 'sint16', 'uint32', 'sint32', 'uint64', 'sint64', 'char',
    'struct'
]

def usbit_sinfo(bits: int):
    unsigned_min = 0
    unsigned_max = (2 ** bits) - 1
    return unsigned_min, unsigned_max

def sbit_sinfo(bits: int):
    signed_min = -(2 ** (bits - 1))
    signed_max = (2 ** (bits - 1)) - 1
    return signed_min, signed_max

usinfo8  = usbit_sinfo(8)
sinfo8   = sbit_sinfo(8)
usinfo16 = usbit_sinfo(16)
sinfo16  = sbit_sinfo(16)
usinfo32 = usbit_sinfo(32)
sinfo32  = sbit_sinfo(32)
usinfo64 = usbit_sinfo(64)
sinfo64  = sbit_sinfo(64)


class mint:
    def __init__(self, value: int, _min: int, _max: int, description: str):
        value = int(value)
        if not (_min <= value <= _max):
            raise ValueError(f"Value {value} out of range [{_min}, {_max}] for {description}.")
        self.value = value
        self.min = _min
        self.max = _max
        self.description = description

    # yardımcı: diğer operand'ı int'e çevir
    def _coerce(self, other):
        if isinstance(other, mint):
            return other.value
        if isinstance(other, int):
            return other
        # eğer diğer tür destekleniyorsa ekle (ör. bool is int subclass zaten)
        raise TypeError(f"Unsupported operand type: {type(other)}")

    def __int__(self):
        return int(self.value)

    def __index__(self):
        return int(self.value)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.value})"

    def __str__(self):
        return str(self.value)

    # Arithmetic
    def __add__(self, other):
        other_v = self._coerce(other)
        result = self.value + other_v
        if not (self.min <= result <= self.max):
            raise ValueError(f"Result {result} out of range for {self.description}.")
        return self.__class__(result)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        other_v = self._coerce(other)
        result = self.value - other_v
        if not (self.min <= result <= self.max):
            raise ValueError(f"Result {result} out of range for {self.description}.")
        return self.__class__(result)

    def __rsub__(self, other):
        other_v = self._coerce(other)
        result = other_v - self.value
        if not (self.min <= result <= self.max):
            raise ValueError(f"Result {result} out of range for {self.description}.")
        return self.__class__(result)

    def __mul__(self, other):
        other_v = self._coerce(other)
        result = self.value * other_v
        if not (self.min <= result <= self.max):
            raise ValueError(f"Result {result} out of range for {self.description}.")
        return self.__class__(result)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __floordiv__(self, other):
        other_v = self._coerce(other)
        if other_v == 0:
            raise ZeroDivisionError
        result = self.value // other_v
        if not (self.min <= result <= self.max):
            raise ValueError(f"Result {result} out of range for {self.description}.")
        return self.__class__(result)

    def __truediv__(self, other):
        # eğer tam sayı bekliyorsan floordiv kullan; burada int sonucu döndürüyoruz
        other_v = self._coerce(other)
        if other_v == 0:
            raise ZeroDivisionError
        result = self.value // other_v
        if not (self.min <= result <= self.max):
            raise ValueError(f"Result {result} out of range for {self.description}.")
        return self.__class__(result)

    # bitwise or
    def __or__(self, other):
        other_v = self._coerce(other)
        result = self.value | other_v
        if not (self.min <= result <= self.max):
            raise ValueError(f"Result {result} out of range for {self.description}.")
        return self.__class__(result)

    def __ror__(self, other):
        return self.__or__(other)


class mstr:
    def __init__(self, value: str, _min: int, _max: int, description: str):
        if not isinstance(value, str):
            raise TypeError("mstr requires a string value")
        l = len(value)
        if not (_min <= l <= _max):
            raise ValueError(f"String length {l} out of range [{_min}, {_max}] for {description}.")
        self.value = value
        self.min = _min
        self.max = _max
        self.description = description

    def __add__(self, other: str):
        if not isinstance(other, str):
            raise TypeError("Can only concatenate str to mstr")
        result = self.value + other
        l = len(result)
        if not (self.min <= l <= self.max):
            raise ValueError(f"Result length {l} out of range for {self.description}.")
        return self.__class__(result)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.value!r})"

    def __str__(self):
        return self.value

    def __or__(self, other):
        raise TypeError("Unsupported operation '|' for mstr")


class uint8(mint):
    def __init__(self, value):
        super().__init__(int(value), usinfo8[0], usinfo8[1], "unsigned int 8")

class sint8(mint):
    def __init__(self, value):
        super().__init__(int(value), sinfo8[0], sinfo8[1], "signed int 8")

class uint16(mint):
    def __init__(self, value):
        super().__init__(int(value), usinfo16[0], usinfo16[1], "unsigned int 16")

class sint16(mint):
    def __init__(self, value):
        super().__init__(int(value), sinfo16[0], sinfo16[1], "signed int 16")

class uint32(mint):
    def __init__(self, value):
        super().__init__(int(value), usinfo32[0], usinfo32[1], "unsigned int 32")

class sint32(mint):
    def __init__(self, value):
        super().__init__(int(value), sinfo32[0], sinfo32[1], "signed int 32")

class uint64(mint):
    def __init__(self, value):
        super().__init__(int(value), usinfo64[0], usinfo64[1], "unsigned int 64")

class sint64(mint):
    def __init__(self, value):
        super().__init__(int(value), sinfo64[0], sinfo64[1], "signed int 64")

class char(mstr):
    def __init__(self, value):
        super().__init__(value, 0, 1, "char")

class struct:
    def __init__(self, items: dict):
        super().__setattr__('items', items)
        super().__setattr__('value', {k: None for k in items.keys()})

    def __repr__(self):
        return f"{self.__class__.__name__}({self.value})"

    def __setattr__(self, name, val):
        # iç alanlara normal atama
        if name in ('items', 'value'):
            super().__setattr__(name, val)
            return

        if name in self.items:
            expected = self.items[name]
            if isinstance(expected, type):
                if issubclass(expected, mint):
                    if isinstance(val, expected):
                        coerced = val
                    elif isinstance(val, int):
                        coerced = expected(val)
                    else:
                        raise TypeError(f"Field '{name}' expects {expected}, got {type(val)}")
                else:
                    if not isinstance(val, expected):
                        raise TypeError(f"Field '{name}' expects {expected}, got {type(val)}")
                    coerced = val
            else:
                if not isinstance(val, expected):
                    raise TypeError(f"Field '{name}' expects {expected}, got {type(val)}")
                coerced = val

            self.value[name] = coerced
            return

        super().__setattr__(name, val)

    def __getattr__(self, name):
        if name in self.items:
            return self.value.get(name)
        raise AttributeError(f"{self.__class__.__name__} has no attribute {name!r}")

    def __call__(self, **kwds):
        for k, v in kwds.items():
            if k not in self.items:
                raise ValueError(f"Unknown field for struct: {k}")
            setattr(self, k, v)