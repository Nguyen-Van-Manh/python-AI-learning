list_demo = ["Javascript", "Python", "PHP", "JAVA", "C++"]
for item in list_demo:
    if item == "Python":
        print("You are learning \"Python\" programming language")
list_demo.append("HTML")
def my_func(item):
    return len(item)

list_demo.insert(0, "CSS")
print("Length of above list is: {}".format(len(list_demo)))
print("Item which you have just inserted into header of list is: " + list_demo[0])
list_demo.remove("C++")
print("Remove \"C++\" from list_demo, current length is: {}".format(len(list_demo)))
list_demo.pop()
print("You have just removed last item from list_demo, current length is: {}".format(len(list_demo)))
del list_demo[0]
print("You have just removed first item from list_demo, current length is: {}".format(len(list_demo)))

list_copy = list_demo.copy()
print(list_demo.count("Javascript"))
print("Your list before sorted like: {}".format(list_copy))
list_copy.sort()
print("Your list after sorted like: {}".format(list_copy))
list_copy.sort(reverse=True, key=my_func)
print("Reverse sorted list by length for each item {}".format(list_copy))