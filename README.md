# Stash ID to Whisparr v3 Monitor Script
This is a script that will take in a list of IDs from idsToMonitor.txt and monitor them Whisparr. I used ChatGPT to help make this so my Whisparr Instance does not get overrun with scenes that I do not want monitored when I transition from V2 to V3.

## You will need the following installed:
 - [Python3](https://www.python.org/downloads/)
 - [PIP](https://pip.pypa.io/en/stable/installation/)
 - [The Python Requests module](https://pypi.org/project/requests/)

After installing, open the main.py file in a text editor and change the WHISPARR_BASE_URL and WHISPARR_API_KEY to match your local instance URL and API key.

Next, open a command prompt or terminal and navigate to where you saved the script and .txt file of your IDs you wish to monitor. Then just run <code>python3 main.py</code> to run the script. You should see the script start outputting to the console when it is monitoring scenes!



You can create your own list of IDs, but I grabbed mine from the stash-go.sqlite database created by stash that already houses all my scenes.
## $${\color{red}WARNING}$$
$${\color{red}YOU \space CAN \space CREATE \space MAJOR \space PROBLEMS \space IN \space YOUR \space DATABASE.}$$
$${\color{red}PLEASE \space COPY \space AND \space PASTE \space YOUR \space DATABASE \space TO \space ANOTHER \space LOCATION \space FOR \space A \space BACKUP \space IF \space YOU \space ARE \space UNSURE}$$
$${\color{red}WHAT \space YOU \space ARE \space DOING}$$

I used a database visualizer tool called [DB Browser for SQLite](https://sqlitebrowser.org/) to get mine.

The query I used returns a list of IDs based on if they were entered using the StashDB endpoint (scraped with StashDB.)

#### <code>SELECT stash_id FROM scene_stash_ids WHERE endpoint = 'https://stashdb.org/graphql';</code>

To use this method:
1. Open database in visualizer
2. Click on the "Execute SQL" tab
3. Paste the above query in the text area below the SQL 1 tab
4. Hit the play button

After hitting play, the list of IDs should populate in the bottom. You can click one, then click CTRL-A to copy them all to paste in the file
