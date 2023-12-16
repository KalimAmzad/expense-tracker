'''
INSERT INTO expense (expense_date, category, amount, notes, documents)
VALUES
('2023-04-01 08:00:00', 'Groceries', 95.75, 'Bought monthly groceries', 'grocery_receipt_01.pdf;grocery_list_01.jpg');

INSERT INTO expense (expense_date, category, amount, notes, documents)
VALUES
('2023-04-02 09:15:00', 'Utilities', 120.00, 'Electricity bill payment', 'electricity_bill_02.pdf');

INSERT INTO expense (expense_date, category, amount, notes, documents)
VALUES
('2023-04-03 12:30:00', 'Healthcare', 60.00, 'Prescription medication', 'prescription_03.pdf;pharmacy_receipt_03.jpg');

INSERT INTO expense (expense_date, category, amount, notes, documents)
VALUES
('2023-04-04 17:00:00', 'Entertainment', 50.00, 'Movie tickets and snacks', 'movie_tickets_04.pdf;snack_receipt_04.jpg');

INSERT INTO expense (expense_date, category, amount, notes, documents)
VALUES
('2023-04-05 20:00:00', 'Education', 200.00, 'Textbooks for new semester', 'textbook_invoice_05.pdf;course_outline_05.docx');
'''




import mysql.connector as mysql

# Establish a connection to the MySQL database
conn = mysql.connect(
    host="your_host",
    user="your_username",
    password="your_password",
    database="your_database"
)

# Create a cursor object
cursor = conn.cursor()

# SQL statement for inserting multiple records
insert_statement = """
INSERT INTO expense (expense_date, category, amount, notes, documents)
VALUES (%s, %s, %s, %s, %s),
       (%s, %s, %s, %s, %s),
       (%s, %s, %s, %s, %s),
       (%s, %s, %s, %s, %s),
       (%s, %s, %s, %s, %s);
"""

# Data for insertion
data = (
    '2023-04-01 08:00:00', 'Groceries', 95.75, 'Bought monthly groceries', 'grocery_receipt_01.pdf;grocery_list_01.jpg',
    '2023-04-02 09:15:00', 'Utilities', 120.00, 'Electricity bill payment', 'electricity_bill_02.pdf',
    '2023-04-03 12:30:00', 'Healthcare', 60.00, 'Prescription medication', 'prescription_03.pdf;pharmacy_receipt_03.jpg',
    '2023-04-04 17:00:00', 'Entertainment', 50.00, 'Movie tickets and snacks', 'movie_tickets_04.pdf;snack_receipt_04.jpg',
    '2023-04-05 20:00:00', 'Education', 200.00, 'Textbooks for new semester', 'textbook_invoice_05.pdf;course_outline_05.docx'
)

# Execute the SQL statement with the data
cursor.execute(insert_statement, data)

# Commit the changes to the database
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()