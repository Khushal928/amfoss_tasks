we need to find the elements that are in B but not in A and display them in ascending<br>
my approach to this problem is that for a number x, if its frequency in B is greater than frequency in A, then that difference between frequency number of x's should be added to the list<br>


I have started this task by creating a function which accepts list and return dictionary with key as each distinct number in list and value as frequency of that number in list<br>
```python
def hashmap(lis):
    hashma={}
    for i in lis:
        if i in hashma:
            hashma[i]=hashma[i]+1
        else:
            hashma[i]=1
    return hashma
```


this is to take the lists and their lengths<br>
```python
a=int(input())
A=list(map(int,input().split()))
b=int(input())
B=list(map(int,input().split()))
answer=[]
hashA=hashmap(A)
hashB=hashmap(B)
```


for a number x, if its frequency in B is greater than frequency in A, then that difference between frequency number of x's should be added to the list and if the number is not in A then that number is to be added in the list<br>
```python
for i in hashB:
    if i not in hashA:
        answer.append(i)
    elif(hashB[i]-hashA[i]>0):
        answer.extend([i]*(hashB[i]-hashA[i]))
```


this will sort the list in ascending order as asked and print each of the value<br>
```python    
answer.sort()
for i in answer:
    print(i,end=" ")
```