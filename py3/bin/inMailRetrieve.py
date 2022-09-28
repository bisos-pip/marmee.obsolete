#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""\
* TODO *[Summary]* :: An =ICM=: Retrieve message with offlineimap from imap server
"""

####+BEGIN: bx:cs:python:top-of-file :partof "bystar" :copyleft "halaal+minimal"
"""
*  This file:/de/bx/nne/dev-py/pypi/pkgs/bisos.marmee/dev/bin/inMailRetrieve.py :: [[elisp:(org-cycle)][| ]]
 is part of The Libre-Halaal ByStar Digital Ecosystem. http://www.by-star.net
 *CopyLeft*  This Software is a Libre-Halaal Poly-Existential. See http://www.freeprotocols.org
 A Python Interactively Command Module (PyICM). Part Of ByStar.
 Best Developed With COMEEGA-Emacs And Best Used With Blee-ICM-Players.
 Warning: All edits wityhin Dynamic Blocks may be lost.
"""
####+END:

"""
*  [[elisp:(org-cycle)][| *ICM-INFO:* |]] :: Author, Copyleft and Version Information
"""
####+BEGIN: bx:cs:python:name :style "fileName"
__icmName__ = "inMailRetrieve"
####+END:

####+BEGIN: bx:global:timestamp:version-py :style "date"
__version__ = "201712253259"
####+END:

####+BEGIN: bx:global:icm:status-py :status "Production"
__status__ = "Production"
####+END:

__credits__ = [""]

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/libre/ByStar/InitialTemplates/update/sw/icm/py/csInfo-mbNedaGpl.py"
csInfo = {
    'authors':         ["[[http://mohsen.1.banan.byname.net][Mohsen Banan]]"],
    'copyright':       "Copyright 2017, [[http://www.neda.com][Neda Communications, Inc.]]",
    'licenses':        ["[[https://www.gnu.org/licenses/agpl-3.0.en.html][Affero GPL]]", "Libre-Halaal Services License", "Neda Commercial License"],
    'maintainers':     ["[[http://mohsen.1.banan.byname.net][Mohsen Banan]]",],
    'contacts':        ["[[http://mohsen.1.banan.byname.net/contact]]",],
    'partOf':          ["[[http://www.by-star.net][Libre-Halaal ByStar Digital Ecosystem]]",]
}
####+END:

####+BEGIN: bx:cs:python:topControls :partof "bystar" :copyleft "halaal+minimal"
"""
*  [[elisp:(org-cycle)][|/Controls/| ]] :: [[elisp:(org-show-subtree)][|=]] [[elisp:(show-all)][Show-All]]  [[elisp:(org-shifttab)][Overview]]  [[elisp:(progn (org-shifttab) (org-content))][Content]] | [[file:Panel.org][Panel]] | [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] | [[elisp:(bx:org:run-me)][Run]] | [[elisp:(bx:org:run-me-eml)][RunEml]] | [[elisp:(delete-other-windows)][(1)]] | [[elisp:(progn (save-buffer) (kill-buffer))][S&Q]]  [[elisp:(save-buffer)][Save]]  [[elisp:(kill-buffer)][Quit]] [[elisp:(org-cycle)][| ]]
** /Version Control/ ::  [[elisp:(call-interactively (quote cvs-update))][cvs-update]]  [[elisp:(vc-update)][vc-update]] | [[elisp:(bx:org:agenda:this-file-otherWin)][Agenda-List]]  [[elisp:(bx:org:todo:this-file-otherWin)][ToDo-List]]
"""
####+END:

####+BEGIN: bx:cs:python:section :title "ContentsList"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *ContentsList*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:cs:python:icmItem :itemType "=Imports=" :itemTitle "*IMPORTS*"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || =Imports=      :: *IMPORTS*  [[elisp:(org-cycle)][| ]]
"""
####+END:

import sys
import os

import shutil


import collections

from unisos import ucf
from unisos import icm

from blee.icmPlayer import bleep

from bisos.marmee import marmeAcctsLib

g_importedCmnds = {        # Enumerate modules from which CMNDs become invokable
    'bleep': bleep.__file__,
    'marmeAcctsLib': marmeAcctsLib.__file__,    
}


