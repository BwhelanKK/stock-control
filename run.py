import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS =  CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('stock_list')

def count_stock_items():
    """
    Counts stock item quantity.  
    This is outputted to the user.
    User can not enter either a quanity higher than this or zero
    """
    print("Welcome to the stock control system.\n")
    
    stock = len(SHEET.worksheet("stock").col_values(1))-1

    print(f"The current quantity of stock items is: {stock}\n")

    return stock

# def get_all_values():
#     """
#     retreives all values in 'stock' worksheet
#     """
#     rows = SHEET.worksheet("stock").get_all_values()

#     return rows

def get_cycle_count_qty():
    """
    Get the number of items for cycle counting from the user
    The number has to be greater than zero and equal to or less than
    the quanity of stock items currently held
    """
    while True:
        try:
            stock_items_to_count = int(input("Enter quantity of stock items to check here: "))
            break
        except ValueError:
            print("That is not a valid number")
    return stock_items_to_count
def line_items_to_count():
    """
    Retrieves the number of line items the user entered as a list
    """
    x = get_cycle_count_qty()
    i = 2
    while i <= x:
        my_items = SHEET.worksheet("stock").row_values(i)
        if i == 0:
            break
        i += 1
    return my_items
    

def update_stock_to_count_sheet(data):
    """
    Updates stock_to_count sheet with user selected range of items
    to be cycle counted
    """
    print("The stock to count sheet is being populated.....\n")
    count_worksheet = SHEET.worksheet("stock_to_count")
    count_worksheet.append_row(data)
    print("Stock to count sheet has been successfully updated.\n")

 

def main():
    """ 
    Run all functions
    """
    
    count_stock_items()
    line_items_to_count()
    data = line_items_to_count()
    update_stock_to_count_sheet(data)
    

main()







