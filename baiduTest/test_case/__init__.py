import os

import importlib
from pathlib import Path

_parent = Path(__file__).parent
modules = []
for r, d, f in os.walk(_parent.absolute()):
    for file in f:
        if file.endswith('py') and not file.startswith('__'):
            modules.append(file[:-3])

# 对modules进行排序,保证按目录默认排列顺序运行
modules.sort()

# 该方法会将当前目录下的所有py结尾的文件导入
for module in modules:
    importlib.import_module(f'{_parent.name}.{module}')

# modules = [eval(m) for m in modules]
print('modules:', modules)
