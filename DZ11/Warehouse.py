class Warehouse:
    length = 1000
    width = 500
    height = 20
    # Словарь подразделений с техникой
    dict_of_company_units = {'scan_unit': [], 'print_unit': [], 'xerox_unit': []}

    # Классовым методом создаем добавление техники в словарь подразделений
    @classmethod
    def add_equipment(cls, equip):
        if type(equip) == Printer:
            cls.dict_of_company_units['print_unit'].append(equip.name)
        elif type(equip) == Scanner:
            cls.dict_of_company_units['scan_unit'].append(equip.name)
        elif type(equip) == Xerox:
            cls.dict_of_company_units['xerox_unit'].append(equip.name)
        else:
            print('This stuff is not office equipment')


class OfficeEquipment:
    material = 'plastic + metal'
    price = 'some_price'

    def __init__(self, name):
        self.name = name


class Printer(OfficeEquipment):
    do_print = True


class Scanner(OfficeEquipment):
    do_scan = True


class Xerox(OfficeEquipment):
    do_xer = True


if __name__ == '__main__':
    printer_1 = Printer('Epson')
    Warehouse.add_equipment(printer_1)
    print(Warehouse.dict_of_company_units)
