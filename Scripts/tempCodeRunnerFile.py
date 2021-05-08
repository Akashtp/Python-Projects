if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
lst = []
for i in x + 1:
    for j in y + 1:
        for k in z + 1:
            if i + j + k != n:
                lst.append([i,j,k])
print(lst)
