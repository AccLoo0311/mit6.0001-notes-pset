# Problem Set 2, hangman.py
# Name: zhenghaoyu
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
def strip(my_word):#my_word（现在已猜出的字母加上未猜出的，用 _代替）,是字符串类型，该函数将“ _”中的空格去掉,经测试可以使用
    my_word_list=list(my_word)
    lengh=len(my_word_list)
    my_word_new=[]#列表类型
    j=0
    for i in range(0,lengh):
        if my_word_list[i]!=" ":
            my_word_new.append(my_word_list[i])
    my_word_new_1=''.join(my_word_new)#此函数将列表类型转换为字符串类型
    return my_word_new_1#返回的是去掉空格后的字符串类型
def yuan_or_fu(letters_guessed):#经测试可以正常使用
    yuanyin1=['a']
    yuanyin2=['e']
    yuanyin3=['i']
    yuanyin4=['o']
    yuanyin5=['u']
    if yuanyin1[0]==letters_guessed[-1]:
        return True
    elif yuanyin2[0]==letters_guessed[-1]:
        return True
    elif yuanyin3[0]==letters_guessed[-1]:
        return True
    elif yuanyin4[0]==letters_guessed[-1]:
        return True
    elif yuanyin5[0]==letters_guessed[-1]:
        return True
    else:
        return False
def unique_letters(secret_word):#此函数用于计算并返回string类型变量secret_word中不同字符的个数
    j=1
    if len(secret_word)==1:
        return 1
    else:
        a=len(secret_word)
        for i in range(1,a):
            if secret_word[i] not in secret_word[0:i]:
                j=j+1
        return j
WORDLIST_FILENAME = "words.txt"
def unique_letters(secret_word):
    #该函数统计secret_word中出现的不同字符的个数，secret_word是string类型,返回一个整数类型。
    j=0
    for i in range(0,len(secret_word)):
        if secret_word[i] not in secret_word[i+1:len(secret_word)]:
            j=j+1
    return j


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    #secret_word是string类型，letters_guessed是list类型
    #只有letters_guessed里的字母包括secret_word里的全部字母时，返回true，否则返回false
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    length=len(secret_word)
    l=0
    if length == 1:
        if secret_word in letters_guessed:
            return True
        else:
            return False
    else:
        for i in secret_word:
            if i in letters_guessed:
                 l=l+1
                 #letters_guessed.remove(i)
                 return True and is_word_guessed(secret_word[l:], letters_guessed)
            else:
                 return False
#secret_word = 'apple'
#letters_guessed = ['a', 'e','p','l', 'e']
#print(is_word_guessed(secret_word, letters_guessed))
                
                
        
        
        
        
   



def get_guessed_word(secret_word, letters_guessed):
    #将猜出的词显示出来，没有猜出的用下划线代替
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    for i in secret_word:#secret_word是列表类型
        if i not in letters_guessed:
             secret_word=secret_word.replace(i,'_ ')
        
    return secret_word
#secret_word = 'apple'
#letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
#print(get_guessed_word(secret_word, letters_guessed))
    



def get_available_letters(letters_guessed):
    #输入已经猜的字母（列表类型），返回剩下的可以猜的字母
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    import string
    str_1=""
    for i in string.ascii_lowercase:
        if i not in letters_guessed:
            str_1=str_1+i
    return str_1
#letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
#print (get_available_letters(letters_guessed))
            
    

def hangman(secret_word):
    guesses_remaining=6
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    warnings_remaining=3
    wordlist = load_words()
    letters_list=string.ascii_lowercase#可以猜的全部字母，string类型
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is",len(secret_word),"letters long.")
    print("You have",warnings_remaining,"warnings left.")
    print("-------------")
    letters_guessed=[]#已被猜的所有字母，list类型，初始化为空列表
    #以下编写循环部分
    while guesses_remaining>0:
        print("You have",guesses_remaining,"guesses left.")
        print("Available letters:",end=' ')
        print(get_available_letters(letters_guessed))
        letters_guessed.append(input("Please guess a letter:"))
        if letters_guessed[-1] in string.ascii_lowercase:#输入的是字母
            if letters_guessed[-1] in letters_guessed[0:-1]:#输入的字母之前已经猜过了
                warnings_remaining=warnings_remaining-1
                if warnings_remaining<0:
                    print("Oops! You've already guessed that letter. You have no warnings left")
                    print("so you lose one guess: ",get_guessed_word(secret_word, letters_guessed))
                    guesses_remaining=guesses_remaining-1
                    print("------------")
                else:
                    print("Oops! You've already guessed that letter. You have",warnings_remaining,"warnings left:")
                    letters_guessed=letters_guessed[0:-1]
                    print(get_guessed_word(secret_word, letters_guessed))
                    print("------------")
            elif letters_guessed[-1] in secret_word:#输入的字母之前没猜过，且在secret_word里
                print("Good guess:",get_guessed_word(secret_word, letters_guessed))
                print("------------")
                if is_word_guessed(secret_word, letters_guessed)==True:#完全猜出
                    print("Congratulations, you won!")
                    print("Your total score for this game is: ",guesses_remaining*unique_letters(secret_word))
                    break
            else:#输入的字母不在secret_word里
                print("Oops! That letter is not in my word: ",get_guessed_word(secret_word, letters_guessed))
                if yuan_or_fu(letters_guessed)==True:#猜错的是元音
                    guesses_remaining=guesses_remaining-2
                elif yuan_or_fu(letters_guessed)==False:#猜错的是辅音
                    guesses_remaining=guesses_remaining-1
                print("------------")
        else:#输入的不是字母
            letters_guessed=letters_guessed[0:-1]
            warnings_remaining=warnings_remaining-1
            print("Oops! That is not a valid letter. You have",warnings_remaining,"warnings left: ",get_guessed_word(secret_word, letters_guessed))
            print("------------")
        if guesses_remaining<=0:
            print("Sorry, you ran out of guesses. The word was "+secret_word+".")







        
        
        
    

            
            
        
      
    
    



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):#my_word（现在已猜出的字母加上未猜出的，用 _代替）, other_word都是字符串类型
    right_word=[]#该列表存储猜对了的单词
    #先判断两个单词是否一样长
    my_word_no_space=strip(my_word)
    lengh=len(my_word_no_space)
    if lengh!=len(other_word):#两个单词不一样长
        return False
    else:#只是比较字母是否一致
        for i in range(0,lengh):
            if my_word_no_space[i]!="_":#该位置是字母，进入比较
                if my_word_no_space[i]!=other_word[i]:#与other_word不同
                    return False
                else:#与other_word相同
                    right_word.append(other_word[i])
    for j in range(0,lengh):
        if my_word_no_space[j]=="_":#若该位置是_，则判断该位置所对应的字母是否在right_word[]里
            if other_word[j] in right_word:
                return False
    return True



