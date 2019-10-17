from keys import calculateKeys, Permutations, permutate
from substitution import substitution

def xor(a, b): 
    return "{0:b}".format(int(a, 2) ^ int(b, 2))

def f(right, key): 
    expansion = permutate(Permutations.EP, right)
    s = xor(expansion, key).zfill(48)
    p = substitution(s)
    exchanged = permutate(Permutations.P, p)
    return exchanged

def des(message, key):
    assert len(message) == 64, "block is not 64 bits"
    assert len(key) == 64, "key is not 64 bits"

    keys = calculateKeys( key )   
    initial_permutation = permutate(Permutations.IP, message)
    left = ["" for i in range(17)]
    right = left.copy()
    left[0], right[0] = initial_permutation[:32], initial_permutation[32:]

    for i in range(1, 17):
        left[i] = right[i-1]
        right[i] = xor( left[i-1], f(right[i-1], keys[i-1]) ).zfill(32)
    
    encrypted = permutate(Permutations.IP_INV, right[16] + left[16])
    return '{0:x}'.format(int(encrypted, 2))

def main(): 
    message = 0xa23456789fdc1abb
    key = 0xa123456789abcdef
    encrypted = des("{0:b}".format(message).zfill(64), "{0:b}".format(key).zfill(64))
    print(encrypted)

if __name__ == '__main__': 
    main()