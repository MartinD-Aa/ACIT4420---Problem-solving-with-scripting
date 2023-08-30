def replace_and_save(filename, target_name, new_name):
    with open(filename, 'r') as file:
        content = file.read()

    content = content.replace(target_name, new_name)

    new_filename = filename.replace('.txt', '_modified.txt')
    with open(new_filename, 'w') as new_file:
        new_file.write(content)

    print(f"File saved as {new_filename}")

if __name__ == "__main__":
    target_name = "Guido van Rossum"
    new_name = "Martin"
    
    replace_and_save("python.txt", target_name, new_name)