

def InSort(Array):

    for main in range(0, len(Array) - 1):
        minIndex = main

        for switch in range(main + 1, len(Array)):
            if Array[switch] < Array[minIndex]:
                minIndex = switch
        
        if minIndex != main:
            Array[main], Array[minIndex] = Array[minIndex], Array[main]

    return Array


Input = [5, 3, 7, 2, 9, 2, 1]

print("List:", Input)

Input = InSort(Input)

print("Sorted:", Input)



