from webdrivermanager_cn.chrome import ChromeDriverManager
from webdrivermanager_cn.geckodriver import GeckodriverManager
from webdrivermanager_cn.microsoft import EdgeWebDriverManager

VERSION = '1.5.1'

__all__ = [
    'VERSION',
    'ChromeDriverManager',
    'EdgeWebDriverManager',
    'GeckodriverManager',
]
