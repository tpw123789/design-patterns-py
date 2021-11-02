import random


class Camera:
    """相機本身"""
    SingleFocus = '單眼相機'
    AreaFocus = '區點對焦'
    BigAreaFicus = '大區點對焦'
    Focus45 = '45點自動對焦'

    def __init__(self, name):
        self._name = name
        self._aperture = 0.0        # 光圈
        self._shutter_speed = 0      # 區域對焦
        self._light_sensitivity = 0  # 感光程度
        self._lens = Lens()         # 鏡頭
        self._sdCard = SDCard()     # SDCard
        self._display = Display()   # 顯示器

    def shooting(self):
        """拍照"""
        print('[開始拍攝中')
        image_lighting = self._lens.collecting()
        # 透過快門、光圈和感光度、測光來控制拍攝的過程，省略此部分
        image = self._transfer_image(image_lighting)
        self._sdCard.add_image(image)
        print('拍攝完成]')

    def view_image(self, index):
        """查看圖像"""
        print(f'查看第{index + 1}張圖像: ')
        image = self._sdCard.get_image(index)
        self._display.show_image(image)

    def _transfer_image(self, image_lighting):
        """接收光線並處理成數位信號，簡單類比"""
        print('接收光線並處裡成數位信號')
        return Image(6000, 4000, image_lighting)

    def setting(self, aperture, shutter_speed, light_sensitivity):
        """設置相機的拍攝性質: 光圈、快門、感光度"""
        self._aperture = aperture
        self._shutter_speed = shutter_speed
        self._light_sensitivity = light_sensitivity

    def focusing(self, focus_mode):
        """對焦，要透過鏡頭來調節焦點"""
        self._lens.set_focus(focus_mode)

    def show_info(self):
        """顯示相機的屬性"""
        print(f'{self._name}的設置 光圈:{self._aperture:0.1f} 快門:1/{self._light_sensitivity} 感光度: ISO{self._light_sensitivity}')


class Lens:
    """鏡頭"""
    def __init__(self):
        self._focus_mode = ''
        self._scenes = {
            0: '風光',
            1: '生態',
            2: '人文',
            3: '紀實',
            4: '人像',
            5: '建築'
        }

    def set_focus(self, focus_mode):
        self._focus_mode = focus_mode

    def collecting(self):
        """圖像採集，採用隨機的方式來類比自然的拍攝過程"""
        print(f'採集光線，{self._focus_mode}')
        index = random.randint(0, len(self._scenes) - 1)
        scenes = self._scenes[index]
        return '美麗的' + scenes + '圖像'


class Display:
    """顯示器"""
    def show_image(self, image):
        print(f'圖片大小:{image.get_width()} X {image.get_height()}，圖片內容: {image.get_pixels()}')


class SDCard:
    """SD儲存卡"""
    def __init__(self):
        self._images = []

    def add_image(self, image):
        print('儲存圖像')
        self._images.append(image)

    def get_image(self, index):
        if 0 <= index < len(self._images):
            return self._images[index]
        else:
            return None


class Image:
    """圖像(圖片)，方便起見用字串來代表圖像內容(圖元)"""
    def __init__(self, width, height, pixels):
        self._width = width
        self._height = height
        self._pixels = pixels

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def get_pixels(self):
        return self._pixels


def test_camera():
    camera = Camera('EOS 80D')
    camera.setting(3.5, 60, 200)
    camera.show_info()
    camera.focusing(Camera.BigAreaFicus)
    camera.shooting()
    print()
    camera.setting(5.6, 720, 100)
    camera.show_info()
    camera.focusing(Camera.Focus45)
    camera.shooting()


test_camera()



