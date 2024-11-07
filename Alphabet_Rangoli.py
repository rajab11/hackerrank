def print_rangoli(size):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    
    # Create list to store lines
    lines = []
    
    # Create each line
    for i in range(size):
        # Get letters from the alphabet
        letters = alpha[i:size]
        # Create the row by reversing letters and adding forward letters (excluding first)
        row = letters[::-1] + letters[1:]
        # Join with '-' and center the line
        line = '-'.join(row).center(4*size-3, '-')
        lines.append(line)
    
    # Print the pattern (top half + bottom half)
    print('\n'.join(lines[::-1] + lines[1:]))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)