# Trello JSON Parser
Trello JSON Parser is a single python file that parses exxported
JSON data from trello and saves the parsed data into a csv file.

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

## Example
```bash
python trello-json-parser.py myTrelloExport.json myTrelloSummary.csv
```

