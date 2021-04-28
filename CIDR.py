def fillOctet(binary):
    while len(binary) < 8:
        binary = '0' + binary
    return binary


def toBinary(ip):
    ip = ip.split('.')
    binary_string = ''
    for octet in ip:
        binary_string = binary_string + \
            fillOctet(bin(int(octet)).replace("0b", ''))
    return binary_string


def toDecimal(binary):
    binary = binary.split('.')
    dotted_decimal_notation = ''
    for octet in binary:
        dotted_decimal_notation = dotted_decimal_notation + \
            '.' + str(int(octet, 2))
    return dotted_decimal_notation[1:len(dotted_decimal_notation)]


def dottedBinaryNotation(dotted_notation):
    arr = list(dotted_notation)
    dotted_notation_string = ''
    i = 1
    while i <= len(arr):
        if i % 8 == 0:
            dotted_notation_string = dotted_notation_string + arr[i-1] + '.'
        else:
            dotted_notation_string = dotted_notation_string + arr[i-1]
        i = i + 1
    return dotted_notation_string[0:35]


def getMask(mask):
    i = 0
    mask_binary_string = ''
    while i < mask:
        mask_binary_string = mask_binary_string + '1'
        i = i + 1
    while mask < 32:
        mask_binary_string = mask_binary_string + '0'
        mask = mask + 1
    return mask_binary_string


def getWildcard(binarymask):
    arr = ''
    for i in list(binarymask):
        if i == '1':
            arr = arr + '0'
        elif i == '0':
            arr = arr + '1'
    return arr


def getAvailableIps(mask):
    return pow(2, 32 - mask) - 2


def andCalculator(first_binary, second_binary):
    and_result = ''
    i = 0
    while i < len(first_binary):
        and_result = and_result + \
            str(int(first_binary[i]) and int(second_binary[i]))
        i = i + 1
    return and_result


def orCalculator(first_binary, second_binary):
    and_result = ''
    i = 0
    while i < len(first_binary):
        and_result = and_result + \
            str(int(first_binary[i]) or int(second_binary[i]))
        i = i + 1
    return and_result


def getFirstIp(decimal):
    decimal = decimal.split('.')
    decimal[3] = str(int(decimal[3]) + 1)
    return toDecimalDottedNotation(decimal)


def getLastIp(decimal):
    decimal = decimal.split('.')
    decimal[3] = str(int(decimal[3]) - 1)
    return toDecimalDottedNotation(decimal)


def toDecimalDottedNotation(decimal):
    decimal_string = ''
    i = 0
    while i < 4:
        decimal_string = decimal_string + decimal[i] + '.'
        i = i + 1
    return decimal_string[0:len(decimal_string)-1]


cidr = '192.168.40.32/24'
# str(input('Please, insert the format cidr ip: '))

# split the ip from the subnet mask
notation = cidr.split('/')

ip = notation[0]
mask = int(notation[1])

print()
print('Ip given: ', cidr)
print()
print('Ip:       ', ip, ' - ', dottedBinaryNotation(toBinary(ip)))
print('Mask:     ', toDecimal(dottedBinaryNotation(getMask(mask))),
      ' - ', dottedBinaryNotation(getMask(mask)))
print('Wildcard: ', toDecimal(dottedBinaryNotation(getWildcard(
    getMask(mask)))), ' - ', dottedBinaryNotation(getWildcard(getMask(mask))))
print('Id Net:   ', toDecimal(dottedBinaryNotation(
    andCalculator(toBinary(ip), getMask(mask)))), ' - ', dottedBinaryNotation(
    andCalculator(toBinary(ip), getMask(mask))))

print('Brcast:   ', toDecimal(dottedBinaryNotation(orCalculator(andCalculator(
    toBinary(ip), getMask(mask)), getWildcard(getMask(mask))))), ' - ', dottedBinaryNotation(orCalculator(andCalculator(
        toBinary(ip), getMask(mask)), getWildcard(getMask(mask)))))

print('First Ip: ', getFirstIp(toDecimal(dottedBinaryNotation(
    andCalculator(toBinary(ip), getMask(mask))))))

print('Last Ip:  ', getLastIp(toDecimal(dottedBinaryNotation(orCalculator(andCalculator(
    toBinary(ip), getMask(mask)), getWildcard(getMask(mask)))))))
print('#Ips', getAvailableIps(mask))
print()
