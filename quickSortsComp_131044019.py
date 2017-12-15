################################################################################
# Gozde DOGAN
# 131044019
# CSE321 - Introduction to Algorithm Design
# Homework 4
# Question 5
################################################################################

################################################################################
#
# Lomuto Partition:
#                   #comparisons = high-low+1
#                   for loop, high-low+1 defa doner
#                   Best case de lomuto partition calisma zamani lineer zamandir.
#                   Worst case de lomuto partition calisma zamanni lineer zamandir.
#                   Average case de worst ve best case'in esit olmasi nedeni ile 
#                   lineer zamandir. 
#                   Avantaji, her zaman swap islemi yapmamasi
#                   Liste pivot, pivottan kucukler ve pivottan buyukler diye 
#                   ayrilmis durumda oldugu icin pivottan buyuk elemana denk 
#                   gelindiginde sadece index arttiriliyor, pivottan kucuk elemana
#                   denk gelindiginde swap yapiliyor, pivottan kucuk elemanlarin
#                   son index'i de 1 arttiriliyor. Bu islem low high arasindaki 
#                   butun elemanlar icin gerceklestirliyor, boylece sort islemi
#                   gerceklestirilmis oluyor. 
#
# Hoare Partition:
#                   Best Case: Butun split islemleri ortadan olma durumudur
#                   (pivot elementin her zaman ortaya denk gelme durumu), bu 
#                   durumda #comporisons nlogn'dir. 
#                   (derste master theorem ile bulduk)
#                   Worst Case: Listenin siraliya yakin olmasi, yani pivot element
#                   ya basta ya sonda olur. Bu durumda da listelerden biri bos,
#                   biri ise listedeki eleman sayisindan bir eksik elemana 
#                   sahip olur. BOylece #comporisons ilk iterasonda n+1, 
#                   2. iterasyonda n seklinde olur. Burdan da (n+1)*(n+2)/2 - 3 
#                   ten n^2 olarak bulunur.
#                   (3, n-1. iterasyondaki karsilastirma sayisi)
#                   Average Case: Listenin s elemanli ve n-s-1 elemanli olarak 
#                   ayrilarak islem gerceklesitirilir. Her s pozisyonundan ayrilma
#                   durumunun olasiligi da 1/n'dir. 
#                   Burdan da nlogn oalrak bulunur. (s elemanli ve n-s-1 elemanli
#                   listelerin average'ndan gelir)
#             
#   Lomuto partition'in Hoare partition'dan her durumda cok iyi oldugunu goruyoruz.      
#   Lomuto partition worst case'de Hoare partition'dan cok daha iyidir.
#   Hoare partition da her iki uctan baslanilarak sub array'ler 
#   pivot ile karsilastirilarak taranir.
#   Lomuto partition da ise array bastan taranmaya baslanir ve sonuna kadar 
#   pivot ile karsilastirilarak taranir.
#
################################################################################

import sys

def main():
################################################################################
    print "\n"
    arr = [15, 4, 68, 24, 75, 16, 42]
    #print "arr:", arr
    
    qsh = quickSortHoare(arr)
    print "qsh:" , qsh
    
    qsl = quickSortLomuto(arr)
    print "qsl:", qsl
    print "\n"
################################################################################    

################################################################################    
#    arr1 = [1, 47, 2, 24, 5, 11, 22, 7, 91, 50, 34]
#    print "arr:", arr1
    
#    qsh = quickSortHoare(arr1)
#    print "qsh:" , qsh
    
#    qsl = quickSortLomuto(arr1)
#    print "qsl:", qsl
#    print "\n\n"
################################################################################    

################################################################################    
#    arr2 = [81, 47, 4, 36, 54, 18, 62, 48, 23, 74, 2, 9, 29]
#    print "arr:", arr2
    
#    qsh = quickSortHoare(arr2)
#    print "qsh:" , qsh
    
#    qsl = quickSortLomuto(arr2)
#    print "qsl:", qsl
#    print "\n\n"
################################################################################    

################################################################################    
#    arr3 = [2, 4, 9, 7, 3, 78, 14, 5, 62, 24]
#    print "arr:", arr3
#    
#    qsh = quickSortHoare(arr3)
#    print "qsh:" , qsh
    
#    qsl = quickSortLomuto(arr3)
#    print "qsl:", qsl
#    print "\n"
################################################################################

################################ HOARE PARTITION ################################
def quickSortHoare(array):
    quickSort_Hoare(array, 0, len(array) - 1)
    return array


def quickSort_Hoare(array, low, high):
    if high - low < 1:
        return
    else:
        pivot = HoarePartition(array, low, high)
        quickSort_Hoare(array, low, pivot - 1)
        quickSort_Hoare(array, pivot + 1, high)


def HoarePartition(array, low, high):
    pivot = array[high]
    i = low
    j = high - 1

    while True:
        while array[i] <= pivot and i < j:
            i += 1

        while array[j] >= pivot and i < j:
            j -= 1

        if i == j:
            if array[i] <= pivot:
                i += 1

            array[i], array[high] = array[high], array[i] #swap
            return i
        else:
            array[i], array[j] = array[j], array[i] #swap

################################################################################ 
        

############################### LOMUTO PARTITION ############################### 
        
def quickSortLomuto(array):
    quickSort_Lomuto(array, 0, len(array) - 1)
    return array


def quickSort_Lomuto(array, low, high):
    if high - low < 1:
        return
    else:
        pivot = LomutoPartition(array, low, high) #pivot eleman indexi
        quickSort_Lomuto(array, low, pivot - 1) #right part
        quickSort_Lomuto(array, pivot + 1, high) #left part


def LomutoPartition(array, low, high):
    pivot = low 
    pivotElm = array[high] 

    for i in range(low, high): 
        if array[i] <= pivotElm:  
            array[i], array[pivot] = array[pivot], array[i]  #swap
            pivot += 1  

    array[high], array[pivot] = array[pivot], array[high]  #swap
    
    return pivot #pivot elemaninin index'i return edilir

################################################################################ 
                        

if __name__ == '__main__':
    main()
