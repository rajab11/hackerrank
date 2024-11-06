def print_formatted(number):
    # Find the width for formatting based on the binary representation of the largest number
    width = len(bin(number)[2:])
    
    for i in range(1, number + 1):
        # Format and print each number in Decimal, Octal, Hexadecimal, and Binary
        print(f"{str(i).rjust(width)} {oct(i)[2:].rjust(width)} {hex(i)[2:].upper().rjust(width)} {bin(i)[2:].rjust(width)}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
