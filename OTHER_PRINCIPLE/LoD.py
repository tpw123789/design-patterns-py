"""
Law of Demeter
每個邏輯單元應對其他邏輯單元有最少了解: 親近當前物件。
X: a.getB().getProperties()
V: a.getProperties()
"""
