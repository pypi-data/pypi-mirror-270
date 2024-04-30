from setuptools import setup


setup(name='hurricaneapi',
      version='0.1.8',
      url='https://github.com/daniil49926/hurricaneapi',
      license='MIT',
      author='Shchipko Daniil',
      description='Hurricaneapi framework',
      packages=['hurricaneapi', 'hurricaneapi.responses', 'hurricaneapi.routing', 'hurricaneapi.middleware'],
      author_email='daniil49925@ya.ru',
      long_description=open('README.md').read(),
      zip_safe=False,
      install_requires=['aiofiles==23.2.1', 'uvicorn==0.20.0', 'grpcio==1.62.2'],
      )
