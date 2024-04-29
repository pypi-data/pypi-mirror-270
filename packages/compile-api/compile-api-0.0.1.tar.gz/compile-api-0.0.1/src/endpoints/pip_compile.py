"""API for compiling requirements."""
import os
import sys
import re

from pip._internal import main as pip_main
from fastapi import APIRouter, Depends
from piptools.scripts.compile import cli
from sqlalchemy.orm import Session

from utils.logger import CustomLogger
from schemas import environment
from models.database import Database
from models.environment import Environment
from domain.virtual_env import VirtualEnvironment


class PipCompileRouter:
    """
    Router class for handling the Compile Requirements API endpoint.
    """


    def __init__(self):
        """
        Initializes the CompileRouter instance.
        """
        self.router = APIRouter()
        self.db_con = Database()
        self.logger = CustomLogger().get_logger()


    def configure_routes(self):
        """
        Configures API routes.
        """

        @self.router.post("/compile")
        async def compile_requirements(request: environment.Compile,db: Session=Depends(self.db_con.get_db)):

            """
            Compile requirements from input.

            Args:
                image_id (int): Image Id
                requirements_in (str): Input requirements.

            Returns:
                str: Compiled requirements.
            """
            image_id=request.image_id
            requirements_in=request.requirements_in

            success=False
            error=[]
            warning=[]

            try:
                exist_requirements = Environment.get_requirements_by_id(db, image_id)
                self.logger.info(exist_requirements)
                with open("pipcompile.in", "w",encoding="utf-8") as f:
                    if exist_requirements!="NULL":
                        requirements_in=requirements_in+"\n"+exist_requirements+"\n"
                    f.write(requirements_in)

                with open('pipcompile.in', 'r',encoding="utf-8") as file:
                    lines = file.readlines()
                    unique_lines = set(lines)

                    if len(lines)!=len(unique_lines):
                        warn="Duplicate requirements"
                        self.logger.warning(warn)
                        warning.append(warn)

                with open('pipcompile.in', 'w',encoding="utf-8") as file:
                    req_str="\n".join(unique_lines)
                    file.writelines(req_str)

                #Validate
                with open("pipcompile.in", "r", encoding="utf-8") as f:
                    for line_num, line in enumerate(f, start=1):
                        line = line.strip()

                        if not line or line.startswith("#"):
                            continue
                        if not re.match(r"^[^=<>]+(?:[=<>]=?[^=<>]+)?$", line):
                            error.append(f"Syntax error in line {line_num}: {line}. Invalid format for version specifier.")
                            success=False
                            return {"success":success,"error":error,"warning":warning}

                #Create virtual environment if validation is successful
                virtual_env = VirtualEnvironment()

                args = [
                    "--dry-run",
                    "pipcompile.in"
                ]

                sys.stdout = open(os.devnull, 'w', encoding="utf-8")
                sys.stderr = open(os.devnull, 'w', encoding="utf-8")

                cli.main(args)

            except SystemExit as e:
                # Check the exit code
                if e.code == 0:
                    self.logger.info("Compiled Successfully")
                    success=True

                else:
                    err="Error compiling requirements"

                    self.logger.error(err)
                    error.append(err)

            except Exception as e:
                if str(e)=="metadata generation failed":
                    err="pip subprocess to install build dependencies exited with 1"
                    self.logger.error(err)
                    error.append(err)

                elif str(e)=="ResolutionImpossible: for help visit https://pip.pypa.io/en/latest/topics/dependency-resolution/#dealing-with-dependency-conflicts" :
                    err="Resolution Impossible dealing with dependency conflict"
                    self.logger.error(err)
                    error.append(err)

                elif str(e)=='list index out of range' :
                    err="Invalid Image Id"
                    self.logger.error(err)
                    error.append(err)

                elif "(from line 1 of pipcompile.in)" in str(e) :
                    err=str(e).replace('(from line 1 of pipcompile.in)','')
                    self.logger.error(err)
                    error.append(err)

                else:
                    self.logger.error(str(e))
                    error.append(str(e))


            finally:
                if success:
                    try:
                        # Delete the virtual environment
                        del virtual_env
                    except NameError:
                        self.logger.error("Failed to delete virtual environment")

            return {"success":success,"error":error,"warning":warning}


# Instantiate the router object
pip_compile_requirement_router = PipCompileRouter()
# Configure the routes
pip_compile_requirement_router.configure_routes()
# Get the router object
router = pip_compile_requirement_router.router
