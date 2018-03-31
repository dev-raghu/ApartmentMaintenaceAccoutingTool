"""
Utility to manage accounting of prakruthi lake view apartments
author@raghu
"""
import sqlite3
from LogManager import LOG


# TODO: Combine table USER and PAYMENT_HISTORY; since there is just one-to-one relation between these two entities
class DBManager:
    """
    Util class to manage database.
    Functions: manage transactions in the database PrakruthiLakeView.db
    """

    def __init__(self):
        """

        :rtype: object
        """
        self.dbName = "PrakruthiLakeView.db"
        self.tableName = " ";

    def openConnection(self):
        try:
            self.conn = sqlite3.connect(self.dbName)
            LOG.info("Connected to db [" + self.dbName + "]")
        except sqlite3.OperationalError as oe:
            LOG.error("Operational Error: " + str(oe))
        except sqlite3.IntegrityError as ie:
            LOG.error("Integrity Error: " + str(ie))
        except sqlite3.InterfaceError as ie:
            LOG.error("Interface Error: " + str(ie))
        except sqlite3.NotSupportedError as ie:
            LOG.error("Not Supported Error: " + str(ie))
        except sqlite3.InternalError as ie:
            LOG.error("Internal Error: " + str(ie))

    def closeConnection(self):
        try:
            # this method takes care of both committing the changes and closing the connection
            self.conn.commit()
            LOG.info("Transactions committed " + self.tableName)
            self.conn.close()
            LOG.info("Connection to db [" + self.dbName + "] closed")
        except sqlite3.OperationalError as oe:
            LOG.error("Operational Error: " + str(oe))
        except sqlite3.IntegrityError as ie:
            LOG.error("Integrity Error: " + str(ie))
        except sqlite3.InterfaceError as ie:
            LOG.error("Interface Error: " + str(ie))
        except sqlite3.NotSupportedError as ie:
            LOG.error("Not Supported Error: " + str(ie))
        except sqlite3.InternalError as ie:
            LOG.error("Internal Error: " + str(ie))

    def initDB(self):
        try:
            self.cursor = self.conn.cursor()
            LOG.info("Cursor created for connection to db [" + self.dbName + "]")
        except sqlite3.OperationalError as oe:
            LOG.error("Operational Error: " + str(oe))
        except sqlite3.IntegrityError as ie:
            LOG.error("Integrity Error: " + str(ie))
        except sqlite3.InterfaceError as ie:
            LOG.error("Interface Error: " + str(ie))
        except sqlite3.NotSupportedError as ie:
            LOG.error("Not Supported Error: " + str(ie))
        except sqlite3.InternalError as ie:
            LOG.error("Internal Error: " + str(ie))

    # for active execution, keep passive execution like select in its own method
    def execute(self, command, message, rowData=None):
        try:
            if rowData is None:
                self.cursor.execute(command)
                LOG.info(message)
            else:
                if "UPDATE" in command:
                    self.cursor.execute(command, rowData)
                    LOG.info(message)
                else:
                    self.cursor.executemany(command, rowData)
                    LOG.info(message)
        except sqlite3.OperationalError as oe:
            LOG.error("Operational Error: " + str(oe))
        except sqlite3.IntegrityError as ie:
            LOG.error("Integrity Error: " + str(ie))
        except sqlite3.InterfaceError as ie:
            LOG.error("Interface Error: " + str(ie))
        except sqlite3.NotSupportedError as ie:
            LOG.error("Not Supported Error: " + str(ie))
        except sqlite3.InternalError as ie:
            LOG.error("Internal Error: " + str(ie))

    def createTable(self, tableName, command):
        self.tableName = tableName
        self.execute(command, "Created table " + self.tableName)

    def insertData(self, tableName, command, rowData):
        self.tableName = tableName
        self.execute(command, "Inserted into table " + self.tableName, rowData)

    def updateData(self, tableName, command, updateData):
        """

        :rtype: object
        """
        self.tableName = tableName
        self.execute(command, "Updated table " + self.tableName, updateData)
        self.conn.commit()

    def selectData(self, tableName, command, searchKey=None):
        self.tableName = tableName
        if searchKey is None:
            LOG.info("Fetching Data from table " + self.tableName + " with key value  " + str(searchKey))
            return self.cursor.execute(command)
        else:
            self.cursor.execute(command,searchKey)
            LOG.info("Fetching Data from table " + self.tableName + " with key value  " + str(searchKey))
            return self.cursor.fetchone()







