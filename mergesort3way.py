def merge_sort_3_way(L):

    if len(L) <= 1:
        return
    mid1 = len(L)//3
    mid2 = 2*len(L)//3
    left, mid, right = L[:mid1], L[mid1:mid2] , L[mid2:]

    #Mergesort core
    merge_sort_3_way(left)
    merge_sort_3_way(mid)
    merge_sort_3_way(right)
    temp = merge_three(left, mid, right)
    for i in range(len(temp)):
        L[i] = temp[i]

def merge_three(left, mid, right):
    L = []
    i = j = k = 0
    while i < len(left) or k < len(right) or j < len(mid):
        #Check it there's still elements to be merged from left and/or right
        if i >= len(left):
            L = L + merge(mid[j:],right[k:])
            break
        elif j >= len(mid):
            L = L + merge(left[i:],right[k:])
            break
        elif k >= len(right):
            L = L + merge(left[i:],mid[j:])
            break
        else:
            if left[i] >= mid[j]:
                if mid[j] >= right[k]:
                    L.append(right[k])
                    k += 1
                else:
                    L.append(mid[j])
                    j += 1
            else:
                if left[i] >= right[k]:
                    L.append(right[k])
                    k += 1
                else:
                    L.append(left[i])
                    i += 1
    return L



def merge(left, right):
    L = []
    i = j = 0
    while i < len(left) or j < len(right):
        #Check it there's still elements to be merged from left and/or right
        if i >= len(left):
            L.append(right[j])
            j += 1
        elif j >= len(right):
            L.append(left[i])
            i += 1
        else:
            if left[i] <= right[j]:
                L.append(left[i])
                i += 1
            else:
                L.append(right[j])
                j+=1
    return L


lista = [4, 60, 4, 8, 23, 89, 45, 44, 100]
merge_sort_3_way(lista)
print(lista)