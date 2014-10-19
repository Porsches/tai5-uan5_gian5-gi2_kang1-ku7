# -*- coding: utf-8 -*-
"""
著作權所有 (C) 民國103年 意傳文化科技
開發者：薛丞宏
網址：http://意傳.台灣
語料來源：請看各資料庫內說明

本程式乃自由軟體，您必須遵照SocialCalc設計的通用公共授權（Common Public Attribution License, CPAL)來修改和重新發佈這一程式，詳情請參閱條文。授權大略如下，若有歧異，以授權原文為主：
	１．得使用、修改、複製並發佈此程式碼，且必須以通用公共授權發行；
	２．任何以程式碼衍生的執行檔或網路服務，必須公開該程式碼；
	３．將此程式的原始碼當函式庫引用入商業軟體，且不需公開非關此函式庫的任何程式碼

此開放原始碼、共享軟體或說明文件之使用或散佈不負擔保責任，並拒絕負擔因使用上述軟體或說明文件所致任何及一切賠償責任或損害。

臺灣言語工具緣起於本土文化推廣與傳承，非常歡迎各界用於商業軟體，但希望在使用之餘，能夠提供建議、錯誤回報或修補，回饋給這塊土地。

感謝您的使用與推廣～～勞力！承蒙！
"""
import os
from 臺灣言語工具.翻譯.摩西工具.摩西翻譯模型訓練 import 摩西翻譯模型訓練
from 臺灣言語工具.翻譯.摩西工具.語句編碼器 import 語句編碼器
from 臺灣言語工具.翻譯.摩西工具.斷詞轉斷字的編碼器 import 斷詞轉斷字編碼器

if __name__ == '__main__':
	平行華語 = ['/home/Ihc/git/i3_thuan5/語料/華', ]
	平行閩南語 = ['/home/Ihc/git/i3_thuan5/語料/閩', ]
	閩南語語料 = ['/home/Ihc/git/i3_thuan5/語料/閩全', ]
	模型訓練 = 摩西翻譯模型訓練()
	斷詞暫存資料夾 = os.path.join(os.path.dirname(__file__), '斷詞暫存資料夾')
	模型訓練.訓練(
		平行華語, 平行閩南語, 閩南語語料,
		斷詞暫存資料夾,
		連紲詞長度=3,
		編碼器=語句編碼器(),
		SRILM執行檔路徑='/usr/local/srilm/bin/i686-m64/',
		GIZA執行檔路徑='/usr/local/mt/',
		MOSES腳本路徑='/usr/local/mosesdecoder/scripts/',
		)

	斷詞編碼器 = 斷詞轉斷字編碼器()
	斷字暫存資料夾 = os.path.join(os.path.dirname(__file__), '斷字暫存資料夾')
	模型訓練.訓練(
		平行華語, 平行閩南語, 閩南語語料,
		斷字暫存資料夾,
		連紲詞長度=3,
		編碼器=斷詞編碼器(),
		SRILM執行檔路徑='/usr/local/srilm/bin/i686-m64/',
		GIZA執行檔路徑='/usr/local/mt/',
		MOSES腳本路徑='/usr/local/mosesdecoder/scripts/',
		)
