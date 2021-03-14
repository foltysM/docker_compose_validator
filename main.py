# Docker Compose YAML validator
# Michal Foltys, 2021-03-02

from lexer import *
from mynewparser import *

if __name__ == "__main__":
    with open("compose.yaml", "r") as file:
        input_txt = file.read()

# print(input_txt)

lexer = Lexer(input_txt)
# for i in lexer.tokens:
#     print(i)
# print(" ")
parser = Parser(lexer)
parser.start()
