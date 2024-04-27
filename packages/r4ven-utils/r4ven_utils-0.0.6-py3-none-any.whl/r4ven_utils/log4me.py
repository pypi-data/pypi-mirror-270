"""
This module contains all logging related functions.
"""

import os
import inspect
import logging
import time
import functools

def function_logger(file_mode: str = "w",
                    file_level: int = logging.INFO,
                    console_level: int = None) -> logging.Logger:
    """
    Creates a logger object specific to the function in which it's called.

    Args:
        file_mode (str): A string that define which mode you want to open the log file.
        Defaults to "w" - Write - Opens a file for writing, creates the file if it does not exist.

        file_level (int): Logging level that will be written in the log file.
        Defaults to logging.INFO.

        console_level (int, optional): Logging level that will be displayed at the console.
        Defaults to None.

    Returns:
        logging.Logger: Logger object of the specific function in which this
        function is called.
    """
    create_logs_folder()
    script_name = os.path.basename(__file__).removesuffix(".py")
    create_script_logs_folder(script_name)

    caller_frame = inspect.stack()[1]

    if caller_frame[3] == "<module>":
        # If the caller is the main module (<module>), get the main function name
        function_name = inspect.getmodulename(caller_frame[1])
    else:
        # Otherwise, get the name of the calling function
        function_name = caller_frame[3]

    logger = logging.getLogger(function_name)

    # Check if handlers are already present and if so, clear them before adding new handlers.
    if (logger.hasHandlers()):
        logger.handlers.clear()

    # By default, logs all messages.
    logger.setLevel(logging.DEBUG)

    if console_level != None:
        # StreamHandler logs to console.
        ch = logging.StreamHandler()
        ch.setLevel(console_level)
        ch_format = logging.Formatter("%(levelname)-8s - %(message)s")
        ch.setFormatter(ch_format)
        logger.addHandler(ch)

    # FileHandler logs to file.
    fh = logging.FileHandler(r"logs/{0}/{1}.log".\
        format(script_name, function_name), mode = file_mode)
    fh.setLevel(file_level)
    fh_format = logging.\
        Formatter("%(asctime)s - %(lineno)d - %(levelname)-8s - %(message)s")
    fh.setFormatter(fh_format)
    logger.addHandler(fh)

    return logger

def create_logs_folder() -> None:
    """
    Check if there's a logs folder (/logs) in the current directory,
    if there isn't, create it.
    """
    project_directory = os.getcwd()
    logs_directory = os.path.join(project_directory, "logs")
    if not os.path.exists(logs_directory):
        os.makedirs(logs_directory)

def create_script_logs_folder(script_name: str) -> None:
    """
    Check if there's a log folder for the script that is running
    in the project directory (/logs/script_name), if there isn't, create it.

    Args:
        script_name (str): The name of the script that's calling the function
        function_logger.
    """
    project_directory = os.getcwd()
    script_logs_directory = os.path.join(project_directory, "logs")
    final_directory = os.path.join(script_logs_directory, script_name)
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)

def calculate_execution_time(logger: logging.Logger):
    """
    Decorator that calculates the execution time of a function and logs this time.

    Args:
        logger (logging.Logger): Logger object returned by the function function_logger.

    Returns:
        function: Decorated function.
    """
    def function_decorator(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            """
            Wrapper function that calculates the execution time of the decorated function and logs it.

            Args:
                *args: Positional arguments of the function.
                **kwargs: Keyword arguments of the function.

            Returns:
                Any: Result of the decorated function.
            """
            start_time = time.time()
            result = function(*args, **kwargs)
            end_time = time.time()
            execution_time = end_time - start_time

            logger.info(f"The function {function.__name__}"+\
                f" was executed in {int(execution_time)} seconds.")

            return result

        return wrapper

    return function_decorator
