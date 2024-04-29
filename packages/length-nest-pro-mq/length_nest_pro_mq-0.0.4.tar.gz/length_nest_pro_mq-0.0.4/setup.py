from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'My first Python package'
LONG_DESCRIPTION = 'My first Python package with a slightly longer description'

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="length-nest-pro-MQ",
    version='0.0.4',
    author="Niels Bos",
    author_email="nielsb00@gmail.com",
    description="length_nest_pro_MQ",
    long_description="Adapted version of length_nest_pro, enhanced with message queue",
    packages=find_packages(),
    package_data={'spam': ['data.txt']},
    install_requires=['numpy', 'wheel', 'setuptools', 'pika'],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'

    keywords=["rabbit mq", "length nest pro"]

)