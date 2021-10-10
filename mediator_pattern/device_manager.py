from abc import ABCMeta, abstractmethod
from enum import Enum


class DeviceType(Enum):
    TypeSpeaker = 1
    TypeMicrophone = 2
    TypeCamera = 3


class DeviceItem:
    """設備項"""
    def __init__(self, device_id, device_name, device_type, is_default=False):
        self._device_id = device_id
        self._device_name = device_name
        self._device_type = device_type
        self._is_default = is_default

    def __str__(self):
        return f'type: {str(self._device_type)}\nid: {str(self._device_id)}\nname: {str(self._device_name)}\n' \
               f'is_default: {str(self._is_default)}'

    def get_device_id(self):
        return self._device_id

    def get_device_name(self):
        return self._device_name

    def get_device_type(self):
        return self._device_type

    def is_default(self):
        return self._is_default


class DeviceList:
    """設備清單"""
    def __init__(self):
        self._devices = []

    def add_device(self, device_item):
        self._devices.append(device_item)

    def get_devices_count(self):
        return len(self._devices)

    def get_by_index(self, device_index):
        if device_index < 0 or device_index >= self.get_devices_count():
            return None
        return self._devices[device_index]

    def get_by_device_id(self, device_id):
        for item in self._devices:
            if item.get_device_id() == device_id:
                return item
        return None


class DeviceManager(metaclass=ABCMeta):
    @abstractmethod
    def enumerate(self):
        """枚舉清單，初始化時，設備插拔都需要重新獲取清單"""
        pass

    @abstractmethod
    def activate(self, device_id):
        """選擇取用的設備"""
        pass

    @abstractmethod
    def get_current_device_id(self):
        """取得正在使用設備id"""
        pass


class SpeakerManager(DeviceManager):
    """揚聲器管理類別"""
    def __init__(self):
        self._current_device_id = None

    def enumerate(self):
        """枚舉清單"""
        devices = DeviceList()
        devices.add_device(DeviceItem(
            device_id='dfdfd45-dffdsfs-fdsfdsfds-fds',
            device_name='Realtek High Definition Audio',
            device_type=DeviceType.TypeSpeaker,
        ))
        devices.add_device(DeviceItem(
            device_id='dfdfd-dffdsfds545-f54545sfds-f4545ds',
            device_name='NVIDIA High Definition Audio',
            device_type=DeviceType.TypeSpeaker,
            is_default=True
        ))
        return devices

    def activate(self, device_id):
        """啟用指定當前設備"""
        self._current_device_id = device_id

    def get_current_device_id(self):
        return self._current_device_id


class DeviceUtil:
    """設備工具類別"""
    def __init__(self):
        self._managers = dict()
        self._managers[DeviceType.TypeSpeaker] = SpeakerManager()
        # self._managers[DeviceType.TypeCamera] = CameraManager()
        # self._managers[DeviceType.TypeMicrophone] = MicrophoneManager()

    def _get_device_manager(self, device_type):
        return self._managers[device_type]

    def get_device_list(self, device_type):
        return self._get_device_manager(device_type).enumerate()

    def activate(self, device_type, device_id):
        self._get_device_manager(device_type).activate(device_id)

    def get_current_device_id(self, device_type):
        return self._get_device_manager(device_type).get_current_device_id()


deviceUtil = DeviceUtil()
deviceList = deviceUtil.get_device_list(DeviceType.TypeSpeaker)
print('micro list: ')
# 設置第一個要用的設備
if deviceList.get_devices_count() > 0:
    deviceUtil.activate(DeviceType.TypeSpeaker, deviceList.get_by_index(0).get_device_id())
for index in range(0, deviceList.get_devices_count()):
    device = deviceList.get_by_index(index)
    print(device)
    print()

print(f'當前使用設備'
      f'{deviceList.get_by_device_id(deviceUtil.get_current_device_id(DeviceType.TypeSpeaker)).get_device_name()}')



