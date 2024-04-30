from setuptools import setup, find_packages

setup(
    name='rainbow_lib',
    version='0.0.3',
    # 自动查找项目中的所有包
    packages=find_packages(exclude=['tests', 'tests.*', 'config.ini']),
    install_requires=[
      'rainbow-cpp-sdk==4.1.0',
      'PyYAML>=6.0.1',
    ],
    dependency_links=[
        'https://mirrors.tencent.com/repository/pypi/tencent_pypi/simple/rainbow-cpp-sdk/'
    ],
    author='kylinmiao',
    author_email='kylinmiao@tencent.com',
    description='A wrapper library for RainbowClient',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    # url='https://github.com/kylinmiao/rainbow_lib',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)