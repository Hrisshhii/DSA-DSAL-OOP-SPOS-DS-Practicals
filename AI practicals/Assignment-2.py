def seletion_sort(arr):
    n=len(arr)
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if arr[j]<arr[min]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]
def main():
    arr=[]
    n=int(input("Enter number of elements in array: "))
    for i in range(n):
        num=int(input(f"Enter Element {i}: "))
        arr.append(num)
    seletion_sort(arr)
    print("Sorted array: ",arr)
main()