import pytest
from page_objects.home_page import HomePage

def test_verify_remaining_products(browser):
    home_page = HomePage(browser)
    home_page.go_to_site()
    
    home_page.search_for_item('Mouse 2')
    product_titles = home_page.get_product_titles()
    assert 'Mouse 2' in product_titles, "Mouse 2 not found in search results"

    home_page.search_for_item('Keyboard 2')
    product_titles = home_page.get_product_titles()
    assert 'Keyboard 2' in product_titles, "Keyboard 2 not found in search results"
