# DriveThruRPG Sales Report Parser

We use this to generate a report for easy sales receipt and deposit entry into Quickbooks. It produces a "report" that provides monthly quantities, gross $ amount, net $ amount, and the fee $ amount.

To use:

1. Download or checkout this tool into a folder. It has no requirements other than python >= 3.7.
1. Generate a sales report from DTRPG using the "Download vs print vs combo by title" setting, monthly subtotals on, and output to CSV.
1. Drop that CSV into the tool's folder with a name of "monthly-report.csv".
1. Run `python main.py`.
1. Open the resulting JSON file in your tool of choice, preferably something that can format it with indentation.

If you have any questions about how this works, post an issue on GitHub, hit us up on twitter at @PlayFutureProof, or Melissa specifically on Mastodon at irrsinn.life/@melissa.