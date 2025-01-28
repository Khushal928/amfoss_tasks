since caption's room only contains 1 person(capitan himself), a particular room's entry will only be once in the given room's list which is capitan's room!<br>
so we have to find the frequency of each room in the list and print the room whose frequency is one<br>


I have started this question by creating hashmap function which find the frequency of each room<br>
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


then take the input and obtain the freqency and print the number with frequency 1<br>
```python
K=int(input())
inputvalues=list(map(int,input().split()))
freq_of_eachroom=hashmap(inputvalues)
for i in freq_of_eachroom:
    if(freq_of_eachroom[i]==1):
        print(i)
        break
```
