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
    while True:
        try:
            # print("Please enter the number of stock items for your cycle count.")
            # print("Quantity should be less than the current quantity of stock items")
        
            stock_items_to_count = int(input("Enter quantity of stock items to check here: "))
            break
        except ValueError:
            print("That is not a valid number")
        
    return stock_items_to_count
        


def all_line_items():
    """
    Retrieves the user input
    """
    user_input = get_cycle_count_qty()
    print(f"{user_input} confirmed for this cycle count")
    
    return (user_input)

 


def main():
    """ 
    Run all functions
    """
    count_stock_items()
    all_line_items()
    

main()




