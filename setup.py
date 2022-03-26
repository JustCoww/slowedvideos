from setuptools import setup, find_packages

VERSION = '0.4.1'
DESCRIPTION = 'Various scripts from justcow.'

# Setting up
setup(
    name="slowedvideos",
    version=VERSION,
    author="JustCow",
    author_email="<justcow@pm.me>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['moviepy', 'pydub', 'pedalboard', 'youtube_dl', 'pillow', 'soundfile', 'requests'],
    keywords=['python', 'video', 'audio', 'justcow'],
    include_package_data=True ,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
