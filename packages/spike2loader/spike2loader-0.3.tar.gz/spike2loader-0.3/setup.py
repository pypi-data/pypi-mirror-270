from distutils.core import setup


setup(
    name='spike2loader',
    packages=['spike2loader'],
    entry_points={
        'console_scripts': [
            'smrx2tsv = spike2loader:smrx2tsv',
        ]
    },
    version='0.3',
    license='MIT',
    description = 'Reads smrx (spike2) files as pandas dataframes',
    description_file = "README.md",
    author="Julien Braine",
    author_email='julienbraine@yahoo.fr',
    url='https://github.com/JulienBrn/Spike2Loader',
    download_url = 'https://github.com/JulienBrn/Spike2Loader.git',
    package_dir={'': 'src'},
    keywords=['python',  'logging'],
    install_requires=['pandas', 'sonpy', "beautifullogger"],
)