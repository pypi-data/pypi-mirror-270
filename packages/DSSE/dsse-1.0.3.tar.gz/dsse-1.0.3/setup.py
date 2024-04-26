from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


download_url = (
    f"https://github.com/pfeinsper/drone-swarm-search/archive/refs/tags/v1.0.3.tar.gz"
)
setup(
    name="DSSE",
    version="1.0.3",
    author="Luis Filipe Carrete, Manuel Castanares, Enrico Damiani, Leonardo Malta, Jorás Oliveira, Ricardo Ribeiro Rodrigues, Renato Laffranchi Falcão, Pedro Henrique Britto Aragão Andrade, Fabricio Barth",
    description="An environment to train drones to search and find a shipwrecked person lost in the ocean using reinforcement learning.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pfeinsper/drone-swarm-search",
    license="MIT",
    keywords=["Reinforcement Learning", "AI", "SAR", "Multi Agent"],
    download_url=download_url,
    packages=find_packages(),
    include_package_data=True,
    package_data={"DSSE": ["environment/imgs/*.png"]},
    install_requires=[
        "numpy",
        "gymnasium",
        "pygame",
        "pettingzoo",
        "matplotlib",
        "numba",
    ],
)
