"""
实验48】集合的简单应用

请编写一个程序，从键盘输入两个字符串，将它们的字符分别转换为集合，
并输出它们的交集、并集和差集。
"""

a= set(input("1"))
b = set(input("2"))

print(a&b,a|b,a-b)
