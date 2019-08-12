from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='ledshimdemo',
    version='0.0.3',
    description='Show various effects on a Pimoroni LED shim.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='John Chase',
    author_email='ratteal@gmail.com',
    python_requires='>=3.5.3',
    url='https://github.com/RatJuggler/led-shim-demo',
    packages=find_packages(exclude=['tests']),
    entry_points={
        'console_scripts': [
            'ledshimdemo = ledshimdemo.__main__:display_effects',
        ]
    },
    install_requires=[
        # Check latest releases on piwheels: https://www.piwheels.hostedpi.com/
        'click ==7.0',
        'ledshim ==0.0.1',
        'numpy >=1.12.1, <=1.16.4',
        'requests >=2.20.0, <=2.21.0',  # Updated from 2.12.4 due to CVE.
        'mock'
    ],
    test_suite='tests',
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3.5',
        'Operating System :: POSIX :: Linux',
        'Topic :: System :: Hardware'
    ]
)
