# -*- coding: utf-8 -*-
import unittest
from 臺灣言語工具.語音合成.閩南語變調 import 閩南語變調
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.字物件篩仔 import 字物件篩仔

class 閩南語變調試驗(unittest.TestCase):
	def setUp(self):
		self.閩南語變調 = 閩南語變調()
		self.分析器 = 拆文分析器()
		self.篩仔 = 字物件篩仔()

	def tearDown(self):
		pass

	def test_句尾變調(self):
		原本 = self.分析器.建立句物件('我愛媠媠')
		self._設定音值(原本,
			[('g', 'ua', '2'), ('ʔ', 'ai', '3'), ('s', 'ui', '2'), ('s', 'ui', '2')])
		變調了 = self.分析器.建立句物件('我愛媠媠')
		self._設定音值(變調了,
			[('g', 'ua', '1'), ('ʔ', 'ai', '2'), ('s', 'ui', '1'), ('s', 'ui', '2')])
		self.assertEqual(self.閩南語變調.變調(原本), None)
		self.assertEqual(原本, 變調了)

	def test_的前無變調(self):
		原本 = self.分析器.建立句物件('我上愛媠媠的姑娘')
		self._設定音值(原本,
			[('g', 'ua', '2'), ('s', 'ioŋ', '7'), ('ʔ', 'ai', '3'),
			('s', 'ui', '2'), ('s', 'ui', '2'), ('ʔ', 'e', '5'), ('k', 'o', '1'), ('n', 'iu', '5')])
		變調了 = self.分析器.建立句物件('我上愛媠媠的姑娘')
		self._設定音值(變調了,
			[('g', 'ua', '1'), ('s', 'ioŋ', '3'), ('ʔ', 'ai', '2'),
			('s', 'ui', '1'), ('s', 'ui', '2'), ('ʔ', 'e', '7'), ('k', 'o', '7'), ('n', 'iu', '5')])
		self.assertEqual(self.閩南語變調.變調(原本), None)
		self.assertEqual(原本, 變調了)
		
	def test_的前代名詞變調(self):
		原本 = self.分析器.建立句物件('我的媠媠')
		self._設定音值(原本,
			[('g', 'ua', '2'), ('ʔ', 'e', '5'),
			('s', 'ui', '2'), ('s', 'ui', '2'), ])
		變調了 = self.分析器.建立句物件('我的媠媠')
		self._設定音值(變調了,
			[('g', 'ua', '1'), ('ʔ', 'e', '7'),
			('s', 'ui', '1'), ('s', 'ui', '2'), ])
		self.assertEqual(self.閩南語變調.變調(原本), None)
		self.assertEqual(原本, 變調了)

	def test_井前無變調(self):
		原本 = self.分析器.建立句物件('我#愛媠媠')
		self._設定音值(原本,
			[('g', 'ua', '2'), (None,), ('ʔ', 'ai', '3'), ('s', 'ui', '2'), ('s', 'ui', '2')])
		變調了 = self.分析器.建立句物件('我#愛媠媠')
		self._設定音值(變調了,
			[('g', 'ua', '2'), (None,), ('ʔ', 'ai', '2'), ('s', 'ui', '1'), ('s', 'ui', '2')])
		self.assertEqual(self.閩南語變調.變調(原本), None)
		self.assertEqual(原本, 變調了)

	def test_章物件句尾變調(self):
		原本 = self.分析器.建立章物件('我愛媠媠。我愛媠媠。')
		self._設定音值(原本,
			[('g', 'ua', '2'), ('ʔ', 'ai', '3'), ('s', 'ui', '2'), ('s', 'ui', '2'), (None,),
			('g', 'ua', '2'), ('ʔ', 'ai', '3'), ('s', 'ui', '2'), ('s', 'ui', '2'), (None,), ])
		變調了 = self.分析器.建立章物件('我愛媠媠。我愛媠媠。')
		self._設定音值(變調了,
			[('g', 'ua', '1'), ('ʔ', 'ai', '2'), ('s', 'ui', '1'), ('s', 'ui', '2'), (None,),
			('g', 'ua', '1'), ('ʔ', 'ai', '2'), ('s', 'ui', '1'), ('s', 'ui', '2'), (None,), ])
		self.assertEqual(self.閩南語變調.變調(原本), None)
		self.assertEqual(原本, 變調了)
		
	def _設定音值(self, 物件, 音值陣列):
		字陣列 = self.篩仔.篩出字物件(物件)
		self.assertEqual(len(字陣列), len(音值陣列))
		for 字物件, 音值 in zip(字陣列, 音值陣列):
			字物件.音 = 音值
		
