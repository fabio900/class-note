Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> tup1=("milk","milo","tea","eggs")
>>> tup1[3]
'eggs'
>>> cars=("bwm","lincoln","cyrsler","escalade")
>>> cars[6]

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    cars[6]
IndexError: tuple index out of range
>>> cars=("bwm","lincoln","cyrsler","escalade")
>>> cars[3]
'escalade'
>>> 
