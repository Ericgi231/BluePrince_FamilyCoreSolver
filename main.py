WORDS = ["pigs","sand","mail","date","head","clam","peak","heat","joya","well","toad","card","will","tape","legs","tree","road","maid","slab","rock","hand","vase","safe","clay","toes"]

def char_to_int(char):
    return ord(char) - ord('a') + 1

def int_to_char(num):
    return chr(num + ord('a') - 1)

def find_core():
    base_nums = []
    for char in word:
        base_nums.append(char_to_int(char))
    values = [
        ((base_nums[0] - base_nums[1]) * base_nums[2]) / base_nums[3],
        ((base_nums[0] - base_nums[1]) / base_nums[2]) * base_nums[3],
        ((base_nums[0] * base_nums[1]) - base_nums[2]) / base_nums[3],
        ((base_nums[0] * base_nums[1]) / base_nums[2]) - base_nums[3],
        ((base_nums[0] / base_nums[1]) - base_nums[2]) * base_nums[3],
        ((base_nums[0] / base_nums[1]) * base_nums[2]) - base_nums[3]
    ]

    ans = []
    for v in values:
        if v % 1 == 0 and 0 < v < 27:
            ans.append(v)

    return int_to_char(int(min(ans)))

for i, word in enumerate(WORDS):
    print(find_core(),end='')
    if (i+1) % 5 == 0:
        print()