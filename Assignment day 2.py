Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> lst=["kavya","python programming",1,2,4]
>>> lst.append("lets upgrade")
>>> print(lst)
['kavya', 'python programming', 1, 2, 4, 'lets upgrade']
>>> lst.index(4)
4
>>> lst1=[]
>>> lst1.copy(lst)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    lst1.copy(lst)
TypeError: copy() takes no arguments (1 given)
>>> lst1=lst.copy()
>>> print(lst1)
['kavya', 'python programming', 1, 2, 4, 'lets upgrade']
>>> lst1.insert(2,"session")
>>> print(lst1)
['kavya', 'python programming', 'session', 1, 2, 4, 'lets upgrade']
>>> lst1.reverse()
>>> print(lst1)
['lets upgrade', 4, 2, 1, 'session', 'python programming', 'kavya']
>>> 
>>> 
>>> #dictionary & default functions
>>> 
>>> dit={"name":"kavya","gender":"female","phno":"12345","subject":"python programming","id":123}
>>> dit
{'name': 'kavya', 'gender': 'female', 'phno': '12345', 'subject': 'python programming', 'id': 123}
>>> dit.get(3)
>>> dit
{'name': 'kavya', 'gender': 'female', 'phno': '12345', 'subject': 'python programming', 'id': 123}
>>> dit1=dit.get("gender")
>>> dit1
'female'
>>> dit2={"key1","key2"}
>>> dit3=5
>>> thisdit=dit.fromkeys(dit2,dit3)
>>> thisdit
{'key2': 5, 'key1': 5}
>>> x=dit.setdefault("gender","female")
>>> x
'female'
>>> dit.popitem()
('id', 123)
>>> dit.clear()
>>> dit
{}
>>> 
>>> 
>>> #set & default functions
>>> x={"lotus","rose","jasmine","lilly"}
>>> x.add("sunflower")
>>> x
{'lotus', 'lilly', 'rose', 'sunflower', 'jasmine'}
>>> y={"blue","black","pink","rose","lotus"}
>>> z=x.difference(y)
>>> z
{'sunflower', 'jasmine', 'lilly'}
>>> j=x.intersection(y)
>>> j
{'lotus', 'rose'}
>>> e=x.union(y)
>>> e
{'lotus', 'lilly', 'rose', 'sunflower', 'jasmine', 'pink', 'black', 'blue'}
>>> s=x.issubset(y)
>>> s
False
>>> d=x.remove("black")
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    d=x.remove("black")
KeyError: 'black'
>>> d=e.remove("black")
>>> d
>>> 
>>> c=("violet","red","yellow")
>>> c.removw("red")
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    c.removw("red")
AttributeError: 'tuple' object has no attribute 'removw'
>>> c={"red","violet","yellow"}
>>> c.remove("red")
>>> c
{'violet', 'yellow'}
>>> 
>>> #tuple
>>> tup=("physics","chemistry",1997,1999,2000)
>>> tup1=(1,2,3,4)
>>> tup2="a","b","c","d"
>>> tup1[0]
1
>>> tup[1:4]
('chemistry', 1997, 1999)
>>> len(tup)
5
>>> max(tup1)
4
>>> min(tup1)
1
>>> cmp(tup,tup1)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    cmp(tup,tup1)
NameError: name 'cmp' is not defined
>>> tup3,tup4=(12,'xy'),(234,'cvb')
>>> print cmp(tup3,tup4)
SyntaxError: invalid syntax
>>> tup2.count()
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    tup2.count()
TypeError: count() takes exactly one argument (0 given)
>>> wrd=("welcome to python programming")
>>> cnt=wrd.count('o')
>>> cnt
4
>>> index=wrd.index("python")
>>> index
11
>>> 
>>> 
>>> #Strings & default methods
>>> 
>>> str1=" welcome to python programming"
>>> x=str1.capitalize()
>>> x
' welcome to python programming'
>>> y=str1.upper()
>>> y
' WELCOME TO PYTHON PROGRAMMING'
>>> z=y.islower()
>>> z
False
>>> w=str1.isalnum()
>>> w
False
>>> wrd1="   is       "
>>> wrd2=wrd1.strip()
>>> print("this ",wrd2,"python programming")
this  is python programming
>>> r=y.swapcase()
>>> r
' welcome to python programming'
>>> 
