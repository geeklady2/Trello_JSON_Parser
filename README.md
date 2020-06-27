# Trello JSON Parser
Trello JSON Parser is a single python file that parses exxported
JSON data from trello and saves the parsed data into a csv file, 
where each row in the csv file represents a single card on the
Trello board

### Output File Column Descriptions

| Column Name                    | Description                                       | Implemented |
---------------------------------|---------------------------------------------------|-------------|
| Card ID                        | Unique ID for the Card                            | Yes         |
| Card Name                      | Name or title on the card                         | Yes         |
| Card URL                       | URL to the card                                   | Yes         |
| Card Description               | The cards detailed description                    | Yes         |
| Labels                         | Labels given to the card                          | Yes         |
| Members                        | Team members associated with the card             | Yes         |
| Due Date                       | Date the task on the card is due                  | Yes         |
| Attachment Count               | Number of attachments                             | Yes         |
| Attachment Links               | URLs to the attachments                           | No          |
| Checklist Item Total Count     | How many checklist items there are                | Yes         |
| Checklist Item Completed Count | How many checklist items have been completed      | Yes         |
| Vote Count                     | How many votes the card has                       | Yes         |
| Latest Activity Date           | Last activity on the card                         | Yes         |
| List Id                        | ID of the list the card is on                     | Yes         |
| List Name                      | The name of the list or group the card belongs to | Yes         |
| Board ID                       | ID of the bard the card is on                     | Yes         |
| Board Name                     | Which board the card belongs to                   | Yes         |
| Archived                       | Whether or not the card is closed                 | Yes         |


## Installation
```bash
curl -H 'Accept: application/vnd.github.v3.raw' \
     -O  \
     -L  https://github.com/geeklady2/Trello_JSON_Parser/blob/master/trello-json-parser.py

pip install pandas
```

## Usage
```python
python trello-json-parser.py <inputFile.json> <outputFile.csv>
```

## Example
```bash
python trello-json-parser.py myTrelloExport.json myTrelloSummary.csv
```


