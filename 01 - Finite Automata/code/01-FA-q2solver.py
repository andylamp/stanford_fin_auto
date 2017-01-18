# The simple recursion formula as required.
def n_rec(k):
    # there are no valid strings < 2
    if k < 2:
        return 0
    # if we have two, then we return 2 as there are
    # only two paths
    elif k == 2:
        return 2
    # all other cases are handled through this one.
    else:
        paths = n_rec(k-2) + 2*n_rec(k-3)
        return paths

# ref. caller
def main():
    len = int(input("Enter a string length: "))
    # enter your desired N.
    print("N is: ", n_rec(len))

if __name__ == '__main__':
    main()