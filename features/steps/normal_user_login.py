from behave import given, when, then
from django.contrib.auth.models import User
from selenium import webdriver


@given(u'Hệ thống có user bình thường A và pass B')
def step_impl(context):
    User.objects.create(username='AAAAAA', password='BBBBBBBB')


@when(u'User đi tới trang quản lý')
def step_impl(context):
    browser = webdriver.Chrome()
    browser.get(context.get_url('/'))
    context.browser = browser


@when(u'User nhập username A pass B')
def step_impl(context):
    browser = context.browser  # type: webdriver.Chrome
    browser.find_element_by_id('id_username').send_keys('AAAAAA')
    browser.find_element_by_id('id_password').send_keys('BBBBBBBB')


@when(u'User bấm nút logn')
def step_impl(context):
    browser = context.browser  # type: webdriver.Chrome
    browser.find_element_by_id('login').click()


@then(u'User login không thành công')
def step_impl(context):
    browser = context.browser  # type: webdriver.Chrome
    assert 'User login khong thanh cong' in browser.page_source


@then(u'User vẫn đứng ở trang login')
def step_impl(context):
    browser = context.browser  # type: webdriver.Chrome
    assert browser.current_url == context.get_url('/')
