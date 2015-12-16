#! /usr/bin/env python3

'''
Thanks to the blog authors:

http://mp.weixin.qq.com/s?__biz=MzA3ODQ2OTAxNA==&mid=401610538&idx=1&sn=7371d8811fa1614281d106d8df7a8096&scene=1&srcid=1215adn4WsRkSQ2eKct3cpfo&from=groupmessage&isappinstalled=0#wechat_redirect
'''

from splinter.browser import Browser
from time import sleep

'''
# parameters
'''
loginname = 'login_name'
loginpass = 'login_password'
searchtype_id = 'sf2' # student:'sf2' normal:'sf1'
site = 'https://kyfw.12306.cn/otn/' # login site, note http:// is required
#browsername = 'chrome' # 'chrome' need browser drivers
browsername = 'firefox' # 'firefox' is better
passenger_id = 'normalPassenger_0'
'''
# find cookies with devtools of browsers
'''
cookiedict_update = {"_jc_save_fromDate":"2016-02-01",
                     "_jc_save_fromStation":"%u53A6%u95E8%2CXMS",
                     "_jc_save_toStation":"%u5317%u4EAC%2CBJP",
                     }

brs = Browser(driver_name=browsername)
brs.visit(site)

brs.find_by_id(u'login_user').click()
brs.fill('loginUserDTO.user_name', loginname)
brs.fill('userDTO.password', loginpass)

#sleep(10)
input("Press Enter to continue...") # choose picture here

'''
# jump to ticket order page
'''
brs.find_by_id(u'selectYuding').click()
brs.cookies.add(cookiedict_update)
print(brs.cookies.all())
brs.reload()
brs.find_by_id(searchtype_id).click()
brs.find_by_id(u'query_ticket').click()
brs.find_by_text(u"预订")[1].click()
brs.find_by_id(passenger_id).click()


