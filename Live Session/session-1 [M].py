import json

# data = open("data/expenses.json", "r")


with open('data/expenses.json', 'r') as f:
    expense_data = json.load(f)

# print(expense_data)
# print(expense_data[0])
# print(type(expense_data[3]))
# print(expense_data[3]["documents"])
# if expense_data[3]["documents"]:
#     print("Document Exit")
    # need to render the document


for data in expense_data:
    if data['documents'] is None:
        print("No document exist for id ", data['id'])
    else:
        print("Document Exist!!!")
        print(data['id'])
        print(data['documents'])
    
    print("------------")

    


# variable
author  = "Kalim"
amount = 10.5
date = '13-12-2023'
category = 'Shopping'
notes = 'puchasing gift for my mom'
uploaded_files = 'gift_purchase_13_12_2023.png'

# print("Author: ", author, "\nAmount: ", amount, "\nDate: ", date)
# print("-----------")
# print(f"Category: {category} \nNotes: {notes} \nRef Files: {uploaded_files}")


# if-else
# store expense record
# parameter inserting
# reporting

def expense_record():
    if author=='Kalim':
        print(f"Hi Admin {author}", end=', ')
    else:
        print(f"Hi {author}", end=', ')
    print("You can record your expenses")

    expense_date = input('Expense Date: ')
    category = input("Category")
    amount = input("Amount")
    notes = input("Notes: ")
    documents = input("Documents: ")

    if not expense_date:
        return "Expense date must"
    if not amount:
        return "Amount mandatory field"
    
    if expense_date and category and amount:
        print("Insert Record in DB")
        # connect to DB

        # INSERT data in DB
        return category, amount, "Successfully Inserted"

    else:
        print("You need to fill up expense_date, amount, category to proceed further")
        return "Error: Input insertion error"


def parameter_insertion():
    pass


def reporting():
    pass



# "hello" + "world"
# "sheow" + str(amount)
# str(23.787) + "sgwe"

mega_shopping_list = [["clothing-1", "jeans", "shirt", "cap"], 
                      ["mango", "apple", "orange"], "katla fish", 
                      [10, 5, 10, 3], 
                      [3, 5, 3], 15]

# print(mega_shopping_list)
# print(mega_shopping_list[2])
# print(mega_shopping_list[-1])
# print(mega_shopping_list["katla fish"])


available_options = ['store expense record', 'parameter inserting', 'reporting']
available_options.append('income record')
# print("Available options", len(available_options))
# print(available_options[:3:2])
user_input_mssg = "Select your options " +  str(available_options) + ": "

# dictionay
shoppin_list = {"katla fish": 15,
                "clothings": ["jeans", "huddy", "cap", "panjabi"],
                "fruits": {"apple": 10,
                           "orange": 5,
                           "dates": 100}}

# print(shoppin_list)
# print(shoppin_list["fruits"]["dates"])
# Select your options: 'store expense record', 'parameter inserting', 'reporting'

while True:
    options = input(user_input_mssg)
    options = options.lower()
    if options == 'exit':
        break

    if options == 'store expense record':
        print("Expense Recording Feature")
        mssg = expense_record()
        print(mssg)

    elif options == "parameter inserting":
        print("Parameter insertion Feature!!!")
        parameter_insertion()

    elif options == "reporting":
        print("Reporting!!!")
        reporting()
    else:
        print("Invalid Options! Please select your option")



