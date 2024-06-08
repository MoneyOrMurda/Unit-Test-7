import pytest
from page_objects.admin_login_page import AdminLoginPage
from page_objects.admin_dashboard_page import AdminDashboardPage
from page_objects.admin_category_page import AdminCategoryPage

def test_create_category(browser):
    admin_login_page = AdminLoginPage(browser)
    admin_dashboard_page = AdminDashboardPage(browser)
    admin_category_page = AdminCategoryPage(browser)
    admin_login_page.go_to_site()
    admin_login_page.login('admin', 'password')
    admin_dashboard_page.go_to_categories()
    admin_category_page.add_new_category('Devices', 'Devices Meta Tag')
