from setuptools import setup

setup(name='markovy',
      version='0.1.2',
      description='Parody generation with Markov Chain',
      url='https://github.com/halilkaya/markovy',
      author='Halil Kaya',
      author_email='halil@halilkaya.net',
      license='GPLv3',
      packages=['markovy'],
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
      ],
      scripts=['markovy/__init__.py'],
      install_requires=['setuptools'],
      zip_safe=False)
