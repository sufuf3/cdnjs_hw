# -*- coding:utf-8 -*-

print "1. Write a program to print “Hello World”\n"
print "Hello World!\n"

print "==============================\n"
print "2. Modify the program to print 9x9 multiplication table using for loop\n"
for i in range(1,10):
    for j in range(1,10):
        print i * j,
    print "\n"

print "==============================\n"
print "3. Use while loop instead of for loop to print 9x9 multiplication table\n"
x = 1
y = 1
while x <= 9:
    while y <= 9:
        print x * y,
        y=y+1
    x=x+1
    y=1
    print "\n"
