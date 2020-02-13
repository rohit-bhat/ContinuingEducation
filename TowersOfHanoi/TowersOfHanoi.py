def TowersOfHanoi(fromr, to, via, n):

    if (n==0):
        return

    # Move n-1 blocks to the "via" rod
    TowersOfHanoi(fromr, via, to, n-1)

    # Move the nth block to the "to" rod
    print('Move %d from %s to %s' %(n, fromr, to))

    # Move the n-1 blocks from the "via" rod to the "to" rod
    TowersOfHanoi(via, to, fromr, n-1)

TowersOfHanoi("A", "C", "B", 4)