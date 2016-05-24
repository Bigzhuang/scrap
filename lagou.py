import requests
import json
import sys

reload(sys)
sys.setdefaultencoding("gbk")


class Lagou():

	def __init__(self,city="shanghai",keyword="python"):
		# self.job_index='''http://www.lagou.com/jobs/positionAjax.json?px=default&city=%s&needAddtionalResult=false'''%city
		self.job_index='''http://www.lagou.com/jobs/positionAjax.json?px=default&city=%E4%B8%8A%E6%B5%B7&needAddtionalResult=false'''
		self.job_detail="http://www.lagou.com/jobs/1517466.html"
		self.post_data={
			'first':False,
			'pn':0,
			'kd':keyword,
			}

	def get_index(self):
		respon=requests.post(self.job_index,self.post_data)
		if respon.ok is True:
			return json.loads(respon.text)["content"]["positionResult"]
		else:
			raise "error"


def main():
	lagou=Lagou()
	page_No=1
	while 1:
		lagou.post_data["pn"]=page_No
		data=lagou.get_index()
		item_No=1
		for item in data["result"]:
			print "page_No:%d-item No:%d\n\n"%(page_No,item_No)
			item_No+=1
			print item["companyId"]
			print item["positionName"]
			print item["positionType"]
			print item["workYear"]
			print item["education"]
			print item["salary"]
			print item["companyName"]
			print item["district"]
			print "\n\n\n\n"
		print "page: %d \n\n"%page_No
		page_No+=1




if __name__ == '__main__':
	main()


