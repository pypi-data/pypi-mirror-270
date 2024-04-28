from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='package_fileDO',
    version='0.1.0',
    packages=find_packages(),
    description='A python SDK for ioc-ic',
    long_description=long_description,
    long_description_content_type='text/markdown',  # 确保格式正确显示在 PyPI 上
    author='Cui Jingyu',
    author_email='1808662399@qq.com',
    url='https://github.com/whalecui1014',
    license='MIT',
    install_requires=[
        'requests',  # 如果你的包依赖于 requests，需要列出来
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)