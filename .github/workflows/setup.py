from setuptools import setup

APP = ['main.py']  # 替换为你的主 Python 文件名
DATA_FILES = ['Reference.txt']  # 如果需要打包额外的数据文件，可以列在这里
OPTIONS = {
    'argv_emulation': True,
    'packages': [],  # 如果使用了外部库，可以列出
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)