__author__ = 'Pavel Kosicin'


def test_search_result(app):
    app.navigate.menu_global_search()
    app.search.check_search_result()
