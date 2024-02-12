import gspread
from google.oauth2.service_account import Credentials

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


def get_cycle_count_qty():
    """
    Get the number of items for cycle counting from the user
    The number has to be greater than zero and equal to or less than 
    the quanity of stock items currently held
    """
    print("Please enter the number of stock items for your cycle count.")
    print("Quanity should be less than the current quantity of stock items")

    stock_items_to_count = input("Enter quantity here: ")
    stock_items_to_count = int(stock_items_to_count)

    
    return (stock_items_to_count)


def validate_input_data():
    """
    Checks to see that the user inputs a number that is lower than
    the quantity of stock items
    """
    quantity_items = int(count_stock_items())
    quantity_entered = int(get_cycle_count_qty())

    try:
        if quantity_entered !< quantity_items:
            raise ValuerError(
            f"You have entered {quantity_entered}")
    
    except ValueError as e:
        print(f"INVALID: {e}, please enter a valid number")
        return False

    return True







def main():
    """ 
    Run all functions
    """
    count_stock_items()
    get_cycle_count_qty()



main()