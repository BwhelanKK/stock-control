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

The user is presented with a simple input screen where they are prompted to enter stock items to be added to the cycle count list:

![Heroku welcome screen](https://github.com/BwhelanKK/stock-control/assets/44683806/d2493d03-6fb4-4af5-8b5f-6213b3b743b6)

The items selected will be selected from the 'stock' worksheet:

![current stock levels](https://github.com/BwhelanKK/stock-control/assets/44683806/0935a31a-5d35-496f-aefe-4895216273e3)

The selection is thenm copied over to the 'stock-to-count' worksheet that the user will print off and undertake a physical count:

![sotck items to count](https://github.com/BwhelanKK/stock-control/assets/44683806/9f31aa6e-7bb4-4434-b5f6-d395ba11068a)

## Features Left to Implement
 I would like to have the following features:
 - When the user inputs the quantity, the app will capture the line items using the randomint() method.
 - The list for items to be counted wouldn't have current stock values displayed.
 - When the physical count has bee completed, the user inputs the quantity counted.  This value is then compared to the current stock value and the variation, if any, is calculated.

## Unfixed Bugs
 - The app asks the user twice to enter the quantity for items to be counted.
 - The number entered by the user is teh index of teh item in the list.  This is not how I wanted this to work.  The number entered was to be used as the number of iterations in a while loop to select the line items and place them in the 'stock_to_count' worksheet.

## Deplyment
- This was deployed with Heroku.  The live links are:
  -  Heroku: https://stock-control-cycle-count-1c1d4bfb310f.herokuapp.com/
  -  Github: https://github.com/BwhelanKK/stock-control.git
  -  googlehseets: https://docs.google.com/spreadsheets/d/1N0MxCKR1aa3Bm-LRqRPR20_ECRRxNN2-6_hCql6jVlM/edit#gid=1538997195
 
## Credits:
 - I used the 'love-sandwiches' codealong to help with some of teh gspread function exampls.
 - gspread documentation







