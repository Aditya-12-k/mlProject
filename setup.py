# setuptools se setup aur find_packages import kar rahe hain
# find_packages project ke andar ke modules ko automatically detect karta hai
from setuptools import find_packages, setup

# typing se List use ho raha hai type hinting ke liye
from typing import List

# Ye variable '-e .' ko detect karne ke liye use hoga jo requirements.txt me ho sakta hai
HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    Ye function requirements.txt ko read karke list me convert karta hai
    aur (-e .) ko remove karta hai agar present ho.
    """
    requirements = []

    # file open kar rahe file_path ke basis par
    with open(file_path) as file_obj:
        # saari lines read kar li
        requirements = file_obj.readlines()
        # newline ("\n") remove kar rahe list me se
        requirements = [req.replace("\n", "") for req in requirements]

        # Agar '-e .' present hai to remove kar dete detection me disturb na ho
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    # clean requirements return kar rahe
    return requirements


# Setup function se package ka metadata define hota hai
# Jaise name, version, author, dependencies (requirements), packages, etc.
setup(
    name='mlproject',                       # project ka naam
    version='0.0.1',                        # project version
    author='Aditya',                        # author ka naam
    author_email='Aditya-12-k@users.noreply.github.com',  # author email
    packages=find_packages(),               # project ke saare modules detect ho jayenge
    install_requires=get_requirements('requirements.txt') # requirements.txt se libs install hongi
)
