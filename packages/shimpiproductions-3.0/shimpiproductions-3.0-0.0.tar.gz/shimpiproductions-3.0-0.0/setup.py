from setuptools import setup, find_packages

with open("README.md", 'r') as f:
    DESCRIPTION = f.read()

VERSION = '0.0'

setup(
    name="shimpiproductions-3.0",
    version=VERSION,
    author="Sarvesh Shimpi",
    author_email="sarveshshimpi18@gmail.com",
    long_description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['numpy', 'matplotlib', 'scikit-learn', 'opencv-python'],
    keywords=['python', 'video', 'stream', 'video stream', 'camera stream', 'sockets'],
    entry_points={
        "console_scripts": [
            "shimpiproductions=shimpiproductions:hi",
        ],
    },
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
