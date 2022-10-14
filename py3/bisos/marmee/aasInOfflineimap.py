# -*- coding: utf-8 -*-

""" #+begin_org
* ~[Summary]~ :: A =CS-Lib= for InMail Service Access Instance (sai) Offline Imap.
#+end_org """

####+BEGIN: b:py3:cs:file/dblockControls :classification "cs-u"
""" #+begin_org
* [[elisp:(org-cycle)][| /Control Parameters Of This File/ |]] :: dblk ctrls classifications=cs-u
#+BEGIN_SRC emacs-lisp
(setq-local b:dblockControls t) ; (setq-local b:dblockControls nil)
(put 'b:dblockControls 'py3:cs:Classification "cs-u") ; one of cs-mu, cs-u, cs-lib, b-lib, pyLibPure
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
** This File: /bisos/git/auth/bxRepos/bisos-pip/marmee/py3/bisos/marmee/saiInMailOfflineimap.py
** Authors: Mohsen BANAN, http://mohsen.banan.1.byname.net/contact
#+end_org """
####+END:

####+BEGIN: b:python:file/particulars-csInfo :status "inUse"
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars-csInfo |]]*
#+end_org """
import typing
csInfo: typing.Dict[str, typing.Any] = { 'moduleName': ['saiInMailOfflineimap'], }
csInfo['version'] = '202209281438'
csInfo['status']  = 'inUse'
csInfo['panel'] = 'saiInMailOfflineimap-Panel.org'
csInfo['groupingType'] = 'IcmGroupingType-pkged'
csInfo['cmndParts'] = 'IcmCmndParts[common] IcmCmndParts[param]'
####+END:

csInfo['description'] = """ #+begin_org
* /[[elisp:(org-cycle)][| Description |]]/ :: [[file:/bisos/git/auth/bxRepos/blee-binders/bisos-core/COMEEGA/_nodeBase_/fullUsagePanel-en.org][BISOS COMEEGA Panel]]
Module description comes here.
** Relevant Panels:
** Status: In use with blee3
** /[[elisp:(org-cycle)][| Planned Improvements |]]/ :
*** TODO complete fileName in particulars.
#+end_org """

####+BEGIN: b:prog:file/orgTopControls :outLevel 1
""" #+begin_org
* [[elisp:(org-cycle)][| Controls |]] :: [[elisp:(delete-other-windows)][(1)]] | [[elisp:(show-all)][Show-All]]  [[elisp:(org-shifttab)][Overview]]  [[elisp:(progn (org-shifttab) (org-content))][Content]] | [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] | [[elisp:(bx:org:run-me)][Run]] | [[elisp:(bx:org:run-me-eml)][RunEml]] | [[elisp:(progn (save-buffer) (kill-buffer))][S&Q]]  [[elisp:(save-buffer)][Save]]  [[elisp:(kill-buffer)][Quit]] [[elisp:(org-cycle)][| ]]
** /Version Control/ ::  [[elisp:(call-interactively (quote cvs-update))][cvs-update]]  [[elisp:(vc-update)][vc-update]] | [[elisp:(bx:org:agenda:this-file-otherWin)][Agenda-List]]  [[elisp:(bx:org:todo:this-file-otherWin)][ToDo-List]]
#+end_org """
####+END:

####+BEGIN: b:python:file/workbench :outLevel 1
""" #+begin_org
* [[elisp:(org-cycle)][| Workbench |]] :: [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pyclbr %s" (bx:buf-fname))))][pyclbr]] || [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pydoc ./%s" (bx:buf-fname))))][pydoc]] || [[elisp:(python-check (format "/bisos/pipx/bin/pyflakes %s" (bx:buf-fname)))][pyflakes]] | [[elisp:(python-check (format "/bisos/pipx/bin/pychecker %s" (bx:buf-fname))))][pychecker (executes)]] | [[elisp:(python-check (format "/bisos/pipx/bin/pycodestyle %s" (bx:buf-fname))))][pycodestyle]] | [[elisp:(python-check (format "/bisos/pipx/bin/flake8 %s" (bx:buf-fname))))][flake8]] | [[elisp:(python-check (format "/bisos/pipx/bin/pylint %s" (bx:buf-fname))))][pylint]]  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:


####+BEGIN: b:py3:cs:orgItem/basic :type "=PyImports= " :title "*Py Library IMPORTS*" :comment "-- with classification based framework/imports"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  =PyImports=  [[elisp:(outline-show-subtree+toggle)][||]] *Py Library IMPORTS* -- with classification based framework/imports  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: b:py3:cs:framework/imports :basedOn "classification"
""" #+begin_org
** Imports Based On Classification=cs-lib
#+end_org """
from bisos import b
from bisos.b import cs
from bisos.b import b_io

