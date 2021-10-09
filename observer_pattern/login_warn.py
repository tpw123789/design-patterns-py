import time
from abc import ABCMeta, abstractmethod
from observer_pattern.observer_pattern_framework import Observer, Observable


class Account(Observable):
    """用戶帳戶"""
    def __init__(self):
        super().__init__()
        self._latest_ip = {}
        self._latest_region = {}

    def login(self, name, ip, time):
        region = self._get_region(ip)
        if self._is_long_distance(name, region):
            self.notify_observers({'name': name, 'ip': ip, 'region': region, 'time': time})
        self._latest_region[name] = region

    def _get_region(self, ip):
        ip_regions = {
            '101.47.18.9': '杭州',
            '67.218.147.69': '洛杉磯'
        }
        region = ip_regions.get(ip)
        return "" if region is None else region

    def _is_long_distance(self, name, region):
        """計算本次登入 與最近幾次登入地區差距"""
        latest_region = self._latest_region.get(name)
        return latest_region is not None and latest_region != region


class SmsSender(Observer):
    """訊息發送"""
    def update(self, observer, obj):
        print('[訊息發送] ' + obj['name'] + '您好!檢測到您的帳戶可能登錄異常。最近一次登錄資訊:\n' +
              '登錄地區: ' + obj['region'] + '登錄ip: ' + obj['ip'] + '登錄時間: ' +
              time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(obj['time']))
              )


class MailSender(Observer):
    """訊息發送"""
    def update(self, observer, obj):
        print('[郵件發送] ' + obj['name'] + '您好!檢測到您的帳戶可能登錄異常。最近一次登錄資訊:\n' +
              '登錄地區: ' + obj['region'] + '登錄ip: ' + obj['ip'] + '登錄時間: ' +
              time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(obj['time']))
              )


account = Account()
account.add_observer(SmsSender())
account.add_observer(MailSender())
account.login('Tony', '62.218.147.69', time.time())
account.login('Tony', '101.47.18.9', time.time())


