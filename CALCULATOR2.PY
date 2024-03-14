from tkinter import *
import requests

previous_result = None

#CURRENCY CONVERSION
def convert_currency(amount, from_currency, to_currency):
    # Exchange rates (INR=>USD)
    exchange_rates = {
        ('EUR', 'USD'): 1.18,
        ('EUR', 'INR'): 89.50,  # Add the exchange rate for INR to EUR
        ('INR', 'USD'): 0.012,
        ('INR', 'EUR'): 0.011,
        ('USD', 'EUR'): 0.91,
        ('USD', 'INR'): 82.75,
    }
    
    try:
        # If currencies are the same, no conversion needed
        if from_currency == to_currency:
            return amount
        
        # If the conversion is supported, perform it
        if (from_currency, to_currency) in exchange_rates:
            exchange_rate = exchange_rates[(from_currency, to_currency)]
            converted_amount = amount * exchange_rate
            return converted_amount
        else:
            print(f"Error: Conversion not supported for {from_currency} to {to_currency}")
            return None
    except Exception as e:
        print(f"Error during currency conversion: {e}")
        return None

# Function to open the currency converter window
def open_currency_converter():
    converter_window = Toplevel(window)
    converter_window.title("Currency Converter")

    amount_label = Label(converter_window, text="Amount:",)
    amount_label.grid(row=0, column=0, padx=10, pady=10)

    amount_entry = Entry(converter_window, font=('Helvetica', 16))
    amount_entry.grid(row=0, column=1, padx=10, pady=10)

    from_currency_label = Label(converter_window, text="From Currency:")
    from_currency_label.grid(row=1, column=0, padx=10, pady=10)

    from_currency_var = StringVar()
    from_currency_var.set("INR")  # Default currency is USD

    from_currency_options = ["USD", "EUR", 'INR']  # Add more currencies as needed
    from_currency_menu = OptionMenu(converter_window, from_currency_var, *from_currency_options)
    from_currency_menu.grid(row=1, column=1, padx=10, pady=10)

    to_currency_label = Label(converter_window, text="To Currency:")
    to_currency_label.grid(row=2, column=0, padx=10, pady=10)

    to_currency_var = StringVar()
    to_currency_var.set("USD")  # Default currency is USD

    to_currency_options = ["USD", "EUR", "INR"]  # Add more currencies as needed
    to_currency_menu = OptionMenu(converter_window, to_currency_var, *to_currency_options)
    to_currency_menu.grid(row=2, column=1, padx=10, pady=10)

    result_label = Label(converter_window, text="")
    result_label.grid(row=3, column=0, columnspan=2, pady=10)

    convert_button = Button(converter_window, text="Convert", padx=20, pady=20, font=('Helvetica', 16),
                            command=lambda: perform_conversion(amount_entry.get(), from_currency_var.get(), to_currency_var.get(), result_label))
    convert_button.grid(row=4, column=0, columnspan=2, pady=10)

