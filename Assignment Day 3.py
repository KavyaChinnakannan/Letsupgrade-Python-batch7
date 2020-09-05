Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> #Question 1
>>> 
>>> feet=int(input("Enter the feet:"))
Enter the feet:400
>>> def land():
	if feet <=1000:
		print("Safe to Land..")
	elif feet >= 4500:
		print("Bring down to 1000ft")
	elif feet >=6500:
		print("Turn Around")
	else:
		print("try again..")

		
>>> land()
Safe to Land..
>>> 
>>> 
>>> #Question 2
>>> 
>>> r=int(input("Enter the upper limit:"))
Enter the upper limit:200
>>> for a in range(2,r+1):
	k=0
	for i in range(2,a//2+1):
		if(a%i==0):
			k=k+1
	if(k<=0):
		print(a)

		
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
101
103
107
109
113
127
131
137
139
149
151
157
163
167
173
179
181
191
193
197
199
>>> 
