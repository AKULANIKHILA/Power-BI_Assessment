##############Assisgnemt############
inventory = [
    # name,       category,   unit_price, units_sold, units_left
    ["Strawberry", "Fruit",      3.50,        40,          10],
    ["Broccoli",   "Vegetable",  2.20,        25,           8],
    ["Cheddar",    "Dairy",      5.00,        18,           4],
    ["Baguette",   "Bakery",     2.80,        35,           2],
    ["Blueberry",  "Fruit",      4.00,        22,           6],
    ["Spinach",    "Vegetable",  1.80,        30,          12],
    ["Yogurt",     "Dairy",      1.20,        50,          15],
    ["Croissant",  "Bakery",     3.00,        28,           3],
]
# unpacking of multiple rows at a time 
for name, category, unit_price, units_sold, units_left in inventory:
    print(f"{name} ({category})  Price: ${unit_price}, Sold: {units_sold}, Left: {units_left}")

numbers = [1, 2, 3, 4, 5]
a, *b, c = numbers
print(a)  # 1
print(b)  # [2, 3, 4]
print(c)  # 5


# ignoring some value '_' is used : 
data = (5, 10, 15)
x, _, z = data  # `_` is used to ignore the second value
print(x, z)  # 5 15

# to unpack items alternately we use unpacking + slicing:
numbers = [1, 2, 3, 4, 5]
a = [numbers[0], numbers[2]]
b = [numbers[1], numbers[3]]
c = numbers[-1]
print(a)  # [1, 3]
print(b)  # [2, 4]
print(c)  # 5


# calculating the total revenue 
rev = 0
for i in inventory:
    rev += unit_price * units_sold 
print(rev)   
    
#items less than 5
l = [] 
for name, category, unit_price, units_sold, units_left in inventory:
    if units_left < 5:
        l.append(name)
print(l)

rev = []
for name, category, unit_price, units_sold, units_left in inventory:
    r = unit_price * units_sold
    rev.append(r)
print(rev)

#####List comprehension####

users = [('akki',True),('nikki',False),('lucky',True)]
active_users = [(name,status) for name,status in users if status]
print(active_users) 
#example
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

#without comprehension
active = []
for name,status in users:
    if status:
        active.append(name)
print(active)
#example
squares = []
for x in range(5):
    squares.append(x**2)
print(squares)  # [0, 1, 4, 9, 16]
