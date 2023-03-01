"""
The provided code is a Python script that scans an input file for valid tokens in a custom programming language called "SPL" (Simple Programming Language)
and saves them to an output file. The script consists of several functions, each of which performs a specific task in the tokenization process.

Here is the documentation for each function:

1. class Token:
    This is a class that represents a single token in the SPL language. Each token has a type, a value, and a pointer to the next token in the linked list.
    __init__(self, token_type, value): This is the constructor method for the Token class. It takes two parameters: token_type and value. These parameters
    are used to set the type and value of the Token object, respectively. It also initializes the next attribute of the Token object to None.

2. class LinkedList:
    This is a class that represents a linked list of tokens in the SPL language. It has a single attribute, head, which is a pointer to the first token in
    the list.
    >> __init__(self): This is the constructor method for the LinkedList class. It initializes the head attribute to None.
    >> add(self, token): This method adds a new token to the linked list. It takes a single parameter, token, which is a Token object. If the linked list
       is empty (i.e., head is None), it sets the head attribute to the new token. Otherwise, it traverses the list until it finds the last token and sets
       the next attribute of that token to the new token.

3. def is_valid_identifier(token):
    This function takes a single parameter, token, which is a string. It returns True if the token is a valid identifier in the SPL language, and False
    otherwise. An identifier is considered valid if it consists entirely of letters, digits, and/or underscores, and does not begin with a digit.

4. def tokenize(line):
    This function takes a single parameter, line, which is a string representing a line of code in the SPL language. It tokenizes the line into a list
    of tokens, using the following rules:
    >> Alphanumeric characters and underscores are considered part of a token.
    >> Any other character is considered a separate token.
    >> Whitespace and newlines are ignored.
    The function returns a list of token strings.

5. def parse_tokens(tokens):
    This function takes a list of token strings as input and converts it to a linked list of Token objects. It iterates over each token in the list and
    creates a new Token object with the appropriate type and value. The Token object is then added to the linked list using the add method of the
    LinkedList class.

6. def scan_file(input_file_path, output_file_path):
    This function is the main driver of the tokenization process. It takes two parameters: input_file_path, which is the path to the input file, and
    output_file_path, which is the path to the output file. It reads each line of the input file, tokenizes it using the tokenize function, and then
    converts the list of tokens to a linked list using the parse_tokens function. The resulting linked list is written to the output file, with each
    token type and value separated by a colon and space. If an error is encountered during the tokenization process, the function prints an error
    message and exits early.

7. Example usage:
    The last line of the script demonstrates how to use the scan_file function to tokenize an input
"""


# Define a Token class to represent a single token
class Token:
    def __init__(self, token_type, value):
        # Initialize the Token with a type and a value
        self.type = token_type
        self.value = value
        # Initialize the "next" attribute to None
        self.next = None


# Define a LinkedList class to represent a linked list of Tokens
class LinkedList:
    def __init__(self):
        # Initialize the LinkedList with a head attribute set to None
        self.head = None

    def add(self, token):
        # Add a new Token to the end of the LinkedList
        if self.head is None:
            # If the LinkedList is empty, set the head to the new Token
            self.head = token
        else:
            # Otherwise, iterate through the LinkedList to find the end
            current = self.head
            while current.next is not None:
                current = current.next
            # Add the new Token to the end of the LinkedList
            current.next = token

def is_valid_identifier(token):
    # Check if a given string is a valid identifier
    return token.isalpha() or (token[0] == '_' and token[1:].isalnum())

def tokenize(line):
    # Tokenize a line of text into a list of individual Tokens
    tokens = []
    current_token = ""
    for char in line:
        if char.isalnum() or char == '_':
            # If the character is alphanumeric or an underscore, add it to the current Token
            current_token += char
        else:
            # Otherwise, if the current Token is not empty, add it to the list of Tokens
            if current_token:
                tokens.append(current_token)
                current_token = ""
            # If the character is not a space or newline, add it as its own Token
            if char != ' ' and char != '\n':
                tokens.append(char)
    # Add the final Token (if there is one) to the list of Tokens
    if current_token:
        tokens.append(current_token)
    return tokens


def parse_tokens(tokens):
    # Parse a list of Tokens into a LinkedList of Tokens
    linked_list = LinkedList()
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token.isnumeric():
            # If the Token is a number, add it to the LinkedList with type "NUMBER"
            linked_list.add(Token("NUMBER", token))
        elif is_valid_identifier(token):
            # If the Token is a valid identifier, add it to the LinkedList with type "IDENTIFIER"
            linked_list.add(Token("IDENTIFIER", token))
        elif token in ("+", "-", "*", "/", "%"):
            # If the Token is an operator, add it to the LinkedList with type "OPERATOR"
            linked_list.add(Token("OPERATOR", token))
        elif token == "=":
            # If the Token is an assignment operator, add it to the LinkedList with type "ASSIGNMENT"
            linked_list.add(Token("ASSIGNMENT", token))
        elif token == "(":
            # If the Token is a left parenthesis, add it to the LinkedList with type "LEFT_PAREN"
            linked_list.add(Token("LEFT_PAREN", token))
        elif token == ")":
            # If the Token is a right parenthesis, add it to the LinkedList with type "RIGHT_PAREN"
            linked_list.add(Token("RIGHT_PAREN", token))
        else:
            # If the Token is not recognized, raise a ValueError
            raise ValueError(f"Invalid token: {token}")
            # Increment the index to move on to the next Token
        i += 1
        return linked_list


def scan_file(input_file_path, output_file_path):
    # Open the input file in read mode and the output file in write mode using a with block
    with open(input_file_path, "r") as input_file, open(output_file_path, "w") as output_file:

        # Create an empty linked list to store the parsed tokens
        linked_list = LinkedList()

        # Initialize a variable to keep track of the current line number being processed
        line_number = 0

        # Loop through each line in the input file
        for line in input_file:

            # Increment the line number
            line_number += 1

            # Try to tokenize and parse the current line of text
            try:

                # Tokenize the current line of text and store the resulting tokens in a list
                tokens = tokenize(line)

                # Parse the list of tokens into a linked list of Token objects
                parsed_list = parse_tokens(tokens)

                # Add the head of the parsed linked list to the main linked list
                linked_list.add(parsed_list.head)

            # If an error occurs during tokenization or parsing, print an error message and exit the function
            except ValueError as error:
                print(f"Error on line {line_number}: {error}")
                return

        # Write each token in the linked list to the output file
        current = linked_list.head
        while current is not None:
            output_file.write(f"{current.type}: {current.value}\n")
            current = current.next


# Example usage:
scan_file("input.txt", "output.txt")
