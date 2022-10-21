#!/bin/env python
# -*- coding: utf-8 -*-

""" #+begin_org
* ~[Summary]~ :: A =CmndSvc= for Notmuch based user agent
#+end_org """

####+BEGIN: b:py3:cs:file/dblockControls :classification "cs-mu"
""" #+begin_org
* [[elisp:(org-cycle)][| /Control Parameters Of This File/ |]] :: dblk ctrls classifications=cs-mu
#+BEGIN_SRC emacs-lisp
(setq-local b:dblockControls t) ; (setq-local b:dblockControls nil)
(put 'b:dblockControls 'py3:cs:Classification "cs-mu") ; one of cs-mu, cs-u, cs-lib, bpf-lib, pyLibPure
#+END_SRC
#+RESULTS:
: cs-mu
#+end_org """
####+END:

####+BEGIN: b:prog:file/proclamations :outLevel 1
""" #+begin_org
* *[[elisp:(org-cycle)][| Proclamations |]]* :: Libre-Halaal Software --- Part Of BISOS ---  Poly-COMEEGA Format.
** This is Libre-Halaal Software. © Neda Communications, Inc. Subject to AGPL.
** It is part of BISOS (ByStar Internet Services OS)
** Best read and edited  with Blee in Poly-COMEEGA (Polymode Colaborative Org-Mode Enhance Emacs Generalized Authorship)
#+end_org """
####+END:

####+BEGIN: b:prog:file/particulars :authors ("./inserts/authors-mb.org")
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars |]]* :: Authors, version
** This File: /bisos/git/auth/bxRepos/bisos-pip/marmee/py3/bin/marmeeNotmuch.cs
** Authors: Mohsen BANAN, http://mohsen.banan.1.byname.net/contact
#+end_org """
####+END:

####+BEGIN: b:py3:file/particulars-csInfo :status "inUse"
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars-csInfo |]]*
#+end_org """
import typing
csInfo: typing.Dict[str, typing.Any] = { 'moduleName': ['marmeeNotmuch'], }
csInfo['version'] = '202210215146'
csInfo['status']  = 'inUse'
csInfo['panel'] = 'marmeeNotmuch-Panel.org'
csInfo['groupingType'] = 'IcmGroupingType-pkged'
csInfo['cmndParts'] = 'IcmCmndParts[common] IcmCmndParts[param]'
####+END:

""" #+begin_org
* [[elisp:(org-cycle)][| ~Description~ |]] :: [[file:/bisos/git/auth/bxRepos/blee-binders/bisos-core/COMEEGA/_nodeBase_/fullUsagePanel-en.org][BISOS COMEEGA Panel]]
Module description comes here.
** Relevant Panels:
** Status: In use with BISOS
** /[[elisp:(org-cycle)][| Planned Improvements |]]/ :
*** TODO complete fileName in particulars.
#+end_org """

####+BEGIN: b:prog:file/orgTopControls :outLevel 1
""" #+begin_org
* [[elisp:(org-cycle)][| Controls |]] :: [[elisp:(delete-other-windows)][(1)]] | [[elisp:(show-all)][Show-All]]  [[elisp:(org-shifttab)][Overview]]  [[elisp:(progn (org-shifttab) (org-content))][Content]] | [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] | [[elisp:(bx:org:run-me)][Run]] | [[elisp:(bx:org:run-me-eml)][RunEml]] | [[elisp:(progn (save-buffer) (kill-buffer))][S&Q]]  [[elisp:(save-buffer)][Save]]  [[elisp:(kill-buffer)][Quit]] [[elisp:(org-cycle)][| ]]
** /Version Control/ ::  [[elisp:(call-interactively (quote cvs-update))][cvs-update]]  [[elisp:(vc-update)][vc-update]] | [[elisp:(bx:org:agenda:this-file-otherWin)][Agenda-List]]  [[elisp:(bx:org:todo:this-file-otherWin)][ToDo-List]]
#+end_org """
####+END:

