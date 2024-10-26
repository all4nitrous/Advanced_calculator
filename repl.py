import os
import pandas as pd
import logging
from calculator.operations import add, subtract, multiply, divide
from app.plugins import load_plugins

# Initialize logging
logging.basicConfig(level=os.getenv('LOG_LEVEL', 'INFO').upper())

# Set up calculation history with Pandas
history_file = "calculation_history.csv"
if os.path.exists(history_file):
    history_df = pd.read_csv(history_file)
else:
    history_df = pd.DataFrame(columns=['operation', 'a', 'b', 'result'])

def save_history():
    history_df.to_csv(history_file, index=False)

# Dictionary of core operations
operation_mappings = {
    'add': add,
    'subtract': subtract,
    'multiply': multiply,
    'divide': divide
}

def calculate(a, b, operation):
    try:
        result = operation_mappings[operation](a, b)
        logging.info(f"Performed {operation} on {a} and {b}, result: {result}")
        history_df.loc[len(history_df)] = [operation, a, b, result]
        save_history()
        return result
    except Exception as e:
        logging.error(f"Calculation error: {e}")
        return f"Error: {e}"

def repl():
    print("Calculator REPL: Type 'help' for a list of commands, or 'exit' to quit.")
    plugins = load_plugins()
    while True:
        user_input = input(">> ").strip()
        if user_input in ('exit', 'quit'):
            print("Exiting...")
            break
        elif user_input == 'help':
            print("Available commands: add, subtract, multiply, divide, history, clear_history, plugins")
            print("Use 'add <a> <b>' to perform addition, and similar for other operations.")
            print("Type 'plugins' to list available plugins.")
        elif user_input == 'history':
            print(history_df)
        elif user_input == 'clear_history':
            history_df.drop(history_df.index, inplace=True)
            save_history()
            print("History cleared.")
        elif user_input == 'plugins':
            print("Available plugins:", list(plugins.keys()))
        else:
            try:
                parts = user_input.split()
                if len(parts) == 3 and parts[0] in operation_mappings:
                    op, a, b = parts[0], float(parts[1]), float(parts[2])
                    print("Result:", calculate(a, b, op))
                else:
                    print("Invalid command. Type 'help' for options.")
            except ValueError:
                print("Invalid input format.")

if __name__ == '__main__':
    repl()
