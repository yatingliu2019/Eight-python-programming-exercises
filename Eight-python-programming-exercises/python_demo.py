# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 15:31:38 2021

@author: yatingliu2019
"""

#exp1_1
def main():
    val = eval(input("请输入您的密码（六位数字):"))
    for i in range(3):
        if val == password:
            print("密码输入正确！")
            print("登陆成功！")
            break
        else:
            if i< 2 :
                print("密码输入不正确，还有%d次机会"%(2-i))
            else:
                print("密码输入不正确，账户已冻结！")
                break
        val = eval(input("请输入您的密码（六位数字):"))
if __name__=='__main__':
    print("--------------------------------------------------")
    print("欢迎来到，亲爱的用户！")
    password = 666666
    main()
    
    
#exp2_1
def is_right_triangle_v1(s1,s2,s3):
    #函数代码和数据出结果的代码
    if isinstance(s1,int) and isinstance(s2,int) and isinstance(s3,int) :
        if (s1 > 0) and (s2 > 0) and (s3 > 0):
            if( s1**2 == s2**2 + s3**2)or( s2**2 == s1**2 + s3**2)or( s3**2 == s1**2+s2**2):
                print("这是一个直角三角形！")
            else:
                print("这不是个直角三角形！")
        else:
            print("错误！输入的数据包含非整数和非正数！")
    else:
        print("错误！输入的数据包含非整或非正数")
   
#调用is_right_triangle_v1函数代码
if __name__=='__main__':    
    s1,s2,s3=eval(input("请输入这个三角形的三边长："))
    is_right_triangle_v1(s1,s2,s3)
    
    
#exp2_2
def is_right_triangle_v2(sides):
    #调用is_right_triangle_v2函数代码
     if isinstance(sides[0],int) and isinstance(sides[1],int) and isinstance( sides[-1],int) :
        if (sides[0] > 0) and (sides[1] > 0) and ( sides[-1] > 0):
            if( sides[0]**2 == sides[1]**2 +  sides[-1]**2)or( sides[1]**2 == sides[0]**2 +  sides[-1]**2)or(  sides[-1]**2 == sides[0]**2+sides[1]**2):
                print("这是一个直角三角形！")
            else:
                print("这不是个直角三角形！")
        else:
            print("错误！输入的数据包含非整数和非正数！")
     else:
        print("错误！输入的数据包含非整或非正数")
    
#调用is_right_triangle_v2函数代码
if __name__=='__main__':    
    s1,s2,s3=eval(input("请输入这个三角形的三边长："))
    sides = [s1,s2,s3]
    is_right_triangle_v2(sides)
   
    
#exp3_1
from collections import Counter
def check_same(lst1,lst2):
    #函数
    if (len(lst1)) != (len(lst2)):
        return False
    else:
        lst1 = Counter(lst1)
        lst2 = Counter(lst2)
        if dict(lst1) == dict(lst2):
            return True
        else:
            return False     
#调用函数
if __name__=='__main__':    
    print('列表1:')
    a=input().split(",")
    print(a)
    print('列表2:') 
    b=input().split(",")
    print(b)
    print(check_same(a,b))


#exp3_2
from collections import Counter
def find_all(lst,func):
    #函数
    p_list = []
    for x in lst:
        if func(x) :
            p=lst.index(x)
            p_list.append(p)
    return p_list
 
#示例function
numbers=[2,4,9,10,-12,6]
print(find_all(numbers,lambda n:n>0))


#exp4_1
def find_max(d):
    max1=max(d,key=d.get)
    min1=min(d,key=d.get)
    return print(f"('{max1}','{min1}')")
if __name__=='__main__':
    d={'Xiaoming':20,'laozhang':50,'dali':40,'kity':16}    
    find_max(d)

    
#exp4_2
def sort(d):
    l=list(d.items())
    l.sort() 
    d = dict(l)
    return d
if __name__=='__main__':
    d={'xiaoming':20, 'laozhang':50,'dali': 40, 'kity': 16}    
    print(sort(d))
 
    
#exp4_3
def combine(d1,d2):
    lst=  []
    for key in d2:
        if key not in d1.keys():
            d1[key] = d2[key]
        else:
            d1[key]=d1[key]+d2[key]
    return d1
if __name__=='__main__':
    d1 = {'a': 90, 'b': 700, 'c':16}
    d2 = {'a': 60, 'b': 200, 'd':25}
    print(combine(d1,d2))


#exp5_1
def add_line_number(src_file,dst_file):
    n=0
    f=open(src_file,'r')
    lines=f.readlines()
    f.close()
    fp=open(dst_file,'w')
    for line in lines:
        fp.write(str(n+1)+' '+line)
        n=n+1
    fp.close()
if __name__=='__main__':
    add_line_number("1.txt","2.txt")
  
    
#exp5_2
def csv_reader(csvfile):
    import csv
    f=open(csvfile,'r')#encoding='utf-8'
    lines=csv.reader(f,dialect='excel')
    for line in lines:
        print(",".join(line))
    f.close()
if __name__=='__main__':
    csv_reader("csvfile.csv")
    
    
#exp6_1
import datetime
class Account:
    def __init__(self,identity='0000',balance=0.0,annual_interest_rate=0.0,date_created=0000-00):
        self.identity=identity#身份码
        self.balance=balance#余额
        self.annual_interest_rate=annual_interest_rate#年利率
        self.date_created=datetime.datetime.now()#系统时间
    def withdraw(self,amount_money):#取钱
        if self.balance>=amount_money:
            self.balance=self.balance-amount_money
    def deposit(self,amount_money):#存钱
        self.balance=self.balance+amount_money
    def get_monthly_interest(self):#计算月利息
        annual_interest_rate=self.annual_interest_rate/100
        monthly_rate=annual_interest_rate/12
        interests=self.balance*monthly_rate
        self.interests=interests
        return interests
if __name__=='__main__':
    person=Account('1111',2000.0,4.5,0000-00-00)
    person.withdraw(100)
    person.deposit(5000)
    print("余额：{}".format(person.balance)+"元") 
    print("月利息：{}".format(person.get_monthly_interest())+"%")
    print("开户时间：{}".format(person.date_created.year)+"年{}".format(person.date_created.month)+"月{}".format(person.date_created.day)+"日")
    
    
#exp7_1
def get_release(html_file):
    from bs4 import BeautifulSoup
    with open(html_file) as f:
        soup=BeautifulSoup(f,'lxml')
        div=soup.find('div',attrs={'class':['row download-list-widget']})
        ol=div.find('ol')
        li_all=ol.find_all('li')
        print("release-number release-date")
        for li in li_all:
            span=li.find_all('span')
            num=span[0].a.string
            date=span[1].string
            print(num+", "+date)
if __name__=='__main__':
    html_file='pythondownloads.html'
    get_release(html_file)
    
    
#exp8_1
import random
import string
import sys
from collections import Counter
 
WORDLIST_FILENAME = "words.txt"
chance=6#6次机会
warning=3#3次警告
word_guessed=''
letters_wrong=''#猜错的内容
letter_already=''#已经使用
string=string.ascii_lowercase#存储26个字符
stringlst=list(string)
wordbak =''
wordlst=[]
 
def load_words():
    print("从文件加载单词...")
    in_file = open(WORDLIST_FILENAME, 'r')
    line = in_file.readline()
    wordlist = line.split()
    print("已加载", len(wordlist), "个单词")
    in_file.close()
    return wordlist
 
def choose_word(wordlist):
    return random.choice(wordlist)
 
wordlist = load_words()
 
def is_word_guessed(secret_word, letters_guessed):#是否全部猜对
    word=list(secret_word)
    l_s=Counter(word)
    l_l=Counter(letters_guessed.lower())#完整单词
    if dict(l_s)==dict(l_l):
        return True
    else:
        return False
 
def get_guessed_word(secret_word, letters_guessed):#有几个被猜对了
    global letter_already
    global letters_wrong
    global chance
    global warning
    global wordbak
    global wordlst
    global string
    global stringlst
 
    if letters_guessed in stringlst:
        stringlst.remove(letters_guessed)
    string1= ''.join(stringlst)
    if letters_guessed in letter_already:#是不是被猜过了
        if letters_guessed in letters_wrong:
            chance=chance-1
        word= ''.join(wordlst)
        print('此字母已猜过 {}'.format(word))
        warning=warning-1
        if warning<0:
            chance=chance-1
            warning=2
        print('-----------------------------')
        print('剩余警告次数{}'.format(warning))
        print('剩余猜字次数{}'.format(chance))
        print('可用字母：{}'.format(string1))
    else:
        letter_already= letter_already+letters_guessed #加入已经猜过了
        if letters_guessed in secret_word: #是不是猜中了
            
            for i,c in enumerate(secret_word):
                if c == letters_guessed:
                    wordlst[i] = letters_guessed #已经猜中的单词
            word= ''.join(wordlst)
            print("猜对了!{}".format(word))
            print('-----------------------------')
            print('剩余猜字次数{}'.format(chance))
        else:
            letters_wrong=letters_guessed+letters_wrong
            word= ''.join(wordlst)
            print('猜错了!{}'.format(word))
            chance=chance-1
            if chance>0:
                print('-----------------------------')
                print('剩余警告次数{}'.format(warning))
                print('剩余猜字次数{}'.format(chance))
                print('可用字母：{}'.format(string1))
    return word
 
def get_available_letters(letters_guessed):#检查代码确定能有几位可以填
    global chance
    global string1
    global warning
 
    s='abcdefghijklmnopqrstuvwxyz'
    if letters_guessed not in s:
        print("你输入的不是字母，请输入一个字母！")
        warning=warning-1
        if warning <0:
            chance=chance-1
            warning=2
        print('-----------------------------')
        print('剩余警告次数{}'.format(warning))
        print('剩余猜字次数{}'.format(chance))
        return False
    return True     
 
def hangman(secret_word):
    global chance
    global warning
    global wordbak
    global wordlst
    
    print("欢迎来到猜字游戏")
    length=len(secret_word)
    print("我有一个{}".format(length)+"个字母的单词，请你猜一猜！")
    print("-----------------------------")
    print("剩余警告次数{}".format(warning))
    print("剩余猜字次数{}".format(chance))
    print("可用字母：{}".format(string))
    wordbak = '-' * len(secret_word)
    wordlst = list(wordbak)#猜的内容
    while True: 
        if chance<=0:
            print("对不起你输了! 单词是{}".format(secret_word))
            break
        else: 
            word=input("请输入一个字母：")
            word1=word.lower()
            while word1== '':
                word=input("请输入一个字母：")
                word1=word.lower()
            result=get_available_letters(word1)
            if result:
                words=get_guessed_word(secret_word, word1)
                if is_word_guessed(secret_word,words):
                    print('恭喜你猜对了!{}'.format(secret_word))
                    break
 
if __name__ == "__main__":
    secret_word = choose_word(wordlist)
    hangman(secret_word)
 
 
 