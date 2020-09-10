def fibonaci(a):
    if a == 1 or a == 2:
        return 1
    else:
        return fibonaci(a-1) + fibonaci(a-2)

print(fibonaci(3))

def print_list(subjects):
    for sb in subjects:
        print(sb)
data = ("Math", "Literature", "Physical")
print_list(data)