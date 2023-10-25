class Operations :

    @classmethod
    def xor_operation(cls, a, b) :
        return a ^ b

    @classmethod
    def circular_left_shift(cls, num, shift_amount, size_of_shift_register) :
        binary_rep = "{0:0{1}b}".format(num, size_of_shift_register)
        shift_amount = shift_amount % size_of_shift_register
        ans = binary_rep[shift_amount:] + binary_rep[:shift_amount]
        return int(ans, 2)