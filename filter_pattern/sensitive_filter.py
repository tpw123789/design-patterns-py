from filter_pattern.filter_pattern_framework import Filter, FilterChain
import re


class SensitiveFilter(Filter):
    """敏感慈過濾"""
    def __init__(self):
        self._sensitives = ['黃色', '反動', '貪汙']

    def do_filter(self, elements):
        """敏感詞列表轉換成規則運算式"""
        regex = ''
        for word in self._sensitives:
            regex += word + '|'
        regex = regex[:len(regex) - 1]
        # 對每個元素進行過濾
        new_elements = []
        for element in elements:
            item, num = re.subn(regex, '', element)
            new_elements.append(item)
        return new_elements


class HtmlFilter(Filter):
    """HTML字元轉換"""
    def __init__(self):
        self._word_map = {
            '&': '&amp;',
            '\'': '&apos;',
            '>': '&gt;',
            '<': '&lt;',
            '\"': '&quot;'
        }

    def do_filter(self, elements):
        new_elements = []
        for element in elements:
            for key, value in self._word_map.items():
                element = element.replace(key, value)
            new_elements.append(element)
        return new_elements


def test_filter_content():
    contents = [
        '有人出售黃色書: <黃情味道>',
        '有人企圖搞反動運動, 一"造謠資訊"'
    ]
    print('過濾前: ', contents)
    filter_chain = FilterChain()
    filter_chain.add_filter(SensitiveFilter())
    filter_chain.add_filter(HtmlFilter())
    new_contents = filter_chain.do_filter(contents)
    print('過濾後: ', new_contents)


test_filter_content()
