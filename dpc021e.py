# DPC 021 [E]
# Digit Rearranger

number = raw_input("type a number >= 10 >> ")

k = len(number)-1
L = [int(number[k])]
k -= 1
L = [int(number[k])] + L

checking = True
while (checking == True):
  swap = False
  j = 0
  while (j < len(L)-1):
    if (L[j] >= L[j+1]):
      j += 1
    else:
      swap = True
      j = len(L)
      
  if (swap == True):
    checking = False
    L2 = []
    replacement = 10
    for i in range(1,len(L)):
      if (L[i] > L[0] and L[i] < replacement):
        replacement = L[i]
    h = L.index(replacement)
    L2 += [L[h]]
    del L[h]
    while (len(L) > 0):
      i = L.index(min(L))
      L2 += [L[i]]
      del L[i]
    answer = 0
    if (k > 0):
      L3 = []
      for f in range(0,k):
        L3 += [int(number[f])]
      L2 = L3 + L2
    for g in range (0,len(L2)):
      answer += L2[g]*(10**(len(L2)-1-g))
    print answer
    
  else:
    if (k == 0):
      print "no swap possible"
      checking = False
    else:
      k -= 1
      L = [int(number[k])] + L
      
