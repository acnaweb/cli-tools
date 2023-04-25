from setuptools import setup, find_packages


requeriments = [
    'click'
  ]


setup (
  name='cli_tools',
  version='1.0',
  description='Setting up a python package',
  author='Antonio Carlos de Lima Junior',
  author_email='ac@marketmining.com.br',
  url='https://blog.godatadriven.com/setup-py',
  packages=find_packages(include=['cli']),
  install_requires=requeriments,
  entry_points={
    'console_scripts': ['greetings = cli.greeter:greet', 
                        'add = cli.calculator:add',
                        'subtract = cli.calculator:subtract',
                        'authenticate = cli.authenticate:auth',
                        'cli = cli.main:main']
  }
)