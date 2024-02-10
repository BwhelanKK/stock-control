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
    print("The current number of stock items are:\n")
    stock = SHEET.worksheet("stock").col_values(1)
    print(len(stock)-1)
    print("Enter the number of stock items that you'd like for your cycle count.\n")
    print("The number has to be equal to or lower than current stock quantity above:\n")

    count_qty = input("Please enter the number of stock items required for the cycle count:")

    print(count_qty)

    print("********************************************\n")


def get_cycle_count_qty():
    """
    Get the number of items for cycle counting from the user
    The number has to be greater than zero and equal to or less than 
    the quanity of stock items currently held
    """
    print




def main():
    """ 
    Run all functions
    """
    count_stock_items()



main()