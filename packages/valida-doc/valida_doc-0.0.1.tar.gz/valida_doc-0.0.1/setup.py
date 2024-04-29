from setuptools import setup

with open('readme.md', 'r') as arq:
    readme= arq.read()

setup(
    name='valida_doc',
    version="0.0.1",
    license="MIT License",
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email="caseiro.gui@hotmail.com",
    keywords="validar documento cpf rg",
    description=u"Biblioteca para validação de documentos",
    packages=['valida_doc'],
)