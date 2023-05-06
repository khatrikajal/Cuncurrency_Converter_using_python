from forex_python.converter import CurrencyRates

import tkinter as tk
from currency_converter import CurrencyConverter


def get_exchange_rates(base_currency):
    c = CurrencyRates()
    rates = c.get_rates(base_currency)
    return rates


def convert_currency():
    amount_text = amount_entry.get()
    if not amount_text:
        result_label["text"] = "Please enter a valid amount."
        return

    try:
        amount = float(amount_text)
    except ValueError:
        result_label["text"] = "Invalid amount. Please enter a numeric value."
        return

    from_currency = from_currency_variable.get()
    to_currency = to_currency_variable.get()

    rates = get_exchange_rates(from_currency)
    if rates is None or to_currency not in rates:
        result_label["text"] = "Currency conversion not available."
        return

    exchange_rate = rates[to_currency]
    converted_amount = amount * exchange_rate
    result_label["text"] = f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}"

# Create the GUI window
window = tk.Tk()
window.title("Currency Converter")

# Create the UI components
amount_label = tk.Label(window, text="Amount:")
amount_label.pack()

amount_entry = tk.Entry(window, width=50)
amount_entry.pack()

from_currency_label = tk.Label(window, text="From Currency:")
from_currency_label.pack()

from_currency_variable = tk.StringVar(window)
from_currency_variable.set("USD")  # Set default currency

from_currency_dropdown = tk.OptionMenu(window, from_currency_variable, "USD", "EUR", "GBP", "JPY")
from_currency_dropdown.pack()

to_currency_label = tk.Label(window, text="To Currency:" )
to_currency_label.pack()

to_currency_variable = tk.StringVar(window)
to_currency_variable.set("EUR")  # Set default currency

to_currency_dropdown = tk.OptionMenu(window, to_currency_variable, "USD", "EUR", "GBP", "JPY")
to_currency_dropdown.pack()


convert_button = tk.Button(window, text="Convert", command=convert_currency)
convert_button.pack()

result_label = tk.Label(window, text="", width=50)  # Adjust the width and height values as desired

result_label.pack()

# Start the GUI event loop
window.mainloop()

