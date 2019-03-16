def find_max(a_list):
    if a_list == []:
        return 0
    else:
        return max(a_list)

a = []
print(find_max(a))
b = [0, 1, 2, 3]
print(find_max(b))