import pylightxl as xl
import platform
import lib.csvutil as csvutil
import lib.stringutil as stringutil
import os
import time
import pyyed

def feedList() -> tuple:

    if (platform.system() == 'Linux'):
        MAIN_FOLDER = "/home/olom/importVIPHierarchy"
    else:
        MAIN_FOLDER ="C:/Users/MOREAUCL/Documents/importVIPHierarchy"

    IMPORTED_FILE = 'VIP - Exigences - Offre Outil Cible.xlsx'
    YEDFILE = 'VIP.graphml'
    INPUT = MAIN_FOLDER + os.path.sep + IMPORTED_FILE
    ELEMENTTYPE = 'Grouping'
    RELATIONTYPE = 'CompositionRelationship'
    KEY = 'import'
    VALUE = 'VIP'
    L1FONTSTYLE = "bold"
    L1FONTSIZE = "14"
    L2FONTSTYLE = "plain"
    L2FONTSIZE = "13"
    L3FONTSTYLE = "plain"
    L3FONTSIZE = "12"
    WIDTH='200'
    L1COLOR="#DE1FF2"
    L2COLOR="#07F2B8"
    L3COLOR="#F2BE1F"

    size = []
    name = []
    parent = []
    level = []
    textinfo = []


    try:
        os.mkdir(MAIN_FOLDER)
    except FileExistsError as fe:
        pass
    except FileNotFoundError as fnf:
        print('wrong path, correct MAIN_FOLDER') 
        exit()
    except Exception as e:
        print(f'unexpected error : {type(e)}{e.args}')
        exit()

    if not os.path.isfile(INPUT):
        print(f'this file does not exists {input}. put it in the folder {MAIN_FOLDER}')

    db = xl.readxl(fn=INPUT)

    colId =  db.ws(ws='Exigences-besoins').col(col=2)
    colCategory = db.ws(ws='Exigences-besoins').col(col=3)
    colPerimeter = db.ws(ws='Exigences-besoins').col(col=5)
    colthematic = db.ws(ws='Exigences-besoins').col(col=6)
    colgroup = db.ws(ws='Exigences-besoins').col(col=7)
    colUseCase = db.ws(ws='Exigences-besoins').col(col=8)
    colDescription = db.ws(ws='Exigences-besoins').col(col=10)
    colPriority = db.ws(ws='Exigences-besoins').col(col=14)

    l_alreadyAdded = []

    for items in zip(colId, colCategory, colPerimeter, colthematic, colgroup, colUseCase, colDescription, colPriority):
#                      0       1            2               3          4         5             6              7
        if items[1] == 'xx':  # coulb be used to avoid processing 'Besoins'
            pass
        else:
            # IDgeneration ####################################################
            Level1ID = stringutil.cleanName(
                                                items[2],
                                                True,
                                                True,
                                                'lowercase',
                                                True,
                                                True,
                                                True) \
                            + '_Level1'
            if Level1ID not in ['NoName_Level1', 'périmètre_Level1', 'thématique_Level1', 'rgpt_Level1']:
                Level2ID = Level1ID+stringutil.cleanName(
                                                    items[3],
                                                    True,
                                                    True,
                                                    'lowercase',
                                                    True,
                                                    True,
                                                    True) \
                                + '_Level2'
                Level3ID = Level2ID+stringutil.cleanName(
                                                    items[4],
                                                    True,
                                                    True,
                                                    'lowercase',
                                                    True,
                                                    True,
                                                    True) \
                                + '_Level3'
                
                #Level1 ###############################################################1
                if Level1ID not in l_alreadyAdded:
                    l_alreadyAdded.append(Level1ID)

                    Name = stringutil.cleanName(
                                                        items[2],
                                                        False,
                                                        False,
                                                        'nochange',
                                                        True,
                                                        False,
                                                        False) \
                            + ' (L1)'
                    Documentation = ''

                    level.append(1) 
                    name.append(Level1ID) 
                    parent.append('VIP')
                    size.append(1)
                    textinfo.append(Name)


                
                #Level2 ###############################################################
                if Level2ID not in l_alreadyAdded:
                    l_alreadyAdded.append(Level2ID)
                    Name = stringutil.cleanName(
                                                        items[3],
                                                        False,
                                                        False,
                                                        'nochange',
                                                        True,
                                                        False,
                                                        False) \
                            + ' (L2)'
                    Documentation = ''

                    level.append(2) 
                    name.append(Level2ID) 
                    parent.append(Level1ID)
                    size.append(1)
                    textinfo.append(Name)


                #Level 3 ##############################################################
                if Level3ID not in l_alreadyAdded:
                    l_alreadyAdded.append(Level3ID)
                    Name = stringutil.cleanName(
                                                        items[4],
                                                        False,
                                                        False,
                                                        'nochange',
                                                        True,
                                                        False,
                                                        False) \
                            + ' (L3)'
                    Doc1 = stringutil.cleanName(
                                                        items[5],
                                                        False,
                                                        False,
                                                        'nochange',
                                                        True,
                                                        False,
                                                        False)
                    Doc2 = stringutil.cleanName(
                                                        items[6],
                                                        False,
                                                        False,
                                                        'nochange',
                                                        True,
                                                        False,
                                                        False)
                
                    level.append(3) 
                    name.append(Level3ID) 
                    parent.append(Level2ID)
                    size.append(1)
                    textinfo.append(Name)

    level.append(0) 
    name.append('VIP') 
    parent.append("")
    size.append(len(level))
    textinfo.append('VIP')

    return parent, name, size, level, textinfo