####+BEGIN: bx:cs:python:section :title "= =Framework::= ICM  Description (Overview) ="
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *= =Framework::= ICM  Description (Overview) =*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: b:py3:cs:cmnd/classHead :modPrefix "new" :cmndName "icmOverview" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 3 :pyInv ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /icmOverview/ parsMand= parsOpt= argsMin=0 argsMax=3 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class icmOverview(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 3,}

    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        argsList=None,         # or Args-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs
        else:
            effectiveArgsList = argsList

        callParamsDict = {}
        if not cs.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
####+END:

        moduleDescription="""
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Description:* | ]]
**  [[elisp:(org-cycle)][| ]]  [Xref]          :: *[Related/Xrefs:]*  <<Xref-Here->>  -- External Documents  [[elisp:(org-cycle)][| ]]

**  [[elisp:(org-cycle)][| ]]   Model and Terminology                                      :Overview:
*** See BISOS Documentation for ICM's model and terminology
**      [End-Of-Description]
"""
        
        moduleUsage="""
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Usage:* | ]]

**      How-Tos:
*** TODO Edit csInfo to identify author, etc
*** TODO Select ICM type in g_icmChars
*** TODO Enhance g_argsExtraSpecify for your parameters
*** TODO Add your Commands
*** TODO Enhance Examples Cmnd
**      [End-Of-Usage]
"""
        
        moduleStatus="""
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Status:* | ]]
**  [[elisp:(org-cycle)][| ]]  [Info]          :: *[Current-Info:]* Status/Maintenance -- General TODO List [[elisp:(org-cycle)][| ]]
** TODO [[elisp:(org-cycle)][| ]]  Current         :: Just getting started [[elisp:(org-cycle)][| ]]
**      [End-Of-Status]
"""

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/libre/ByStar/InitialTemplates/update/sw/icm/py/moduleOverview.py"
        cmndArgsSpec = {"0&-1": ['moduleDescription', 'moduleUsage', 'moduleStatus']}
        cmndArgsValid = cmndArgsSpec["0&-1"]
        icm.unusedSuppressForEval(moduleDescription, moduleUsage, moduleStatus)
        for each in effectiveArgsList:
            if each in cmndArgsValid:
                if interactive:
                    exec("""print({})""".format(each))
                
        return(format(str(__doc__)+moduleDescription))
####+END:

    

####+BEGIN: bx:cs:python:section :title "= =Framework::= ICM Hooks ="
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *= =Framework::= ICM Hooks =*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:cs:python:func :funcName "g_icmChars" :comment "ICM Characteristics Spec" :funcType "FrameWrk" :retType "Void" :deco "" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-FrameWrk  :: /g_icmChars/ =ICM Characteristics Spec= retType=Void argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def g_icmChars(
):
####+END:
    csInfo['panel'] = "{}-Panel.org".format(__icmName__)
    csInfo['groupingType'] = "IcmGroupingType-pkged"
    csInfo['cmndParts'] = "IcmCmndParts[common] IcmCmndParts[param]"
    
g_icmChars()


####+BEGIN: bx:cs:python:func :funcName "g_icmPreCmnds" :funcType "FrameWrk" :retType "Void" :deco "default" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-FrameWrk  :: /g_icmPreCmnds/ retType=Void argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def g_icmPreCmnds(
):
####+END:
    """ PreHook """
    pass


####+BEGIN: bx:cs:python:func :funcName "g_icmPostCmnds" :funcType "FrameWrk" :retType "Void" :deco "default" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-FrameWrk  :: /g_icmPostCmnds/ retType=Void argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def g_icmPostCmnds(
):
####+END:
    """ PostHook """
    pass


