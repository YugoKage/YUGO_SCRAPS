
filepath = "/Users/mattlyndonabuel/Desktop/CODES/PYTHON/TXT_FILES/Scrap4File.txt"

def read_file_content(filepath):

    try:
        with open(filepath, "r") as f:
            content = f.read()
            print(f"Content:\n{content}")

    except FileNotFoundError:
        print(f"Error: The file was not found.")

    except Exception as e:
        print(f"An error occurred: {e}")

print(read_file_content(filepath))
