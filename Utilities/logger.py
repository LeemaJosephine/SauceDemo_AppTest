import logging
import os

class LogGen:

    @staticmethod
    def loggen():

        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        log_dir = os.path.join(project_root, "logs")
        os.makedirs(log_dir, exist_ok=True)
        log_path = os.path.join(log_dir, "automation.log")

        logger = logging.getLogger("automation")
        logger.setLevel(logging.INFO)
        print("INFO: Logging started", log_path)

        # Avoid duplicates logs
        if not logger.handlers:

            file_handler = logging.FileHandler(log_path, mode="a")
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        return logger
