#To convert binary no to decimal no
def binary_to_decimal(num):
    num = num[::-1]
    decimal = 0
    for place in range(len(num)):
        digit = num[place]
        two_expo = 2 ** place
        adduct = int(digit) * two_expo
        decimal += adduct
    return decimal

#__main__
if __name__ == '__main__':
    num = '101'
    print(binary_to_decimal(num))
