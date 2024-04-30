from setuptools import setup, find_packages

VERSION = '0.0.3' 
DESCRIPTION = 'Trellis plot tool'
LONG_DESCRIPTION = 'Package to plot trellis functionality. Updated with width normalization, new default colormap, and reduced boxplot'

# Setting up
setup(
        name="trellisplot", 
        version=VERSION,
        author="Ethan S. Lee",
        author_email="<sukraelee@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['matplotlib', 'numpy', 'seaborn', 'pandas', 'scipy'],
        
        keywords=['python', 'trellisplot'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 3",
            "Operating System :: Microsoft :: Windows",
        ]
)