import pytest
from page_objects.admin_login_page import AdminLoginPage
from page_objects.admin_dashboard_page import AdminDashboardPage
from page_objects.admin_category_page import AdminCategoryPage

def test_add_products(browser):
    admin_login_page = AdminLoginPage(browser)
    admin_dashboard_page = AdminDashboardPage(browser)
    admin_category_page = AdminCategoryPage(browser)
    admin_login_page.go_to_site()
    admin_login_page.login('admin', 'password')
    admin_dashboard_page.go_to_categories()
    admin_category_page.add_new_category('Mouse 1', 'Mouse 1 Meta Tag')
    admin_category_page.add_new_category('Mouse 2', 'Mouse 2 Meta Tag')
    admin_category_page.add_new_category('Keyboard 1', 'Keyboard 1 Meta Tag')
    admin_category_page.add_new_category('Keyboard 2', 'Keyboard 2 Meta Tag')
