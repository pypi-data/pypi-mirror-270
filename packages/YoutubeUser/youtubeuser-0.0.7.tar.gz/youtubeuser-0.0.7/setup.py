from setuptools import setup, find_packages

setup(
    name="YoutubeUser",
    version='0.0.7',
    author='R1TGAMING',
    author_email='rafisofyangaming1234@gmail.com',
    description='A Lib For Search Youtube User Or Channels',
  
    long_description_content_type='text/markdown',
   url='https://github.com/R1TGAMING/YoutubeUser',
    packages=["YoutubeUser"],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires= ["requests>=2.25.1"]
)
