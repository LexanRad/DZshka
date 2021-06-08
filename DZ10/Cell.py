# В целом после лекции решил исправить его
class Cell:
    def __init__(self, cells_in):
        self.cells_in = int(cells_in)

    def __add__(self, other):
        return Cell(self.cells_in + other.cells_in)

    def __sub__(self, other):
        result_cells_in = self.cells_in - other.cells_in
        if result_cells_in > 0:
            return Cell(result_cells_in)
        else:
            return 'Невозможно вычесть'

    def __mul__(self, other):
        return Cell(self.cells_in * other.cells_in)

    def __floordiv__(self, other):
        return Cell(self.cells_in // other.cells_in)

    def __str__(self):
        return f'{self.cells_in} cells'

    # Позаимствовал. Мое было совсем не але
    def making_order(self, amount_of_cells_in_row):
        rows_amount, add_to_last_row = \
            divmod(self.cells_in, amount_of_cells_in_row)

        cell_as_string = ''
        for _ in range(rows_amount):
            cell_as_string += f'{"*" * amount_of_cells_in_row}\n'

        return cell_as_string.rstrip() + '*' * add_to_last_row


if __name__ == '__main__':
    cell_1 = Cell(70)
    cell_2 = Cell(60)
    cell_add = cell_1 + cell_2
    cell_sub = cell_1 - cell_2
    cell_mul = cell_1 * cell_2
    cell_div = cell_1 // cell_2
    print(cell_add, cell_sub, cell_mul, cell_div)
    print(cell_add.making_order(5))
