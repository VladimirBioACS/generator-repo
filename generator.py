import os
import sys
import random

def generate_random_bytes(file_size):
    return bytes(random.getrandbits(8) for _ in range(file_size))

def write_bytes_to_file(byte_array, file_name):
    with open(file_name, 'wb') as file:
        file.write(byte_array)

def main():
    try:
        print("=======Simple test data generator=======")
        file_size = int(input("Enter the desired file size in bytes: "))
        byte_array = generate_random_bytes(file_size)
        output_file = str(file_size) + "_bytes_test_data.bin" 
        write_bytes_to_file(byte_array, output_file)

        print(f"Random byte array of size {file_size} has been written to {output_file}")

    except Exception as e:
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    main()