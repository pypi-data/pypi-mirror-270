"""
Upgrade local pip package to the latest version.
"""
import os


def mian() -> None:
    """
    Main function
    Returns:

    """
    package_name = os.listdir('dist')[0]
    os.system(f'pip install dist/{package_name} --upgrade')