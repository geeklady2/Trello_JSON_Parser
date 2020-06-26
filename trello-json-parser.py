#!/usr/bin/env python2

#######################################################################
# Name: trello-json-to-csv.py
# Created: June 26, 2020
# Author: Shannon Jaeger
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

lists = {l['id']: l['name'] for l in data['lists']}
users = {u['id']: u['fullName'] for u in data['members']}
labels = {l['id']: l['name'] for l in data['labels']}
check_lists = {c['id']: c['name'] for c in data['checklists']}



card_matrix = []
for c in data['cards']:
    card = [
        c['name'],
        c['dateLastActivity'],
        data['name'],
        data['shortUrl'],
        c['closed'],
        lists[c['idList']],
        c['desc'],
        ':'.join([u for k, u in users.items() if k in c['idMembers']]),
        ':'.join([l for k, l in labels.items() if k in c['idLabels']]),
        ':'.join([l for k, l in check_lists.items() if k in c['idCheckLists']])
    ]
    card_matrix.append(card)
#print(card_matrix)

df = pd.DataFrame(card_matrix,columns=['Title', 'Last Activity','Board Name', 'Board URL', 'Closed', 'List Name', 'Description', 'Members', 'Labels', 'Check Lists']) 
df.to_csv(args.output, sep=',', encoding='utf-8', index=False)

