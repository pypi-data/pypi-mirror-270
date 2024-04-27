#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This file is part of dcc-xmljsonconv (https://gitlab1.ptb.de/digitaldynamicmeasurement/dcc_XMLJSONConv)
# Copyright 2024 [Benedikt Seeger(PTB), Thomas Bruns (PTB), Vanessa Stehr(PTB)]
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
import requests
import json
from lxml import etree
import sys
import pathlib
import io

def download_xsd(url: str):
    """
    Downloads an XSD file from a given URL.

    Parameters:
        url (str): The URL of the XSD file to download.

    Returns:
        io.BytesIO: A bytes stream of the downloaded XSD file if successful, None otherwise.
    """
    response = requests.get(url)
    if response.status_code == 200:
        return io.BytesIO(response.content)
    return None

def find_list_types(xsd_path: str):
    """
    Parses an XSD file to find elements with types ending in 'ListType'.

    Parameters:
        xsd_path (str): The path to the XSD file.

    Returns:
        tuple: A tuple containing two elements; the first is a list of names of the list types,
               and the second is a list of attributes of the list types.
    """
    tree = etree.parse(xsd_path)
    list_types = []
    for element in tree.iter():
        if 'type' in element.attrib and element.attrib['type'].endswith('ListType'):
            list_types.append(dict(element.attrib))
    names = [list_type['name'] for list_type in list_types]
    return names, list_types

def find_repeated_elements(xsd_path: str):
    """
    Parses an XSD file to identify elements that can be repeated.

    Parameters:
        xsd_path (str): The path to the XSD file.

    Returns:
        tuple: A tuple containing two elements; the first is a list of names of the repeated elements,
               and the second is a dictionary with the names as keys and the max occurrences as values.
    """
    tree = etree.parse(xsd_path)
    repeated_elements = {}
    for element in tree.iter():
        if element.tag is etree.Comment:
            continue
        if element.tag.endswith('element'):
            name = element.get('name')
            max_occurs = element.get('maxOccurs', '1')  # Default is 1 if not specified
            if max_occurs not in ('1', 'unbounded'):
                repeated_elements[name] = max_occurs
            elif max_occurs == 'unbounded':
                repeated_elements[name] = 'unbounded'
    names = list(repeated_elements.keys())
    return names, repeated_elements

def write_to_json(data, file_path: str):
    """
    Writes a given data structure to a JSON file.

    Parameters:
        data (dict): The data to write to the file.
        file_path (str): The path to the JSON file where the data should be saved.
    """
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def getListTypesFromUrl(url: str):
    """
    Downloads an XSD file from a URL and analyzes it to find list types and repeated elements.

    Parameters:
        url (str): The URL of the XSD file.

    Returns:
        tuple: A tuple containing information about list types and repeated elements found in the XSD file.
    """
    xsd_file = download_xsd(url)
    if xsd_file:
        names, list_types = find_list_types(xsd_file)
        xsd_file.seek(0)  # Reset file pointer to the beginning
        repeated_field_names, repeated_field_types = find_repeated_elements(xsd_file)
        return names, list_types, repeated_field_names, repeated_field_types
    else:
        print("Failed to download XSD file.")
        return ['Failed to download XSD file.'], ['Failed to download XSD file.'], ['Failed to download XSD file.'], ['Failed to download XSD file.']

def main():
    """
    The main function to run the script. It handles command-line arguments for the XSD URL
    and output JSON file path, processes the XSD file to extract list types and repeated elements,
    and writes the results to a JSON file.
    """
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = "https://ptb.de/dcc/v3.2.1/dcc.xsd"
        url= "https://ptb.de/si/v2.1.0/SI_Format.xsd"
    if len(sys.argv) > 2:
        json_file_path = sys.argv[2]
    else:
        script_location = pathlib.Path(__file__).resolve().parent.parent
        json_file_path = script_location.parent / 'data' / 'listDCCElements.json'
    names, list_types, repeatedFiledNames, repeatedFiledTypes = getListTypesFromUrl(url)
    write_to_json({'schemaUrl': url, 'listTypeElements': names, 'listTypeElementsDetails': list_types, 'repeatedFieldNames': repeatedFiledNames, 'repeatedFieldNamesDetails': repeatedFiledTypes}, json_file_path)
    print(f"List types have been written to {json_file_path}")

if __name__ == "__main__":
    main()
