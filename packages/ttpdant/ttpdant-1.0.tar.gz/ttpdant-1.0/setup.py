from setuptools import setup, find_packages

setup(
    name='ttpdant',
    version='1.0',
    packages=find_packages(),
    py_modules=['adam', 'autoencoder', 'Cnn', 'fnn-perceptron', 'mc-culloch-pitt', 'mini-batch-gd', 'momentum-gd', 'nestrov-gd', 'optimization-adagrad-gd', 'optimization-stocastic-gd', 'optimization-vanilla-gd', 'rms', 'Rnn-lstm'],  # Add your module names here
    install_requires=[],  # Add any dependencies here
    # Metadata
    author='Taylor Swift',
    author_email='taylor@swift.com',
    description='The Tortured Poets Department',
    url='https://taylorswift.com',
)

