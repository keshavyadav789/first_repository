# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 22:15:33 2020

@author: sahil
"""

#taking two inputs from user using splitL() method
a,b=input("enter values for a and b:").split()
print("a=",a,"b=",b)


#input data a customer of a bank
name,age,account,balance=input("Enter Values a bank customer:").split()
print("Name=",name,"age=",age,"account=",account,"balance:",balance)

#input data a customer of a bank using seprators
name,age,account,balance=input("Enter Values for a customer:").split(',')
print("Name=",name,"age=",age,"account=",account,"balance:",balance)