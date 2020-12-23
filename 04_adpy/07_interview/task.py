class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)


def check(txt):
    if len(txt) % 2 != 0:
        return 'Небалансированно'
    s = Stack()
    for char in txt:
        if char == '(' or char == '{' or char == '[':
            s.push(char)
        elif (char == ')' or char == '}' or char == ']') and s.isEmpty():
            return 'Небалансированно'
        elif (char == ')' and s.peek() == '(') or (char == ']' and s.peek() == '[') or (char == '}' and s.peek() == '{'):
            s.pop()

    if s.isEmpty():
        return 'Сбалансировано'
    return 'Небалансированно'


print(check('(((([{}]))))'))
print(check('[([])((([[[]]])))]{()}'))
print(check('{{[()]}}'))
print(check('}{}'))
print(check('{{[(])]}}'))
print(check('[[{())}]'))



