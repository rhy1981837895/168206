# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 17:34:37 2018

@author: asus
"""
#考试题
#A：我没有偷钻石。 
#B：D就是罪犯。 
#C：B是盗窃这块钻石的罪犯。 
#D：B有意诬陷我。 
#假定只有一个人说的是真话，编程序判断谁偷走了钻石。

def find(init_list, true_man):
    flag = 0   
    for i in range(len(init_list)):     #遍历所有情况
        sum = (init_list[i]!="A") + (init_list[i]=="D") + (init_list[i]=="B") + (init_list[i]!="D")
        if ( sum == true_man ):
            flag = 1
            print("%s is a thief" %init_list[i])
    if(flag == 0):
        print("Can not find")

true_man = 1    #说真话的人数
init_list = ["A", "B", "C", "D"]    #初始嫌疑人 
find(init_list, true_man)
        
