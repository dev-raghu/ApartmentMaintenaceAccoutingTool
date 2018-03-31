# ApartmentMaintenaceAccoutingTool  
Simple python utility I wrote to manage my apartment's maintenance accounts. Used pyqt5 for gui and sqlite3 for db. I didn't care to improve much on it as this was sufficient for my work.  
For some context, there are 50 houses' in my apartment and I had to manually manage it in excel. So I though of writing a quick program that would enable me to add maintenance amount, date and mode of payment quickly and export it to excel/csv if wanted, saving me some time.  
  
## USAGE:  
1. If you want to play around, just run the `Init.py` script to popuate the db with some dummy data and then run `AccountingInterface.py` for testing the gui and actual functionality.  
  
2. After running `AccountingInterface.py`, you should be able to:  
  

	>     a. Double click on flat# to edit flat details  
	>       
	>     b. Click on export button to export the table to a csv