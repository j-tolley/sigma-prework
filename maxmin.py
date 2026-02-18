# Finds the min and max by iterating through the list without using any functions
def min_max(lst_integers):
    if lst_integers:
        min = lst_integers[0]
        max = lst_integers[0]
        for num in lst_integers:
            if num < min:
                min = num
            elif num > max:
                max = num
        return [min, max]
    else:
        print("Empty list so no min or max")

# Finds the min and max by using sort


def min_max_using_sort(lst_integers):
    if lst_integers:
        lst_integers.sort()
        return [lst_integers[0], lst_integers[-1]]
    else:
        print("Empty list so no min or max")


print(min_max([2, 4, 1, 0, 2, -1]))
print(min_max([100, -100]))
print(min_max_using_sort([2, 4, 1, 0, 2, -1]))
print(min_max_using_sort([100, -100]))
