# Define lista que funcionará como memória e suas operações

MEMORY_SIZE = 4095

# memory allocation starts in 0 and goes to 65562
memory = [None for i in range(0, MEMORY_SIZE)]


def read_byte(address):
    if(address < 0 or address > MEMORY_SIZE - 1):
        return "UNABLE TO ACCESS ADRESS"
    else:
        return memory[address]


def print_byte(address):
    if(address < 0 or address > MEMORY_SIZE - 1):
        print("UNABLE TO ACCESS ADRESS")
    else:
        print(memory[address])


def write_byte(value, address):
    if(address < 0 or address > MEMORY_SIZE - 1):
        print("UNABLE TO ACCESS ADRESS")
    elif(value > 0xff):
        print("THE VALUE IS BIGGER THAN A BYTE")
    else:
        memory[address] = hex(value)


def read_word(address):
    if(address < 0 or address > MEMORY_SIZE - 2):
        return "UNABLE TO ACCESS ADRESS"
    elif(str(memory[address + 1]) == "None"):
        # Concatena dois bytes, porém o segundo é None
        return (str(memory[address]) + str(memory[address + 1]))
    else:
        # Concatena dois bytes
        return (str(memory[address]) + str(memory[address + 1])[2:])


def print_word(address):
    if(address < 0 or address > MEMORY_SIZE - 2):
        print("UNABLE TO ACCESS ADRESS")
    elif(str(memory[address + 1]) == "None"):
        # Concatena dois bytes, porém o segundo é None
        print(str(memory[address]) + str(memory[address + 1]))
    else:
        # Concatena dois bytes
        print(str(memory[address]) + str(memory[address + 1])[2:])


def write_word(value, address):
    if(address < 0 or address > MEMORY_SIZE - 2):
        return "UNABLE TO ACCESS ADDRESS"
    else:
        if(value < 0x100):  # Se o byte mais significativo é 0x00
            memory[address] = hex(0x00)
            memory[address + 1] = hex(value)
        elif(value < 0x1000):  # Se o byte mais significativo tem primeiro digito hex 0
            memory[address] = hex(int("0" + str(hex(value))[2]))
            memory[address +
                   1] = hex(int(str(hex(value))[3] + str(hex(value))[4], 16))
        elif(value > 0xffff):
            print("THE VALUE IS BIGGER THAN A WORD")
            return 0
        else:
            memory[address] = hex(
                int(str(hex(value))[2] + str(hex(value))[3], 16))
            memory[address +
                   1] = hex(int(str(hex(value))[4] + str(hex(value))[5], 16))
