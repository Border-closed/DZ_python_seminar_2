#Задайте список из n чисел последовательности (1 + 1/n) ** n и выведите на экран их сумму.
#Пример:
#-Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
#Сумма 9.06

n=int(input('Введите число  '))
l=[]
f=0
s=0
for i in range(1,n+1):
    if i<n:
        f=round((1+1/i)**i,2)
        print (i,' : ',f, end=',  ')
        s=s+f
    else:
        f=round((1+1/i)**i,2)
        print (i,' : ',f)
        s=s+f
print('Сумма: ', s)
#for i in range(1,n+1):
 #   print (i,' : ',f, end=',')