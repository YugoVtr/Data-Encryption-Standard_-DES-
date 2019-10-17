from permutations import Permutations, permutate

def calculateKeys(key):
    chosen_permutation = permutate(Permutations.PC1, key).zfill(56)
    keys = ["" for i in range(16)]
    left = ["" for i in range(17)]
    right = left.copy()
    left[0], right[0] = chosen_permutation[:28], chosen_permutation[28:]

    for i in range(1,17): 
        left[i] = left_shift(i, left[i-1])
        right[i] = left_shift(i, right[i-1])
        keys[i-1] = permutate(Permutations.PC2, left[i] + right[i])
    return keys
    
def left_shift(index, key): 
    if index in [1,2,9,16]: 
        return key[1:] + key[0]
    else:
        return key[2:] + key[:2]

if __name__ == "__main__": 
    print( "run 'main.py' file to exec DES " )