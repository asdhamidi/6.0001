def get_permutations(sequence):
    if len(sequence) == 1:
        return sequence

    perm_list = []
    res = []
    perm_list.extend(get_permutations(sequence[1:]))

    for word in perm_list:
        for r in range(len(sequence)):
            res.append(word[0:r]+sequence[0]+word[r:])
    
    return res


if __name__ == '__main__':
    example_input = input("Enter the string : ")
    print('Input:', example_input)
    print('Possible permutations:', sorted(set(get_permutations(example_input))))
