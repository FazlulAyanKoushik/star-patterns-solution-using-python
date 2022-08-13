'''
Pattern 1:

*****
*****
*****
*****
*****
'''
print('pattern 1: ')
n = 5
for i in range(n):
    print(5*'*')
    
    
'''
Pattern 2:

*
**
***
****
*****
'''

print('')
print('pattern 2: ')
n = 5
for i in range(1, n+1):
    print(i*'*')
    

'''
Pattern 3:

*****
****
***
**
*
'''

print('')
print('pattern 3: ')
n = 5
for i in range(n, 0, -1):
    print(i*'*')
    

'''
Pattern 4:

    *
   **
  ***
 ****
*****
'''

print('')
print('pattern 4: ')
n = 5
for i in range(1,n+1):
    interval = 5 - i
    print(interval*' ', i*'*')
    
    
'''
Pattern 5:

*****
 ****
  ***
   **
    *
'''

print('')
print('pattern 5: ')
n = 5
for i in range(n, 0, -1):
    interval = 5 - i
    print(interval*' ', i*'*')
    
    
'''
Pattern 6:

    *
   ***
  *****
 *******
*********
'''

print('')
print('pattern 6: Hill pattern')
n = 5
for i in range(1,n+1):
    interval = 5 - i
    if i == 1:
        star = i
        
    if i > 1:
        start = star + 2
    print(interval*' ', star*'*')
    
    

'''
Pattern 7:

*********
 *******
  *****
   ***
    *
'''

print('')
print('pattern 6: Reverse Hill')
n = 5
count = 0
interval = 0
for i in range(n,0, -1):
    star = i + i - 1
    if count >= 1:
        interval = count
    print(interval*' ', star*'*')
    count = count + 1