# encoding=utf8
import requests
import json
import sys
import re
import urllib
reload(sys)
sys.setdefaultencoding("gbk")


class Positon():

    def __init__(self, resultsItem):
        self.__dict__.update(resultsItem)

    @property
    def detail(self):
        self.position_url = "http://www.lagou.com/jobs/%s.html" % self.positionId
        respon = requests.get(self.position_url)
        detail_data = re.findall(
            '<h3 class="description(.*?)</dd>',
            respon.text,
            re.S)[0]
        return detail_data

    def __repr__(self):
        return "%s:%s\n%s" % (self.companyName, self.positionName, self.salary)


class Page():

    def __init__(self, data):
        self.pageNo = data["content"]["pageNo"]
        self.result = data["content"]["positionResult"]["result"]
        self.positions = [Positon(item) for item in self.result]

    @property
    def have_next(self):
        if self.result == []:
            return False
        else:
            return True


class Lagou():

    def __init__(self, city=u"上海", keyword="python"):
        city = urllib.urlencode({"city": city.encode("utf8")})
        self.job_index_url = '''http://www.lagou.com/jobs/positionAjax.json?px=default&%s&needAddtionalResult=false''' % city
        self.pn = 1
        self.post_data = {
            'first': False,
            'pn': self.pn,
            'kd': keyword,
        }

    def get_page(self):
        respon = requests.post(self.job_index_url, self.post_data)
        if respon.ok is True:
            page_data = json.loads(respon.text)
            return Page(page_data)

    def next(self):
        page = self.get_page()
        if page.have_next:
            print self.post_data["pn"]
            for i in page.positions:
                print i
            self.post_data["pn"] += 1
            # return page
        else:
            raise StopIteration

    def __iter__(self):
        return self


if __name__ == '__main__':
    lagou = Lagou(u"广州", "python")
    for i in lagou:
        print i
