
str=input()
str=str.lower()
kpoint=0
spoint=0
vowels=['a','e','i','o','u']
for i in range(len(str)):
  if str[i] in vowels:
    vo=str[i:]
    break
for i in range(len(str)):
  if str[i] not in vowels:
    conso=str[i:]
    break    
temp=vo
for i in range(len(temp)):
  if vo[i] in vowels:
    temp=vo[i:]
    for j in range(len(temp)):
      sub=temp[:j+1]
      
      if(sub in temp):
        kpoint+=1
  else:
    continue
temp=conso
for i in range(len(temp)):
  if conso[i] not in vowels:
    temp=conso[i:]
    for j in range(len(temp)):
      sub=temp[:j+1]
      if(sub in temp):
        spoint+=1  
  else:
    continue            
if kpoint>spoint:
  print("kevin ",kpoint)
else:
  print("stuart",spoint)
