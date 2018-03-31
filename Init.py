"""
Init script to populate db with current lot of people in the flat
Also to reduce the effort in drastically having to re-write when editing through interface
author@raghu
"""
from DBManager import DBManager
from LogManager import LOG
import json

class Init:
    def __init__(self):
        dbManager = DBManager()
        dbManager.openConnection()
        dbManager.initDB()
        # create table to store the tenant/owner maintenance data
        self.tableName = "maintenance"
        self.tableCommand = '''CREATE TABLE IF NOT EXISTS maintenance 
                                (FLATNO TEXT PRIMARY KEY NOT NULL,
                                OCCUPANT_NAME TEXT,
                                DATE TEXT,
                                AMT_PAID REAL NOT NULL,
                                AMT_DUE REAL NOT NULL,
                                MODE_OF_PAYMENT TEXT NOT NULL)'''
        dbManager.createTable(self.tableName, self.tableCommand)

        self.tableName = "reference"
        self.tableCommand = '''CREATE TABLE IF NOT EXISTS reference
                                (ID INT PRIMARY KEY NOT NULL,
                                MAINT_AMT REAL NOT NULL,
                                LATE_FEE_AMT REAL NOT NULL,
                                LAST_DATE TEXT NOT NULL
                                )'''
        dbManager.createTable(self.tableName, self.tableCommand)
        self.populateDB(dbManager)
        dbManager.closeConnection()

    def populateDB(self, dbManager):
        with open('UserSettings.json') as datastore:
            initialUserSettings = json.load(datastore)
            LOG.info("INITIAL USER SETTINGS: " + json.dumps(initialUserSettings))
            flatNumbers = initialUserSettings["flatNumbers"]
            occupantNames = initialUserSettings["defaultOccupantNames"]
            date = initialUserSettings["date"]
            amtPaid = initialUserSettings["amtPaid"]
            amtDue = initialUserSettings["amtDue"]
            currentMaintenanceAmt = initialUserSettings["currentMaintenanceAmt"]
            currentLateFee = initialUserSettings["currentLateFee"]
            currentLastDate = initialUserSettings["currentLastDate"]
            defaultPaymentMode = initialUserSettings["defaultPaymentMode"]

            # maintenance schema
            ##########################################################################
            # Flat No # Occupant Name # Owner Name # Date # Amount Paid # Amount Due #
            ##########################################################################
            # This is to insert preliminary data about occupants and their data
            self.tableName = "maintenance"
            self.tableCommand = "INSERT INTO maintenance VALUES (?, ?, ?, ?, ?, ?)"
            for flatNumber, occupantName in zip(flatNumbers,occupantNames):
                rowData = [(flatNumber, occupantName, date, amtPaid, amtDue, defaultPaymentMode)]
                dbManager.insertData(self.tableName, self.tableCommand, rowData)
            # reference scheme
            ############################################################
            # currentMaintenanceAmt # currentLateFee # currentLastDate #
            ############################################################
            # This is to insert fixed maintenance at the beginning, keep only one entry and keep updating that entry
            self.tableName = "reference"
            self.tableCommand = "INSERT INTO reference VALUES (?, ?, ?, ?)"
            rowData = [(1, currentMaintenanceAmt, currentLateFee, currentLastDate)]
            dbManager.insertData(self.tableName, self.tableCommand, rowData)

accountingTool = Init()