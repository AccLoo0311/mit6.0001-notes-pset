# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <zheng haoyu>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10,'*': 0
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"
def max(m,n):#m,n都是数字，该函数取两个数中的较大值
    if m > n:
        return m
    return n
def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):#假设word是有效的，返回该word所对应的分数，输入的总是一串字母（可能有大写字母）
#，或是空字符串，word是string类型，n是整数类型（大于等于0），返回的分数是整数类型（大于等于0）。
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    word_lower=word.lower()
    component_a=0#表示单词中字母的总分数
    component_b=0#表示公式所计算出的分数
    length=len(word_lower)
    for i in range(0,length):
        component_a=component_a+SCRABBLE_LETTER_VALUES[word_lower[i]]
    component_b=7*length-3*(n-length)
    if component_b<1:
        component_b=1
    else:
        component_b=component_b
    return component_a*component_b



    
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    #print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}#空字典
    num_vowels = int(math.ceil(n / 3))#元音个数
    x="*"
    hand[x]=1
    for i in range(num_vowels-1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):#输入的hand是字典类型，表示给出的字母及次数，word是输入的单词（字符串类型）
#返回字典类型，表示剩下的字母及次数，需要保持原有hand字典不变
#字典使用.copy???

    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    hand_copy=hand.copy()#使用该函数，当hand_copy和hand发生变化时，两者互不影响
    word_lower=word.lower()
    length=len(word)
    for i in range(0,length):
        if word_lower[i] in hand:#如果第i个字母在hand里
            if hand_copy[word_lower[i]] >=1:#且在hand中的次数大于等于1
                hand_copy[word_lower[i]]=hand_copy[word_lower[i]]-1
    hand_copy_2=hand_copy.copy()
    for j in list(hand_copy.keys()):
        if hand_copy[j]==0:
            del(hand_copy_2[j])
    return hand_copy_2


#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    #word_list是单词表，列表类型，需要hand和word_list不改变，word是字符串类型,全部由有效字母(或通配符)组成
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    word_new=""#表示将通配符替换成某个元音字母i后所组成的新单词
    hand_true=True#判断单词中的字母（通配符）是否在都符合hand字典要求
    word_list_true=False #判断单词是否在word_list列表中
    word_lower=word.lower()
    location_wildcard=word_lower.find("*")
    hand_copy=hand.copy()
    hand_copy_2=hand.copy()
    if location_wildcard==-1:#word单词中没有通配符
        if word_lower in word_list:
            word_list_true=True#单词在word_list列表中
        else:
            return False#单词不在word_list列表中
        for i in word_lower:
            if i in hand.keys():#word的第i个字母在字典hand的关键字中
                hand_copy[i]=hand_copy[i]-1
                if hand_copy[i]<0:#使用字母的次数超过hand所规定的的次数
                    hand_true=False
                    return False
            else:#word的第i个字母不在字典hand的关键字中
                hand_true=False
                return False
            hand_true=True
        if (word_list_true==True and hand_true==True):
            return True
        else:
            return False
    else:#word单词中有通配符,
        for i in VOWELS:
            if (word_lower[0:location_wildcard]+i+word_lower[location_wildcard+1:]) in word_list:
                word_list_true=True#该步骤运行正常,表明新单词在word_list列表中
            #将通配符替换成某个元音字母i后的新单词在word_list中
                word_new=(word_lower[0:location_wildcard]+i+word_lower[location_wildcard+1:])
                #print(word_new)
                for j in word_lower:
                    if j in hand.keys():#word的第i个字母在字典hand的关键字中
                        hand_copy_2[j]=hand_copy_2[j]-1
                        if hand_copy_2[j]<0:#使用字母的次数超过hand所规定的的次数
                            print(word_new+"单词在word_list列表中，但不符合hand要求")
                            hand_true=False
                            return False
                    else:#word的第j个字母不在字典hand的关键字中
                        print(j+"字母不在hand字典中")
                        hand_true=False
                        return False
                    hand_true=True#在hand字典中且符合hand字典次数要求
            if (word_list_true==True and hand_true==True):
                return True
    














                    





                    



    

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):#返回整数，表示hand中的字母个数
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    nums=0
    for i in hand.values():
        nums=nums+i
    return nums
    

