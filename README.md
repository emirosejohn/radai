# radai
Command Line python to query data from https://github.com/radaisystems/food-facilities-challenge

Use the command line flags to query results.

Examples:
python index.py --applicant-name=Cochinita  
python index.py --latitude=37.730906150359694 --longitude=-122.37330257748522 --status=EXPIRED


PROBLEMS:
The search params are no inclusive. The query will return correct results for exact searches. Searching for --applicant-name=Coc will not return the expected results for an applicant with the name Cochinita. Unfortunately, I do not have the bandwith to complete this project.


Emily