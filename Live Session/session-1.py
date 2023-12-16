import json

# data = open("data/expenses.json", "r")


# with open('data/expenses.json', 'r') as f:
#     expense_data = json.load(f)

# print(expense_data)
# print(expense_data[0])
# print(type(expense_data[3]))
# print(expense_data[3]["documents"])
# if expense_data[3]["documents"]:
#     print("Document Exit")
    # need to render the document


# for data in expense_data:
#     if data['documents'] is None:
#         print("No document exist for id ", data['id'])
#     else:
#         print("Document Exist!!!")
#         print(data['id'])
#         print(data['documents'])
    
#     print("------------")

    


# variable
user = "kalim"
expense_date = '13-12-2023'
amount = 4000
category = 'shopping'
notes = "test"
documents = 'invoice_1_abc.png'

# print("Expense Date: ", expense_date, "Amount: ", amount, category)
# print(f"Category: {category} \nNotes: {notes} \nDocuments: {documents}")


def save_expense_data():
    print("Expense Data Recoding Feature!!")
    expense_date = input("Expense date: ")
    amount = input("Amount: ")
    category = input("Category: ")
    notes = input("Notes: ")
    documents = input("Documents: ")

    if expense_date and amount and category:
        # connect to db
        # INSERT into db
        # you can store data
        print("Data Inserted Successfully!!!")
    else:
        # print("You must input mandatory field")
        return "Mandatory field is not set!!"
    
    return expense_date, "Successfully Inserted"


def parameter_insertion():
    pass

# if-else
while True:
    option = input("Select your option: ")
    option = option.lower()
    # save expense data
    # parameter insertion
    # reporting
    if option == 'exit':
        break

    elif option == "save expense data":
        mssg = save_expense_data()
        print(mssg)


    elif option == "parameter insertion":
        print("Parameter Insertion Feature!!!")
        parameter_insertion()

    elif option == "reporting":
        print("Reporting Feature!!!")

    else:
        print("Invalid Option!!! Select perfect option")
    
