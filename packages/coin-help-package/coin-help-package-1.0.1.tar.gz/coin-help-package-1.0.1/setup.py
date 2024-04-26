from setuptools import setup

setup(  name= 'coin-help-package', 
        version='1.0.1', 
        description='Coin-help-package For Tr@ding bot.', 
        py_modules=["coin-help-package"],
        package_dir={'': 'src'},
        install_requires = ["blessings ~= 1.7"],
        extras_require={
            "dev": [
                "pytest>=3.7",
            ],
        },
    )

