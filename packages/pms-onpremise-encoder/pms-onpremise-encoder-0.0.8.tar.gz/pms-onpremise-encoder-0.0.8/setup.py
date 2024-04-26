from setuptools import setup, find_packages

setup(
    name='pms-onpremise-encoder',
    version='0.0.8',
    description='',
    author='Heeyong Kwon',
    author_email='heeyong.kwon@4by4inc.com',
    url='',
    install_requires=['ffmpeg-python', 'pms-inference-engine', 'loguru', 'numpy', 'python-dotenv', 'redis', 'PyMySQL', ],
    packages=find_packages(exclude=[]),
    keywords=['pms-encoder'],
    python_requires='>=3.10',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)