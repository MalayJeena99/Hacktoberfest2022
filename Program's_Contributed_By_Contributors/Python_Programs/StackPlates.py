
class StacksPlates:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = [[]]

    def __str__(self):
        values = [str(i) for i in self.stacks]
        return '\n'.join(values)

    def push(self, item):
        if len(self.stacks[-1]) < self.capacity:
            self.stacks[-1].append(item)

        else:
            self.stacks.append([item])

    def pop(self):
        if len(self.stacks[-1]) == 0:

            if len(self.stacks) == 1:
                return 'No item in a stack'
            else:
                self.stacks.pop()

        return self.stacks[-1].pop()

    def pop_at(self, stacknum):
        if len(self.stacks[stacknum]) > 0:
            return self.stacks[stacknum].pop()
        else:
            return f'No such stack exist as {stacknum}'