from setuptools import setup, find_packages

setup(
    name='dazbo_commons',
    version='0.1.2',
    author='Darren Lester',
    author_email='derailed.dash@gmail.com',
    description='Handy utility code, such as coloured logging.',
    long_description='See the README in the project repo',
    long_description_content_type='text/markdown',
    url='https://github.com/derailed-dash/dazbo-commons-py',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    classifiers=[
        'Development Status :: 4 - Beta', 
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    python_requires='>=3.7',
    install_requires=[
        'colorama',
    ],
    extras_require={
        'dev': [
            'pytest>=5.4',
            'check-manifest',
            'twine',
        ],
    },
)
