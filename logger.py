import logging
import os
import traceback
from datetime import datetime

fecha = datetime.now().strftime("%Y-%m-%d %Hh%Mm%Ss")


class CustomFormatter(logging.Formatter):
    def format(self, record):
        message = record.getMessage()

        # Para separadores visuales, escribir solo el mensaje sin prefijo de nivel.
        if message and set(message) == {"="} or (message and (message[:7] == "❌ Fila" or message[:7] == "⚠️ Fila")):
            return message

        return super().format(record)

class Logger():

    def __set_logger(self):
        log_directory = 'Logs/'
        log_filename = fecha + '  validaciones.log'
        

        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)



        log_path = os.path.join(log_directory, log_filename)
        file_handler = logging.FileHandler(log_path, encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)

        formatter = CustomFormatter(
            '%(levelname)s | %(message)s', "%Y-%m-%d %H:%M:%S")
        file_handler.setFormatter(formatter)

        if (logger.hasHandlers()):
            logger.handlers.clear()

        logger.addHandler(file_handler)

        return logger
    
    @classmethod
    def add_to_log(cls, level, message):
        try:
            logger = cls.__set_logger(cls)

            if (level == "critical"):
                logger.critical(message)
            elif (level == "debug"):
                logger.debug(message)
            elif (level == "error"):
                logger.error(message)
            elif (level == "info"):
                logger.info(message)
            elif (level == "warn"):
                logger.warn(message)

        except Exception as ex:
            print(traceback.format_exc())#Esto es para traza de errores
            print(ex)