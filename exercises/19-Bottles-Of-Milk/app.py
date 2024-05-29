# ✅↓ Write your code here ↓✅
def number_of_bottles():
    for i in range(100,2,-1):
        print(f'{i} bottles of milk on the wall, {i} bottles of milk.\n Take one down and pass it around, {i-1} bottles of milk on the wall.\n')
    print('\n2 bottles of milk on the wall, 2 bottles of milk.\n Take one one down and pass it around, 1 bottle of milk on the wall.\n')
    print('\n1 bottle of milk on the wall, 1 bottle of milk.\n Take one one down and pass it around, no more bottles of milk on the wall.\n')
    print('No more bottles of milk on the wall, no more bottles of milk.\nGo to the store and buy some more, 99 bottles of milk on the wall.')
number_of_bottles()