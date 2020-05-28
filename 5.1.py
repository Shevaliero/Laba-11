'''5.
а) Дан текстовий файл f. Отримати в файлі g кількість букв, що знаходяться в
файлі f.
(Кудрявцев В.С)'''
import os
user=0
while user!=4:
    user=int(input('1 - New Folder\n2 - Create and/or write in txt file\n3 - Output result\n4 - Stop program\nEnter number:'))
    try:
        if user == 1:
            poth=input('Enter folder path:')
            os.mkdir(poth)  #Создает папку
            os.chdir(poth)  #Переходит в эту папку
        elif user == 2:
            poth1=input('Enter file path:')
            f=open(poth1,"w")
            print('Created,write:')
            f.write(input())    #Вызов функции для записи в файл
            f.close()
        elif user == 3:
            poth1=input('Enter file path:')
            f=open(poth1)
            fr=f.read() #Вызов функции для чтения файла
            count=0
            for i in range(len(fr)):
                if fr[i]!=' ' and fr[i]!='.' and fr[i]!=','and fr[i]!='?' and fr[i]!='!' and fr[i]!='-':
                    count+=1  #Подсчитывает буквы
            count=str(count)
            g=open('g.txt','w')
            g.write(count)  #Записывает кол-во букв из первого файла
            g.close()
            g=open('g.txt')
            gr=g.read()
            print(gr)
            g.close()
    except FileExistsError:
        print('Folder already exist')
        continue
    
