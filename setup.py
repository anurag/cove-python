from setuptools import setup

setup(
    name='cove-python',
    packages=['cove'],
    version='0.1.0',
    description='https://cove.sh Python library',
    author='Cove',
    author_email='dev@cove.sh',
    license='MIT',
    url='https://github.com/cove-dev/cove-python',
    download_url='https://github.com/cove-dev/cove-python/archive/0.1.tar.gz',
    keywords='cove functions http',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development'

    ],
    install_requires=['werkzeug>=0.12'],
    python_requires='~=3.5'
)
