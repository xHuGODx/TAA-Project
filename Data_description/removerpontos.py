def removedots():
    """
    Remove dots from the text in the file 'data.txt'.
    """
    with open('base_data/adultdataset.csv', 'r') as file:
        text = file.read()

    # Remove dots
    text = text.replace('.', '')

    with open('base_data/data.txt', 'w') as file:
        file.write(text)

def replace_question_marks():
    """
    Replace question marks with NaN in the text file 'data.txt'.
    """
    with open('base_data/data.txt', 'r') as file:
        text = file.read()

    # Replace question marks with NaN
    text = text.replace('?', 'NaN')

    with open('base_data/data.txt', 'w') as file:
        file.write(text)

if __name__ == "__main__":
    removedots()
    replace_question_marks()
    print("Dots removed from the file 'data.txt'.")