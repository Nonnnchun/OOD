#BigO n^2 || ใหญ่สุดก่อน ล่ะรองลงมา
def bubble_sort(lst): 
    for last in range(len(lst)-1,0,-1): #from last index to 0
        swaped = False  
        for i in range(last):
            if lst[i] > lst[i+1] :
                lst[i],lst[i+1] = lst[i+1],lst[i]
                swaped  = True
        if not swaped : break
    return lst

lst = [5,6,2,3,0,1,4]
print(bubble_sort(lst))

#BigO n^2 || key last biggest
def selection_sort(lst):
    for last in range(len(lst)-1,0,-1):
        biggest = lst[0]
        biggest_i = 0
        for i in range( 1,last+1):
            if lst[i] > biggest :
                biggest = lst[i]
                biggest_i = i
        lst[last],lst[biggest_i] = lst[biggest_i],lst[last]
    return lst

lst = [5,6,2,3,0,1,4]
print(selection_sort(lst))

#BigO n^2 || have 2 list frist lst will sort
# and add from each second lst
def insertion_sort(lst):
    for i in range(1, len(lst)): #from index 1 to last
        iEle = lst[i] #assign insertElement
        for j in range(i, -1, -1):
            if j > 0 and lst[j-1] > iEle :
                lst[j] = lst[j-1]
            else:
                lst[j] = iEle
                break
    return lst

lst = [5,6,2,3,0,1,4]
print(insertion_sort(lst))

#BigO n^2 || ประมาณว่าแบ่งออกเป็นส่วนๆ
def shell_sort(lst,dIncrements):
    for inc in dIncrements: 
        #for each diminishing increment 
        for i in range(inc,len(lst)):
            #insertion sort
            iEle = lst[i] #inserting element
            for j in range(i, -1, -inc):
                if lst[j-inc] > iEle and j >= inc:
                    lst[j] = lst[j-inc]
                else:
                    lst[j] = iEle
                    break
    return lst

lst = [5,6,2,3,0,1,4]
print(shell_sort(lst,[5,3,1]))

#BigO nlog2n || ไม่เชิงเรียงแค่เอาตัวน้อยสุดไว้บนสุด
# ที่เหลือก็ต้นไม้ทั่วไป
def heap_sort(h,i):
    """insertMinHeap"""
    insertEle = h[i]
    fi = (i-1)//2 #
    while i > 0 and insertEle < h[fi] :
        h[i] = h[fi]
        i = fi
        fi = (i-1)//2
    h[i] = insertEle
    return h

h = [13,14,16,24,21,12,68,65,26,32,31]
for i in range(1, len(h)):
    heap_sort(h, i)
print(h)

# max to min => heap_sort
def delMin(h, last):
    insertEle = h[last]
    h[last] = h[0] #inplace sort the root
    hole = 0
    ls = hole*2+1 # left son indicies 
    found = False 
    while ls < last and not found:
        rs = ls if ls+1 >= last else ls+1 
        min = ls if h[ls] < h[rs] else rs # minson index
        if h[min] < insertEle:
            h[hole] = h[min] # promote small son up to hole
            hole = min # going down the tree
            ls = hole*2+1
        else:
            found = True
    h[hole] = insertEle

h = [13,14,16,24,21,19,68,65,26,32,31]
for last in range(len(h)-1, -1, -1):
    delMin(h, last)
print(h)

#BigO nlog2n || แยกแล้วรวม
def merge_sort(l, left, right):
    center = (left+right)//2
    if left < right:
        merge_sort(l, left, center)
        merge_sort(l, center+1, right)
        merge(l, left, center+1, right)

def merge(l, left, right, rightEnd):
    start = left
    leftEnd = right-1
    result = []
    while left <= leftEnd and right <= rightEnd:
        if l[left] < l[right]:
            result.append(l[left])
            left += 1
        else:
            result.append(l[right])
            right += 1
    while left <= leftEnd: # copy remaining left half if any
        result.append(l[left])
        left += 1
    while right <= rightEnd: # copy remaining right half if any
        result.append(l[right])
        right += 1
    for ele in result: # copy result back to list l
        l[start] = ele
        start += 1
        if start > rightEnd:
            break
        
l = [5,3,6,1,2,7,8,4]
print(l)
merge_sort(l,0, len(l)-1)
print(l)

#BigO nlog2n || 
def quickSort(l) :
    qSort(l, 0, len(l)-1)

def qSort(l, left, right):
    if left < right : 
        p = partition(l, left, right)
        qSort(l, left, p - 1)
        qSort(l, p + 1, right)

def partition(l, left, right):
    if left == right - 1 : #only 2 elements
        if l[left] > l[right] :
            l[left],l[right] = l[right],l[left] #swap
        return left
    pivot = l[left] #first element pivot
    i, j = left + 1, right
    while i<j:
        while i<right and l[i]<=pivot:
            i += 1
        while j>left and l[j]>=pivot:
            j -= 1
        if i<j:
            l[i], l[j] = l[j], l[i] #swap
    if left is not j:
        l[left], l[j] = l[j], l[left] 
        # swap pivot to index j
    return j 

l = [5,1,4,9,6,3,8,2,7,0]
quickSort(l)
print(l)