####+BEGIN: b:py3:file/workbench :outLevel 1
""" #+begin_org
* [[elisp:(org-cycle)][| Workbench |]] :: [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pyclbr %s" (bx:buf-fname))))][pyclbr]] || [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pydoc ./%s" (bx:buf-fname))))][pydoc]] || [[elisp:(python-check (format "/bisos/pipx/bin/pyflakes %s" (bx:buf-fname)))][pyflakes]] | [[elisp:(python-check (format "/bisos/pipx/bin/pychecker %s" (bx:buf-fname))))][pychecker (executes)]] | [[elisp:(python-check (format "/bisos/pipx/bin/pycodestyle %s" (bx:buf-fname))))][pycodestyle]] | [[elisp:(python-check (format "/bisos/pipx/bin/flake8 %s" (bx:buf-fname))))][flake8]] | [[elisp:(python-check (format "/bisos/pipx/bin/pylint %s" (bx:buf-fname))))][pylint]]  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: b:py3:cs:framework/imports :basedOn "classification"
""" #+begin_org
** Imports Based On Classification=cs-mu
#+end_org """
from bisos import b
from bisos.b import cs
from bisos.b import b_io

import collections
####+END:

import sys
import os
import shutil

#from bisos.currents import bxCurrentsConfig

#from unisos.common import icmsPkgLib
#from bisos.marmee import marmeAcctsLib



""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CsFrmWrk   [[elisp:(outline-show-subtree+toggle)][||]] ~csuList emacs-list Specifications~  [[elisp:(blee:org:code-block/above-run)][ /Eval Below/ ]] [[elisp:(org-cycle)][| ]]
#+BEGIN_SRC emacs-lisp
(setq  b:py:cs:csuList
  (list
   "bisos.b.cs.ro"
   "blee.icmPlayer.bleep"
   "bisos.marmee.marmeeTrackingLib"
 ))
#+END_SRC
#+RESULTS:
| bisos.b.cs.ro | blee.icmPlayer.bleep | bisos.marmee.marmeeTrackingLib |
#+end_org """

####+BEGIN: b:py3:cs:framework/csuListProc :pyImports t :csuImports t :csuParams t
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CsFrmWrk   [[elisp:(outline-show-subtree+toggle)][||]] =Process CSU List= with /3/ in csuList pyImports=t csuImports=t csuParams=t
#+end_org """

from bisos.b.cs import ro
from blee.icmPlayer import bleep
from bisos.marmee import marmeeTrackingLib


csuList = [ 'bisos.b.cs.ro', 'blee.icmPlayer.bleep', 'bisos.marmee.marmeeTrackingLib', ]

g_importedCmndsModules = cs.csuList_importedModules(csuList)

def g_extraParams():
    csParams = cs.param.CmndParamDict()
    cs.csuList_commonParamsSpecify(csuList, csParams)
    cs.argsparseBasedOnCsParams(csParams)

####+END:

####+BEGIN: b:py3:cs:main/exposedSymbols :classes ()
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CsFrmWrk   [[elisp:(outline-show-subtree+toggle)][||]] ~Exposed Symbols List Specification~ with /0/ in Classes List
#+end_org """
####+END:

####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :sep nil :title "CmndSvcs" :anchor ""  :extraInfo "Command Services Section"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _CmndSvcs_: |]]  Command Services Section  [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "examples" :extent "verify" :ro "noCli" :comment "FrameWrk: CS-Main-Examples" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<examples>>  *FrameWrk: CS-Main-Examples*  =verify= argsMin=0 argsMax=0 ro=noCli   [[elisp:(org-cycle)][| ]]
#+end_org """
class examples(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}
    rtInvConstraints = cs.rtInvoker.RtInvoker.new_noRo() # NO RO From CLI

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:
        """FrameWrk: CS-Main-Examples"""
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
####+END:
        self.cmndDocStr(f""" #+begin_org ***** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Conventional top level example.
        #+end_org """)

        def cpsInit(): return collections.OrderedDict()
        def menuItem(verbosity): cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity=verbosity) # 'little' or 'none'
        def execLineEx(cmndStr): cs.examples.execInsert(execLine=cmndStr)

        #logControler = b_io.log.Control()
        #logControler.loggerSetLevel(20)

        cs.examples.myName(cs.G.icmMyName(), cs.G.icmMyFullName())

        cs.examples.commonBrief()

        bleep.examples_icmBasic()

        defaultMailDom = marmeAcctsLib.enabledInMailAcctObtain(
            bxoId=curGet_bxoId(),
            sr=curGet_sr(),
        )

####+BEGIN: bx:cs:python:cmnd:subSection :title "Dev And Testing"

