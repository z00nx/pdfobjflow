from setuptools import setup
setup(
    name='pdfobjflow',
    version='1.1',
    description='',
    long_description=('This program is meant to be used with pdf-parser from Didier Stevens.'
			'It reads the output from pdf-parser and creates the map of the objects flows'
			'under the form of a DOT file. You can then use the dot utility to export an'
			'image (e.g. PNG file)'),
    url='https://bitbucket.org/sebastiendamaye/pdfobjflow',
    author='Sebastien Damaye',
    license='???',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='didier stevens pdf malware analysis dot graph',
    scripts=['bin/pdfobjflow.py']
)
