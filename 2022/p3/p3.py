from suffix_trees import STree

def get_priority(ch):
    if 97 <= ord(ch) <= 122:
        return ord(ch) - 96
    else:
        return ord(ch) - 38

def longestSubstringFinder(string1, string2):
    answer = ""
    len1, len2 = len(string1), len(string2)
    for i in range(len1):
        for j in range(len2):
            lcs_temp = 0
            match = ''
            while ((i+lcs_temp < len1) and (j+lcs_temp<len2) and string1[i+lcs_temp] == string2[j+lcs_temp]):
                match += string2[j+lcs_temp]
                lcs_temp += 1
            if len(match) > len(answer):
                answer = match
    return answer

def find_longest_substring(strings):
    st = STree.STree(strings)
    return st.lcs()

def p1():
    with open('input', 'r') as input:
        total = 0
        for line in input.readlines():
            stuff = line.strip()
            if len(stuff) > 0:
                a, b = stuff[:len(stuff) // 2], line[len(stuff) // 2:]
                a1 = longestSubstringFinder(a, b)
                total += get_priority(a1)
        print(total)

def p2():
    with open('input', 'r') as input:
        total = 0
        lines = input.readlines()
        l = len(lines)
        for i in range(l // 3):
            a1 = find_longest_substring([line.strip() for line in lines[3 * i:3 * i + 3]])
            total += get_priority(a1)
        print(total)
        
p2()