####+END:
        #cs.examples.menuChapter('*General Dev and Testing IIFs*')

        cs.examples.menuChapter('*Config File Creation Facilities*')

        cs.examples.menuSection('*Automated Config File Creation Facilities*')

        cmndName = "notmuchConfigUpdate" ; cmndArgs = ""
        cps=cpsInit(); cmndParsCurBxoSr(cps);
        menuItem(verbosity='none'); menuItem(verbosity='full')

        cmndName = "notmuchConfigStdout" ; cmndArgs = ""
        cps=cpsInit(); cmndParsCurBxoSr(cps);
        menuItem(verbosity='none'); menuItem(verbosity='full')

        configFile = withInMailDomGetNotmuchConfigPath(
            defaultMailDom,
            bxoId=curGet_bxoId(),
            sr=curGet_sr(),
        )

        b_io.ann.write(
            """ls -l {}""".format(configFile)
        )
        b_io.ann.write(
            """cat  {} """.format(configFile)
        )

        cs.examples.menuSection('*Interactive Config File Creation Facilities*')

        cmndName = "runNotmuch" ; cmndArgs = "setup" ;
        cps=cpsInit() ;  cmndParsCurBxoSr(cps);
        cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='basic',
                             comment='# Creates/Edits notmuch-config', icmWrapper=None, icmName=None)

        cs.examples.menuSection('*Show/List Config Parameter Settings*')

        cmndName = "runNotmuch" ; cmndArgs = "config list" ;
        cps=cpsInit() ;  cmndParsCurBxoSr(cps);
        cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='basic',
                             comment='# Shows Key aspects of notmuch-config', icmWrapper=None, icmName=None)


        cs.examples.menuChapter('*Run notmuch -- new, Search*')

        cmndName = "runNotmuch" ; cmndArgs = "new" ;
        cps=cpsInit() ;  cmndParsCurBxoSr(cps);
        cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='basic',
                             comment='# Refresh the index', icmWrapper=None, icmName=None)


        cmndName = "runNotmuch" ; cmndArgs = '''-- search --format=text --output=files "from:"''' ;
        cps=cpsInit() ;  cmndParsCurBxoSr(cps);
        cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='basic',
                             comment='# Search Based on from', icmWrapper=None, icmName=None)

        cmndName = "runNotmuch" ; cmndArgs = '''-- search --format=text --output=files "from:"''' ;
        cps=cpsInit() ;  cmndParsCurBxoSr(cps);
        cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='none',
                             comment='# Search Based on from', icmWrapper='echo', icmName=None)

        cmndName = "runNotmuch" ; cmndArgs = '''-- search "from:"''' ;
        cps=cpsInit() ;  cmndParsCurBxoSr(cps);
        cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='basic',
                             comment='# Search Based on from', icmWrapper=None, icmName=None)

        cmndName = "runNotmuch" ; cmndArgs = '''-- search "from:"''' ;
        cps=cpsInit() ;  cmndParsCurBxoSr(cps);
        cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='none',
                             comment='# Search Based on from', icmWrapper='echo', icmName=None)

        cmndName = "runNotmuch" ; cmndArgs = '''-- search --format=text --output=files "from:" | grep Inbox | xargs egrep "^Subject:"''' ;
        cps=cpsInit() ;  cmndParsCurBxoSr(cps);
        cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='basic',
                             comment='# Search Based on from', icmWrapper=None, icmName=None)

        cmndName = "runNotmuch" ; cmndArgs = '''-- search --format=text --output=files "from:" | grep Inbox | xargs egrep "^Subject:"''' ;
        cps=cpsInit() ;  cmndParsCurBxoSr(cps);
        cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='none',
                             comment='# Search Based on from', icmWrapper="echo", icmName=None)

        cmndName = "runNotmuch" ; cmndArgs = '''-- search --output=files "to: example.com"''' ;
        cps=cpsInit() ;  cmndParsCurBxoSr(cps);
        cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='none',
                             comment='# Search Based on from', icmWrapper="echo", icmName=None)


        b.ignore(ro.__doc__,)  # We are not using these modules, but they are auto imported.

        return(cmndOutcome)

####+BEGIN: bx:icm:py3:section :title "CS-Commands"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    [[elisp:(outline-show-subtree+toggle)][||]] *CS-Commands*  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "someCmnd" :comment "" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<someCmnd>>  =verify= ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class someCmnd(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:

        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  A starting point command.
        #+end_org """)

        if b.subProc.WOpW(invedBy=self, log=1).bash(
                f"""echo hello World""",
        ).isProblematic():  return(b_io.eh.badOutcome(cmndOutcome))

        return(cmndOutcome)


