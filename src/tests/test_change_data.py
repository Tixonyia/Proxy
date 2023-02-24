# Тесты функции замены строк в html.
from src.proxy_data import change_data
import pytest


# Тесты с валидными данными. Вход строка.
@pytest.mark.parametrize('data, expected_result', [('Black Russia', 'BlackHub Games'),
                                                   ('`Black<span>Russia`', 'BlackHub Games'),
                                                   ('BLACK Russia', 'BlackHub Games'),
                                                   ('ddsfsfdgf ddfs Black RussiA dfsgsdfsd', 'ddsfsfdgf ddfs BlackHub '
                                                                                             'Games dfsgsdfsd')])
def test_change_data(data, expected_result):
    assert change_data(data) == expected_result


# Тесты с не валидными данными.
@pytest.mark.parametrize('expected_exception, data', [(TypeError, 12),
                                                      (TypeError, None)])
def test_change_data_eror(expected_exception, data):
    with pytest.raises(expected_exception):
        change_data(data)


