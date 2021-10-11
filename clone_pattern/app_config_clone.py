from clone_pattern.clone_framework import Clone


class AppConfig(Clone):
    """application config"""
    def __init__(self, config_name):
        self._config_name = config_name
        self.parser_from_file = './config/default.xml'
        self._font_type = '宋體'
        self._font_size = 14
        self._language = '中文'
        self._log_path = './logs/appException.log'

    def parse_from_file(self, file_path):
        """pass"""
        pass

    def save_to_file(self, file_path):
        """pass"""
        pass

    def copy_config(self, config_name):
        """創建一個配置的副本"""
        config = self.deep_clone()
        config._config_name = config_name
        return config

    def show_info(self):
        print(f'{self._config_name} 配置資訊如下:')
        print(f'字體: {self._font_type}')
        print(f'字型: {self._font_size}')
        print(f'語言: {self._language}')
        print(f'Log: {self._log_path}')

    def set_font_type(self, font_type):
        self._font_type = font_type

    def set_font_size(self, font_size):
        self._font_size = font_size

    def set_language(self, language):
        self._language = language

    def set_log_path(self, log_path):
        self._log_path = log_path


default = AppConfig('default')
default.show_info()
print()
newConfig = default.copy_config('henry config')
newConfig.show_info()
print()
newConfig.set_font_type('雅黑')
newConfig.set_font_size(56)
newConfig.set_language('English')
newConfig.show_info()



