import os
from app.config import is_defined_in_environ, load_config
import pytest

dummy_config = "app/tests/dummyConfig.json"
dummy_var_names = ['dummyhost', 'dummyuser', 'dummypass']


def test_environ_setting():
    os.environ['DUMMYHOST'] = 'dummyEnvHost'
    os.environ['DUMMYUSER'] = 'dummyEnvUser'
    os.environ['DUMMYPASS'] = 'dummyEnvPass'

    assert is_defined_in_environ(var_names=dummy_var_names)

    del os.environ['DUMMYHOST']
    del os.environ['DUMMYUSER']
    del os.environ['DUMMYPASS']


def test_environment_config():
    os.environ['DUMMYHOST'] = 'dummyEnvHost'
    os.environ['DUMMYUSER'] = 'dummyEnvUser'
    os.environ['DUMMYPASS'] = 'dummyEnvPass'

    config = load_config(var_names=dummy_var_names, config_file=dummy_config)

    assert(config['dummyhost'] == 'dummyEnvHost')
    assert(config['dummyuser'] == 'dummyEnvUser')
    assert(config['dummypass'] == 'dummyEnvPass')

    del os.environ['DUMMYHOST']
    del os.environ['DUMMYUSER']
    del os.environ['DUMMYPASS']


def test_dummy_config_file():

    config = load_config(var_names=dummy_var_names, config_file=dummy_config)

    assert(config['dummyhost'] == 'dummyConfHost')
    assert(config['dummyuser'] == 'dummyConfUser')
    assert(config['dummypass'] == 'dummyConfPass')


def test_config_not_found():

    # this does not exist on purpose!
    bad_config_path = "app/tests/missing_config.json"

    with pytest.raises(FileNotFoundError):
        load_config(var_names=dummy_var_names, config_file=bad_config_path)
