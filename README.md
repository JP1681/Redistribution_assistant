This tool is designed to assist with drawing boundaries for federal redistributions.
If you want to use this tool for the 2023 redistribution in Victoria, just open redist.html.
**Note:** the default enrolment data is the newest version (published January 2024). The original data (published October 2023) contained errors.

There are instructions for drawing other states/territories at the end of this file.

Once you open redist.html, use the file selection tools to pick the boundary files. The SA1 shapefile must be added using the first **Browse...** button. Other boundary files can be added using the second **Browse...** button.
For these other files, you can click their name to select a display colour.

View mode
* Use the dropdown menu to highlight each group that you have proposed. A group contains one or more divisions. You can also view all groups at once (**None**) or only SA1s that have not been allocated (**Unallocated SA1s**).
* Use the **Change colour** button to edit the display colour of a particular group.
* Press the **Heatmap** button to cycle through various heatmaps, highlighting SA1s by current/projected population, and growth.
* Use the **Save progress** button to generate a .js file containing the groups and names you have proposed so far. Once you press the button, click the download link. You should overwrite the existing ``allocations.js`` file in the directory.
* Use the **Generate allocation.csv** button to download a .csv file containing each SA1 code, and its allocated group.
* Use the checkboxes to toggle other boundaries on and off.
* Use the **Get image** button in the top right corner of the map to save a copy of the current view. **Note that the scale parameter does not behave as expected, so it is recommended that you only use a scale of 1. I plan to fix this in a future version.**

Edit mode:
* Use the dropdown menu to select a group to edit. You can edit the name in the textbox, then press ``Enter``.
* You can use groups to split a state or territory into regions consisting of multiple divisions, then splitting the region further. This may be a better approach than simply drawing one division at a time.
* When your map is finished, every group should contain exactly 1 division.
* SA1s are coloured as follows:
    * Current division: green
	* Different division: red
	* Not yet allocated: black
* Group names and populations are coloured as follows:
	* Outside either tolerance: red
	* Inside both tolerances but group contains more than one division: yellow
	* Inside both tolerances and group contains exactly one division: green
* Groups that contain more than one division appear in italics.
* To move to another group, either use the dropdown menu or right-click on an SA1 in a different group.
* You can add/remove SA1s to/from a group by left-clicking on them. The current and projected populations will update automatically.
* Click the **SA1** button to move to SA2/3/4. For example, if SA3 is selected, clicking an SA1 will add/remove all other SA1s in that SA3.
* Select the **Lock SA1s** checkbox to lock SA1s that are already allocated to a different group.
* The dropdown menu is highlighted according to the population in each group. If the group's population is within current and projected tolerances, it will be yellow (>1 division) or green (1 division). Otherwise, it will be red.
* There is information about divisions that are outside the required tolerances. It DOES NOT refresh automatically, only when you click **Refresh this data** or the dropdown menu. Monitor this to ensure you don't draw too many divisions under or over.

Using this tool for other states/territories:
* Install Python, if you don't have it already.	
* You will need the SA1 shapefile for the state/territory you are drawing. You may also want to display state districts, current divisions or LGAs. I have created compressed and non-compressed versions of each file, and you can find them at this link: https://drive.google.com/drive/folders/1ml4ganrZFcE4lVtFHDeJRpPdG6cSjEbS?usp=sharing. You can also select other files in GeoJSON format.
* You also need the enrolment data from the AEC. Of the two Excel files available, download the one that does NOT end with "by Division". There is no need to convert to .csv format.
* Run the batch file ``switchStates.bat``. It will ensure **numpy** and **openpyxl** are installed. Then, select the enrolment data file. It will ask you to identify which columns contain SA1 codes and population estimates, and how many divisions you are drawing.
* The program will create two files (``populations.js`` and ``allocations.js``). You can then open ``redist.html``.