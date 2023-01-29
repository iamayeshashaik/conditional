# Importing Pandas as pd
import pandas as pd

# Creating Table with below details
df = pd.DataFrame.from_dict(
    {
        'Product': ['Table', 'Desktop', 'Bed', 'Dressing Table'],
        'Selling Price': [1500,3000,6000,3800],
        'Profit': [500, 1000, 1200, 800],
        'Shiping mode': ['First Class', 'Second class', 'Same day', 'Standard Class'],
        'Destination': ['Hyderabad', 'Chennai', 'Noida', 'Mumbai'],

    }
)
# print(df)
# Adding Surcharge column based on Shipping mode
def surcharge(x):

        if x == "Same day":
            return 0.2
        
        elif x == "First Class":
            return 0.1

        elif x == "Standard Class":
            return 0.5
        else:
            return 0
df["Surcharge"] = df["Shiping mode"].apply(surcharge)
# print(df)
# Adding Total cost column based on formula total cost = (sales - profit ) * ( 1 + surcharge) and converting to integer values
df['Total Cost'] = ((df['Selling Price']-df['Profit'])*(1+df['Surcharge'])).apply(int)
print(df)


# Output:-
#           Product  Selling Price  Profit    Shiping mode Destination  Surcharge  Total Cost
# 0           Table           1500     500     First Class   Hyderabad        0.1      1100
# 1         Desktop           3000    1000    Second class     Chennai        0.0      2000
# 2             Bed           6000    1200        Same day       Noida        0.2      5760
# 3  Dressing Table           3800     800  Standard Class      Mumbai        0.5      4500