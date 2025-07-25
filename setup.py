from setuptools import setup, Extension, find_packages

with open("README.md", "r", encoding="UTF-8") as readme:
    description = readme.read()

setup(
    name                            = "hugetsu",
    version                         = "0.1.1",
    packages                        = find_packages(),
    long_description                = description,          # パッケージの詳細な説明 (通常はREADME.mdから読み込む)
    long_description_content_type   = "text/markdown",      # long_descriptionの形式
    classifiers                     = [                     # パッケージの分類情報
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires                 = ">=3.6",              # 必須とするPythonのバージョン
)