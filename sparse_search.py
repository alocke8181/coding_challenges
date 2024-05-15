def sparse_search(query, input):
    high = len(input)-1
    low = 0
    mids = []
    while low <= high and len(mids)<20:
        mid = int((low+high)/2)
        mids.append(mid)
        if input[mid] == query:
            return mid
        elif input[mid] == '':
            searching = True
            while searching:
                difTop = 1
                difBot = 1
                if input[mid-difBot] == '':
                    if mid-difBot > 0:
                        difBot = difBot+1
                else:
                    mid = mid-difBot
                    searching = False
                if input[mid+difTop] == '':
                    if mid+difTop < len(input)-1:
                            difTop = difTop+1
                else:
                    mid = mid+difTop
                    searching = False
            if input[mid] < query:
                low = mid + 1
            if input[mid] > query:
                high = mid -1
        
        if input[mid] < query:
            low = mid + 1
        if input[mid] > query:
            high = mid -1
    return mids
