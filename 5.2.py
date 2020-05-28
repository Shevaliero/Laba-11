'''5.
б) Дано текстові файли f1 і f2. Переписати зі збереженням порядку проходження
кожен другий компонент файлу f1 в f2, а кожен другий компонент файлу f2 - в файл f1.
Використовувати допоміжний файл h.
(Кудрявцев В.С)'''
import os
user=0
while user!=4:
    user=int(input('1 - New Folder\n2 - Create and/or write in txt file\n3 - Output result\n4 - Stop program\nEnter number:'))
    if user == 1:
            poth=input('Enter folder path:')
            os.mkdir(poth)
            os.chdir(poth)
    elif user == 2:
            f1=open('f1.txt',"w")
            print('Created,write:')
            f1.write(input())    #Запись в файл ф1
            f1.close()
    elif user == 3:
            f2=open('f2.txt','w')
            f1=open('f1.txt')
            f1r=f1.read()
            if f1r=='': #Возвращает к выбору если файл пустой
                print('Please write in file by button 2')
                continue
            for i in range(len(f1r)):
                if i%2!=0:
                    f2.write(f1r[i])  #Заполнение ф2 каждым вторым компонентом файла ф1
            f1.close()
            f2.close()
            f1=open('f1.txt','a')   #Режим="а" не стирает предыдущие записи в файле, а добавляет к нему новые
            f2=open('f2.txt')
            f2r=f2.read()
            for i in range(len(f2r)):
                if i%2!=0:
                    f1.write(f2r[i])  #Заполнение ф1 каждым вторым компонентом файла ф2
            f1.close()
            f2.close()
            f1=open('f1.txt')
            f1r=f1.read()
            print('f1:\n',f1r)
            f2=open('f2.txt')
            f2r=f2.read()
            print('f2:\n',f2r)
                
            
            
