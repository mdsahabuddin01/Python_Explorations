"""
import array as arr
#pop
#remove
#insert
#index
#count
a = arr.array('i', [1,2,3,4,5])
l = len(a)
a.insert(1, 7)
for i in range(5):
    print(a[i], end=' ') """
# Storing expenses chronologically from January to May
monthly_expenses = [2200, 2350, 2600, 2130, 2190]

#1. in feb, how many dollars you spent extra compare to January?
print(-(monthly_expenses[0] - monthly_expenses[1]))
#2 find out your total expense in first quater (first three months) of the year
print(monthly_expenses[0] + monthly_expenses[1] + monthly_expenses[2])
#3 find out if you spend exactly 2000 dollars in any month
print("Did i spent 2000 in any month?", 2000 in monthly_expenses)
#4 June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
monthly_expenses.append(1980)

print(monthly_expenses)
#5  you returned an item that you bought in a month of april and got a refund of 200. make a correction
# to your monthly expense list based on this

monthly_expenses[3] = monthly_expenses[3] - 200

print(monthly_expenses)




