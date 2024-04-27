from setuptools import setup, find_packages

setup(
    name='ld_msgs',
    version='0.2',
    packages=find_packages(),
    description='ld_msg lib for python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='shuo shen',
    author_email='shuo.shen@liangdao.de',
    url='',
    install_requires=[
        'geometry_msgs',
        'std_msgs',
        'sensor_msgs',
        'genpy'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.10',
    ],
)