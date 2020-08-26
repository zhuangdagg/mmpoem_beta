from fontTools.ttLib import TTFont
import fontTools.merge as merge
from fontTools import subset
from bs4 import BeautifulSoup
import requests,html5lib
from pathlib import Path
import os


class fontCreate(object):
	"""输入一个字符串，
	"""
	def __init__(self,fontFile,):
		self.name = []
		self.cwd = os.getcwd()
		self.fontFile = fontFile
		self.session = requests.session()
		self.font = TTFont(fontFile)
		# print(self.font.getGlyphNames())
		for uni in self.font.getGlyphNames():
			if 'uni' == uni[0:3]:
				uni =chr(int(uni[3:],16))
				self.name.append(uni)





	def woffCreate(self,text=None,No='2'):
		mergeTools = merge.Merger()
		woffFile = "static/font/" + No + ".woff"
		saveFilename = str(Path(self.cwd)/woffFile)
		filename =[self.fontFile,saveFilename]
		textLuck = []
		baseUrl ='https://www.font.cn/preview/getFont?font_id=303&format=ttf&vers=v1.0&words='
		urlEnd = '&hex=1'
		if text is None:
			return
		collectText = {t for t in text}
		text = ''.join(collectText)
		for t in text:
			if t not in self.name:
				hexT = str(hex(ord(t)))
				textLuck.append(hexT[2:])
		# print(len(textLuck))
		if len(textLuck) != 0:
			mergeUrl = ','.join(textLuck)
			aimUrl = baseUrl + mergeUrl + urlEnd
			fontDown = self.downloadWoff(aimUrl,saveFilename)
			if fontDown != None:
				mergeFont = mergeTools.merge(filename)
				mergeFont.save(self.fontFile)
		# 拆分合并后的字体文件成2.woff
		options = subset.Options()
		fontMerge = subset.load_font(self.fontFile,options)
		subsetter = subset.Subsetter(options)
		subsetter.populate(text=text)
		subsetter.subset(fontMerge)
		options.flavor = 'woff'
		subset.save_font(fontMerge,saveFilename,options)



	def downloadWoff(self,url,saveFilename):
		html = self.session.get(url)
		if html.status_code == 200 :
			with open(saveFilename,'wb') as f:
				f.write(html.content)
				print('successful to download the font!')
		else:
			print(html.status_code)
			return None

		fontDownload = TTFont(saveFilename)
		return fontDownload



if __name__ == '__main__':
	os.chdir(cwd)
	fontClass = fontCreate('1.woff')
	# print(fontClass.name)
	text='控制台面制枣点！'
	fontClass.woffCreate(text)

