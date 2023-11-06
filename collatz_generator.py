from bitarray import bitarray, decodetree
from bitarray.util import ba2int

class CollatzMember():
    __value = None
    __bit_array = None
    __one_child = None
    __zero_child = None
    __parent = None
    __distance = 0
    __D = decodetree({'0': bitarray('0'), '1': bitarray('1')})

    def __init__(self, value, distance = 0, bit_array = bitarray(''), one_child = None, zero_child = None, parent = None) -> None:
        self.__value = value
        self.__bit_array = bit_array
        self.__one_child = one_child
        self.__zero_child = zero_child
        self.__parent = parent
        self.__distance = distance

    #--Getters and setters for __value
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        if type(value) is not int:
            raise TypeError("value must be type int")
        self.__value = value

    #--Getters and setters for __distance
    @property
    def distance(self):
        return self.__distance
    
    @distance.setter
    def distance(self, value):
        if type(value) is not int:
            raise TypeError("value must be type int")
        self.__distance = value

    #--Getters and setters for __bit_array
    @property
    def bit_array(self):
        return ''.join(bitarray(self.__bit_array).decode(CollatzMember.__D))
    
    def get_bit_array_as_int(self):
        return ba2int(self.__bit_array)
    
    def get_bit_array_as_bitarray(self):
        return self.__bit_array

    @bit_array.setter
    def bit_array(self, value):
        if type(value) is str:
            self.__bit_array = bitarray(value)
        elif type(value) is bitarray:
            self.__bit_array = value
        else:
            raise TypeError("value must be type bitarray or str")
    
    #--Getters and setters for __one_child
    @property
    def one_child(self):
        return self.__one_child
    
    @one_child.setter
    def one_child(self, value):
        if type(value) is not CollatzMember:
            raise TypeError("value must be type CollatzMember")
        self.__one_child = value

    #--Getters and setters for __zero_child
    @property
    def zero_child(self):
        return self.__zero_child
    
    @zero_child.setter
    def zero_child(self, value):
        if type(value) is not CollatzMember:
            raise TypeError("value must be type CollatzMember")
        self.__zero_child = value

    #--Getters and setters for __parent
    @property
    def parent(self):
        return self.__parent
    
    @parent.setter
    def parent(self, value):
        if type(value) is not CollatzMember:
            raise TypeError("value must be type CollatzMember")
        self.__parent = value

    def __str__(self) -> str:
        return("CollatzMember:\n"
               f"\tValue: {self.__value}\n"
               f"\tDistance: {self.__distance}\n"
               f"\tBitarray: {''.join(self.bit_array)}\n"
               f"\tOne Child: {self.__one_child.value if self.__one_child is not None else None}\n"
               f"\tZero Child: {self.__zero_child.value if self.__zero_child is not None else None}\n"
               f"\tParent: {self.__parent.value if self.__parent is not None else None}\n")

    def __repr__(self) -> str:
        return(f"CollatzMember({self.__value}, {self.__bit_array}, {self.__one_child}, {self.__zero_child}, {self.__parent})")
    

class CollatzGenerator():
    __values = {1}
    __distance = 0
    __allow_repeats = False
    __shortcut = False
    __first_member = CollatzMember(1)

    def __init__(self, distance, shortcut = False, allow_repeats = False) -> None:
        self.__distance = distance
        self.__allow_repeats = allow_repeats
        self.__shortcut = shortcut

    def generate(self):
        print(self.__first_member)
        self.__add_children(self.__first_member)

    def __add_children(self, parent):
        if not parent.distance < self.__distance:
            return
        
        z_possible = parent.value * 2
        o_possible = (parent.value - 1) / 3
        if z_possible not in self.__values:
            self.__values.add(z_possible)
            zero_mem = CollatzMember(z_possible, parent.distance + 1,  '0'.join(parent.bit_array), parent=parent)
            parent.zero_child = zero_mem
            print(zero_mem)
            self.__add_children(zero_mem)
        if o_possible not in self.__values and o_possible % 2 == 1:
            self.__values.add(o_possible)
            one_mem = CollatzMember(o_possible, parent.distance + 1, '1'.join(parent.bit_array), parent=parent)
            parent.one_child = one_mem
            print(one_mem)
            self.__add_children(one_mem)