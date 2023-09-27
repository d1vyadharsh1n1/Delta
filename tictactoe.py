def game(n):
    a = (' -'*n)
    c = ' '
    b = ((' |'*(n-1)))
    d = c+b
    print('\n'.join(( d,a)*(n-1)))
    print(d)

a=int(input("Enter the grid size:"))
game(a)