def tribonacci(sig, n):
    if n > 2:
        for i in range(n-3):
            sig.append(sig[i] + sig[i+1] + sig[i+2])
        return sig
    else:
        if len(sig) <= 1:
            return sig
        for  i in range(1,n):
            sig.append(sig[i])
            return sig

            
print(tribonacci([1, 1, 1], 1))

