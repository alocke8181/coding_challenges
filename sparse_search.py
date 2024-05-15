def sparse_search(query, input):
    high = len(input)-1
    low = 0
    going_up = False

    while low <= high:
        mid = int((low+high)/2)
        if input[mid] == query:
            return mid
        if len(input[mid]) != 0:
            if input[mid] < query:
                low = mid + 1
                going_up = True
            elif input[mid] > query:
                high = mid -1
                going_up = False
            else:
                return mid
        else:
            if going_up:
                low = low+1
            if not going_up:
                high = high-1
    return -1
