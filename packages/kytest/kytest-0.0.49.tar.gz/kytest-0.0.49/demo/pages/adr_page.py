"""
@Author: kang.yang
@Date: 2023/8/1 11:53
"""
from kytest.adr import Page, Elem


class DemoPage(Page):
    """APP首页"""
    activity_name = '.me.MeSettingActivity'

    adBtn = Elem(rid='bottom_btn')
    myTab = Elem(text='我的')
    spaceTab = Elem(text='科创空间')
    setBtn = Elem(rid='me_top_bar_setting_iv')
    title = Elem(rid='tv_actionbar_title')
    agreeText = Elem(rid='agreement_tv_2')
    moreService = Elem(text='更多服务')

