# File: Bai_tap_11/mo_doc_tap_tin.py
from xu_ly_tap_tin import read_file

def main():
    filename = input("Nhập tên tập tin: ")
    content = read_file(filename)
    print("\nNội dung tập tin:")
    print(content)

if __name__ == "__main__":
    main()
