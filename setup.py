import setuptools


setuptools.setup(
    name='encrypt_it',
    version='0.0.1',
    long_description='',
    author='CDS-SNC',
    url='https://github.com/cds-snc/encrypt_it',
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
    ],
    entry_points='''
        [console_scripts]
        encrypt_it=encrypt_it.cli:main
    '''
)
