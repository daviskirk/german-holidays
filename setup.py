from setuptools import setup, find_packages

setup(
    name='German-Holidays',
    version='0.1',
    url='http://github.com/daviskirk/german-holidays',
    license='MIT',
    author='Davis Kirkendall',
    author_email='davis.e.kirkendall@gmail.com',
    description='German holidays in pandas',
    packages=find_packages(),
    keywords=["pandas", "calendar", "holidays"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "Development Status :: 4 - Beta",
    ],
    platforms='any'
)
