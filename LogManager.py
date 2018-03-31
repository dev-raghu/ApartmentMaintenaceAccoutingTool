import logging
from logging.handlers import RotatingFileHandler
import os, errno

# configure log level to INFO level
LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)

# create a logger file and assign a handler to manage logs
try:
    os.makedirs("logs")
except OSError as ose:
    if ose.errno != errno.EEXIST:
        raise
logHandler = RotatingFileHandler("logs/AccountsManager.log", maxBytes = 1024*1024*1024, backupCount = 10)
logHandler.setLevel(logging.INFO)

# create a logging format
logFormatter = logging.Formatter('[%(levelname)s]: %(asctime)s : %(message)s')
logHandler.setFormatter(logFormatter)

# add logHandler to logger
LOG.addHandler(logHandler)