####+BEGIN: b:py3:cs:cmnd/classHead :modPrefix "new" :cmndName "notmuchConfigUpdate" :comment "" :parsMand "" :parsOpt "bxoId sr controlProfile inMailAcct" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<notmuchConfigUpdate>>  =verify= parsOpt=bxoId sr controlProfile inMailAcct ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class notmuchConfigUpdate(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'bxoId', 'sr', 'controlProfile', 'inMailAcct', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             bxoId: typing.Optional[str]=None,  # Cs Optional Param
             sr: typing.Optional[str]=None,  # Cs Optional Param
             controlProfile: typing.Optional[str]=None,  # Cs Optional Param
             inMailAcct: typing.Optional[str]=None,  # Cs Optional Param
    ) -> b.op.Outcome:

        callParamsDict = {'bxoId': bxoId, 'sr': sr, 'controlProfile': controlProfile, 'inMailAcct': inMailAcct, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
####+END:
        outcome = notmuchConfigStdout().cmnd(
            interactive=False,
            controlProfile=controlProfile,
            inMailAcct=inMailAcct,
            bxoId=bxoId,
            sr=sr,
        )
        if outcome.isProblematic(): return(io.eh.badOutcome(outcome))

        configFileStr = outcome.stdout

        configFilePath = withInMailDomGetNotmuchConfigPath(
            inMailAcct,
            bxoId=bxoId,
            sr=sr,
        )

        rcFileFromControl = "{controlProfileBaseDir}/inMail/{inMailAcct}/conf/_notmuch-config".format(
            # ../control/inMail/example.com/conf/_notmuch-config
            controlProfileBaseDir=marmeAcctsLib.controlProfileBaseDirGet(
                controlProfile,
                bxoId=bxoId,
                sr=sr,
            ),
            inMailAcct=inMailAcct,
        )

        if os.path.isfile(rcFileFromControl):
            shutil.copyfile(rcFileFromControl, configFilePath)
        else:
            with open(configFilePath, "w") as thisFile:
                thisFile.write(configFileStr + '\n')

        if rtInv.outs:
            icm.ANN_here("configFilePath={val}".format(val=configFilePath))

        return cmndOutcome.set(
            opError=b.OpError.Success,
            opResults=None,
        )

####+BEGIN: b:py3:cs:func/args :funcName "withInMailDomGetNotmuchConfigPath" :funcType "anyOrNone" :retType "bool" :deco "default" :argsList "inMailAcct bxoId=None sr=None"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-A-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /withInMailDomGetNotmuchConfigPath/ deco=default  [[elisp:(org-cycle)][| ]] deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
@cs.track(fnLoc=True, fnEntry=True, fnExit=True)
def withInMailDomGetNotmuchConfigPath(
    inMailAcct,
    bxoId=None,
    sr=None,
):
####+END:
    inMailAcctConfBase = os.path.abspath(
        "{configBaseDir}/{inMailAcct}"
        .format(
            configBaseDir=marmeAcctsLib.configBaseDirGet(
                bxoId=bxoId,
                sr=sr,
            ),
            inMailAcct=inMailAcct,
        )
    )

    try:
        os.makedirs(inMailAcctConfBase)
    except OSError:
        if not os.path.isdir(inMailAcctConfBase):
            raise

    filePath = os.path.join(
        inMailAcctConfBase,
        "_notmuch-config"
    )
    return filePath


####+BEGIN: b:py3:cs:cmnd/classHead :modPrefix "new" :cmndName "notmuchConfigStdout" :comment "" :parsMand "" :parsOpt "bxoId sr controlProfile inMailAcct" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<notmuchConfigStdout>>  =verify= parsOpt=bxoId sr controlProfile inMailAcct ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class notmuchConfigStdout(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'bxoId', 'sr', 'controlProfile', 'inMailAcct', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             bxoId: typing.Optional[str]=None,  # Cs Optional Param
             sr: typing.Optional[str]=None,  # Cs Optional Param
             controlProfile: typing.Optional[str]=None,  # Cs Optional Param
             inMailAcct: typing.Optional[str]=None,  # Cs Optional Param
    ) -> b.op.Outcome:

        callParamsDict = {'bxoId': bxoId, 'sr': sr, 'controlProfile': controlProfile, 'inMailAcct': inMailAcct, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
####+END:

        templateFile = os.path.join(
            marmeAcctsLib.inputsBaseDirGet(),
            "inputs",
            "notmuch/_notmuch-config.template",
        )

        outcome = icm.subProc_bash(
            """\
cat {templateFile} | \
        sed \
            -e "s@%mailDirPath%@{mailDirPath}@g" \
            -e "s@%firstName%@{firstName}@g" \
            -e "s@%lastName%@{lastName}@g"
"""
            .format(
                templateFile=templateFile,
                # ../var/inMail/example/maildir/Inbox
                mailDirPath=marmeAcctsLib.getPathForAcctMaildir(
                   controlProfile,
                    inMailAcct,
                    bxoId=bxoId,
                    sr=sr,
                ),
                firstName="FirstName",
                lastName="LastName",
            )
        ).log()
        if outcome.isProblematic(): return(io.eh.badOutcome(outcome))

        if rtInv.outs:
            b_io.ann.write(outcome.stdout)

        return outcome.set(
            opError=b.OpError.Success,
            #opResults=outcome.stdout
        )

####+BEGIN: b:py3:cs:cmnd/classHead :modPrefix "new" :cmndName "runNotmuch" :comment "" :parsMand "" :parsOpt "bxoId sr inMailAcct" :argsMin 0 :argsMax 1000 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<runNotmuch>>  =verify= parsOpt=bxoId sr inMailAcct argsMax=1000 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class runNotmuch(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'bxoId', 'sr', 'inMailAcct', ]
    cmndArgsLen = {'Min': 0, 'Max': 1000,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             bxoId: typing.Optional[str]=None,  # Cs Optional Param
             sr: typing.Optional[str]=None,  # Cs Optional Param
             inMailAcct: typing.Optional[str]=None,  # Cs Optional Param
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

        callParamsDict = {'bxoId': bxoId, 'sr': sr, 'inMailAcct': inMailAcct, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
####+END:
        cmndArgs = self.cmndArgsGet("0&-1", cmndArgsSpecDict, argsList)
        joinedArgs = ucf.str_joinedArgs(cmndArgs)

        defaultMailDom = marmeAcctsLib.enabledInMailAcctObtain(
            bxoId=bxoId,
            sr=sr,
        )
        configFile = withInMailDomGetNotmuchConfigPath(
            defaultMailDom,
            bxoId=bxoId,
            sr=sr,
        )

        outcome = icm.subProc_bash(
            """notmuch --config={configFile} {joinedArgs}"""
            .format(
                configFile=configFile,
                joinedArgs=joinedArgs,
            )
        ).out()
        if outcome.isProblematic(): return(io.eh.badOutcome(outcome))

        if rtInv.outs:
            pass

        return outcome.set(
            opError=b.OpError.Success,
            #opResults=outcome.stdout
        )

####+BEGIN: b:py3:cs:method/args :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList "self"
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndArgsSpec/ deco=default  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self, ):
####+END:
        """
    ***** Cmnd Args Specification
"""
        cmndArgsSpecDict = cs.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&-1",
            argName="cmndArgs",
            argDefault=None,
            argChoices='any',
            argDescription="Rest of args for use by action"
        )

        return cmndArgsSpecDict




####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :sep nil :title "Main" :anchor ""  :extraInfo "Framework Dblock"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _Main_: |]]  Framework Dblock  [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:

####+BEGIN: b:py3:cs:framework/main :csInfo "csInfo" :noCmndEntry "examples" :extraParamsHook "g_extraParams" :importedCmndsModules "g_importedCmndsModules"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CsFrmWrk   [[elisp:(outline-show-subtree+toggle)][||]] =g_csMain= (csInfo, _examples_, g_extraParams, g_importedCmndsModules)
#+end_org """

if __name__ == '__main__':
    cs.main.g_csMain(
        csInfo=csInfo,
        noCmndEntry=examples,  # specify a Cmnd name
        extraParamsHook=g_extraParams,
        importedCmndsModules=g_importedCmndsModules,
    )

####+END:

####+BEGIN: b:py3:cs:framework/endOfFile :basedOn "classification"
""" #+begin_org
* [[elisp:(org-cycle)][| *End-Of-Editable-Text* |]] :: emacs and org variables and control parameters
#+end_org """

#+STARTUP: showall

### local variables:
### no-byte-compile: t
### end:
####+END:
