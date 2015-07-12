

from setuptools import setup, find_packages


setup(
    name='ugetch',
    version='0.1.0',
    description='utf-8 getch, with tab, arrows, echo, etc',
    long_description=open('README.rst').read(),
    url='https://github.com/toejough/ugetch',
    author='toejough',
    author_email='toejough@gmail.com',
    license='MIT',
    classifiers=[
            # How mature is this project? Common values are
            #   3 - Alpha
            #   4 - Beta
            #   5 - Production/Stable
            'Development Status :: 3 - Alpha',

            # Indicate who your project is intended for
            'Intended Audience :: Developers',

            # Pick your license as you wish (should match "license" above)
             'License :: OSI Approved :: MIT License',

            # Specify the Python versions you support here. In particular, ensure
            # that you indicate whether you support Python 2, Python 3 or both.
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.4',
    ],
    keywords="getch utf8 utf-8 tab arrow",
    packages=find_packages(),
    install_requires=[],
)
