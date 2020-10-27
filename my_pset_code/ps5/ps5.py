# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz
def raw_text(text):
    #该函数将字符串text中的多余的符号去掉，返回一个只由单词和单个空格组成的字符串,并返回小写格式的列表类型
    #经测试可以使用
    new_text=text
    for word in string.punctuation:
        if word in new_text:
            new_text=new_text.replace(word," ")
    new_text=new_text.lower()
    text_list=new_text.split() #列表类型
    return text_list
    #text_final=" ".join(text_list)
    #return text_final
def raw_text_2(text):
    #该函数将字符串text中的多余的符号去掉，返回一个只由单词和单个空格组成的字符串,并返回小写格式的字符串类型
    #经测试可以使用
    new_text=text
    for word in string.punctuation:
        if word in new_text:
            new_text=new_text.replace(word," ")
    new_text=new_text.lower()
    text_list=new_text.split() #列表类型
    text_final=" ".join(text_list)
    return text_final

#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

# TODO: NewsStory
class NewsStory(object):
    """ docstring for NewsStory
        GUID - a string
        title - a string
        description - a string
        link to more content - a string
        pubdate - a ​datetime


    """
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title=title
        self.description=description
        self.link=link
        self.pubdate=pubdate
    def get_guid(self):
        return self.guid
    def get_title(self):
        return self.title
    def get_description(self):
        return self.description
    def get_link(self):
        return self.link
    def get_pubdate(self):
        return self.pubdate

#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # 不写？
        #title=story.get_title() #string
        #description=story.get_description() #string
        #if "Microsoft Office" in title or  "Boston" in description:
         #   return True
        #else:
        #    return False
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
# TODO: PhraseTrigger
class PhraseTrigger(Trigger):#繁琐？？
    def __init__(self, phrase): #phrase is a string
        self.phrase = phrase
    def is_phrase_in(self,text): #text is a string 
        new_texts_list=raw_text(text) # purple cows are cool!
        phrase_lower=self.phrase.lower()
        phrase_lower_list=phrase_lower.split()
        for i in phrase_lower_list:
            if i not in new_texts_list:
                return False
        new_text=raw_text_2(text)
        if phrase_lower not in new_text:
            return False
        return True



# Problem 3
# TODO: TitleTrigger
class TitleTrigger(PhraseTrigger):
    def __init__(self, phrase):
        PhraseTrigger.__init__(self, phrase)
    def evaluate(self, story): #story 属于 NewsStory类
        title=story.get_title()
        if self.is_phrase_in(title)==True:
            return True
        else:
            return False
# Problem 4
# TODO: DescriptionTrigger
class DescriptionTrigger(PhraseTrigger):
    def __init__(self, phrase):
        PhraseTrigger.__init__(self, phrase)
    def evaluate(self, story): #story 属于 NewsStory类
        description=story.get_description()
        if self.is_phrase_in(description)==True:
            return True
        else:
            return False

        
# TIME TRIGGERS

# Problem 5
# TODO: TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.
class TimeTrigger(Trigger):
    def __init__(self,time):#输入的time是字符串类型，要进行转换 —>datetime
    #str:3 Oct 2016 17:00:10(输入) -> 2015-6-1 18:19:59
        self.time = datetime.strptime(time, '%d %b %Y %H:%M:%S')

# Problem 6
# TODO: BeforeTrigger and AfterTrigger
class BeforeTrigger(TimeTrigger):
    """docstring for BeforeTrigger"""
    def __init__(self, time):
        TimeTrigger.__init__(self,time)
    def evaluate(self, story):
        pubdate=story.get_pubdate() #story's time
        pubdate = pubdate.replace(tzinfo=pytz.timezone("EST"))
        if pubdate<self.time.replace(tzinfo=pytz.timezone("EST")):
            return True
        else:
            return False


        
