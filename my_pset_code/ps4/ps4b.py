# Problem Set 4B
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx
import string #导入string这个模块
#print string.letters #包含所有字母(大写或小写)的字符串
#print string.lowercase #包含所有小写字母的字符串
#print string.uppercase #包含所有大写字母的字符串
#print string.punctuation #包含所有标点的字符串
#print string.ascii_letters #与string.letters一样
def add_space(strings,integer):
    #该函数可以在一个字符串的特定位置增加空格
    #经测试可以使用
    return strings[0:integer]+" "+strings[integer:]
def change(character,shift):
    # 该函数返回移动后的字母，返回的是字符串类型
    #charecter是字符串类型，shift是整数
    #经测试可以正常使用
    length=26
    number=0
    if character in string.ascii_lowercase:
        for i in range(0,length):
            if character==string.ascii_lowercase[i]:
                number=i
                break
        number=number+shift
    else:
        for i in range(0,length):
            if character==string.ascii_uppercase[i]:
                number=i
                break
        number=number+shift
    if number>=26:
        number=number-26
    if character in string.ascii_lowercase:
        return string.ascii_lowercase[number]
    else:
        return string.ascii_uppercase[number]
### HELPER CODE ###
def load_words(file_name):
    #该函数输入文件名，返回列表类型的有效单词
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
    #该函数判断word是否有效，不考虑大小写和标点
    #返回 True or False
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    #返回加密文本
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        self.message_text=text
        self.valid_words = load_words("words.txt")
        #列表类型

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
        valid_words_copy=self.valid_words[:]
        return valid_words_copy

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        # 创建字典，字典只能有52个关键字，分别是所有的大小写字母
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26
        shift是int类型，小于26大于等于0
        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        #返回的是字典类型，string:string
        '''
        shift_dict={}
        for i in string.ascii_lowercase:
            shift_dict[i]=change(i,shift)
        for i in string.ascii_uppercase:
            shift_dict[i]=change(i,shift)
        return shift_dict
            


    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26
        #返回转换完成的text，字符串类型
        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        #self.message
        shifted_message=""
        message_text_list=self.message_text.split()
        for i in message_text_list:
            for j in i:
                if j not in string.ascii_uppercase and j not in string.ascii_lowercase:
                    shifted_message=shifted_message+j
                else:
                    shifted_message=shifted_message+change(j,shift)
        return shifted_message



class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message
        s
        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        Message.__init__(self, text)
        self.shift=shift
        #加密字典
        self.encryption_dict=Message.build_shift_dict(self, shift)
        #加密文本
        self.message_text_encrypted=Message.apply_shift(self, shift)


    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift


    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        encryption_dict_copy=self.encryption_dict.copy() 
        return encryption_dict_copy
    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted
        

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26
        #改变该类的shift值，更新随之变化的其他属性，无返回值
        '''
        self.shift=shift
        #加密字典
        self.encryption_dict=build_shift_dict(self, shift)
        #加密文本
        self.message_text_encrypted=apply_shift(self, shift)




class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)

    def decrypt_message(self):
        #解密method
        #使用​is_word(wordlist, word)和string.split
        #注意：is_word(wordlist, word)不考虑标点和其它特殊字符,去掉了所有特殊字符
        #找到最好的shift，即与最多valid_word相对应的shift
        #加密为s，解密为26-s
        #若有多个best shift，任选一个，并返回其对应的解密messages
        #返回元组，（best shift,decrypted message）
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        max_key=0
        shift_dictionary={}#创建一个字典，关键字为shift，数值为各个shift所对应的valid_word个数
        #创建字典，储存空格出现的位置
        space_dic={}
        num_space=0
        for i in self.message_text:
            if i ==" ":
                space_dic[num_space]=1
                num_space=num_space+1
            else:
                num_space=num_space+1
        #print(space_dic)
        decrypt_message_list=self.message_text.split()#将各个单词分隔，存入列表中
        for i in range(0,26):#每一次shift循环
            num=0
            for j in decrypt_message_list:
                #print(j)
                k=Message(j)
                #print(Message.apply_shift(k,i))
                if is_word(load_words(WORDLIST_FILENAME),Message.apply_shift(k,i) ) ==True:
                    num=num+1
            shift_dictionary[i]=num
        maximum_shift=max(shift_dictionary.values())
        #print(shift_dictionary)
        for key,values in shift_dictionary.items():
            if values==maximum_shift:
                max_key=key
                break
        final_message=Message.apply_shift(self,max_key)
        for i in space_dic.keys():
            final_message=add_space(final_message,int(i))


        return (max_key,final_message)



            


if __name__ == '__main__':

#    #Example test case (PlaintextMessage)
    plaintext = PlaintextMessage('hello', 2)
    print('Expected Output: jgnnq')
    print('Actual Output:', plaintext.get_message_text_encrypted())
    plaintext = PlaintextMessage('HI,ALice', 3)
    print('Expected Output: KL,DOlfh')
    print('Actual Output:', plaintext.get_message_text_encrypted())

#    #Example test case (CiphertextMessage)
    ciphertext = CiphertextMessage('jgnnq')
    print('Expected Output:', (24, 'hello'))
    print('Actual Output:', ciphertext.decrypt_message())
    ciphertext = CiphertextMessage('JK, yqtnf!')
    print('Expected Output:', (24, 'HI, world!'))
    print('Actual Output:', ciphertext.decrypt_message())
    #print(is_word(load_words(WORDLIST_FILENAME),"HI!"))
    ciphertextMessage=CiphertextMessage(get_story_string())
    print(ciphertextMessage.decrypt_message())
    