# Function to perform the currency conversion and display the result
def perform_conversion(amount_str, from_currency, to_currency, result_label):
    try:
        amount = float(amount_str)
        converted_amount = convert_currency(amount, from_currency, to_currency)

        if converted_amount is not None:
            result_label.config(text=f"Result: {amount} {from_currency} = {converted_amount:.2f} {to_currency}")
            save_to_file(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
    except ValueError:
        result_label.config(text="Error: Please enter a valid number for the amount.")

#TEMPRATURE CONVERSION
def convert_temperature(temperature, from_unit, to_unit):
    try:
        if from_unit == to_unit:
            return temperature
        
        if from_unit == 'Celsius' and to_unit == 'Fahrenheit':
            converted_temperature = (temperature * 9/5) + 32
        elif from_unit == 'Fahrenheit' and to_unit == 'Celsius':
            converted_temperature = (temperature - 32) * 5/9
        elif from_unit == 'Celsius' and to_unit == 'Kelvin':
            converted_temperature = temperature + 273.15
        elif from_unit == 'Kelvin' and to_unit == 'Celsius':
            converted_temperature = temperature - 273.15
        elif from_unit == 'Fahrenheit' and to_unit == 'Kelvin':
            converted_temperature = (temperature + 459.67) * 5/9
        elif from_unit == 'Kelvin' and to_unit == 'Fahrenheit':
            converted_temperature = temperature * 9/5 - 459.67
        else:
            print(f"Error: Conversion not supported for {from_unit} to {to_unit}")
            return None
        
        return converted_temperature
    except Exception as e:
        print(f"Error during temperature conversion: {e}")
        return None

def open_temperature_converter():
    temp_converter_window = Toplevel(window)
    temp_converter_window.title("Temperature Converter")

    temperature_label = Label(temp_converter_window, text="Temperature:")
    temperature_label.grid(row=0, column=0, padx=10, pady=10)

    temperature_entry = Entry(temp_converter_window, font=('Helvetica', 16))
    temperature_entry.grid(row=0, column=1, padx=10, pady=10)

    from_unit_label = Label(temp_converter_window, text="From Unit:")
    from_unit_label.grid(row=1, column=0, padx=10, pady=10)

    from_unit_var = StringVar()
    from_unit_var.set("Celsius")

    from_unit_options = ["Celsius", "Fahrenheit", "Kelvin"]
    from_unit_menu = OptionMenu(temp_converter_window, from_unit_var, *from_unit_options)
    from_unit_menu.grid(row=1, column=1, padx=10, pady=10)

    to_unit_label = Label(temp_converter_window, text="To Unit:")
    to_unit_label.grid(row=2, column=0, padx=10, pady=10)

    to_unit_var = StringVar()
    to_unit_var.set("Fahrenheit")

    to_unit_options = ["Celsius", "Fahrenheit", "Kelvin"]
    to_unit_menu = OptionMenu(temp_converter_window, to_unit_var, *to_unit_options)
    to_unit_menu.grid(row=2, column=1, padx=10, pady=10)

    result_label = Label(temp_converter_window, text="")
    result_label.grid(row=3, column=0, columnspan=2, pady=10)

    convert_button = Button(temp_converter_window, text="Convert", padx=20, pady=20, font=('Helvetica', 16),
                            command=lambda: perform_temperature_conversion(temperature_entry.get(), from_unit_var.get(), to_unit_var.get(), result_label))
    convert_button.grid(row=4, column=0, columnspan=2, pady=10)

# Function to perform the temperature conversion and display the result
def perform_temperature_conversion(temperature_str, from_unit, to_unit, result_label):
    try:
        temperature = float(temperature_str)
        converted_temperature = convert_temperature(temperature, from_unit, to_unit)

        if converted_temperature is not None:
            result_str = f"Result: {temperature} {from_unit} = {converted_temperature:.2f} {to_unit}"
            result_label.config(text=result_str)
            save_to_file(result_str)  # Save the result to calculator history
    except ValueError:
        result_label.config(text="Error: Please enter a valid number for the temperature.")

#MAIN WINDOW
window = Tk()

result_var = StringVar()
result_var.set('0')
expression = ''

#window.geometry('300x400')
window.configure(bg='#1e1e1e')
window.title('CALCULATOR')
icon = PhotoImage(file='calc.png')
window.iconphoto(True, icon)

entry = Entry(window, font=('Helvetica', 16), textvariable=result_var, bd=10)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    button = Button(window, text=text, padx=20, pady=20, font=('Helvetica', 16),
                    command=lambda t=text: button_click(t), fg= 'white',bg = '#008080', 
                    activebackground = 'white', activeforeground='#008080', )
    button.grid(row=row, column=col)

ans_button = Button(window, text="ANS", padx=6, pady=20, font=('Helvetica', 16),
                    command=lambda: button_click('ANS'), fg='white', bg='#008080',
                    activebackground='white', activeforeground='#008080')
ans_button.grid(row=5, column=0,)

del_button = Button(window, text="DEL", padx=6, pady=20, font=('Helvetica', 16),
                    command=lambda: button_click('DEL'), fg='white', bg='#008080',
                    activebackground='white', activeforeground='#008080')
del_button.grid(row=5, column=1,)

def button_click(text):
    global expression, previous_result
    
    if text == '=':
        try:
            result = str(eval(expression))
            result_var.set(result)
            save_to_file(result)
            previous_result = result  # Store the current result as previous result
            expression = ""
        except Exception as e:
            result_var.set("Error")

    elif text == 'C':
        expression = ""
        result_var.set("0")

    elif text == 'ANS':
        if previous_result is not None:
            expression += str(previous_result)
            result_var.set(expression)

    elif text == 'DEL':
        delete_last_character()

    else:
        expression += text
        result_var.set(expression)

# Function to delete the last character from the expression
def delete_last_character():
    global expression
    if expression:
        expression = expression[:-1]
        result_var.set(expression)

def save_to_file(result):
    global expression
    if expression == 'ANS':  # Check if the expression is 'ANS'
        expression = previous_result  # Set the expression to the previous result
    with open('calculator_history.txt', 'a') as file:
        file.write(f"{expression} = {result}\n")


currency_converter_button = Button(window, text="Currency Converter", padx=10, pady=10, 
                                   font=('Helvetica', 16), command=open_currency_converter,
                                   fg = 'white', bg = '#008080', activebackground='white', activeforeground= '#008080')
currency_converter_button.grid(row=6, column=0, columnspan=4, pady=5)

temperature_converter_button = Button(window, text="Temperature Converter", padx=10, pady=10,
                                      font=('Helvetica', 16), command=open_temperature_converter,
                                      fg='white', bg='#008080', activebackground='white', activeforeground='#008080')
temperature_converter_button.grid(row=7, column=0, columnspan=4, pady=5)

window.mainloop()
