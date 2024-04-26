from setuptools import setup

setup(  name= 'coinanalyse', 
        version='1.0.1', 
        description='Coin-help-package For Tr@ding bot.', 
        py_modules=["coinanalyse"],
        package_dir={'': 'src'},
        install_requires = ["blessings ~= 1.7"],
        extras_require={
            "dev": [
                "pytest>=3.7",
            ],
        },
    )