####+END:

import sys
import collections
import gnupg

import collections
import pathlib
import os
import shutil

from bisos.bpo import bpoRunBases
from bisos.bpo import bpo

#from bisos.marmee import saiInMailControl
from bisos.marmee import aasInFps

from bisos import b


####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :sep nil :title "Classes" :anchor ""  :extraInfo "InMail_Control"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _Classes_: |]]  InMail_Control  [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:


####+BEGIN: b:py3:class/decl :className "Sai_InMail_Offlineimap" :superClass "bpoRunBases.BpoRunEnvBases" :comment "" :classType "basic"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Cls-basic  [[elisp:(outline-show-subtree+toggle)][||]] /Sai_InMail_Offlineimap/  superClass=bpoRunBases.BpoRunEnvBases  [[elisp:(org-cycle)][| ]]
#+end_org """
class Sai_InMail_Offlineimap(bpoRunBases.BpoRunEnvBases):
####+END:
    """ #+begin_org
** [[elisp:(org-cycle)][| DocStr| ]]  InMail Service Access Instance Class for an Accessible Abstract Service.
    #+end_org """

    def __init__(
            self,
            bpoId,
            envRelPath,
    ):
        super().__init__(bpoId, envRelPath,)

####+BEGIN: b:py3:cs:method/args :methodName "offlineimapRcPath" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList "self"
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /offlineimapRcPath/ deco=default  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def offlineimapRcPath(self, ):
####+END
        """ #+begin_org
*** [[elisp:(org-cycle)][| DocStr| ]]  Return path to =offlineimapRc= in ~var/control~
        #+end_org """
        varBase = self.varBasePath_obtain()
        varControlBase = pathlib.Path(pathlib.PurePath(varBase, 'control'))
        varControlBase.mkdir(parents=True, exist_ok=True)
        return pathlib.Path(pathlib.PurePath(varControlBase, 'offlineimapRc'))

####+BEGIN: b:py3:cs:method/typing :methodName "offlineimapRcTemplate" :methodType "" :retType "bool" :deco "default" :argsList ""
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-     [[elisp:(outline-show-subtree+toggle)][||]] /offlineimapRcTemplate/ deco=default  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def offlineimapRcTemplate(
####+END
            self,
            inMailSvcProv,
    ):
        """ #+begin_org
*** [[elisp:(org-cycle)][| DocStr| ]]  Look in control dir for file params.
        #+end_org """

        supportedSvcProviders = ("generic", "gmail")

        if not (inMailSvcProv in supportedSvcProviders):
            b_io.eh.problem_usageError(f"{inMailSvcProv} is not supported")
            return ""

        inMailSvcProvTemplate = getattr(self, f"offlineimapRcTemplate_{inMailSvcProv}")

        return inMailSvcProvTemplate()

        
####+BEGIN: b:py3:cs:method/typing :methodName "offlineimapRcTemplate_generic" :methodType "" :retType "bool" :deco "default" :argsList ""
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-     [[elisp:(outline-show-subtree+toggle)][||]] /offlineimapRcTemplate_generic/ deco=default  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def offlineimapRcTemplate_generic(
####+END
            self,
    ):
        """ #+begin_org
*** [[elisp:(org-cycle)][| DocStr| ]]  Look in control dir for file params.
        #+end_org """
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


