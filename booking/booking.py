import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import pause
import naver_config as Config
import pyperclip

import requests
from bs4 import BeautifulSoup

def main() :
	driver	= webdriver.Chrome()
	wait	= WebDriverWait(driver, 10)
	driver.get(Config.nUrl)
	
	# get id/pwd Elem
	nId_Elem = wait.until(EC.element_to_be_clickable((By.ID, "id")))
	nPw_Elem = driver.find_element_by_id("pw")

	#login btn
	nLoginBtn = driver.find_element_by_class_name("btn_global")
	
	# 캡챠 방지
	#nId_Elem.send_keys(Config.nId)
	#nPw_Elem.send_keys(Config.nPw)
	
	#nId_Elem.click()
	pyperclip.copy(Config.nId)
	nId_Elem.send_keys(Keys.COMMAND, 'v')
	#time.sleep(10)
	
	#nPw_Elem.click()
	pyperclip.copy(Config.nPw)
	nPw_Elem.send_keys(Keys.COMMAND, 'v')
	#time.sleep(10)
	
	nLoginBtn.click()

	#time.sleep(10)


	#Choose Target Month
	#nNextMonth = driver.find_element_by_class_name("calendar-btn calendar-btn-next-mon")
	#driver.find_element_by_xpath('//*[@id="calendar"]/div/a[2]').click()
	nNextMonth = wait.until(EC.element_to_be_clickable((By.XPATH,  '//*[@id="calendar"]/div/a[2]')))
	nNextMonth.click()

	# Choose Date
	nValid = 0
	nFind = 0
	anInvDateLst = []
	anCalendar = driver.find_element_by_class_name('tb_calendar')
	anDateLst  = anCalendar.find_elements_by_class_name('num') 

	nFirstInCalendar = anDateLst[0] 

	time.sleep(1)

	anInvDateLstTemp = anCalendar.find_elements_by_class_name("calendar-unselectable")

	for nInvalidDateLst in anInvDateLstTemp :
		anInvDateLst.append(int(nInvalidDateLst.text))	
	
	for nDate in anDateLst:
		nDateTemp = int(nDate.text)
		#print("Debug")
		#print (nDateTemp)

		#print(anInvDateLst)

		#print(type(anInvDateLst))
		#print(type(anInvDateLst[0]))
		#print(type(nDateTemp))

		if (nDateTemp in anInvDateLst):
			pass
		else : 
			if (nDateTemp in [1,2,3,4,5]):
				nValid = 1

			if (nValid == 1):
				anInvTime = []
				nDate.click()

				time.sleep(1)

				# 1. choose date
				# 2. lookup booking time
				# 3. if empty -> next date

				anTimeTable = driver.find_element_by_class_name("lst_time")
				anTimeItem	= anTimeTable.find_elements_by_class_name("item")
				anInvalidTime = anTimeTable.find_elements_by_class_name("none")
				for nInvTime in anInvalidTime :
					anInvTime.append(nInvTime)	

				if ( len(anTimeItem) == len(anInvTime)) :
					pass
				else :
					for nTimeItem in anTimeItem:
						if (nTimeItem.text in anInvTime) :
							pass
						else :
							nTimeItem.click()
							nFind = 1
							break;
			time.sleep(1)		

			if (nFind == 1):
			#	nPay = driver.find_element_by_xpath('//*[@id="container"]/bk-restaurant/div/div/div[3]/bk-submit/div/button')
			#	nPay.click()
				nTalkTalk = driver.find_element_by_xpath('//*[@id="container"]/bk-restaurant/div/div/div[3]/bk-submit/button')
				nTalkTalk.click()
				time.sleep(100)
				break;
			if (nDateTemp == 30):
				nValid = 0
		
	
'''
	# Get Dates
	soup = BeautifulSoup(driver.page_source, "lxml")
	anDates = soup.find_all("span", attrs={"class":"num"})

	nValidDate = 0
	for nDate in anDates:
		nDateTemp = nDate.get_text()

		print(nDateTemp)

		# 가성의 일자들은 제외
		if (nDateTemp == 1):
			nValidDate = 1
		if (nDateTemp == Config.nDayPerMonth):
			nValidDate = 0

		if (nValidDate == 1):
			pass	
'''
	#anTimeTable = soup.find_all("ul", attrs={"class":"lst_time"})
	#anTimes		= anTimeTable.find_all("a", attrs={"class":"anchor"})

#	for nTimeTable in anTimeTable:
#		print("Time Table")
#		print (anTimeTable.get_text())
#		
#	for nTime in anTimes:
#		print("Time")
#		print(nTime)

if __name__ == "__main__":
	# 시간과 연동해서 
	# 특정 시간에 함수 실행하도록
	# 추가 필요 
	main()

'''
class Booking:
	def __init__(self, name):
		super().__init__()
		self.name = name
		print ("{0} 이 생성되었습니다".format(self.name))

	def __new__(cls):
		super().__new__(cls)


	def main():
		print "Main Function"


	if __name__ == "__main__":
		main()




naver = Booking("네이버")
'''
