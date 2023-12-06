#!/usr/bin/python3
def search_replace(my_list, search, replace):
    latestList = my_list[:]
    for x in latestList:
        if x == search:
            latestList[latestList.index(x)] = replace
    return latestList
