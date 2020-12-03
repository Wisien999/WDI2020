def find_the_longest_cohesive_subsequence(seq):
    max_length = -5
    for i in range(0, len(seq)):
        sum_index = i
        sum_el = seq[i]
        for j in range(i+1, len(seq)):
            # print("i", i, "j", j)
            sum_index += j
            sum_el += seq[j]

            if seq[j-1] >= seq[j] or sum_index != sum_el:
                # print("wew")
                j -= 1
                max_length = max(max_length, j-i+1)
                break
        
            if j == len(seq)-1:
                # print("j ostatnie")
                max_length = max(max_length, j-i+1)


        if i == len(seq)-1:
            # print("i ostatnie")
            if sum_index == sum_el and seq[i-1] < seq[i]:
                # print("i wew")
                max_length = max(max_length, len(seq)-i-1)
        
    
    if max_length == 1:
        for i in range(len(seq)):
            if seq[i] == i:
                return 1
        return 0
    

    return max_length

                




sequence = [0,1,2,3,4,5,6,7]
print(sequence, find_the_longest_cohesive_subsequence(sequence))

sequence = [0,1,2,3,7,5,6,7]
print(sequence, find_the_longest_cohesive_subsequence(sequence))

sequence = [1, 9, 5, 4, 2, 1, 6, 2, 7, 9]
print(sequence, find_the_longest_cohesive_subsequence(sequence))

sequence = [1, 6, 7, 3, 2, 6, 3, 9, 8, 2]
print(sequence, find_the_longest_cohesive_subsequence(sequence))

sequence = [8,7,6,5,4,5,6,7]
print(sequence, find_the_longest_cohesive_subsequence(sequence))

sequence = [1,2,3,4,5,6]
print(sequence, find_the_longest_cohesive_subsequence(sequence))
