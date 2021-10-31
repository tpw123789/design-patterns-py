from abc import ABCMeta, abstractmethod


class Expression(metaclass=ABCMeta):
    """抽象運算式"""
    @abstractmethod
    def interpreter(self, var):
        pass


class VarExpression(Expression):
    """變數解析器"""
    def __init__(self, key):
        self._key = key

    def interpreter(self, var):
        return var.get(self._key)


class SymbolExpression(Expression):
    """運算子解析器，運算子的抽象類別"""
    def __init__(self, left, right):
        self._left = left
        self._right = right


class AddExpression(SymbolExpression):
    """加法解析器"""
    def __init__(self, left, right):
        super().__init__(left, right)

    def interpreter(self, var):
        return self._left.interpreter(var) + self._right.interpreter(var)


class SubExpression(SymbolExpression):
    """減法解析"""
    def __init__(self, left, right):
        super().__init__(left, right)

    def interpreter(self, var):
        return self._left.interpreter(var) - self._right.interpreter(var)


class Stack:
    """封裝堆疊類別"""
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[len(self.items) - 1]

    def size(self):
        len(self.items)


class Calculator:
    """計算機類別"""
    def __init__(self, expression_text):
        self._expression = self.parse_text(expression_text)

    def parse_text(self, expression_text):
        # 定義一個棧，處理運算先後順序
        stack = Stack()
        left = right = None
        idx = 0
        while idx < len(expression_text):
            if expression_text[idx] == '+':
                left = stack.pop()
                idx += 1
                right = VarExpression(expression_text[idx])
                stack.push(AddExpression(left, right))
            elif expression_text[idx] == '-':
                left = stack.pop()
                idx += 1
                right = VarExpression(expression_text[idx])
                stack.push(SubExpression(left, right))
            else:
                stack.push(VarExpression(expression_text[idx]))
            idx += 1
        return stack.pop()

    def run(self, var):
        return self._expression.interpreter(var)


def test_calculator():
    """獲取運算式"""
    expression_string = input('請輸入運算式:')
    # 獲取各參數的鍵值對
    new_expression, expression_map = get_map_value(expression_string)
    calculator = Calculator(new_expression)
    result = calculator.run(expression_map)
    print(f'運算結果為:{expression_string}={result}')


def get_map_value(expression_string):
    """回傳tuple (字元陣列, 參數對應值字典)"""
    expression_map = {}
    new_expression = []
    # 去除空字元
    expression_string = expression_string.replace(' ', '')
    for i in range(len(expression_string)):
        new_expression.append(expression_string[i])
        if expression_string[i] != '+' and expression_string[i] != '-':
            key = expression_string[i]
            var = input(f'請輸入參數{key}的值:')
            var = var.replace(' ', '')
            expression_map[key] = float(var)
    return new_expression, expression_map


test_calculator()
