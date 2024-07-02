import logging
logger = logging.getLogger(__name__)


# create logging formatter
logFormatter = logging.Formatter(f'%(asctime)s - %(name)s - %(levelname)s - %(message)s')


#Create a file handler
fileHandler = logging.FileHandler('calls.log')
fileHandler.setLevel(logging.INFO)

#Create a console handler
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.INFO)
consoleHandler.setFormatter(logFormatter)

logger.addHandler(consoleHandler)
logger.addHandler(fileHandler)