####+BEGIN: b:py3:cs:method/typing :methodName "offlineimapRcTemplate_gmail" :methodType "" :retType "bool" :deco "default" :argsList ""
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-     [[elisp:(outline-show-subtree+toggle)][||]] /offlineimapRcTemplate_gmail/ deco=default  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def offlineimapRcTemplate_gmail(
####+END
            self,
    ):
        """ #+begin_org
*** [[elisp:(org-cycle)][| DocStr| ]]  Look in control dir for file params.
        #+end_org """
        templateStr = """
# offlineimaprc for use with gmail -- Taken from:
# https://github.com/sadsfae/misc-dotfiles/blob/7089bf68ade2f82d4962bd08f040c05ab476e8d6/offlineimaprc-gmail
[general]
accounts = MyAccount

[Account MyAccount]
localrepository = LocalIMAP
remoterepository = RemoteIMAP

[Repository RemoteIMAP]
type = IMAP
remotehost = {imapServer}
remoteuser = {userName}
ssl = yes
starttls = no
sslcacertfile = /etc/ssl/certs/ca-certificates.crt
ssl_version=tls1_2

### You'll need to configure the gmail API stuff here:
# https://github.com/OfflineIMAP/offlineimap/blob/master/offlineimap.conf#L858
# https://github.com/OfflineIMAP/offlineimap/blob/master/offlineimap.conf#L886-L894
auth_mechanisms = XOAUTH2
oauth2_client_id = 377167941016-d08lcj3hlcrnlb3nk5fgtlass6heqoqr.apps.googleusercontent.com
oauth2_client_secret = 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
oauth2_request_url = https://accounts.google.com/o/oauth2/token
oauth2_refresh_token = 1//06Zgb6afI1ULICgYIARAAGAYSNwF-L9IrCjdK4qrkRqjE4c8nGwLo8wWihRlgFR_N63E2B-v7savDiSSByhqW0p2pmz_WhRn_G3k
nametrans = lambda f: f.replace('[Gmail]/', '') if f.startswith('[Gmail]/') else f

[Repository LocalIMAP]
type = Maildir
localfolders = {inMailAcctMboxesPath}
restoreatime = no
# Do not sync this folder
folderfilter = lambda folder: folder not in ['some-inbox']
## Remove GMAIL prefix on Google-specific IMAP folders that are pulled down.
nametrans = lambda f: '[Gmail]/' + f if f in ['Drafts', 'Starred', 'Important', 'Spam', 'Trash', 'All Mail', 'Sent Mail'] else f


"""
        return templateStr


####+BEGIN: b:py3:cs:method/typing :methodName "offlineimapRcString" :methodType "eType" :retType "" :deco "default" :argsList ""
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-eType [[elisp:(outline-show-subtree+toggle)][||]] /offlineimapRcString/ deco=default  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def offlineimapRcString(
####+END:
            self,
    ):
        """ #+begin_org
*** [[elisp:(org-cycle)][| DocStr| ]]  Outputs on stdout, a complete offlineimapRc based on template.
        #+end_org """

        outcome = b.op.Outcome()

        controlInst = saiInMailControl.Sai_InMail_Control(self.bpoId, self.envRelPath)  # This should be obsoleted in favor of aasInFps.AasIn_accessFPs

        if not (accessPars := controlInst.accessFps_wOp(outcome=outcome).results):
            return b_io.eh.badOutcome(outcome)

        #print(accessPars)
        svcProvider = accessPars['svcProvider'].parValueGet()
        if not svcProvider: return b_io.eh.badOutcome(outcome)

        offlineimapRcString_svcProvider = getattr(self, f"offlineimapRcString_{svcProvider}")

        return offlineimapRcString_svcProvider()


