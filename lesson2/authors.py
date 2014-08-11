#!/usr/bin/env python
# Your task here is to extract data from xml on authors of an article
# and add it to a list, one item for an author.
# See the provided data structure for the expected format.
# The tags for first name, surname and email should map directly
# to the dictionary keys
import xml.etree.ElementTree as ET

article_file = "exampleResearchArticle.xml"


def get_root(fname):
    tree = ET.parse(fname)
    return tree.getroot()


def get_authors(root):
    authors = []
    for author in root.findall('./fm/bibl/aug/au'):
        data = {
                "insr": [],
                "fnm": None,
                "snm": None,
                "email": None
        }

        # YOUR CODE HERE
        for i in author.findall('insr'):
            iid = i.attrib['iid']
            data['insr'].append(iid)
        fnm = author.find('fnm')
        snm = author.find('snm')
        email = author.find('email')
        data['fnm'] = fnm.text
        data['snm'] = snm.text
        data['email'] = email.text
        authors.append(data)
        print data

    return authors

def test():
    solution = [{'insr': ['I1'], 'fnm': 'Omer', 'snm': 'Mei-Dan', 'email': 'omer@extremegate.com'},
               {'insr': ['I2'], 'fnm': 'Mike', 'snm': 'Carmont', 'email': 'mcarmont@hotmail.com'},
               {'insr': ['I3', 'I4'], 'fnm': 'Lior', 'snm': 'Laver', 'email': 'laver17@gmail.com'},
               {'insr': ['I3'], 'fnm': 'Meir', 'snm': 'Nyska', 'email': 'nyska@internet-zahav.net'},
               {'insr': ['I8'], 'fnm': 'Hagay', 'snm': 'Kammar', 'email': 'kammarh@gmail.com'},
               {'insr': ['I3', 'I5'], 'fnm': 'Gideon', 'snm': 'Mann', 'email': 'gideon.mann.md@gmail.com'},
               {'insr': ['I6'], 'fnm': 'Barnaby', 'snm': 'Clarck', 'email': 'barns.nz@gmail.com'},
               {'insr': ['I7'], 'fnm': 'Eugene', 'snm': 'Kots', 'email': 'eukots@gmail.com'}]
    root = get_root(article_file)
    data = get_authors(root)
    assert data[0] == solution[0]
    assert data[1]["insr"] == solution[1]["insr"]


test()