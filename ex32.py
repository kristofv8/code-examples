the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes',3, 'quarters']
the_count[1]
# this first kind of for-loop goes through a list
for number in the_count:
    print(f"This is count {number}")

#same as above
for fruit in fruits:
        print(f"A fruit of type: {fruit}")
#Also we can go trough mixed lists too
#notice we have to use {} since we don't know what's in it # for i in change:
for i in change:
     print(f" I got {i}")
#we can also build lists, first start with an empty one
elements = []

# then use range function to do 0 to 5 counts
for g in range(0, 100):
    print(f"Adding {g} to the list.")
    #append is a function that lists understand
    elements.append(g)

# now we can print them out too
for g in elements:
    print(f"Element was: {g}")
