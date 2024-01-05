# File: Bai_tap_11/xu_ly_tap_tin.py

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return f"File '{filename}' not found."
    except Exception as e:
        return f"Error reading file '{filename}': {str(e)}"
