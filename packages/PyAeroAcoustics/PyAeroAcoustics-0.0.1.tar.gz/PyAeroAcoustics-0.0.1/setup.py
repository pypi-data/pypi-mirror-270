from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'PyAeroAcoustics'
LONG_DESCRIPTION = 'PyAeroAcoustics'

setup(
        name="PyAeroAcoustics", 
        version=VERSION,
        author="Thomas Brunner",
        author_email="<thomas.brunner@tugraz.at>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'PyAeroAcoustics'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)