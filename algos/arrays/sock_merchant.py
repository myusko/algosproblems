def sock_merchant(n, ar):
    a = set(ar)
    p = 0
    for x in a:
        p += ar.count(x) // 2
    return p
