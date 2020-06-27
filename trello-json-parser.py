#!/usr/bin/env python2

#######################################################################
# Name: trello-json-to-csv.py
# Created: June 26, 2020
# Author: Shannon Jaeger, Boast Capital
# 
# Description:
# This script converts JSON exported from a Trello board and creates
# a CSV file, each row representing a card on the Trello board
#
# Usage:
# Before executing code
# pip install pandas
#
# python trello-json-to-csv.py <inputFile> <outputFile>
#
# eg.
# python trello-json-to-csv.py myTrelloData.json  myTrellData.csv
#
#############################################3########################
import json
import os
import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("input", help="JSON File from Trello", type=str)
parser.add_argument("output", help="File to output to", type=str)
parser.add_help = True
args = parser.parse_args()


print "Reading Data..."
with open(os.path.abspath(args.input)) as f:
    data = json.load(f)
#print(json.dumps(data, indent=4))

print "Found {} cards in {} lists.".format(len(data['cards']), len(data['lists']))
print "Parsing..."
#print(json.dumps(data, indent=4))

# Grab some of the 
lists = {l['id']: l['name'] for l in data['lists']}
users = {u['id']: u['fullName'] for u in data['members']}
labels = {l['id']: l['name'] for l in data['labels']}
check_lists = {c['id']: c['name'] for c in data['checklists']}


column_names = [
    'Card Id',
    'Card Name',
    'Card URL', 
    'Card Description',
    'Labels',
    'Members',
    'Due Date',
    'Attachment Count',
    'Attachment Links',
    'Checklist Item Total Count',
    'Checklist Item Completed Count', 
    'Vote Count',
    'Last Activity Date',
    'List ID',
    'List Name',
    'Board ID',
    'Board Name',
    'Archived'
]

card_matrix = []
for c in data['cards']:
    card = [
        c['id'],                                                              # Card ID
        c['name'],                                                            # Card Name
        c['url'],                                                             # Card URL
        c['desc'],                                                            # Card Description
        ':'.join([l for k, l in labels.items() if k in c['idLabels']]),       # Labels
        ':'.join([u for k, u in users.items() if k in c['idMembers']]),       # Members
        c['badges']['due'] != "null" if c['due'] else " ",                                # Due Date
        0,                                                                    # Attachment Count
        "",                                                                   # Attachment Links
        0,                                                                    # Checklist Item Total Count
        0,                                                                    # Checklist Item Completed Count
        0,                                                                    # Vote Count
        c['dateLastActivity'],                                                # Last Activity Date
        c['idList'],                                                          # List ID
        lists[c['idList']],                                                   # List Name
        data['id'],                                                           # Board ID
        data['name'],                                                         # Bard Name
        c['closed'],                                                          # Archived
    ]
    card_matrix.append(card)
#print(card_matrix)

df = pd.DataFrame(card_matrix,columns=column_names) 
df.to_csv(args.output, sep=',', encoding='utf-8', index=False)

