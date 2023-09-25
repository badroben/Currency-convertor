import tkinter as tk
import requests

APP_ID = 'YOUR_APP_ID'

# This function fetches current exchange rates from the openexchangerates API
def fetch_exchange_rates():
    target_currency = combo_to_currency.get()
    url = f"https://openexchangerates.org/api/latest.json?app_id={APP_ID}&symbols={target_currency}"

    try:
        response = requests.get(url)
        data = response.json()
        exchange_rate = data['rates'][target_currency]
        return exchange_rate
    except requests.exceptions.RequestException:
        return None

# This function converts the given amount using the exchange rate fetched
def convert_currency():
    try:
        amount = float(entry_amount.get())
        # get the current exchange rate from the API result
        exchange_rate = fetch_exchange_rates()
        
        if exchange_rate is None:
            result_label.config(text="Result: Unable to fetch exchange rate")
        else:
            # convert the amount using the rate
            converted_amount = amount * exchange_rate
            result_label.config(text=f"Result: {amount} {combo_from_currency.get()} = {converted_amount:.2f} {combo_to_currency.get()}")
    except ValueError:
        result_label.config(text="Result: Please enter a valid amount")

# Create the main window
root = tk.Tk()
root.title("Currency Converter")

# Label for the title
title_label = tk.Label(root, text="Currency Converter", font=("Arial", 16))
title_label.pack(pady=10)

# Entry for entering the amount
entry_amount = tk.Entry(root, width=20)
entry_amount.pack(pady=5)

# Dropdown menu for selecting the 'from' currency
combo_from_currency = tk.StringVar()
combo_from_currency.set("USD")
from_currency_label = tk.Label(root, text="From Currency:")
from_currency_label.pack()
# the only option available in the free plan is USD :/
to_currency_menu = tk.OptionMenu(root, combo_from_currency, "USD") 
to_currency_menu.pack()

# Dropdown menu for selecting the 'to' currency
combo_to_currency = tk.StringVar()
combo_to_currency.set("EUR")
to_currency_label = tk.Label(root, text="To Currency:")
to_currency_label.pack()
to_currency_menu = tk.OptionMenu(root, combo_to_currency, "DZD", "EUR", "GBP", "JPY") 
to_currency_menu.pack()

# Button to perform the conversion
convert_button = tk.Button(root, text="Convert", command=convert_currency)
convert_button.pack(pady=10)

# Label to display the result
result_label = tk.Label(root, text="Result:", font=("Arial", 14))
result_label.pack()

# Start the GUI application
root.mainloop()
