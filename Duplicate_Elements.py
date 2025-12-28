# print all duplicates from a list


from collections import Counter
def find_duplicates(list):
    freq=Counter(list)
    return [item for item,c in freq.items() if c>1]
print(find_duplicates([1,1,2,3,4,4,5,6]))