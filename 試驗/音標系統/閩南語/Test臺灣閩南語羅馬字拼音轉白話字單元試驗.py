'''
Created on 2018年4月12日

@author: pigu
'''
import unittest
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from unittest.case import skip
from 臺灣言語工具.音標系統.閩南語.對照表 import 臺羅對白話字
from _ast import Dict


class 臺羅轉白話字單元試驗(unittest.TestCase):

    def test_大寫數字調(self):
        拼音物件 = 臺灣閩南語羅馬字拼音('Tsui2')
        self.assertEqual(拼音物件.轉白話字(), 'Chuí')

    def test_大寫傳統調(self):
        拼音物件 = 臺灣閩南語羅馬字拼音('Tsuí')
        self.assertEqual(拼音物件.轉白話字(), 'Chuí')

    @skip('TODO 待討論')
    def test_大寫輕聲(self):
        拼音物件 = 臺灣閩南語羅馬字拼音('0Tsuí')
        self.assertEqual(拼音物件.轉白話字(), '0Chuí')

    def test_小寫數字調(self):
        拼音物件 = 臺灣閩南語羅馬字拼音('tshui2')
        self.assertEqual(拼音物件.轉白話字(), 'chhuí')

    def test_小寫傳統調(self):
        拼音物件 = 臺灣閩南語羅馬字拼音('tshuí')
        self.assertEqual(拼音物件.轉白話字(), 'chhuí')

    @skip('TODO 待討論')
    def test_小寫輕聲(self):
        拼音物件 = 臺灣閩南語羅馬字拼音('0tsuí')
        self.assertEqual(拼音物件.轉白話字(), '0chuí')

    def test_單母音調符(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('hoo7').轉白話字(), 'hō͘')
        self.assertEqual(臺灣閩南語羅馬字拼音('hah8').轉白話字(), 'ha̍h')
        self.assertEqual(臺灣閩南語羅馬字拼音('hinnh8').轉白話字(), 'hı̍hⁿ')

    @skip('愛參考Phah4 Tai5-gi2的規範')
    def test_雙母音調符(self):
        # o＞e＞a＞u＞i＞ng＞m，
        self.assertEqual(臺灣閩南語羅馬字拼音('gio2').轉白話字(), 'gió')
        self.assertEqual(臺灣閩南語羅馬字拼音('uan5').轉白話字(), 'ôan')
        self.assertEqual(臺灣閩南語羅馬字拼音('ainn7').轉白話字(), 'āiⁿ')
        self.assertEqual(臺灣閩南語羅馬字拼音('au3').轉白話字(), 'àu')
        
    def test_鼻母音調符(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('mng5').轉白話字(), 'mn̂g')

    @skip('愛參考Phah4 Tai5-gi2的規範')
    def test_三母音調符(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('kuai3').轉白話字(), 'kòai')
        self.assertEqual(臺灣閩南語羅馬字拼音('iau7').轉白話字(), 'kòai')
        
    def test_韻對照表(self):
        for 臺羅韻, 白話字韻 in sorted(臺羅對白話字.韻對照表.items()):
            self.assertEqual(臺灣閩南語羅馬字拼音(臺羅韻).轉白話字(), 白話字韻)

#     def test_方言韻(self):
#         self.assertEqual(臺灣閩南語羅馬字拼音('tere5').轉白話字(), 'terê')
#         self.assertEqual(臺灣閩南語羅馬字拼音('tir5').轉白話字(), 'tîr')
#
#     def test_外來語佮輕聲(self):
#         # 符號予別的工具處理
#         self.assertEqual(臺灣閩南語羅馬字拼音('0tir5').轉白話字(), '0tîr')
#         self.assertEqual(臺灣閩南語羅馬字拼音('1tir5').轉白話字(), '1tîr')
