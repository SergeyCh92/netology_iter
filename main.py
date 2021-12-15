nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]]


class MyIter:

    def __init__(self, nest_list: list):
        self.nest_list = nest_list
        self.cursor = 0
        self.cursor_nested = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.cursor_nested + 1 < len(self.nest_list[self.cursor]):
            self.cursor_nested += 1
        elif self.cursor + 1 < len(self.nest_list):
            self.cursor += 1
            self.cursor_nested = 0
        else:
            raise StopIteration
        return self.nest_list[self.cursor][self.cursor_nested]


def my_gen(nest_list: list):
    len_list = 0
    cursor = 0
    while len_list < len(nest_list):
        if cursor < len(nest_list[len_list]):
            yield nest_list[len_list][cursor]
            cursor += 1
        elif len_list + 1 != len(nest_list):
            cursor = 0
            len_list += 1
            yield nest_list[len_list][cursor]
            cursor += 1
        else:
            break


for el in MyIter(nested_list):
    print(el)

flat_list = [item for item in MyIter(nested_list)]
print(flat_list)

for i in my_gen(nested_list):
    print(i)
