# my_sdk/setup.py
from setuptools import setup, find_packages

setup(
    name='charles_sdk',  # 包的名称
    version='0.1',  # 初始版本号
    description='A simple addition SDK',
    packages=find_packages(),  # 自动发现所有模块
    author='Charles',  # 作者名称
    author_email='your.email@example.com',  # 作者邮箱
    url='https://github.com',  # 项目的主页链接
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