####+BEGIN: b:py3:cs:method/typing :methodName "offlineimapRcString_gmail" :methodType "eType" :retType "" :deco "default" :argsList ""
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-eType [[elisp:(outline-show-subtree+toggle)][||]] /offlineimapRcString_gmail/ deco=default  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def offlineimapRcString_gmail(
####+END:
            self,
    ):
        """ #+begin_org
*** [[elisp:(org-cycle)][| DocStr| ]]  ~self~ is an instance of XXX. Outputs on stdout, a complete offlineimapRc based on template.
        #+end_org """

        basedFps = b.pattern.sameInstance(
            aasInFps.AasIn_accessFPs,
            bpoId=self.bpoId,
            envRelPath=self.envRelPath,
        )

        userName = basedFps.fps_getParam('userName').parValueGet()
        svcProvider = basedFps.fps_getParam('svcProvider').parValueGet()

        somePasswd = basedFps.fpCrypt_getParam('somePasswd').parValueGet()

        print(f"Example of how to access encrypted params: {somePasswd}")

        if svcProvider == "gmail":
            imapServer = "imap.gmail.com"
        else:
            return

        mailDirFullPath = 'NOTYEY_inMailAcctMboxesPath'

        #mailDirFullPath = retrievalPars['inMailAcctMboxesPath'].parValueGet()
        #if not mailDirFullPath: return b_io.eh.badOutcome(outcome)

        #mboxesList = retrievalPars['mboxesList'].parValueGet()
        mboxesList = "all"

        foldersListStr = ""
        if mboxesList == "all":
            folderFilterLineStr = "#"
        else:
            for each in mboxesList.split():
                foldersListStr += "'INBOX.{}',".format(each)

            folderFilterLineStr = """folderfilter = lambda name: name in [ {foldersListStr} ]""".format(
                foldersListStr=foldersListStr)


        resStr = self.offlineimapRcTemplate("gmail").format(
            inMailAcctMboxesPath=mailDirFullPath,
            imapServer=imapServer,
            userName=userName,
            foldersListStr=foldersListStr,
            folderFilterLine=folderFilterLineStr,
        )

        return resStr


####+BEGIN: b:py3:cs:method/typing :methodName "offlineimapRcString_gmailOBSOLETED" :methodType "eType" :retType "" :deco "default" :argsList ""
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-eType [[elisp:(outline-show-subtree+toggle)][||]] /offlineimapRcString_gmailOBSOLETED/ deco=default  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def offlineimapRcString_gmailOBSOLETED(
####+END:
            self,
    ):
        """ #+begin_org
*** [[elisp:(org-cycle)][| DocStr| ]]  Outputs on stdout, a complete offlineimapRc based on template.
        #+end_org """
        controlInst = saiInMailControl.Sai_InMail_Control(self.bpoId, self.envRelPath)

        outcome = b.op.Outcome()

        if not (accessPars := controlInst.accessFps_wOp(outcome=outcome).results):
            return b_io.eh.badOutcome(outcome)

        if not (retrievalPars := controlInst.retrievalFps_wOp(outcome=outcome).results):
            return b_io.eh.badOutcome(outcome)

        mailDirFullPath = 'NOTYEY_inMailAcctMboxesPath'

        #mailDirFullPath = retrievalPars['inMailAcctMboxesPath'].parValueGet()
        #if not mailDirFullPath: return b_io.eh.badOutcome(outcome)

        #mboxesList = retrievalPars['mboxesList'].parValueGet()
        mboxesList = "all"

        foldersListStr = ""
        if mboxesList == "all":
            folderFilterLineStr = "#"
        else:
            for each in mboxesList.split():
                foldersListStr += "'INBOX.{}',".format(each)

            folderFilterLineStr = """folderfilter = lambda name: name in [ {foldersListStr} ]""".format(
                foldersListStr=foldersListStr)


        resStr = self.offlineimapRcTemplate("gmail").format(
            inMailAcctMboxesPath=mailDirFullPath,
            imapServer=accessPars['imapServer'].parValueGet(),
            userName=accessPars['userName'].parValueGet(),
            foldersListStr=foldersListStr,
            folderFilterLine=folderFilterLineStr,
        )

        return resStr



