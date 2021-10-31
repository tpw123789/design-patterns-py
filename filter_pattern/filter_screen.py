

class FilterScreen:
    """過濾網"""
    def do_filter(self, raw_materials):
        for material in raw_materials:
            if material == '豆渣':
                raw_materials.remove(material)
        return raw_materials


def test_filter_screen():
    raw_materials = ['豆漿', '豆渣']
    print('過濾前: ', raw_materials)
    filter_screen = FilterScreen()
    filter_materials = filter_screen.do_filter(raw_materials)
    print('過濾後: ', filter_materials)


test_filter_screen()
