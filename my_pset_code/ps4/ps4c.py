# Problem Set 4C
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    #print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    #print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word_list,列表类型，单词的列表
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    print(is_word(WORDLIST_FILENAME,"bat"))
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text=text #字符串类型
        self.valid_words=load_words(WORDLIST_FILENAME) #列表类型
    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        valid_words_copy=self.valid_words.copy()
        return valid_words_copy
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        #vowels_permutation 字符串类型，元音对应的转换方式
        #返回一个字典，包含52个关键字，辅音对应不变，元音转换，大小写的转换一致
        #字典的关键字和取值都是string类型
        num_1=0
        num_2=0
        vowels_permutation_lower=vowels_permutation.lower()
        vowels_permutation_upper=vowels_permutation.upper()
        transpose_dict={}
        for i in CONSONANTS_LOWER:#小写辅音
            transpose_dict[i]=i
        for i in CONSONANTS_UPPER:#大写辅音
            transpose_dict[i]=i
        for i in VOWELS_LOWER:#小写元音
            transpose_dict[i]=vowels_permutation_lower[num_1]
            num_1=num_1+1
        for i in VOWELS_UPPER:#大写元音
            transpose_dict[i]=vowels_permutation_upper[num_2]
            num_2=num_2+1
        return transpose_dict
    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        #返回一个编码后的版本

        encrypted_list=""
        for i in self.message_text:
            if i in transpose_dict.keys():
                encrypted_list=encrypted_list+transpose_dict[i]
            else:
                encrypted_list=encrypted_list+i
        return encrypted_list

class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        SubMessage.__init__(self, text)

    def decrypt_message(self):
        #对加密的字符进行解密
        #测试每一种可能的加密方式，找到一种加密方式，其对应的valid_word个数最多
        #返回最有可能的解密文档，若所有解密方式都没有valid_word，返回原字符串，存在多种best解密方式时，返回任意一个
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        #print(is_word(load_words(WORDLIST_FILENAME),"bat"))
        final_dict={}#建立一个字典，存储每一种变换方式所对应的valid_word的个数
        all_kinds_lower_list=get_permutations("aeiou")
        for i in all_kinds_lower_list:
            num=0
            transpose_dict=self.build_transpose_dict(i)
            message_transposed=self.apply_transpose(transpose_dict)#转换后的文本
            #print(i)
            #print(self.build_transpose_dict(i))
            #print(message_transposed)#输出转换后的文本
            words_transposed_list=message_transposed.split()
            #print(words_transposed_list)
            for j in words_transposed_list:
                #print(j)
                if is_word(load_words(WORDLIST_FILENAME), j)==True: #单词没有识别出来
                    #print("yes")
                    num=num+1
            final_dict[i]=num
            max_valid_word_num=max(final_dict.values())
        #print(final_dict)   字典正确
        #print(len(final_dict.keys()))    #字典关键字正确
        if max_valid_word_num<1:
            print("no")
            return self.message_text

        else:
            for key,values in final_dict.items():
                if values==max_valid_word_num:
                    best_permutation=key
                    break
            return self.apply_transpose(self.build_transpose_dict(best_permutation))





        

        



        
    

if __name__ == '__main__':

    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict)) 
    print("Decrypted message:", enc_message.decrypt_message())
    message = SubMessage("Too fast!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Tuu fest!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict)) #加密的字符串，正确
    print("Decrypted message:", enc_message.decrypt_message())

