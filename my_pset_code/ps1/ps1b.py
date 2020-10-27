#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 09:52:43 2020

@author: zhenghaoyu
"""
#ps1b.py
annual_salary=float(input("Enter your annual salary:"))
portion_saved=float(input("Enter the percent of your salary to save, as a decimal:"))
total_cost=float(input("Enter the cost of your dream home:"))
semi_annual_raise=float(input("Enter the semi­annual raise, as a decimal:"))
portion_down_payment=total_cost*0.25
r=0.04
current_savings=0
months=0
while current_savings<portion_down_payment:
    while months%6==0 and months!=0:
        annual_salary=annual_salary+annual_salary*semi_annual_raise
        break
    current_savings=current_savings+current_savings*(r/12)
    current_savings=current_savings+annual_salary/12*portion_saved
    months=months+1
print("Number of months:​",months)

