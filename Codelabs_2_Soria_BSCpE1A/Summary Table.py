#Printing all the types of variables
print("\t\t\tSummary Table")
print()
print()
num_strings = []
num_strings.append("15")
num_strings.append("100")
num_strings.append("55")
num_strings.append("42")
print("The variable num_strings is a",(type(num_strings)))
print("It contains the elements: ", (num_strings))
print("The element "+ (num_strings[0]) +" is a", type(num_strings[0]))
print()
print()
num_ints = []
num_ints.append(15)
num_ints.append(100)
num_ints.append(55)
num_ints.append(42)
print("The variable num_ints is a",(type(num_ints)))
print("It contains the elements: ", (num_ints))
print("The element "+ str(num_ints[0]) +" is a", type(num_ints[1]))
print()
print()
num_floats=[ ]
num_floats.append(2.2)
num_floats.append(5.0)
num_floats.append(1.245)
num_floats.append(0.142857)
print("The variable num_floats is a",(type(num_floats)))
print("It contains the elements: ", (num_floats))
print("The element "+ str(num_floats[0]) +" is a", type(num_floats[1]))
print()
print()
num_lists=[ ]
num_lists.append([1, 2, 3])
num_lists.append([4, 5, 6])
num_lists.append([7, 8, 9])
print("The variable num_lists is a",(type(num_lists)))
print("It contains the elements: ", (num_lists))
print("The element "+ str(num_lists[0]) +" is a", type(num_lists[1]))
print()
print()
print("Now sorting num_strings and num_ints...")
print("Sorted num_strings:"+ str(sorted(num_strings)))
print("Sorted num_ints:"+ str(sorted(num_ints)))
print()
print()
print("Strings are sorted alphabetically while integers are sorted numerically!!!")