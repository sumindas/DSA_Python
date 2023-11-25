class UndoRedoStack:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []

    def do(self, operation):
        # Perform the operation
        operation()

        # Push the operation to the undo stack
        self.undo_stack.append(operation)

        # Clear the redo stack since a new operation was performed
        self.redo_stack = []

    def undo(self):
        if not self.undo_stack:
            print("Nothing to undo.")
            return

        # Pop the last operation from the undo stack
        operation = self.undo_stack.pop()

        # Perform the inverse of the operation
        operation()

        # Push the operation to the redo stack
        self.redo_stack.append(operation)

    def redo(self):
        if not self.redo_stack:
            print("Nothing to redo.")
            return

        # Pop the last operation from the redo stack
        operation = self.redo_stack.pop()

        # Perform the operation
        operation()

        # Push the operation to the undo stack
        self.undo_stack.append(operation)

# Define some operations
def add():
    global counter
    counter += 1
    print(f"Counter incremented: {counter}")

def subtract():
    global counter
    counter -= 1
    print(f"Counter decremented: {counter}")

# Create an instance of UndoRedoStack
stack = UndoRedoStack()

stack.do(add)
