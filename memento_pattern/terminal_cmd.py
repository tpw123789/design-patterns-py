from memento_pattern.memento_pattern_framework import Memento, Originator, Caretaker
import logging


class TerminalCmd(Originator):
    """終端命令"""
    def __init__(self, text):
        self.cmd_name = ''
        self.cmd_args = []
        self.parse_cmd(text)

    def parse_cmd(self, text):
        """從字串中解析命令"""
        # text第二欄位開始所有參數list
        sub_strings = self.get_arguments_from_string(text, ' ')
        if len(sub_strings) > 0:
            self.cmd_name = sub_strings[0]
        # 獲取第一個欄位之後的所有字元作為命令的參數
        if len(sub_strings) > 1:
            self.cmd_args = sub_strings[1:]

    @staticmethod
    def get_arguments_from_string(text, split_flag):
        """透過split flag進行分割，獲得參數陣列"""
        if split_flag == '':
            logging.warning('split flag 為空!')
        data = text.split(split_flag)
        result = []
        for item in data:
            # 過濾多餘空格
            item.strip()
            if item != '':
                result.append(item)
        return result

    def show_cmd(self):
        print(f'{self.cmd_name}{self.cmd_args}')


class TerminalCaretaker(Caretaker):
    """終端命令的備忘錄管理類別"""
    def show_history_cmd(self):
        """顯示歷史命令"""
        for key, obj in self._mementos.items():
            name = ''
            value = []
            if obj.cmd_name:
                name = obj.cmd_name
            if obj.cmd_args:
                value = obj.cmd_args
            print(f'第{key}條命令: {name}{value}')


def test_terminal():
    cmd_index = 0
    caretaker = TerminalCaretaker()
    current_cmd = TerminalCmd('')
    while True:
        string_cmd = input('請輸入指令: ')
        string_cmd = string_cmd.lower()
        if string_cmd.startswith('q'):
            exit(0)
        elif string_cmd.startswith('h'):
            caretaker.show_history_cmd()
        # 透過'!'符號獲取歷史的某個命令
        elif string_cmd.startswith('!'):
            index = int(string_cmd[1:])
            current_cmd.restore_from_memento(caretaker.get_memento(index))
            current_cmd.show_cmd()
        else:
            current_cmd = TerminalCmd(string_cmd)
            current_cmd.show_cmd()
            caretaker.add_memento(cmd_index, current_cmd.create_memento())
            cmd_index += 1


test_terminal()



