from abc import ABCMeta, abstractmethod


class ComputerComponent(metaclass=ABCMeta):
    """元件，所有子配件的基類別"""
    def __init__(self, name):
        self._name = name

    @abstractmethod
    def show_info(self, indent=''):
        pass

    def is_composite(self):
        return False

    def startup(self, indent=''):
        print(f'{indent}{self._name}準備開始工作...')

    def shutdown(self, indent=''):
        print(f'{indent}{self._name}即將結束工作...')


class CPU(ComputerComponent):
    """中央處理氣"""
    def __init__(self, name):
        super().__init__(name)

    def show_info(self, indent=''):
        print(f'{indent}CPU{self._name}，可以進行高速運算。')


class MemoryCard(ComputerComponent):
    """記憶體條"""
    def __init__(self, name):
        super().__init__(name)

    def show_info(self, indent=''):
        print(f'{indent}記憶體{self._name}，可以緩存資料，讀寫速度快。')


class HardDisk(ComputerComponent):
    """硬碟"""
    def __init__(self, name):
        super().__init__(name)

    def show_info(self, indent=''):
        print(f'{indent}硬碟{self._name}，可以永久儲存資料，容量大。')


class GraphicsCard(ComputerComponent):
    """顯卡"""
    def __init__(self, name):
        super().__init__(name)

    def show_info(self, indent=''):
        print(f'{indent}顯示卡{self._name}，可以高速計算和處理圖形圖像。')


class Battery(ComputerComponent):
    """電源"""
    def __init__(self, name):
        super().__init__(name)

    def show_info(self, indent=''):
        print(f'{indent}電源{self._name}，可以持續提供主機板和外接配件供電。')


class Fan(ComputerComponent):
    """風扇"""
    def __init__(self, name):
        super().__init__(name)

    def show_info(self, indent=''):
        print(f'{indent}風扇{self._name}，輔助CPU散熱。')


class Display(ComputerComponent):
    """顯示器"""
    def __init__(self, name):
        super().__init__(name)

    def show_info(self, indent=''):
        print(f'{indent}顯示器{self._name}，負責內容的顯示。')


class ComputerComposite(ComputerComponent):
    """配件組合器"""
    def __init__(self, name):
        super().__init__(name)
        self._components = []

    def show_info(self, indent=''):
        print(f'{self._name}，由以下部件組成: ')
        indent += '\t'
        for element in self._components:
            element.show_info(indent)

    def is_composite(self):
        return True

    def add_component(self, component):
        self._components.append(component)

    def remove_component(self, component):
        self._components.remove(component)

    def startup(self, indent=''):
        super().startup(indent)
        indent += '\t'
        for element in self._components:
            element.startup(indent)

    def shutdown(self, indent=''):
        super().shutdown(indent)
        indent += '\t'
        for element in self._components:
            element.shutdown(indent)


class MainBoard(ComputerComposite):
    """主機板"""
    def __init__(self, name):
        super().__init__(name)

    def show_info(self, indent=''):
        print(f'{indent}主機版: ', end='')
        super().show_info(indent)


class ComputerCase(ComputerComposite):
    """主機殼"""
    def __init__(self, name):
        super().__init__(name)

    def show_info(self, indent=''):
        print(f'{indent}主機殼: ', end='')
        super().show_info(indent)


class Computer(ComputerComposite):
    """電腦"""
    def __init__(self, name):
        super().__init__(name)

    def show_info(self, indent=''):
        print(f'{indent}電腦: ', end='')
        super().show_info(indent)


def test_computer():
    main_board = MainBoard('GIGABYTE Z170M M-ATX 主機板')
    main_board.add_component(CPU('Intel Core i5-6600K CPU 中央處理器'))
    main_board.add_component(MemoryCard('Kingston Fury DDR4 記憶體'))
    main_board.add_component(HardDisk('Kingston V300 硬碟'))
    main_board.add_component(GraphicsCard('Colorful iGame750 顯示卡'))

    computer_case = ComputerCase('SAMA MATA 主機殼')
    computer_case.add_component(main_board)
    computer_case.add_component(Battery('Antec VP 450P 電源'))
    computer_case.add_component(Fan('DEEPCOOL 120T 風扇'))

    computer = Computer('Tony DIY 電腦')
    computer.add_component(computer_case)
    computer.add_component(Display('AOC LV243XIP 螢幕'))

    computer.show_info('')
    print('\n開機過程: ')
    computer.startup('')
    print('\n關機過程: ')
    computer.shutdown('')


test_computer()