def show_possible_matches(my_word):#该函数应该输入带有“ _”的字符串类型，表示现在已猜出的部分单词。
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    print(my_word[0:-1])#这里的my
    j=0
    length_wordlist=len(wordlist)
    for i in range (0,length_wordlist):
        if match_with_gaps(my_word,wordlist[i])==True:
            print(wordlist[i], end=' ')
        else:j=j+1
    print('\n------------')
    if j==length_wordlist:
        print("No matches found")

    return None



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    guesses_remaining=6
    warnings_remaining=3
    #wordlist = load_words()
    letters_list=string.ascii_lowercase#可以猜的全部字母，string类型
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is",len(secret_word),"letters long.")
    print("You have",warnings_remaining,"warnings left.")
    print("-------------")
    letters_guessed=[]#已被猜的所有字母，list类型，初始化为空列表
    guessed_word=""#定义一个空字符串，用来存储带有“_ ”的字符串类型
    #以下编写循环部分
    while guesses_remaining>0:
        print("You have",guesses_remaining,"guesses left.")
        print("Available letters:",end=' ')
        print(get_available_letters(letters_guessed))
        letters_guessed.append(input("Please guess a letter:"))
        if letters_guessed[-1] in string.ascii_lowercase:#输入的是字母
            if letters_guessed[-1] in letters_guessed[0:-1]:#输入的字母之前已经猜过了
                warnings_remaining=warnings_remaining-1
                if warnings_remaining<0:
                    print("Oops! You've already guessed that letter. You have no warnings left")
                    print("so you lose one guess: ",get_guessed_word(secret_word, letters_guessed))
                    guesses_remaining=guesses_remaining-1
                    print("------------")
                else:
                    print("Oops! You've already guessed that letter. You have",warnings_remaining,"warnings left:")
                    letters_guessed=letters_guessed[0:-1]
                    print(get_guessed_word(secret_word, letters_guessed))
                    print("------------")
            elif letters_guessed[-1] in secret_word:#输入的字母之前没猜过，且在secret_word里
                print("Good guess:",get_guessed_word(secret_word, letters_guessed))
                guessed_word=get_guessed_word(secret_word, letters_guessed)
                print("------------")
                if is_word_guessed(secret_word, letters_guessed)==True:#完全猜出
                    print("Congratulations, you won!")
                    print("Your total score for this game is: ",guesses_remaining*unique_letters(secret_word))
                    break
            else:#输入的字母不在secret_word里
                print("Oops! That letter is not in my word: ",get_guessed_word(secret_word, letters_guessed))
                if yuan_or_fu(letters_guessed)==True:#猜错的是元音
                    guesses_remaining=guesses_remaining-2
                elif yuan_or_fu(letters_guessed)==False:#猜错的是辅音
                    guesses_remaining=guesses_remaining-1
                print("------------")
        elif letters_guessed[-1]!="*":#输入的不是字母,也不是提示符号
            letters_guessed=letters_guessed[0:-1]
            warnings_remaining=warnings_remaining-1
            print("Oops! That is not a valid letter. You have",warnings_remaining,"warnings left: ",get_guessed_word(secret_word, letters_guessed))
            print("------------")
        else:#输入的是提示符号
            print("Possible word matches are:")
            show_possible_matches(guessed_word)
            


        if guesses_remaining<=0:
            print("Sorry, you ran out of guesses. The word was "+secret_word+".")



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word="apple"
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
