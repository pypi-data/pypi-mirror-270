import setuptools


setuptools.setup(
    name="krx-rank", # Replace with your own username
    version="0.0.1",
    author="FinPro",
    author_email="finpro1224@gmail.com",
    description="KRX 정보데이터시스템 순위 통계",
    readme="README.md",
    url="https://github.com/FinanceProgrammer/krx-rank",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6')