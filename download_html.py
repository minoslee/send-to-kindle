from bs4 import BeautifulSoup
import os
import os.path
import pdfkit
from  save_as_pdf import  save_pdf
from os_test import send_email

class ribao(object):

	def __init__(self):
		self.home_url = 'http://daily.zhihu.com'
		self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}

	def home_html(self):
		content = requests.get(self.home_url,headers = self.headers)
		all_href = BeautifulSoup(content.text,'html5lib').find_all('a',class_ = 'link-button')
		for href in all_href:
			url = self.home_url + href['href']
			self.story_html(url)

	def story_html(self,url):
		html = requests.get(url,headers = self.headers)
		title = BeautifulSoup(html.text,'html5lib').find('h1',class_ = 'headline-title').get_text()
		path = title.strip()
		save_pdf(url,path)

	send_email()

if __name__ == '__main__':
	Ribao = ribao()
	Ribao.home_html()

