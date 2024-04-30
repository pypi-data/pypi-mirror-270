from typing import TypeVar, Generic


Output = TypeVar('Output')
Input = TypeVar('Input')


class Flexa(Generic[Output, Input]):
    def __init__(self):
        self.pairs = []

    def contains_input(self, input: Input) -> bool:
        input_column_index = 1
        mapped_pairs = self.mapped_pairs(input_column_index)
        return input in mapped_pairs

    def mapped_pairs(self, input_column_index) -> list[Input]:
        return list(map(lambda pair: pair[input_column_index], self.pairs))

    def set(self, output: Output, input: Input):
        if self.contains_input(input):
            raise ValueError("Invalid input value when set pair but input exists")
        self.pairs.append([output, input])

    def result(self, input: Input) -> Output:
        if not self.contains_input(input):
            raise ValueError("Invalid input value when output result")
        output_column_index = 0
        input_column_index = 1
        mapped_pairs = self.mapped_pairs(input_column_index)
        row_index = mapped_pairs.index(input)
        return self.pairs[row_index][output_column_index]