####+BEGIN: bx:cs:python:section :title "= =Framework::= Options, Arguments and Examples Specifications ="
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *= =Framework::= Options, Arguments and Examples Specifications =*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:cs:python:func :funcName "g_argsExtraSpecify" :comment "FrameWrk: ArgsSpec" :funcType "FrameWrk" :retType "Void" :deco "" :argsList "parser"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-FrameWrk  :: /g_argsExtraSpecify/ =FrameWrk: ArgsSpec= retType=Void argsList=(parser)  [[elisp:(org-cycle)][| ]]
"""
def g_argsExtraSpecify(
    parser,
):
####+END:
    """Module Specific Command Line Parameters.
    g_argsExtraSpecify is passed to G_main and is executed before argsSetup (can not be decorated)
    """
    G = cs.globalContext.get()
    csParams = cs.CmndParamDict()

    csParams.parDictAdd(
        parName='moduleVersion',
        parDescription="Module Version",
        parDataType=None,
        parDefault=None,
        parChoices=list(),
        parScope=icm.CmndParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--version',
    )
    
    bleep.commonParamsSpecify(csParams)    
    
    marmeAcctsLib.commonParamsSpecify(csParams)
       
    cs.argsparseBasedOnCsParams(parser, csParams)

    # So that it can be processed later as well.
    G.icmParamDictSet(csParams)
    
    return


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "examples" :cmndType "ICM-Cmnd-FWrk"  :comment "FrameWrk: ICM Examples" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd-FWrk  :: /examples/ =FrameWrk: ICM Examples= parsMand= parsOpt= argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class examples(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {}
        if not cs.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
####+END:
        def cpsInit(): return collections.OrderedDict()
        def menuItem(verbosity): cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity=verbosity) # 'little' or 'none'
        def execLineEx(cmndStr): cs.examples.execInsert(execLine=cmndStr)

        logControler = b_io.log.Control()
        logControler.loggerSetLevel(20)

        cs.examples.myName(G.icmMyName(), G.icmMyFullName())
        
        cs.examples.commonBrief()    

        bleep.examples_icmBasic()

        controlProfile = marmeAcctsLib.enabledControlProfileObtain(curGet_bxoId(), curGet_sr())
        defaultMailDom = marmeAcctsLib.enabledInMailAcctObtain(curGet_bxoId(), curGet_sr())
        
####+BEGIN: bx:cs:python:cmnd:subSection :title "Dev And Testing"
        """
**  [[elisp:(beginning-of-buffer)][Top]] ================ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]          *Dev And Testing*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:
        #cs.examples.menuChapter('*General Dev and Testing IIFs*')

        cs.examples.menuChapter('*Config File Creation Facility IIFs*')

        cmndName = "offlineimaprcUpdate" ;  cmndArgs = ""
        cps=cpsInit(); cmndParsCurBxoSr(cps); 
        menuItem(verbosity='none') ; menuItem(verbosity='full')

        cmndName = "offlineimaprcStdout" ;  cmndArgs = ""
        cps=cpsInit(); cmndParsCurBxoSr(cps); 
        menuItem(verbosity='none') ; menuItem(verbosity='full')

        configFile = withInMailDomGetOfflineimaprcPath(
            controlProfile,
            defaultMailDom,
            curGet_bxoId(),
            curGet_sr(),
        )

        b_io.ann.write(
            """ls -l {}""".format(configFile)
        )
        b_io.ann.write(
            """cat  {} """.format(configFile)
        )
        
        cs.examples.menuChapter('*Operation Facility IIFs -- (offlineimapRun)*')

        cmndName = "offlineimapRun" ;  cmndArgs = ""
        cps=cpsInit(); cmndParsCurBxoSr(cps); 
        menuItem(verbosity='none') ; menuItem(verbosity='full')

        marmeAcctsLib.examples_controlProfileManage()

        #marmeAcctsLib.examples_marmeAcctsLibControls()
        marmeAcctsLib.examples_enabledInMailAcctConfig()

        marmeAcctsLib.examples_inMailAcctAccessPars()
        

####+BEGIN: bx:cs:python:section :title "ICM Commands"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *ICM Commands*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:cs:python:func :funcName "curGet_bxoId" :funcType "anyOrNone" :retType "bool" :deco "" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /curGet_bxoId/ retType=bool argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def curGet_bxoId():
####+END:
    return "mcm"


####+BEGIN: bx:cs:python:func :funcName "curGet_sr" :funcType "anyOrNone" :retType "bool" :deco "" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /curGet_sr/ retType=bool argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def curGet_sr():
####+END:
    return "marme/dsnProc"


####+BEGIN: bx:cs:python:func :funcName "cmndParsCurBxoSr" :funcType "void" :retType "bool" :deco "" :argsList "cps"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-void      :: /cmndParsCurBxoSr/ retType=bool argsList=(cps)  [[elisp:(org-cycle)][| ]]
"""
def cmndParsCurBxoSr(
    cps,
):
####+END:
    cps['bxoId'] = curGet_bxoId()
    cps['sr'] = curGet_sr()


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "offlineimapRun" :comment "" :parsMand "" :parsOpt "bxoId sr controlProfile inMailAcct" :argsMin 0 :argsMax 0 :pyInv ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /offlineimapRun/ parsMand= parsOpt=bxoId sr controlProfile inMailAcct argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class offlineimapRun(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'bxoId', 'sr', 'controlProfile', 'inMailAcct', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        bxoId=None,         # or Cmnd-Input
        sr=None,         # or Cmnd-Input
        controlProfile=None,         # or Cmnd-Input
        inMailAcct=None,         # or Cmnd-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {'bxoId': bxoId, 'sr': sr, 'controlProfile': controlProfile, 'inMailAcct': inMailAcct, }
        if not cs.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        bxoId = callParamsDict['bxoId']
        sr = callParamsDict['sr']
        controlProfile = callParamsDict['controlProfile']
        inMailAcct = callParamsDict['inMailAcct']

####+END:
        """