def play_hand(hand, word_list):

    total=0
    while calculate_handlen(hand)!=0:
        print("")
        print("Current Hand:", end=' ')
        display_hand(hand)
        word=input("Enter word, or \"!!\" to indicate that you are finished: ")
        if word=="!!":#如果输入的是！！，中断游戏
            print("Total score: "+str(total)+" points")
            break
        else:#如果输入是单词,该部分有问题，通配符不识别,有待修改
            if (is_valid_word(word, hand, word_list))==True:#输入的单词在word_list中
                total=total+get_word_score(word,calculate_handlen(hand))
                print("\""+word+"\""+" earned "+str(get_word_score(word,calculate_handlen(hand)))+" points. Total: "+str(total)+" points")
                print("")
            else:#输入的单词不在word_list中
                print("That is not a valid word. Please choose another word.")
                print()
            hand=update_hand(hand, word)
        if calculate_handlen(hand)==0:
            print("Ran out of letters. Total score: "+str(total)+" points")            
    return total
    
    
#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    #允许用户用随机的一个字母代替hand中的一个字母（与被代替的的字母不同，也不应该是hand中已经出现的其他字母）
    #如果作者想要代替的字母不在hand中，hand不变
    #hand字典类型，letter字符串类型
    #返回一个新的字典类型
    #hand始终不被改变
    #letter为字符串类型
    letters_ok=""#初始定义为空字符串
    letters = 'aeioubcdfghjklmnpqrstvwxyz'#字符串类型，全部字母
    for i in letters:
        if i not in hand.keys():
            letters_ok=letters_ok+i
    hand_copy=hand.copy()
    if letter not in hand.keys():#字母不在hand字典中
        return hand_copy
    else:#字母在hand字典中
        number=hand[letter]
        del(hand_copy[letter])#删掉该字母所对应的字典
        letter_choosen=random.choice(letters_ok)
        hand_copy[letter_choosen]=number
        return hand_copy

def play_game(word_list):#此为测试版本
    #要求用户输入hands的总数
    #将每个hand所得的分数相加起来，得总分
    #进行每个hand之前，问用户是否要代替一个字母，该功能只能使用一次
    #每次hand结束后，询问用户是否要重玩该hand，若是，则重玩该hand，并保留较高的分数，该功能只能使用一次
    #重玩不算做用户最初想玩hands的数目
    #如果你想重玩，则无代替字母的功能，只能重玩刚才的hand(有可能已经substituted过)
    #返回总分
    #word_list，列表类型
    total_score=0
    hands_number=int(input("Enter total number of hands: "))#hands个数
    replay_number=1#重玩次数
    substitute_number=1#代替字母次数
    for i in range(0,hands_number):
        hand=deal_hand(HAND_SIZE)
        #hand={"a":1,"c":1,"i":1,"*":1,"p":1,"r":1,"t":1}#实际使用时应注释掉
        #hand={"d":2,"*":1,"a":1,"o":1,"u":1,"t":1}#实际使用时应注释掉
        print("Current Hand:", end=' ')
        display_hand(hand)
        if substitute_number>=1:#若之前未使用代替字母功能
            substitute_or_not=input("Would you like to substitute a letter? ")
            if substitute_or_not=="yes":
                substituted_letter=input("Which letter would you like to replace: ")
                hand=substitute_hand(hand, substituted_letter)
        score=play_hand(hand, word_list)
        print("Total score for this hand: "+str(score))
        print("----------")
        if replay_number>=1:#若未使用重玩功能
            repaly_or_not=input("Would you like to replay the hand? ")
            if repaly_or_not=="yes":
                score_1=play_hand(hand,word_list)
                score=max(score,score_1)
        total_score=total_score+score
    print("----------")
    print("Total score over all hands: "+str(total_score))


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#

if __name__ == '__main__':
    word_list = load_words()
    #hand={'h':1, 'e':1, 'l':2, 'o':1}
    #print(substitute_hand(hand, "l"))
    #hand={"a":1,"c":1,"i":1,"*":1,"p":1,"r":1,"t":1}
    #hand={"d":2,"*":1,"a":1,"o":1,"u":1,"t":1}
    #hand={"a":1,"j":1,"e":1,"f":1,"*":1,"r":1,"x":1}
    #hand={"a":1,"c":1,"f":1,"i":1,"*":1,"t":1,"x":1}
    #play_hand(hand, word_list)
    play_game(word_list)



