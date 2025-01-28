for this question, 1ist l i have created a list of leangth 10 with 0's where each number is frequency of its its (index) number.<br>
```python
S=input()
l=[0]*10
```


and then, I have iterated through each character in given string and if that character is a number, then l[i] is increased by 1 since l[i] represents the frequency of i which is initialised with 0.<br>
```python
for i in S:
    if(i.isnumeric()):
        i=int(i)
        l[i]+=1
```


finally, each number in list l is printed<br>
```python
for i in l:
    print(i,end=" ")
```