** TODO Make inMailAcct come from args not params
        """
        offlineimaprcPath = withInMailDomGetOfflineimaprcPath(
            controlProfile,
            inMailAcct,
            bxoId,
            sr,
        )            

        outcome = icm.subProc_bash("""offlineimap -c {offlineimaprcPath}"""
                                    .format(offlineimaprcPath=offlineimaprcPath)
        ).log()
        if outcome.isProblematic(): return(io.eh.badOutcome(outcome))
        
        return cmndOutcome.set(
            opError=cs.OpError.Success,
            opResults=None,
        )


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "offlineimaprcUpdate" :comment "" :parsMand "" :parsOpt "bxoId sr controlProfile inMailAcct" :argsMin 0 :argsMax 0 :pyInv ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /offlineimaprcUpdate/ parsMand= parsOpt=bxoId sr controlProfile inMailAcct argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class offlineimaprcUpdate(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'bxoId', 'sr', 'controlProfile', 'inMailAcct', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        bxoId=None,         # or Cmnd-Input
        sr=None,         # or Cmnd-Input
        controlProfile=None,         # or Cmnd-Input
        inMailAcct=None,         # or Cmnd-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {'bxoId': bxoId, 'sr': sr, 'controlProfile': controlProfile, 'inMailAcct': inMailAcct, }
        if not cs.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        bxoId = callParamsDict['bxoId']
        sr = callParamsDict['sr']
        controlProfile = callParamsDict['controlProfile']
        inMailAcct = callParamsDict['inMailAcct']

####+END:
        outcome = offlineimaprcStdout().cmnd(
            interactive=False,
            inMailAcct=inMailAcct,
            bxoId=bxoId,
            sr=sr,
        )
        if outcome.isProblematic(): return(io.eh.badOutcome(outcome))

        offlineimaprcStr = outcome.results

        offlineimaprcPath = withInMailDomGetOfflineimaprcPath(
            controlProfile,
            inMailAcct,
            bxoId,
            sr,
        )

        rcFileFromControl = "{controlProfileBaseDir}/inMail/{inMailAcct}/conf/_offlineimaprc".format(
            # ../control/inMail/example.com/conf/_offlineimaprc
            controlProfileBaseDir=marmeAcctsLib.controlProfileBaseDirGet(
                controlProfile,
                bxoId=bxoId,
                sr=sr,
            ),
            inMailAcct=inMailAcct,
        )
        
        if os.path.isfile(rcFileFromControl):
            shutil.copyfile(rcFileFromControl, offlineimaprcPath)
        else:
            with open(offlineimaprcPath, "w") as thisFile:
                thisFile.write(offlineimaprcStr + '\n')

        thisPath = marmeAcctsLib.getPathForAcctMaildir(
            controlProfile,
            inMailAcct,
            bxoId=bxoId,
            sr=sr,
        )

        try:
            os.makedirs(thisPath)
        except OSError:
            if not os.path.isdir(thisPath):
                raise

        if interactive:
            icm.ANN_here("offlineimaprcPath={val}".format(val=offlineimaprcPath))
        
        return cmndOutcome.set(
            opError=cs.OpError.Success,
            opResults=offlineimaprcStr,
        )

####+BEGIN: bx:cs:python:func :funcName "withInMailDomGetOfflineimaprcPath" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "controlProfile inMailAcct bxoId sr"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /withInMailDomGetOfflineimaprcPath/ retType=bool argsList=(controlProfile inMailAcct bxoId sr)  [[elisp:(org-cycle)][| ]]
"""
def withInMailDomGetOfflineimaprcPath(
    controlProfile,
    inMailAcct,
    bxoId,
    sr,
):
####+END:
    inMailAcctConfBase = os.path.abspath(
        "{configBaseDir}"
        .format(configBaseDir=marmeAcctsLib.getPathForInMailConfig(
            controlProfile,
            inMailAcct,
            bxoId=bxoId,
            sr=sr,
        ))
    )

    try: 
        os.makedirs(inMailAcctConfBase)
    except OSError:
        if not os.path.isdir(inMailAcctConfBase):
            raise

    offlineimaprcFile = os.path.join(
        inMailAcctConfBase,
        "_offlineimaprc"
    )
    return offlineimaprcFile


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "offlineimaprcStdout" :comment "" :parsMand "" :parsOpt "bxoId sr inMailAcct mboxesList ssl" :argsMin 0 :argsMax 0 :pyInv ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /offlineimaprcStdout/ parsMand= parsOpt=bxoId sr inMailAcct mboxesList ssl argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class offlineimaprcStdout(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'bxoId', 'sr', 'inMailAcct', 'mboxesList', 'ssl', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        bxoId=None,         # or Cmnd-Input
        sr=None,         # or Cmnd-Input
        inMailAcct=None,         # or Cmnd-Input
        mboxesList=None,         # or Cmnd-Input
        ssl=None,         # or Cmnd-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {'bxoId': bxoId, 'sr': sr, 'inMailAcct': inMailAcct, 'mboxesList': mboxesList, 'ssl': ssl, }
        if not cs.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        bxoId = callParamsDict['bxoId']
        sr = callParamsDict['sr']
        inMailAcct = callParamsDict['inMailAcct']
        mboxesList = callParamsDict['mboxesList']
        ssl = callParamsDict['ssl']

####+END:

        outcome = marmeAcctsLib.inMailAcctParsGet().cmnd(
            interactive=False,
            bxoId=bxoId,
            sr=sr,
            inMailAcct=inMailAcct,
            argsList=['access'],
        )
        if outcome.isProblematic(): return(io.eh.badOutcome(outcome))

        fileParamDict = outcome.results

        outcome = marmeAcctsLib.inMailAcctParsGet().cmnd(
            interactive=False,
            bxoId=bxoId,
            sr=sr,
            inMailAcct=inMailAcct,
            argsList=['retrieval']
        )
        if outcome.isProblematic(): return(io.eh.badOutcome(outcome))
        fileParamRetrievalDict = outcome.results

        mailDirFullPath = fileParamRetrievalDict['inMailAcctMboxesPath'].parValueGet()
        if not mailDirFullPath: return b_io.eh.badOutcome(outcome)

        try: 
            os.makedirs(mailDirFullPath)
        except OSError:
            if not os.path.isdir(mailDirFullPath):
                raise

        mboxesList = fileParamRetrievalDict['mboxesList'].parValueGet()

        foldersListStr = ""
        if mboxesList == "all":
            folderFilterLineStr = "#"
        else:
            for each in mboxesList.split():
                foldersListStr += "'INBOX.{}',".format(each)
                
            folderFilterLineStr = """folderfilter = lambda name: name in [ {foldersListStr} ]""".format(
                foldersListStr=foldersListStr)

        resStr = offlineimaprcTemplate().format(
            inMailAcctMboxesPath=mailDirFullPath,
            imapServer=fileParamDict['imapServer'].parValueGet(),
            userName=fileParamDict['userName'].parValueGet(),
            userPasswd=fileParamDict['userPasswd'].parValueGet(),
            ssl=fileParamRetrievalDict['ssl'].parValueGet(),            
            foldersListStr=foldersListStr,
            folderFilterLine=folderFilterLineStr,
        )

        if interactive:
            print(resStr)
        
        return cmndOutcome.set(
            opError=cs.OpError.Success,
            opResults=resStr
        )

####+BEGIN: bx:cs:python:func :funcName "offlineimaprcTemplate" :funcType "anyOrNone" :retType "bool" :deco "" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /offlineimaprcTemplate/ retType=bool argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def offlineimaprcTemplate():
####+END:
    templateStr = """ 
[general]
accounts = MyAccount
#pythonfile = .offlineimap.py

[Account MyAccount]
localrepository = LocalIMAP
remoterepository = RemoteIMAP
# autorefresh = 5
# postsynchook = notmuch new

[Repository LocalIMAP]
type = Maildir
localfolders = {inMailAcctMboxesPath}

[Repository RemoteIMAP]
type = IMAP
sslcacertfile = /etc/ssl/certs/ca-certificates.crt
remotehost = {imapServer}
remoteuser = {userName}
remotepass = {userPasswd}
ssl = {ssl}
nametrans = lambda name: re.sub('^INBOX.', '', name)
{folderFilterLine}
# folderfilter = lambda name: name in [ {foldersListStr} ]
# folderfilter = lambda name: not (name in [ 'INBOX.spam', 'INBOX.commits' ])
# holdconnectionopen = yes
# maxconnections = 3
# foldersort = lld_cmp

"""
    return templateStr


    

####+BEGIN: bx:cs:python:section :title "Supporting Classes And Functions"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Supporting Classes And Functions*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:
"""
*       /Empty/  [[elisp:(org-cycle)][| ]]
"""
    
####+BEGIN: bx:cs:python:section :title "Common/Generic Facilities -- Library Candidates"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Common/Generic Facilities -- Library Candidates*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:
"""
*       /Empty/  [[elisp:(org-cycle)][| ]]
"""

    
####+BEGIN: bx:cs:python:section :title "= =Framework::=   G_main -- Instead Of ICM Dispatcher ="
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *= =Framework::=   G_main -- Instead Of ICM Dispatcher =*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:cs:python:func :funcName "G_main" :funcType "FrameWrk" :retType "Void" :deco "" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-FrameWrk  :: /G_main/ retType=Void argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def G_main():
####+END:
    """ 
** Replaces ICM dispatcher for other command line args parsings.
"""
    pass


####+BEGIN: bx:cs:python:icmItem :itemType "Configuration" :itemTitle "= =Framework::= g_ Settings -- ICMs Imports ="
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Configuration  :: = =Framework::= g_ Settings -- ICMs Imports =  [[elisp:(org-cycle)][| ]]
"""
####+END:

g_examples = examples  # or None 
g_mainEntry = None  # or G_main

####+BEGIN: bx:dblock:global:file-insert :file "/libre/ByStar/InitialTemplates/update/sw/icm/py/icm2.G_main.py"
"""
*  [[elisp:(beginning-of-buffer)][Top]] # /Dblk-Begin/ # [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *= =Framework::= ICM main() =*
"""

def classedCmndsDict():
    """
** Should be done here, can not be done in icm library because of the evals.
"""
    callDict = dict()
    for eachCmnd in icm.cmndList_mainsMethods().cmnd(
            interactive=False,
            importedCmnds=g_importedCmnds,
            mainFileName=__file__,
    ):
        try:
            callDict[eachCmnd] = eval("{}".format(eachCmnd))
            continue
        except NameError:
            pass

        for mod in g_importedCmnds:
            try:
                eval("{mod}.{cmnd}".format(mod=mod, cmnd=eachCmnd))
            except AttributeError:
                continue
            try:                
                callDict[eachCmnd] = eval("{mod}.{cmnd}".format(mod=mod, cmnd=eachCmnd))
                break
            except NameError:
                pass
    return callDict

csInfo['icmName'] = __icmName__
csInfo['version'] = __version__
csInfo['status'] = __status__
csInfo['credits'] = __credits__

G = cs.globalContext.get()
G.csInfo = csInfo

def g_icmMain():
    """This ICM's specific information is passed to G_mainWithClass"""
    sys.exit(
        icm.G_mainWithClass(
            inArgv=sys.argv[1:],                 # Mandatory
            extraArgs=g_argsExtraSpecify,        # Mandatory
            G_examples=g_examples,               # Mandatory            
            classedCmndsDict=classedCmndsDict(),   # Mandatory
            mainEntry=g_mainEntry,
            g_icmPreCmnds=g_icmPreCmnds,
            g_icmPostCmnds=g_icmPostCmnds,
        )
    )

g_icmMain()

"""
*  [[elisp:(beginning-of-buffer)][Top]] ## /Dblk-End/ ## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *= =Framework::= ICM main() =*
"""

####+END:

####+BEGIN: bx:cs:python:section :title "Unused Facilities -- Temporary Junk Yard"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Unused Facilities -- Temporary Junk Yard*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:
"""
*       /Empty/  [[elisp:(org-cycle)][| ]]
"""

####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :title " ~End Of Editable Text~ "
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *End Of Editable Text*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/libre/ByStar/InitialTemplates/software/plusOrg/dblock/inserts/endOfFileControls.org"
#+STARTUP: showall
####+END:
