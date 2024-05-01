from setuptools import setup, find_packages

# test: pip install -e .
# rm -rf dist/ && python setup.py sdist bdist_wheel
# twine upload --repository openseneca dist/*

VERSION = '0.0.6'
DESCRIPTION = 'OpenSeneca'
LONG_DESCRIPTION = ''

def read_requirements():
    with open('openseneca/requirements.txt', 'r') as req:
        content = req.read()
        requirements = content.split('\n')

    return requirements

# Setting up
setup(
        name="openseneca",
        version=VERSION,
        author="Ottavio Fogliata",
        author_email="ottavio.fogliata@openseneca.ai",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=read_requirements(),
        package_data={
          'openseneca': ['router.pk', 'config.yml'],
        },
        keywords=['python']
)