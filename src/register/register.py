# Define registradores e suas operações
REGISTER_SIZE = 2 # Tamanho de uma WORDs

SP = [None for i in range(0, REGISTER_SIZE)]
PC = [None for i in range(0, REGISTER_SIZE)]
AX = [None for i in range(0, 8*REGISTER_SIZE)] # A0 to A7
DX = [None for i in range(0, 8*REGISTER_SIZE)] # D0 to D7
SR = [None] # SR tem só um byte

def read_byte(register):
    if register == SR:
        return register[0]
    elif list(register)[0] == "A" or list(register)[0] == "D":
        if list(register)[0] == "A":
            return AX[(int(list(register)[1])*2)+1]
        else:
            return DX[(int(list(register)[1])*2)+1]
    else:
        return register[1] # Lê o menos significativo, que é o segundo byte na ordem


def print_byte(register):
    if register == SR:
        print(register[0])
    elif list(register)[0] == "A" or list(register)[0] == "D":
        if list(register)[0] == "A":
            print(AX[(int(list(register)[1])*2 + 1)])
        else:
            print(DX[(int(list(register)[1])*2 + 1)])
    else:
        print(register[1]) # Lê o menos significativo, que é o segundo byte na ordem


def write_byte(value, register):
    if register == SR:
        register[0] = hex(value)
    elif list(register)[0] == "A" or list(register)[0] == "D":
        if list(register)[0] == "A":
            AX[(int(list(register)[1])*2 + 1)] = hex(value)
        else:
            DX[(int(list(register)[1])*2 + 1)] = hex(value)
    else:
        register[1] = hex(value)

def read_word(register):
    if register == SR:
        return register[0]
    elif list(register)[0] == "A" or list(register)[0] == "D":
        if list(register)[0] == "A":
            return str((AX[(int(list(register)[1])*2)])) + str((AX[(int(list(register)[1])*2)+1])[2:]) 
        else:
            return str((DX[(int(list(register)[1])*2)])) + str((DX[(int(list(register)[1])*2)+1])[2:]) 
    else:
        return (str(register[0]) + str((register[1])[2:])) 


def print_word(register):
    if register == SR:
        print(register[0])
    elif list(register)[0] == "A" or list(register)[0] == "D":
        if list(register)[0] == "A":
            print(str((AX[(int(list(register)[1])*2)])) + str((AX[(int(list(register)[1])*2)+1])[2:]))
        else:
            print(str((DX[(int(list(register)[1])*2)])) + str((DX[(int(list(register)[1])*2)+1])[2:]))
    else:
        print((str(register[0]) + str((register[1])[2:])))


def write_word(value, register):
    if(register == SR):
        print("THE SR REGISTER ONLY HAS ONE BIT")
    elif(value < 0x100):  # Se o byte mais significativo é 0x00
        if list(register)[0] == "A" or list(register)[0] == "D":
            if list(register)[0] == "A":
                AX[(int(list(register)[1])*2)] = hex(0)
                AX[(int(list(register)[1])*2 + 1)] = hex(value)
            else:
                DX[(int(list(register)[1])*2)] = hex(0)
                DX[(int(list(register)[1])*2 + 1)] = hex(value)
        else:
            register[0] = hex(0)
            register[1] = hex(value)
    elif(value < 0x1000):  # Se o byte mais significativo tem primeiro digito hex 0
        if list(register)[0] == "A" or list(register)[0] == "D":
            if list(register)[0] == "A":
                AX[(int(list(register)[1])*2)] = hex(int("0" + str(hex(value))[2]))
                AX[(int(list(register)[1])*2 + 1)] = hex(int(str(hex(value))[3] + str(hex(value))[4], 16))
            else:
                DX[(int(list(register)[1])*2)] = hex(int("0" + str(hex(value))[2]))
                DX[(int(list(register)[1])*2 + 1)] = hex(int(str(hex(value))[3] + str(hex(value))[4], 16))
        else:
            register[0] = hex(int("0" + str(hex(value))[2]))
            register[1] = hex(int(str(hex(value))[3] + str(hex(value))[4], 16))
    elif(value > 0xffff):
        print("THE VALUE IS BIGGER THAN A WORD")
        return 0
    else:
        if list(register)[0] == "A" or list(register)[0] == "D":
            if list(register)[0] == "A":
                AX[(int(list(register)[1])*2)] = hex(int(str(hex(value))[2] + str(hex(value))[3], 16))
                AX[(int(list(register)[1])*2 + 1)] = hex(int(str(hex(value))[4] + str(hex(value))[5], 16))
            else:
                DX[(int(list(register)[1])*2)] = hex(int(str(hex(value))[2] + str(hex(value))[3], 16))
                DX[(int(list(register)[1])*2 + 1)] = hex(int(str(hex(value))[4] + str(hex(value))[5], 16))
        else:
            register[0] = hex(int(str(hex(value))[2] + str(hex(value))[3], 16))
            register[1] = hex(int(str(hex(value))[4] + str(hex(value))[5], 16))