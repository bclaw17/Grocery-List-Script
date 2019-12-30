

'''
The task is broken down into three sections.
Section 1 - User Input
Section 2 - loop through the grocery list
Section 3 - provide output to the console
'''

####Created an empty dictionary####
grocery_item = {}
####Created an empty list####
grocery_history = []

###While-loop coupled with a Boolean variable that is equal to False
stop = False

while not stop:

####User input for variables item_name, quantity, and cost
    item_name = input("Item name:\n")
    
    quantity = input("Quantity purchased:\n")
    
    cost = input("Price per item:\n")
####Add key-value pairs to dictionary from user input
    grocery_item = {'item_name':item_name, 'quantity':int(quantity), 'cost':float(cost)}
####Add(append) grocery_item dictionary data to grocery_history list. A list of dictionaries!! 
    grocery_history.append(grocery_item)
####User prompted to either continue adding data... or not.
    done_shopping = input("Would you like to enter another item?\nType 'c' for continue or 'q' to quit:\n")
    if done_shopping == 'q':
      stop = True
      
####Grand total variable set to zero at beginning of loop. Ready to be modified.
grand_total = 0
  
#### For-loop iterates through each item contained in the grocery_history list of dictionaries 
for item in grocery_history:
  
####Calculated item total by accessing quantity and cost keys in grocery item dictionary and multiplying  
  item_total = item['quantity'] * item['cost']
####Grand total value gets modified from zero to the value of item total for each iteration through the loop  
  grand_total += item_total
####Information printed for the user to view
  print('%d %s @ $%.2f ea $%.2f' %(item['quantity'], item['item_name'], item['cost'], item_total))
  
####Item total variable set to zero after it is used to calculate grand total. It is now ready to re-calculate during the next iteration.
  item_total = 0
#Print the grand total once all items have been iterated through.
print("Grand Total: $%.2f" % grand_total)
