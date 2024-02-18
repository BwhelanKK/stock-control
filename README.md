# Stock Control - Cycle Count List

The stock Control - Cycle Count List is a small module in a Stock Management System that generates a cycle count list.  A cycle count is a quanity check on a selected amount of stock items.  The cycle count can be a random check to ensure that stockroom operations are being undertaken accurately.  Any variations have to be noted and investigated.  This module asks a user to input the items to be counted.  The stock item is then appnded to a googlesheet worksheet 'stock_to_count'. 

![Hereku image](https://github.com/BwhelanKK/stock-control/assets/44683806/0f393272-de33-48b7-9644-c46322a1a896)

## Design & Technologies used:
As this is a Python back end program, thre is no HTML or CSS.
- The project was coded in Python
- googlesheets spreadsheets was used to store the stock line itens as a list
- gspread was utilised for getting and setting data in teh google worksheet
- Heroku was used to deploy the app


## How Stock Control - Cycle Count List is used

The user is oresented by a simple input screen where they are prompted to enter stock items to be added to the cycle count list:

![Heroku welcome screen](https://github.com/BwhelanKK/stock-control/assets/44683806/d2493d03-6fb4-4af5-8b5f-6213b3b743b6)

The items selected will be selected from the 'stock' worksheet:

![current stock levels](https://github.com/BwhelanKK/stock-control/assets/44683806/0935a31a-5d35-496f-aefe-4895216273e3)

The selection is thenm copied over to the 'stock-to-count' worksheet that the user will print off and undertake a physical count:

![sotck items to count](https://github.com/BwhelanKK/stock-control/assets/44683806/9f31aa6e-7bb4-4434-b5f6-d395ba11068a)





- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!
