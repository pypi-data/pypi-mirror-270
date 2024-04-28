from setuptools import setup

# Used in pypi.org as the README description of your package
with open("README.md", 'r') as f:
    long_description = f.read()

setup(
        name='kostsample',
        version='1.0.1',
        description='python-sample-app is a starter template for new python applications',
        author='Benjamin Costa & Vitalii Kostyreva',
        author_email='kostyreva-09876@gmail.com',
        license="MIT",
        url="https://github.com/becosta/python-sample-app",
        packages=['kostsample'],
        entry_points={
                'console_scripts': [
                    'sample=kostsample.main:main',
                ],
        },
        long_description=long_description,
        long_description_content_type="text/markdown",
)
exit(0)