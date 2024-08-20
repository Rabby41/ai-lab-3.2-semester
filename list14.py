# Function to remove empty strings from a list
def remove_empty_strings(string_list):
    # Use list comprehension to filter out empty strings
    return [string for string in string_list if string]


# Main function
def main():
    # Prompt the user to input strings separated by commas
    user_input = input("Enter strings separated by commas: ")

    # Split the input string into a list of strings
    list1 = [s.strip() for s in user_input.split(",")]

    # Display the original list
    print("Original list:", list1)

    # Remove empty strings
    filtered_list = remove_empty_strings(list1)

    # Display the filtered list
    print("Filtered list:", filtered_list)


# Run the main function
if __name__ == "__main__":
    main()
