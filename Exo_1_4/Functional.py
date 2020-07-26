# sum only if it's a digit : á la rencontre d'un int on fera la somme
def Sum_of_list(list):
 somme=0
 for i in list:
    if i.isdigit():
     print(int(i))
     somme= somme+ int(i)
 return somme
 
def Persistence(number):

 count = 0
 while(len(str(number))>1):
     mult=1
     for x in list(str(number)):
       mult=mult* int(x)
     count=count+1
     number=mult

     print('le count est de ',count)


 if(len(str(number)) == 1):
     print('le count est de ',count)

def sum_consecutives():
    source_list = [0, 7, 7, 7, 5, 4, 9, 9, 0]
    result_list = []
    sum=0
    current = source_list[0]
    count = 0
    for value in source_list:

        if value == current:
            count += 1
            sum= sum+current



        else:

                  result_list.append(sum)
                  current = value
                  sum=value
                  count = 1




    result_list.append(sum)



    print(result_list)







texte = input(" Veuillez introduire une chaine de caractere  :\n ")
print(Sum_of_list(texte))
Persistence(999)
sum_consecutives()
