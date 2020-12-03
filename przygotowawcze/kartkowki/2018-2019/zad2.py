def find_the_longest_cohesive_subsequence(seq):
    p, q = 0, 0

    sum_el = seq[p]
    sum_index = p

    max_leng = 1
    while p <= q and q < len(seq):

        sum_el += seq[q]
        sum_index += q

        if sum_el == sum_index:
            max_leng = max(max_leng, q-p+1)

        if sum_el != sum_index or seq[p-1] < seq[p]:
            while (sum_el > sum_index or seq[p-1] < seq[p]) and p <= q:
                sum_index -= p
                sum_el -= seq[p]
                p += 1

        q += 1
    

    return max_leng


sequence = [0,1,2,3,7,5,6,7]
sequence = [1, 9, 5, 4, 2, 1, 6, 2, 7, 9]

print(find_the_longest_cohesive_subsequence(sequence))