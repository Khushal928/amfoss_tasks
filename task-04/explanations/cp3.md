for this problem, my approach is to find all the nth powers of the natural numbers until x^n is <= target<br>
And then find all combinations of those numbers and count number of combination's sum that results in the target 


I have defined the finalcombinations list at the beginning where all the combinations will be stored and then combinations function is defined which take a list and a number as parameter k and split the numbers in the list taken k at a tim<br>
```python
finalcombinations=[]
answer=0


def combinations(listofuniqueints, k):
    global finalcombinations
    combination = list(range(k))
    while True:
        temp=[]
        for i in combination:
            temp.append(listofuniqueints[i])
        finalcombinations.append(temp)
       
        for i in reversed(range(k)):
            if combination[i] != i + len(listofuniqueints) - k:
                break
        else:
            return
   
        combination[i] += 1
        for j in range(i + 1, k):
            combination[j] = combination[j - 1] + 1
```


then i have created list named x_power_n and appended all the possible numbers as said earlier<br>
```python
x_power_n=[]
n=1
while(n**N<=X):
    x_power_n.append(n**N)
    n+=1
```


now in a list of n numbers, we can get combination with 1 number at a time, 2 numbers at a time........till taken every number in that list taken at a time<br>
so, i have called the combinations functions len(x_power_n) times with list as x_power_n and k as 1,2,....len(x_power_n) and every time that function is called, all the combinations are sent to finalcombinations list as it is defined global in the function.<br>
```python
for i in range(1,len(x_power_n)+1):
    combinations(x_power_n,i)
```


finally our finalcombination list is ready. so I have iterated through it and if sum of any list is target, then count of answer is increased by 1 and finally after iterating through all the lists in finalcombinations, answer is printed<br>
```python
for i in finalcombinations:
    if sum(i)==X:
        answer=answer+1

print(answer)
```