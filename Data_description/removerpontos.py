def removedots():
    """
    Remove dots from the text in the file 'data.txt'.
    """
    with open('base_data/adult.test', 'r') as file:
        text = file.read()

    # Remove dots
    text = text.replace('.', '')

    with open('base_data/data.txt', 'w') as file:
        file.write(text)

if __name__ == "__main__":
    removedots()
    print("Dots removed from the file 'data.txt'.")