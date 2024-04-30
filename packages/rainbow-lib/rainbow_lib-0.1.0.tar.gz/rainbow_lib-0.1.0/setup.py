from setuptools import setup, find_packages

setup(
    name='rainbow_lib',
    version='0.1.0',
    # 自动查找项目中的所有包
    packages=find_packages(),
    install_requires=[
      'rainbow-cpp-sdk>=4.1.0',
      'PyYAML>=6.0.1',
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