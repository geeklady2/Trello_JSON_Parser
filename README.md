# Trello JSON Parser
Trello JSON Parser is a single python file that parses exxported
JSON data from trello and saves the parsed data into a csv file, 
where each row in the csv file represents a single card on the
Trello board

> Output Column Descriptions

| Column Name     | Description                                       |
------------------|---------------------------------------------------|
| Title           | Name or title on the card                         |
| Latest Activity | Last activity on the card                         |
| Board Name      | Which board the card belongs to                   |
| Board URL       | URL to the board the card belongs to              |
| Closed          | Whether or not the card is closed                 |
| List Name       | The name of the list or group the card belongs to |
| Description     | The cards detailed description                    |
| Members         | Team members associated with the card             |
| Labels          | Labels given to the card                          |
| Check Lists     | Check lists associated with the card              |
|-----------------|---------------------------------------------------|
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


