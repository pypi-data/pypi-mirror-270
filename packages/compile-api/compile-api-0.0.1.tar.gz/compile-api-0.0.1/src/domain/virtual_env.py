"""virtual_env.py"""

import os
import shutil
import venv
import sys
from utils.logger import CustomLogger

class VirtualEnvironment:
    """
    Class to handle virtual environment operations.
    """

    def __init__(self):
        """
        Constructor for VirtualEnvironment.
        """
        self.logger = CustomLogger().get_logger()
        self.venv_dir = "temp"
        self.create_virtualenv()
        self.install_requirements()


    def __del__(self):
        """
        Destructor for VirtualEnvironment.
        """

        self.delete_virtualenv()


    def create_virtualenv(self):
        """
        Create a virtual environment.
        """

        venv.create(self.venv_dir, with_pip=True)


    def install_requirements(self):
        """
        Install requirements in the virtual environment.
        """

        activate_path = os.path.join("temp", "bin", "activate") if sys.platform != 'win32' else os.path.join("temp", "Scripts", "activate")

        if sys.platform!='win32':
            activate_cmd = f"source {activate_path}"
        else:
            activate_cmd = f"{activate_path}"

        os.system(f"{activate_cmd}")


    def delete_virtualenv(self):
        """
        Delete the virtual environment.
        """

        try:
            if os.path.exists(self.venv_dir):
                shutil.rmtree(self.venv_dir)
                self.logger.info("Virtual environment deleted successfully.")
            else:
                self.logger.error("Virtual environment not found.")

        except Exception as e:
            self.logger.exception("Failed to delete virtual environment")
