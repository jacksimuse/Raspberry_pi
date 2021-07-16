import urllib.request as urq
import urllib.parse as uparse
import datetime
import json

class naverSearch(object):
    def __init__(self):
        print("Naver Search API 생성")

    # 네이버 API 요청함수
    def getRequestUrl(self, url):
        req = urq.Request(url)
        req.add_header('X-Naver-Client-Id', 'LZFRc9rPryYtEhhFYs9z')
        req.add_header('X-Naver-Client-Secret', 'f43x06JKFp')

        try:
            res = urq.urlopen(req)
            if res.getcode() == 200: #ok
                print('[{0}] URL Request succeed'.format(datetime.datetime.now()))
                return res.read().decode('utf-8')
        except Exception as e:
            print(e)
            return None

    # 네이버 검색API 사용함수
    def getNaverSearchResult(self, sNode, search_word, page_start, display):
        base = 'https://openapi.naver.com/v1/search/'
        node = '{0}.json'.format(sNode)
        param = '?start={0}&display={1}&query={2}'.format(page_start, display, uparse.quote(search_word))
        url = base + node + param # https://openapi.naver.com...nodeval.json?

        retData = self.getRequestUrl(url)
        if retData == None:
            return None
        else:
            return json.loads(retData)

    # 데이터 처리
    def getPostData(self, post, jsonResult):
        title = post['title']
        desc = post['description']
        org_link = post['originallink']
        link = post['link']
        pDate = datetime.datetime.strptime(post['pubDate'], '%a, %d %b %Y %H:%M%S +0900')
        p_date = pDate.strftime('%Y-%m-%d %H:%M:%S')

        #jsonResult.append({})