import setuptools 
setuptools.setup(
    name='a4a',
    version='0.4',
    author='Ali-Mahmoud-Fadhil',
    description='Hi ! By This Lib You Can Check Users In Sosial Midea ,',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License"
    ],
    requires=['user_agent',
              'requests']
)