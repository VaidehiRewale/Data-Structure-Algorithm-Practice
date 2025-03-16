 Find the intersection of two lists 
E.g List1=[1, 2, 3, 4, 5] List2=[3, 4, 6] Intersection=[3, 4]

def find_intersection(list1, list2):
    return list(set(list1) & set(list2)) 
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 6]
print("Intersection:", find_intersection(list1, list2))