####+BEGIN: b:py3:cs:method/typing :methodName "offlineimapRcString_generic" :methodType "eType" :retType "" :deco "default" :argsList ""
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-eType [[elisp:(outline-show-subtree+toggle)][||]] /offlineimapRcString_generic/ deco=default  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def offlineimapRcString_generic(
####+END:
            self,
    ):
        """ #+begin_org
*** [[elisp:(org-cycle)][| DocStr| ]]  Outputs on stdout, a complete offlineimapRc based on template.
        #+end_org """
        controlInst = saiInMailControl.Sai_InMail_Control(self.bpoId, self.envRelPath)

        outcome = b.op.Outcome()

        if not (accessPars := controlInst.accessFps_wOp(outcome=outcome).results):
            return b_io.eh.badOutcome(outcome)

        if not (retrievalPars := controlInst.retrievalFps_wOp(outcome=outcome).results):
            return b_io.eh.badOutcome(outcome)

        mailDirFullPath = retrievalPars['inMailAcctMboxesPath'].parValueGet()

        mailDirFullPath = retrievalPars['inMailAcctMboxesPath'].parValueGet()
        if not mailDirFullPath: return b_io.eh.badOutcome(outcome)

        mboxesList = retrievalPars['mboxesList'].parValueGet()

        foldersListStr = ""
        if mboxesList == "all":
            folderFilterLineStr = "#"
        else:
            for each in mboxesList.split():
                foldersListStr += "'INBOX.{}',".format(each)

            folderFilterLineStr = """folderfilter = lambda name: name in [ {foldersListStr} ]""".format(
                foldersListStr=foldersListStr)


        resStr = self.offlineimapRcTemplate("generic").format(
            inMailAcctMboxesPath=mailDirFullPath,
            imapServer=accessPars['imapServer'].parValueGet(),
            userName=accessPars['userName'].parValueGet(),
            userPasswd=accessPars['userPasswd'].parValueGet(),
            ssl=retrievalPars['ssl'].parValueGet(),
            foldersListStr=foldersListStr,
            folderFilterLine=folderFilterLineStr,
        )

        return resStr

    
####+BEGIN: b:py3:cs:method/typing :methodName "offlineimapRcUpdate" :methodType "eType" :retType "" :deco "default" :argsList ""
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-eType [[elisp:(outline-show-subtree+toggle)][||]] /offlineimapRcUpdate/ deco=default  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def offlineimapRcUpdate(
####+END
            self,
    ):
        """ #+begin_org
*** [[elisp:(org-cycle)][| DocStr| ]]  Look in control dir for file params.
        #+end_org """
        controlBase = self.controlBasePath_obtain()


####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :sep nil :title "CmndSvcs" :anchor ""  :extraInfo "Command Services Section"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _CmndSvcs_: |]]  Command Services Section  [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:


####+BEGIN: bx:cs:py3:section :title "CS-Lib Examples"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    [[elisp:(outline-show-subtree+toggle)][||]] *CS-Lib Examples*  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: b:py3:cs:func/typing :funcName "examples_csu" :funcType "eType" :retType "" :deco "default" :argsList ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-eType  [[elisp:(outline-show-subtree+toggle)][||]] /examples_csu/  deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
@cs.track(fnLoc=True, fnEntry=True, fnExit=True)
def examples_csu(
####+END:
        bpoId: typing.Optional[str],
        envRelPath: typing.Optional[str],
        sectionTitle: typing.AnyStr = "",
) -> None:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] Examples of Service Access Instance Commands.
    #+end_org """

    def cpsInit(): return collections.OrderedDict()
    def menuItem(verbosity): cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity=verbosity) # 'little' or 'none'
    # def execLineEx(cmndStr): cs.examples.execInsert(execLine=cmndStr)

    def cmndParsCurBpoAndEnvRelPath(cps): cps['bpoId'] = bpoId ; cps['envRelPath'] = envRelPath

    if sectionTitle == "default":
        cs.examples.menuChapter('*inMail --- Service Access Instance Commands*')

    if bpoId == None:
        return

    cs.examples.menuChapter('*Config File Creation Facility IIFs*')

    cmndName = "offlineimapRcUpdate" ;  cmndArgs = ""
    cps=cpsInit(); cmndParsCurBpoAndEnvRelPath(cps);
    menuItem(verbosity='none') ; menuItem(verbosity='full')

    cmndName = "offlineimapRcStdout" ;  cmndArgs = ""
    cps=cpsInit(); cmndParsCurBpoAndEnvRelPath(cps);
    menuItem(verbosity='none') #; menuItem(verbosity='full')

    cs.examples.menuChapter('*Operation Facility IIFs -- (offlineimapRun)*')

    cmndName = "offlineimapRun" ;  cmndArgs = ""
    cps=cpsInit(); cmndParsCurBpoAndEnvRelPath(cps);
    menuItem(verbosity='none') #; menuItem(verbosity='full')


