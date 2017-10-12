from setuptools import setup

setup(
    name='germanholidays',
    use_scm_version=True,
    url='http://github.com/daviskirk/german-holidays',
    license='MIT',
    author='Davis Kirkendall',
    author_email='davis.e.kirkendall@gmail.com',
    description='German holidays in pandas',
    packages=[
        'german_holidays',
    ],
    package_dir={'german_holidays': 'german_holidays'},
    include_package_data=True,
    install_requires=[
        'pandas',
    ],
    setup_requires=['pytest-runner', 'setuptools_scm'],
    tests_require=['pytest', 'pytest-cov'],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "Development Status :: 4 - Beta",
    ],
    keywords=["pandas", "calendar", "holidays"],
    platforms='any'
)
