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


class Token:
    def __init__(self, token_type, value):
        self.type = token_type
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, token):
        if self.head is None:
            self.head = token
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = token


def is_valid_identifier(token):
    # Check if the token is a valid identifier
    return token.isalpha() or (token[0] == '_' and token[1:].isalnum())


def tokenize(line):
    # Tokenize a line of text into a list of tokens
    tokens = []
    current_token = ""
    for char in line:
        if char.isalnum() or char == '_':
            current_token += char
        else:
            if current_token:
                tokens.append(current_token)
                current_token = ""
            if char != ' ' and char != '\n':
                tokens.append(char)
    if current_token:
        tokens.append(current_token)
    return tokens


def parse_tokens(tokens):
    # Parse a list of tokens into a linked list
    linked_list = LinkedList()
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token.isnumeric():
            linked_list.add(Token("NUMBER", token))
        elif is_valid_identifier(token):
            linked_list.add(Token("IDENTIFIER", token))
        elif token in ("+", "-", "*", "/", "%"):
            linked_list.add(Token("OPERATOR", token))
        elif token == "=":
            linked_list.add(Token("ASSIGNMENT", token))
        elif token == "(":
            linked_list.add(Token("LEFT_PAREN", token))
        elif token == ")":
            linked_list.add(Token("RIGHT_PAREN", token))
        else:
            raise ValueError(f"Invalid token: {token}")
        i += 1
    return linked_list


def scan_file(input_file_path, output_file_path):
    # Scan an input file for valid SPL tokens and save them to a linked list in an output file
    with open(input_file_path, "r") as input_file, open(output_file_path, "w") as output_file:
        linked_list = LinkedList()
        line_number = 0
        for line in input_file:
            line_number += 1
            try:
                tokens = tokenize(line)
                parsed_list = parse_tokens(tokens)
                linked_list.add(parsed_list.head)
            except ValueError as error:
                print(f"Error on line {line_number}: {error}")
                return
        current = linked_list.head
        while current is not None:
            output_file.write(f"{current.type}: {current.value}\n")
            current = current.next


# Example usage:
scan_file("input.txt", "output.txt")
