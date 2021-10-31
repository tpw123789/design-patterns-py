from abc import ABCMeta, abstractmethod
import logging
import time

logging.basicConfig(level=logging.INFO)


class PooledObject:
    """池物件，也稱池化物件"""
    def __init__(self, obj):
        self._obj = obj
        self._busy = False

    def get_object(self):
        return self._obj

    def set_object(self, obj):
        self._obj = obj

    def is_busy(self):
        return self._busy

    def set_busy(self, busy):
        self._busy = busy


class ObjectPool(metaclass=ABCMeta):
    """物件集區"""
    """物件集區初始化大小"""
    InitialNumObjects = 10
    """物件集區最大的大小"""
    MaxNumObjects = 50

    def __init__(self):
        self._pools = []
        for i in range(ObjectPool.InitialNumObjects):
            obj = self.create_pool_object()
            self._pools.append(obj)

    @abstractmethod
    def create_pool_object(self):
        """創建池物件，子類別實現該方法"""
        pass

    def borrow_object(self):
        """借用對象"""
        # 如果找到空閒物件，直接返回
        obj = self._find_free_object()
        if obj is not None:
            logging.info(f'{id(obj):x}對象已被占用，time:{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))}')
            return obj
        # 如果物件集區未滿，增加新物件，初始為10個物件
        if len(self._pools) < ObjectPool.MaxNumObjects:
            pooled_object = self.add_object()
            if pooled_object is not None:
                pooled_object.set_busy(True)
                logging.info(f'{id(obj):x}對象已被占用，time:{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))}')
            return pooled_object.get_object()
        # 物件集區已沒有空嫌物件，返回None
        return None

    def return_object(self, obj):
        """歸還對象"""
        for pooled_obj in self._pools:
            if pooled_obj.get_object() == obj:
                pooled_obj.set_busy(False)
                logging.info(f'{id(obj):x}對象已歸還，time:{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))}')
                break

    def add_object(self):
        """新增對象"""
        obj = None
        if len(self._pools) < ObjectPool.MaxNumObjects:
            obj = self.create_pool_object()
            self._pools.append(obj)
            logging.info(f'{id(obj)}新增新對象，time:{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))}')
            return obj

    def clear(self):
        """清空物件集區"""
        self._pools.clear()

    def _find_free_object(self):
        """查找空閒物件"""
        obj = None
        for pooled_obj in self._pools:
            # 如果 obj not busy，返回obj，如果都busy返回None
            if not pooled_obj.is_busy():
                obj = pooled_obj.get_object()
                pooled_obj.set_busy(True)
                break
        return obj



