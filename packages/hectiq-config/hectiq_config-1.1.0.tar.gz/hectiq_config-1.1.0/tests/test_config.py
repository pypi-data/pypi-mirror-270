import pytest
import os


@pytest.fixture
def path():
    dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(dir, "config.json")


def test_config_load(path):
    from hectiq_config import Config

    config = Config.load(path)


def test_config_with_float_keys():
    from hectiq_config import Config

    data = {
        "24.0": 0,
        "12.0": 1,
        "18.0": 2,
        "6.0": 3,
        "36.0": 4,
    }
    config = Config.from_dict(data)
    assert config.get("24.0") == 0
