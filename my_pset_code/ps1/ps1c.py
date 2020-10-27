#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 14:51:34 2020

@author: zhenghaoyu
"""
def total_savings(starting_salary,saving_rate):
    #用于计算已知初始工资和节省占比时所能省下的总钱数,经测试可以运行
    semi_anualraise=0.07
    total_savings=0
    anual_return=0.04
    for months in range(0,36):
        if (months%6==0 and months!=0):
            starting_salary=starting_salary+starting_salary*semi_anualraise
        total_savings=total_savings+total_savings*anual_return/12
        total_savings=total_savings+(starting_salary/12)*saving_rate
    return total_savings
def total_savings_max(starting_salary):
    #用于计算已知初始工资时最多能省下的钱数,经测试可以运行
    semi_anualraise=0.07
    total_savings=0
    anual_return=0.04
    for months in range(0,36):
        if (months%6==0 and months!=0):
            starting_salary=starting_salary+starting_salary*semi_anualraise
        total_savings=total_savings+total_savings*anual_return/12
        total_savings=total_savings+starting_salary/12
    return total_savings
def best_savings(starting_salary):
    #使用二分法，找到best_saving_rate,
    high=10000
    low=0
    guess=int((high+low)/2.0)#guess是一个整数
    steps=0
    saving_rate=guess/10000
    cost=1000000
    down_payment=0.25
    if total_savings_max(starting_salary)<(cost*down_payment):
        print("It is not possible to pay the down payment in three years.")
        return None
    while abs(total_savings(starting_salary, saving_rate)-(cost*down_payment))>100:
        guess=int((high+low)/2.0+0.5)
        saving_rate=guess/10000
        steps=steps+1
        if (total_savings(starting_salary, saving_rate)>(cost*down_payment)):
            high=guess
        elif (total_savings(starting_salary, saving_rate)<(cost*down_payment)):
            low=guess
    print("Best savings rate:​",saving_rate)
    return steps
starting_salary=int(input("Enter the starting salary:​"))
a=best_savings(starting_salary)
if a!=None:
    10print("Steps in bisection search:​",a)

#print(total_savings(62523,1))

            
        