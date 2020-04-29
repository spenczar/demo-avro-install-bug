from setuptools import setup

install_requires = [
    'avro-python3==1.9.2.1',
]

setup(name='demo-avro-install-bug',
      version="0.1.0",
      url='https://github.com/spenczar/demo-avro-install-bug',
      author='Spencer Nelson',
      author_email='swnelson@uw.edu',
      install_requires=install_requires,
      zip_safe=False)
