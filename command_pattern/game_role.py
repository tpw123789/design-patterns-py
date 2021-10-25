from abc import ABCMeta, abstractmethod
import time


class GameRole:
    """遊戲的角色"""
    # 每次移動距離
    STEP = 5

    def __init__(self, name):
        self._name = name
        self._x = 0
        self._y = 0
        self._z = 0

    def left_move(self):
        self._x -= self.STEP

    def right_move(self):
        self._x += self.STEP

    def up_move(self):
        self._y += self.STEP

    def down_move(self):
        self._y -= self.STEP

    def jump_move(self):
        self._z += self.STEP

    def squat_move(self):
        self._z -= self.STEP

    def attack(self):
        print(f'{self._name}發動攻擊....')

    def show_position(self):
        print(f'{self._name}的位置: (x:{self._x} y:{self._y} z:{self._z})')


class GameCommand(metaclass=ABCMeta):
    """遊戲角色的命令類別"""
    def __init__(self, role):
        self._role = role

    def set_role(self, role):
        self._role = role

    @abstractmethod
    def execute(self):
        pass


class Left(GameCommand):
    """左移命令"""
    def execute(self):
        self._role.left_move()
        self._role.show_position()


class Right(GameCommand):
    """右移命令"""
    def execute(self):
        self._role.right_move()
        self._role.show_position()


class Up(GameCommand):
    """上移命令"""
    def execute(self):
        self._role.up_move()
        self._role.show_position()


class Down(GameCommand):
    """下移命令"""
    def execute(self):
        self._role.down_move()
        self._role.show_position()


class Jump(GameCommand):
    """彈跳命令"""
    def execute(self):
        self._role.jump_move()
        self._role.show_position()
        # 空中停留
        time.sleep(0.5)


class Squat(GameCommand):
    """下蹲命令"""
    def execute(self):
        self._role.squat_move()
        self._role.show_position()
        # 下蹲伏地
        time.sleep(0.5)


class Attack(GameCommand):
    """攻擊命令"""
    def execute(self):
        self._role.attack()


class MacroCommand(GameCommand):
    """巨集命令，組合命令"""
    def __init__(self, role=None):
        super().__init__(role)
        self._commands = []

    def add_command(self, command):
        # 讓所有命令作用於同一物件
        self._commands.append(command)

    def remove_command(self, command):
        self._commands.remove(command)

    def execute(self):
        for command in self._commands:
            command.execute()


class GameInvoker:
    """命令調度者"""
    def __init__(self):
        self._command = None

    def set_command(self, command):
        self._command = command

    def action(self):
        self._command.execute()


def test_game():
    """在控制台在字元來類比命令"""
    role = GameRole('常山趙子龍')
    invoker = GameInvoker()
    commands_dict = {
        'L': Left(role),
        'R': Right(role),
        'U': Up(role),
        'D': Down(role),
        'J': Jump(role),
        'S': Squat(role),
        'A': Attack(role)
    }
    while True:
        str_cmd = input('請輸入命令:')
        str_cmd = str_cmd.upper()
        if str_cmd == 'Q':
            role.show_position()
            exit()

        for command in str_cmd:
            if command not in commands_dict:
                print(f'錯誤指令{command}...')
                continue
            invoker.set_command(commands_dict[command])
            invoker.action()








test_game()
