# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx
def insert(character,strings):
    #定义一个插入函数，该函数输入一个字母，一个字符串，都是字符串类型
    #返回该字母插入该字符串的所有组合，返回为list类型
    #经测试可以使用
    all_kinds_list=[]
    number =len(strings)
    for i in range(0,number+1):
        all_kinds_list.append(strings[0:i]+character+strings[i:])
    return all_kinds_list
def get_permutations(sequence):
    #sequence 字符串类型
    #return 为列表类型
    j=1
    permutations=[]
    permutations_recursive=[]
    if len(sequence)==1:
        return [sequence]
    else:
        for i in get_permutations(sequence[j:]):#该函数返回n-1个单词的所有排列，i是所有排列中的一个
            permutations_recursive=permutations_recursive+insert(sequence[0],i)
        sequence=sequence[j+1:]
        return permutations_recursive

        


if __name__ == '__main__':

    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    example_input="ecd"
    print('Input:', example_input)
    print('Expected Output:', ['ecd', 'edc', 'ced', 'cde', 'dec', 'dce'])
    print('Actual Output:', get_permutations(example_input))
    example_input="fg"
    print('Input:', example_input)
    print('Expected Output:', ['fg','gf'])
    print('Actual Output:', get_permutations(example_input))

    

