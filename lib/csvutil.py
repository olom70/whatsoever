# useful functions written while manipulating files
import csv
import time
import os

def createfiles(l: list()) -> list():
    '''
        create the files for MAP import
        input : a list of filename to create
        output : for each input file : a file named after the input, and a csv.writer to put content in it
    '''
    r = []
    for v in l:
        csvfile = open(v, 'w+', newline='', encoding="utf-8")
        writer = csv.writer(csvfile, delimiter=';',
                            quotechar='"', quoting=csv.QUOTE_ALL)
        r += [csvfile, writer]
    return r


def initElements(**kwargs):
    '''
        initialise the row that is about to be written in a file containing the artefacts to import into Archi
    '''
    ID = ''
    Type = ''
    Name = ''
    Documentation = ''

    for k, v in kwargs.items():
        if k == 'ID': ID = v
        if k == 'Type' : Type = v
        if k == 'Name' : Name = v
        if k == 'Documentation' : Documentation = v

    return [ID, Type, Name, Documentation]

def initElementsHeader():
    '''
        Initialise the first row of the element file : the header
        "ID","Type","Name","Documentation"
    '''
    return initElements(ID='ID', Type='Type', Name='Name', Documentation='Documentation')

def initProperties(**kwargs):
    '''
        initialise the row that is about to be written in a file containing the properties to import into Archi
    '''
    ID = ''
    Key = ''
    Value = ''
    for k, v in kwargs.items():
        if k == 'ID': ID = v
        if k == 'Key': Key = v
        if k == 'Value': Value = v

    return [ID, Key, Value]

def initPropertiesHeader():
    '''
        Initialise the first row of the relation file : the header
        "ID","Key","Value"
    '''
    return initProperties(ID='ID', Key='Key', Value='Value')

def initRelations(**kwargs):
    '''
        initialise the row that is about to be written in a file containing the relations to import into Archi
        "ID","Type","Name","Documentation","Source","Target"
    '''
    ID = ''
    Type = ''
    Name = ''
    Documentation = ''
    Source = ''
    Target = ''
    for k, v in kwargs.items():
        if k == 'ID': ID = v
        if k == 'Type': Type = v
        if k == 'Name': Name = v
        if k == 'Documentation': Documentation = v
        if k == 'Source': Source = v
        if k == 'Target': Target = v

    return [ID, Type, Name, Documentation, Source, Target]

def initRelationsHeader():
    '''
        Initialise the first row of the relation file : the header
        "ID","Type","Name","Documentation","Source","Target"
    '''
    return initRelations(ID='ID', Type='Type', Name='Name', Documentation='Documentation', Source='Source', Target='Target')
