from setuptools import setup

setup(
    name='orbslam3',
    version='0.0',
    description='A Python wrapper for ORBSLAM3',
    url='https://github.com/hello-binit/ORB_SLAM3-PythonBindings',
    author='Binit Shah',
    author_email='bshah@hello-robot.com',
    zip_safe=True,
    packages=[''],
    package_dir={'': '.'},
    package_data={'': ['orbslam3.so']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: BSD License"
    ],
)
