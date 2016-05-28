import requests
import re

# id:2877651


class Xiami():

	def __init__(self,id):
		self.id=id
		self.lib_url = "http://www.xiami.com/space/lib-song/u/%s/page/"%id
		self.header = {
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
		}
	
	def get_page(self,char_num="1"):
		respon=requests.get(
				self.lib_url+char_num+"/",
				headers=self.header
			)
		return respon.text



if __name__ == '__main__':
	page=Xiami("2877651")
	data=page.get_page()
