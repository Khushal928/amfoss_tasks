First of all, I have cloned 2 repositories using git clone https.......

```
cd TheCommandLineCup
```
here, 1st perfect number is 6 so x=6 and y=5 
```
cd 06<br>
cat Spell_05.txt
```
here, we get Impedimenta now by going into spellbook and executing it will give secret code
```python
python3 Impedimenta.py 
```


similarly for the second challenge, x=3 and y=2 from given clues<br>
so we need to find what is in 02/Spell_03.txt. and implimenting that will give secret code 


```
git branch
```
 to find all the branches that local machine is aware of<br>
git branch -r to find all the branches including remote branches 
```
git fetch origin <remotebranch>
```
to include those branches in local repository

```
git checkout <specified branch> 
```
to shift to that branch<br>
and in the spell book in that branch, pwd will give location of that directory
```
git checkout main to move to main branch<br>
git checkout <specified branch> <location we got earlier>
```
from the given clues, we get Riddikuls.py contain required secret code

```
git fetch origin graveyard 
```
to introduce graveyard branch to local machine<br>
following same steps as earlier(using git checkout graveyard <location of spellbook in remote branch>) <br>
and using git log we can see all the commits made and from the clues in that commit log, 'Priori Incantatem.py' is where the hidden code is and executing it gives final part of secret code 

```git add task-01<br>
git commit -m 'message'<br>
git push origin main<br>
```
above three lines to push work into repo



![congrats image](/task-01/codes/congrats.png)

