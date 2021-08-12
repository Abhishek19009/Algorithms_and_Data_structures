# String splitting algorithm is basic but will be used multiple times so know how to create it
# String splitter will split the string into list based on the special character

def string_splitter(string, replace):
    string_temp = ""
    string_list = []
    for char in string:
        if char != replace:
            string_temp += char
        else:
            string_list.append(string_temp)
            string_temp = ""
    string_list.append(string_temp)
    return string_list


def main():
    string = input("Enter the string: ")
    split_list = string_splitter(string, " ")
    print(split_list)


if __name__ == "__main__":
    main()