class Data:
    def __init__(self, data):
        self.data = data

    @classmethod
    def data_out(cls, data):
        cls.data = data
        number = int(cls.data[:2])
        month = int(cls.data[3:5])
        year = int(cls.data[-4:])
        return number, month, year

    @staticmethod
    def data_is_valid(data):
        number = int(data[:2])
        month = int(data[3:5])
        year = int(data[-4:])
        if 0 < number < 31:
            print('Correct number', type(number))
        if 0 < month < 12:
            print('Correct month', type(month))
        if len(data[-4:]) == 4:
            print('Correct year', type(year))
        return number, month, year


if __name__ == '__main__':
    print(Data.data_out('21.04.1993'))
    d1 = Data('30.05.2008')
    print(d1.data_is_valid(d1.data))
