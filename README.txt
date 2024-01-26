This tool is designed to assist with drawing boundaries for federal redistributions.
It is currently set up for the 2023 redistribution of Victoria into 38 divisions.
If you want to use this tool for drawing boundaries in Victoria, just open redist.html. Otherwise, there are instructions to modify the setup at the end of this file.

View mode:
	Use the dropdown menu to highlight each division that you have proposed.

	Press the heatmap button to cycle through various heatmaps, highlighting SA1s by current/projected population, and growth.

	Use the save progress button to generate a .js file containing the divisions and names you have proposed so far. Once you press the button, click the download link. You should overwrite the existing 'allocations.js' file in the directory.

	Use the Generate allocation.csv button to download a .csv file containing each SA1 code, and its allocated division.

	Use the checkboxes to toggle other boundaries on and off.

Edit mode:
	Use the dropdown menu to select a division to edit. You can edit the name in the textbox, then press Enter or click the Change name button.

	SA1s are coloured as follows:
		Current division: green
		Different division: red
		Not yet allocated: black
	
	To move to another division, either use the dropdown menu or right-click on an SA1 in a different division.

	You can add/remove SA1s to/from a division by left-clicking on them. The current and projected populations will update automatically.

	Click the SA1 button to move to SA2/3/4. For example, if SA3 is selected, clicking an SA1 will add/remove all other SA1s in that SA3.

	Select the Lock SA1s checkbox to lock SA1s that are already in a different division.

	The dropdown menu is highlighted according to the population in each division. A division name will remain red until both current and projected populations are within the required tolerances, when it will become green.

	The Remaining divisions section contains information about divisions that are outside the required tolerances. It DOES NOT refresh automatically when you edit the division. It will only refresh when you click the Refresh this data button, or if you click on the dropdown menu. Monitor this data to ensure you don't draw too many divisions under or over.


Using this tool for other states/territories:
	Install Python, if you don't have it already.

	Shapefiles for state districts, current divisions, SA1s and LGAs are needed. I have created compressed and non-compressed versions of these in the required format, and you can find them at this link: https://drive.google.com/drive/folders/1VpdPAenFMvrSHnL26kkZiUetMWNbmTgV?usp=sharing

	You also need the enrolment data from the AEC. Of the two Excel files available, pick the one that does NOT end with "by Division". There is no need to convert to .csv format.
	
	Select the boundary files you want to use, and save them in the shapefiles folder.

	Run the batch file switchStates.bat. It will ensure numpy and openpyxl are installed. Then, you need to select the file containing enrolment data. It will ask you to identify which columns contain SA1 codes and population estimates, then ask how many divisions you are drawing.
	The program will create one file (allocations.js). You can then open redist.html.