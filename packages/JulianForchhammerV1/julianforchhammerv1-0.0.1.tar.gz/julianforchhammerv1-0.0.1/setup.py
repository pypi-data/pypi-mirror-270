from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Operating System :: Microsoft :: Windows',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='JulianForchhammerV1',
    version='0.0.1',
    description='Short Description',
    long_description="Very long Description",
    url='', 
    author='Julian Forchhammer',
    author_email='julian@deadniggers.org',
    license='MIT',
    classifiers=classifiers,
    keywords='Ratting',
    packages=find_packages(),
    install_requires=[]  
)