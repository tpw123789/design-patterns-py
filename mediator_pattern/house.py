

class HouseInfo:
    """房源訊息"""
    def __init__(self, area, price, has_window, has_bathroom, has_kitchen, address, owner):
        self._area = area
        self._price = price
        self._has_window = has_window
        self._has_bathroom = has_bathroom
        self._has_kitchen = has_kitchen
        self._address = address
        self._owner = owner

    def get_address(self):
        return self._address

    def get_owner_name(self):
        return self._owner.get_name()

    def show_info(self, is_show_owner=True):
        print(f'面積: {str(self._area)}平方米\n'
              f'價格: {str(self._price)}元\n'
              f'窗戶: {"有" if self._has_window else "沒有"}\n'
              f'衛浴: {self._has_bathroom}\n'
              f'廚房: {"有" if self._has_kitchen else "沒有"}\n'
              f'位址: {self._address}\n'
              f'房東: {self.get_owner_name() if is_show_owner else ""}\n')


class HousingAgency:
    """房屋仲介"""
    def __init__(self, name):
        self._house_infos = []
        self._name = name

    def get_name(self):
        return self._name

    def add_house_info(self, house_info):
        self._house_infos.append(house_info)

    def remove_house_info(self, house_info):
        for info in self._house_infos:
            if info == house_info:
                self._house_infos.remove(info)

    def get_search_condition(self, description):
        """將使用者描述資訊轉換成搜尋條件邏輯"""
        return description

    def get_match_infos(self, search_condition):
        """根據房源資訊個屬性查找最匹配的資訊"""
        print(f'{self.get_name()} 為你找到適合房源')
        for info in self._house_infos:
            info.show_info(True)
        return self._house_infos

    def sign_contract(self, house_info, period):
        """與房東簽訂協定"""
        print(f'{self.get_name()}與房東{house_info.get_owner_name()}簽訂{house_info.get_address()}，'
              f'的房子租賃合約，租期{period}年。合約期內，{self.get_name()}有權對其轉租。')

    def sign_contracts(self, period):
        for info in self._house_infos:
            self.sign_contract(info, period)


class HouseOwner:
    """房東"""
    def __init__(self, name):
        self._name = name
        self._house_info = None

    def get_name(self):
        return self._name

    def set_house_info(self, address, area, price, has_window, bathroom, kitchen):
        self._house_info = HouseInfo(area, price, has_window, bathroom, kitchen, address, self)

    def publish_house_info(self, agency):
        agency.add_house_info(self._house_info)
        print(f'{self.get_name()}在{agency.get_name()}發佈房源出租資訊')
        self._house_info.show_info()


class Customer:
    """用戶，租房的人"""
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def find_house(self, description, agency):
        print(f'我是{self.get_name()}，我想找一個 {description} 的房子')
        return agency.get_match_infos(agency.get_search_condition(description))

    def see_house(self, house_infos):
        """去看房，選最實用的房子"""
        size = len(house_infos)
        return house_infos[size - 1]

    def sign_contract(self, house_info, agency, period):
        """與仲介簽訂協定"""
        print(f'{self.get_name()}與仲介{agency.get_name()}簽訂{house_info.get_address()}'
              f'的房子租賃合約，租期{period}年。合約內{self.get_name()}有權對其進行使用')


house_agency = HousingAgency('仲介')
house_owner_1 = HouseOwner('屋主1')
house_owner_1.set_house_info(
    address='台北市信義區北七路701號',
    area=100,
    price=2500,
    has_window=1,
    bathroom='獨立衛浴',
    kitchen=0
)

house_owner_2 = HouseOwner('屋主2')
house_owner_2.set_house_info(
    address='台北市信義區北七路702號',
    area=200,
    price=3500,
    has_window=2,
    bathroom='共用衛浴',
    kitchen=0
)

house_owner_3 = HouseOwner('屋主3')
house_owner_3.set_house_info(
    address='台北市信義區北七路703號',
    area=300,
    price=4500,
    has_window=3,
    bathroom='獨立衛浴',
    kitchen=1
)

house_owner_1.publish_house_info(house_agency)
house_owner_2.publish_house_info(house_agency)
house_owner_3.publish_house_info(house_agency)

house_agency.sign_contracts(3)

customer_1 = Customer('客戶1')
house_infos = customer_1.find_house('隨便', house_agency)
appropriation = customer_1.see_house(house_infos)
customer_1.sign_contract(appropriation, house_agency, 2)

