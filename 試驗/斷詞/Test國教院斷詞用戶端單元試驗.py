# -*- coding: utf-8 -*-
from unittest.case import TestCase
from unittest.mock import patch


from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.斷詞.國教院斷詞用戶端 import 國教院斷詞用戶端


class 國教院斷詞用戶端單元試驗(TestCase):

    @patch('臺灣言語工具.斷詞.國教院斷詞用戶端.國教院斷詞用戶端.語句斷詞做陣列')
    def test_語句斷一句話(self, 回應mock):
        回應mock.return_value = [
            ["市面", "Nc"], ["上", "Ncd"], ["很少", "D"], ["有", "V_2"],
            ["「", "PUNC"], ["教科書", "Na"], ["設計", "Na"], ["」", "PUNC"],
            ["的", "DE"], ["專", "VH"], ["書", "Na"],
        ]
        結果句物件 = 拆文分析器.分詞句物件('市-面 上 很-少 有 「 教-科-書 設-計 」 的 專 書')

        原本句物件 = 拆文分析器.建立句物件('市面上很少有「教科書設計」的專書')
        self.assertEqual(國教院斷詞用戶端.斷詞(原本句物件), 結果句物件)
