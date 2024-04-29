from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='assertbr',
    version='0.0.2',
    license='MIT License',
    author='André Vieira dos Santos',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='assertbr7@gmail.com',
    keywords='assert br',
    description=u'Framework pra testes de API',
    packages=['assertbr'],
    install_requires=['requests'],)