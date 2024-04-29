from setuptools import setup, find_packages

setup(
    author= "Dear Norathee",
    description="Expansion of inspect to help analyze and automate python code",
    name="inspect_py",
    version="0.1.0",
    packages=find_packages(),
    license="MIT",
    install_requires=["pandas"],

    # example
    # install_requires=['pandas>=1.0',
    # 'scipy==1.1',
    # 'matplotlib>=2.2.1,<3'],
    

)