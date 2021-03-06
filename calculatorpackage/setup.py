import setuptools
 
with open("README.md", "r") as fh:
    long_description = fh.read()
 
setuptools.setup(
    name="calculator_seungtaemoon", # pip 으로 설치한 패키지 이름입니다
    author="seungtaemoon",
    author_email="conanmoon@gmail.com",
    description="A calculator package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/seungtaemoon/my_projects/calculatorpackage/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)