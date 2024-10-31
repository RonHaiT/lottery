from setuptools import setup, find_packages

setup(
    name="lottery-generator",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "lottery-generator=lottery.main:main",
        ],
    },
    author="你的名字",
    author_email="你的邮箱",
    description="一个简单的彩票号码生成器",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
