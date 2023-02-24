# Тесты функции проверки на Url.
from src.proxy_data import valid_url
import pytest


@pytest.mark.parametrize('url, expected_result', [('True', False),
                                                  ('https://open-meteo.com/', True),
                                                  ('https://blackrussia.online/politica.html', True),
                                                  (' ', False)])
def test_change_data(url, expected_result):
    assert valid_url(url) == expected_result


@pytest.mark.parametrize('expected_exception, url', [(TypeError, 12),
                                                     (TypeError, None)])
def test_change_data_eror(expected_exception, url):
    with pytest.raises(expected_exception):
        valid_url(url)