class AfterTrigger(TimeTrigger):
    """docstring for AfterTrigger"""
    def __init__(self, time):
        TimeTrigger.__init__(self,time)
    def evaluate(self, story):
        pubdate=story.get_pubdate() #story's time
        pubdate = pubdate.replace(tzinfo=pytz.timezone("EST"))
        if pubdate>self.time.replace(tzinfo=pytz.timezone("EST")):
            return True
        else:
            return False
# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger
class NotTrigger(Trigger):
    """docstring for NotTrigger"""
    def __init__(self, trigger):
        self.trigger = trigger
    def evaluate(self, x): #given a trigger ​T​ and a news item ​x
        return not self.trigger.evaluate(x)


# Problem 8
# TODO: AndTrigger
class AndTrigger(Trigger):
    def __init__(self, trigger1,trigger2):
        self.trigger1 = trigger1
        self.trigger2=trigger2
    def evaluate(self, x): 
        if (self.trigger1.evaluate(x) and self.trigger2.evaluate(x)) ==True:
            return True
        else:
            return False
# Problem 9
# TODO: OrTrigger
class OrTrigger(Trigger):
    def __init__(self, trigger1,trigger2):
        self.trigger1 = trigger1
        self.trigger2=trigger2
    def evaluate(self, x): 
        if (self.trigger1.evaluate(x) or self.trigger2.evaluate(x)) ==True:
            return True
        else:
            return False

#======================
# Filtering
#======================

# Problem 10

def filter_stories(stories, triggerlist):
    #stories, triggerlist都是列表类型
    #return 列表类型(stories for which a trigger fires.)
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # (we're just returning all the stories, with no filtering)
    stories_final=[]#初始定义一个空列表
    for i in stories:
        for j in triggerlist:
            if j.evaluate(i)==True:
                stories_final.append(i)
                break
    return stories_final



#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    #可以建立keyword 与class对应的字典，待改进
    # 返回列表类型， a list of triggers
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    #keyword=['TITLE',​'DESCRIPTION​','AFTER',​'BEFORE'​,'NOT'​,'AND'​,'OR'​]
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)
    returned_trigger=[]
    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers
    # lines ,列表类型
    trigger_dictionary={} #关键字是trigger names，数值是具体的trigger
    for string in lines: #string 中的每一个字符串
        if string[0:3] != "ADD":#该字符串是一个Trigger definitions
            definitions_list=string.split(",") #列表类型
            if definitions_list[1]=="TTITLE":
                trigger_dictionary[definitions_list[0]]=TitleTrigger(definitions_list[2])
            elif definitions_list[1]=="DESCRIPTION":
                trigger_dictionary[definitions_list[0]]=DescriptionTrigger(definitions_list[2])
            elif definitions_list[1]=="AFTER":
                trigger_dictionary[definitions_list[0]]=AfterTrigger(definitions_list[2])
            elif definitions_list[1]=="BEFORE":
                trigger_dictionary[definitions_list[0]]=BeforeTrigger(definitions_list[2])
            elif definitions_list[1]=="NOT":
                trigger_dictionary[definitions_list[0]]=NotTrigger(trigger_dictionary(definitions_list[2]))
            elif definitions_list[1]=="OR":
                trigger_dictionary[definitions_list[0]]=OrTrigger(trigger_dictionary(definitions_list[2]),trigger_dictionary(definitions_list[3]))
            elif definitions_list[1]=="AND":
                trigger_dictionary[definitions_list[0]]=AndTrigger(trigger_dictionary(definitions_list[2]),trigger_dictionary(definitions_list[3]))
        else: #该字符串是一个Trigger addition
            trigger_addition_list=string.split(",")
            for j in range(1,len(trigger_addition_list)):
                returned_trigger.append(trigger_dictionary[j])
    return returned_trigger






    #print(lines) # for now, print it so you see what it contains!



SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("COVID")
        t2 = DescriptionTrigger("Trump")
        t3 = DescriptionTrigger("Clinton")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        #triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            #stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            #stories.extend(process("http://news.yahoo.com/rss/topstories"))
            stories = process("http://news.yahoo.com/rss/topstories")

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

