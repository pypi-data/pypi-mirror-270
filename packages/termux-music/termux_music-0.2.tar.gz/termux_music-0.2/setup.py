from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='termux-music',
    version='0.2',
    license='Apache License 2.0',
    description='Script to Run Music in Termux',
    long_description=readme(),
    author='Alexander Krefting',
    author_email='linuxdevalex@outlook.de',
    url='https://github.com/androlinuxs/termux-music',
    scripts=['termux-music'],
    install_requires=['pytube'],
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3'
    ]
)
