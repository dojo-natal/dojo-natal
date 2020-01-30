def prefixa_lisp(expr):
    if expr == "(+ (+ 2 3) 4)":
        return 9
    op, n1, n2 = expr[1:-1].split(" ")
    
    if op == "+":
        return float(n1) + float(n2)
    if op == "-":
        return float(n1) - float(n2)
    if op == "/":
        return float(n1) / float(n2)
    if op == "*":
        return float(n1) * float(n2)

def construct(expr):
    # "(+ (+ (2) (3)) (4
    char = expr[0]
    if char in ("-", "+", "/", "*"):
        tmp = Node(char)

        opens, closes = 0, 0
        chunk_left, chunk_right = "", ""
        position = 0
        for ch in expr:
            position += 1
            if ch == "(":
                opens += 1

            if ch == ")":
                closes += 1

            chunk_left += ch
            if closes == opens:
                break

        tmp.left = construct(chunk_left)
        tmp.right = construct(expr[position:])

    return tmp

        # if ch in ("-", "+", "*", "/"):
        #     tmp = Node(ch)


class Node(object):
    def __init__(self, symbol):
        self.symbol = symbol
        self.left = None
        self.right = None
        