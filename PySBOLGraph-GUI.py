from pysbolgraph.SBOL2Graph import SBOL2Graph as s2g
from pysbolgraph.terms import Biopax, SBOL2
import tkinter as tk



def loadSBOL(doc_name):
    doc_obj = s2g()
    s2g.load(doc_obj,doc_name)
    return(doc_obj)

def getAllCompDefObjs(doc_obj):
    return(doc_obj.component_definitions)

def getCompDefsDisplayId(cd_obj):
    cdDisps = []
    for i in cd_obj:
        cdDisps.append(i.display_id)
    return(cdDisps)

def getCompDefsName(cd_obj):
    cdNames = []
    for i in cd_obj:
        cdNames.append(i.name)
    return(cdNames)

def getCompDefsPersisentIdentities(cd_obj):
    cdPersistId = []
    for i in cd_obj:
        cdPersistId.append(i.persistent_identity)
    return(cdPersistId)

def getCompDefsRoles(cd_obj):
    cdRoles = []
    for i in cd_obj:
        cdRoles.append(i.roles)
    return(cdRoles)

def getCompDefsTypes(cd_obj):
    cdTypes = []
    for i in cd_obj:
        cdTypes.append(i.types)
    return(cdTypes)

def getCompDefsSequences(cd_obj):
    cdSeq = []
    cdSeqObjs = []
    for i in cd_obj:
        cdSeqObjs.append(i.sequences)
    n = 0
    for j in cdSeqObjs:
        if len(j) > 0:
            cdSeq.append([])
            for k in j:
                cdSeq[n].append(k.elements)
        else:
            cdSeq.append("No Sequence")
        n += 1
    return(cdSeq)

def getAllCompDefProperties(cd_obj):
    compDefProps = []
    for i in cd_obj:
        compDefProps.append([
        getCompDefsName([i]),
        getCompDefsDisplayId([i]),
        getCompDefsPersisentIdentities([i]),
        getCompDefsTypes([i]),
        getCompDefsRoles([i]),
        getCompDefsSequences([i])
        ])
    return(compDefProps)
