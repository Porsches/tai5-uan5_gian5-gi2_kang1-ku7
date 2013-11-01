
from 資料庫.欄位資訊 import 偏漳優勢音腔口
from 資料庫.欄位資訊 import 偏泉優勢音腔口
from 資料庫.欄位資訊 import 混合優勢音腔口
from 斷詞標音.閩南語標音整合 import 閩南語標音整合
from 字詞組集句章.綜合標音.句綜合標音 import 句綜合標音
from 字詞組集句章.綜合標音.閩南語字綜合標音 import 閩南語字綜合標音
from 斷詞標音.客話標音整合 import 客話標音整合
from 資料庫.欄位資訊 import 四縣腔
from 資料庫.欄位資訊 import 海陸腔
from 資料庫.欄位資訊 import 大埔腔
from 資料庫.欄位資訊 import 饒平腔
from 資料庫.欄位資訊 import 詔安腔
from 字詞組集句章.綜合標音.客話字綜合標音 import 客話字綜合標音
from 字詞組集句章.解析整理工具.解析錯誤 import 解析錯誤
from 斷詞標音.型音辭典 import 型音辭典
from 斷詞標音.國語標音整合 import 國語標音整合
from 斷詞標音.現掀辭典 import 現掀辭典
from 資料庫.欄位資訊 import 國語臺員腔
from 字詞組集句章.綜合標音.國語字綜合標音 import 國語字綜合標音
from 斷詞標音.排標音結果 import 排標音結果

class 自動標音():
	標音模組 = {
		(閩南語標音整合, 閩南語字綜合標音, 現掀辭典):[偏漳優勢音腔口, 偏泉優勢音腔口, 混合優勢音腔口],
		(客話標音整合, 客話字綜合標音, 現掀辭典):[四縣腔, 海陸腔, 大埔腔, 饒平腔, 詔安腔],
		(國語標音整合, 國語字綜合標音, 現掀辭典):[國語臺員腔],
		}
	支援腔口 = None
	腔口標音工具 = None
	腔口綜合標音 = None
	排標音 = 排標音結果()
# 	支援腔口 = {偏漳優勢音腔口:(閩南語偏漳標音,閩南語字綜合標音),
# 		偏泉優勢音腔口:(閩南語偏泉標音,閩南語字綜合標音),
# 		混合優勢音腔口:(閩南語混合標音,閩南語字綜合標音),
# 		四縣腔:(客家話四縣標音,客話字綜合標音),
# 		海陸腔:(客家話海陸標音,客話字綜合標音),
# 		大埔腔:(客家話大埔標音,客話字綜合標音),
# 		饒平腔:(客家話饒平標音,客話字綜合標音),
# 		詔安腔:(客家話詔安標音,客話字綜合標音),
# 		}
	def __init__(self):
		self.支援腔口 = set()
		self.腔口標音工具 = {}
		self.腔口綜合標音 = {}
		for 工具, 腔口 in self.標音模組.items():
			標音整合, 字綜合標音, 辭典 = 工具
			for 腔 in 腔口:
				標音工具 = 標音整合(腔, 辭典)
				self.支援腔口.add(腔)
				self.腔口標音工具[腔] = 標音工具
				self.腔口綜合標音[腔] = 字綜合標音
		return
	
	def 有支援無(self,腔):
		return 腔 in self.支援腔口
		
	def 標音(self, 查詢腔口, 查詢語句):
		if 查詢腔口 not in self.腔口標音工具:
			raise(解析錯誤, '腔口毋著：{0}'.format(查詢腔口))
		字綜合標音 = self.腔口綜合標音[查詢腔口]
		章物件 = self.斷詞標音物件(查詢腔口, 查詢語句)
		標音句 = 句綜合標音(字綜合標音, 章物件)
		return 標音句.轉json格式()
	
	def 斷詞標音物件(self, 查詢腔口, 查詢語句):
		if 查詢腔口 not in self.腔口綜合標音:
			raise(解析錯誤, '腔口毋著：{0}'.format(查詢腔口))
		標音工具 = self.腔口標音工具[查詢腔口]
		章物件 = 標音工具.產生標音結果(查詢語句, '')
		排好章物件 = self.排標音.照白文層排(章物件)
		return 排好章物件