####+BEGIN: bx:cs:py3:section :title "CS-Params  --- Place Holder, Empty"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    [[elisp:(outline-show-subtree+toggle)][||]] *CS-Params  --- Place Holder, Empty*  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: bx:cs:py3:section :title "CS-Commands"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    [[elisp:(outline-show-subtree+toggle)][||]] *CS-Commands*  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "offlineimapRun" :comment "" :parsMand "bpoId envRelPath" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<offlineimapRun>>  =verify= parsMand=bpoId envRelPath ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class offlineimapRun(cs.Cmnd):
    cmndParamsMandatory = [ 'bpoId', 'envRelPath', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             bpoId: typing.Optional[str]=None,  # Cs Mandatory Param
             envRelPath: typing.Optional[str]=None,  # Cs Mandatory Param
    ) -> b.op.Outcome:

        callParamsDict = {'bpoId': bpoId, 'envRelPath': envRelPath, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  As subProc, runs offlineimap -c offlineimapRcPath.
        #+end_org """)

        offlineimapInst = Sai_InMail_Offlineimap(bpoId, envRelPath)

        offlineimapRcPath = offlineimapInst.offlineimapRcPath()


        if not (resStr := b.subProc.WOpW(invedBy=self, log=1).bash(
                f"""echo offlineimap -c {offlineimapRcPath}""",
        ).stdout):  return(io.eh.badOutcome(cmndOutcome))

        #print(resStr)

        return cmndOutcome.set(
            opError=b.OpError.Success,
            opResults=True,
        )


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "offlineimapRcUpdate" :comment "" :parsMand "bpoId envRelPath" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<offlineimapRcUpdate>>  =verify= parsMand=bpoId envRelPath ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class offlineimapRcUpdate(cs.Cmnd):
    cmndParamsMandatory = [ 'bpoId', 'envRelPath', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             bpoId: typing.Optional[str]=None,  # Cs Mandatory Param
             envRelPath: typing.Optional[str]=None,  # Cs Mandatory Param
    ) -> b.op.Outcome:

        callParamsDict = {'bpoId': bpoId, 'envRelPath': envRelPath, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Updates offlineimapRc file using offlineimapRcStr.
        #+end_org """)

        offlineimapInst = Sai_InMail_Offlineimap(bpoId, envRelPath)

        resStr = offlineimapInst.offlineimapRcString()

        offlineimapRcPath = offlineimapInst.offlineimapRcPath()

        if os.path.isfile(offlineimapRcPath):
            shutil.copyfile(offlineimapRcPath, "/tmp/t1")

        with open(offlineimapRcPath, "w") as thisFile:
            thisFile.write(resStr + '\n')

        if rtInv.outs:
            icm.ANN_here(f"offlineimapRcPath={offlineimapRcPath}")
            if b.subProc.Op(outcome=cmndOutcome, log=1).bash(
                    f"""ls -l {offlineimapRcPath}""",
            ).isProblematic():  return(io.eh.badOutcome(cmndOutcome))


        return cmndOutcome.set(
            opError=b.OpError.Success,
            opResults=offlineimapRcPath,
        )

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "offlineimapRcStdout" :comment "" :parsMand "bpoId envRelPath" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<offlineimapRcStdout>>  =verify= parsMand=bpoId envRelPath ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class offlineimapRcStdout(cs.Cmnd):
    cmndParamsMandatory = [ 'bpoId', 'envRelPath', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             bpoId: typing.Optional[str]=None,  # Cs Mandatory Param
             envRelPath: typing.Optional[str]=None,  # Cs Mandatory Param
    ) -> b.op.Outcome:

        callParamsDict = {'bpoId': bpoId, 'envRelPath': envRelPath, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
####+END:

        offlineimapInst = Sai_InMail_Offlineimap(bpoId, envRelPath)

        resStr = offlineimapInst.offlineimapRcString()

        if rtInv.outs:
            print(resStr)

        return cmndOutcome.set(
            opError=b.OpError.Success,
            opResults=resStr
        )


####+BEGIN: b:py3:cs:framework/endOfFile :basedOn "classification"
""" #+begin_org
* [[elisp:(org-cycle)][| *End-Of-Editable-Text* |]] :: emacs and org variables and control parameters
#+end_org """

#+STARTUP: showall

### local variables:
### no-byte-compile: t
### end:
####+END:
