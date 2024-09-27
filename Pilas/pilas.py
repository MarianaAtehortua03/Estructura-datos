class Pila:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return "Error: Pila Vacía"

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            return "Error: Pila Vacía"

    def isEmpty(self):
        return self.items == []

pila = Pila()
pila.push(10)
pila.push(20)
print(pila.peek())  # Devolver 20
print(pila.pop())   # Devolver 20
print(pila.isEmpty()) # Devolver False
print(pila.pop())   # Devolver 10
print(pila.isEmpty()) # Devolver True
