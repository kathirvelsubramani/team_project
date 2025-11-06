def write_to_file(filename, text):
    with open(filename, 'w') as f:
        f.write(text)

def read_from_file(filename):
    with open(filename, 'r') as f:
        return f.read()
