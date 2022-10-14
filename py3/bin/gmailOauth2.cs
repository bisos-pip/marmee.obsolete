#!/bin/env python
# -*- coding: utf-8 -*-
"""\
* ~[gmailOauth2.cs]~ :: Gmail Oauth2 Facilities Commands Services: Obtain / Refresh tokens for use in IMAP and SMTP.
"""

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
** This File: /bisos/git/auth/bxRepos/bisos/bpip1/bin/gmailOauth2.cs
** Authors: Mohsen BANAN, http://mohsen.banan.1.byname.net/contact
#+end_org """
####+END:

####+BEGIN: b:python:file/particulars-csInfo :status "inUse"
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars-csInfo |]]*
#+end_org """
import typing
csInfo: typing.Dict[str, typing.Any] = { 'moduleName': ['gmailOauth2'], }
csInfo['version'] = '202210121250'
csInfo['status']  = 'inUse'
csInfo['panel'] = 'gmailOauth2-Panel.org'
csInfo['groupingType'] = 'IcmGroupingType-pkged'
csInfo['cmndParts'] = 'IcmCmndParts[common] IcmCmndParts[param]'
####+END:


csInfo['moduleDescription'] = """ #+begin_org
* [[elisp:(org-cycle)][| ~Description~ |]] :: [[file:/bisos/git/auth/bxRepos/blee-binders/bisos-core/COMEEGA/_nodeBase_/fullUsagePanel-en.org][BISOS COMEEGA Panel]]
A =CmndSvc= Gmail Oauth2 Facilities Commands Services: Obtain / Refresh tokens for use in IMAP and SMTP.
** Relevant Panels:
** Status: In use with BISOS
** /[[elisp:(org-cycle)][| Planned Improvements |]]/ :
*** TODO complete fileName in particulars.
** Links:
*** +
*** https://github.com/google/gmail-oauth2-tools -- An origin for this module.
*** https://github.com/googleworkspace/python-samples/blob/master/gmail/quickstart/quickstart.py  -- Origin for this module.
*** https://developers.google.com/gmail/api/quickstart/python -- Python 2.6+ An origin for this module.
*** ---
*** https://developers.google.com/gmail/api/auth/scopes
*** https://google-auth.readthedocs.io/en/stable/_modules/google/oauth2/credentials.html
*** https://developers.google.com/gmail/imap/xoauth2-protocol
*** https://www.thepythoncode.com/article/use-gmail-api-in-python
*** -------- BEGIN From oauth2.py
Performs client tasks for testing IMAP OAuth2 authentication.

To use this script, you'll need to have registered with Google as an OAuth
application and obtained an OAuth client ID and client secret.
See https://developers.google.com/identity/protocols/OAuth2 for instructions on
registering and for documentation of the APIs invoked by this code.

This script has 3 modes of operation.

1. The first mode is used to generate and authorize an OAuth2 token, the
first step in logging in via OAuth2.

  oauth2 --user=xxx@gmail.com \
    --client_id=1038[...].apps.googleusercontent.com \
    --client_secret=VWFn8LIKAMC-MsjBMhJeOplZ \
    --generate_oauth2_token

The script will converse with Google and generate an oauth request
token, then present you with a URL you should visit in your browser to
authorize the token. Once you get the verification code from the Google
website, enter it into the script to get your OAuth access token. The output
from this command will contain the access token, a refresh token, and some
metadata about the tokens. The access token can be used until it expires, and
the refresh token lasts indefinitely, so you should record these values for
reuse.

2. The script will generate new access tokens using a refresh token.

  oauth2 --user=xxx@gmail.com \
    --client_id=1038[...].apps.googleusercontent.com \
    --client_secret=VWFn8LIKAMC-MsjBMhJeOplZ \
    --refresh_token=1/Yzm6MRy4q1xi7Dx2DuWXNgT6s37OrP_DW_IoyTum4YA

3. The script will generate an OAuth2 string that can be fed
directly to IMAP or SMTP. This is triggered with the --generate_oauth2_string
option.

  oauth2 --generate_oauth2_string --user=xxx@gmail.com \
    --access_token=ya29.AGy[...]ezLg

The output of this mode will be a base64-encoded string. To use it, connect to a
IMAPFE and pass it as the second argument to the AUTHENTICATE command.

  a AUTHENTICATE XOAUTH2 a9sha9sfs[...]9dfja929dk==
*** -------- END From oauth2.py
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
** Imports Based On Classification=cs-mu
#+end_org """
from bisos import b
from bisos.b import cs
from bisos.b import b_io

import collections
####+END:

from bisos.currents import currentsConfig

from datetime import datetime
import pathlib

# pip install google-api-python-client google-auth-oauthlib

import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient import errors
#from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.pickle.
#SCOPES = ['https://www.googleapis.com/auth/postmaster.readonly']
SCOPES = ['https://mail.google.com/']


""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CsFrmWrk   [[elisp:(outline-show-subtree+toggle)][||]] ~csuList emacs-list Specifications~  [[elisp:(blee:org:code-block/above-run)][ /Eval Below/ ]] [[elisp:(org-cycle)][| ]]
#+BEGIN_SRC emacs-lisp
(setq  b:py:cs:csuList
  (list
   "bisos.b.cs.ro"
   "blee.csPlayer.bleep"
 ))
#+END_SRC
#+RESULTS:
| bisos.b.cs.ro | blee.csPlayer.bleep |
#+end_org """

####+BEGIN: b:py3:cs:framework/csuListProc :pyImports t :csuImports t :csuParams t
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CsFrmWrk   [[elisp:(outline-show-subtree+toggle)][||]] =Process CSU List= with /2/ in csuList pyImports=t csuImports=t csuParams=t
#+end_org """

from bisos.b.cs import ro
from blee.csPlayer import bleep


csuList = [ 'bisos.b.cs.ro', 'blee.csPlayer.bleep', ]

g_importedCmndsModules = cs.csuList_importedModules(csuList)

def g_extraParams():
    csParams = cs.param.CmndParamDict()
    cs.csuList_commonParamsSpecify(csuList, csParams)
    cs.argsparseBasedOnCsParams(csParams)

####+END:

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "examples" :cmndType "Cmnd-FmWrk"  :comment "FrameWrk: ICM Examples" :parsMand "" :parsOpt "cntnrId rosmu" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-Cmnd-FmWrk [[elisp:(outline-show-subtree+toggle)][||]] <<examples>>  *FrameWrk: ICM Examples*  =verify= parsOpt=cntnrId rosmu ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class examples(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'cntnrId', 'rosmu', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             cntnrId: typing.Optional[str]=None,  # Cs Optional Param
             rosmu: typing.Optional[str]=None,  # Cs Optional Param
    ) -> b.op.Outcome:
        """FrameWrk: ICM Examples"""
        callParamsDict = {'cntnrId': cntnrId, 'rosmu': rosmu, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
####+END:
        self.cmndDocStr(f""" #+begin_org *
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Conventional top level example.
        #+end_org """)

####+BEGIN: b:py3:cs:module/cur_paramsAssign  :curParsList ("aasMarmee_bpoId" "aasMarmee_svcInMail" "aasMarmee_svcOutMail" "aasMarmee_svcProvider" "aasMarmee_svcInstance" "aasMarmee_envRelPath")
        """ #+begin_org
***  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Currents   [[elisp:(outline-show-subtree+toggle)][||]] ~cur_examples~ (aasMarmee_bpoId aasMarmee_svcInMail aasMarmee_svcOutMail aasMarmee_svcProvider aasMarmee_svcInstance aasMarmee_envRelPath)
        #+end_org """
        _parNamesList = [ 'aasMarmee_bpoId', 'aasMarmee_svcInMail', 'aasMarmee_svcOutMail', 'aasMarmee_svcProvider', 'aasMarmee_svcInstance', 'aasMarmee_envRelPath',]
        if not (curParsDictValue := currentsConfig.curParsGetAsDictValue_wOp(_parNamesList, outcome=cmndOutcome).results): return(cmndOutcome)
        cur_aasMarmee_bpoId = curParsDictValue['aasMarmee_bpoId']
        cur_aasMarmee_svcInMail = curParsDictValue['aasMarmee_svcInMail']
        cur_aasMarmee_svcOutMail = curParsDictValue['aasMarmee_svcOutMail']
        cur_aasMarmee_svcProvider = curParsDictValue['aasMarmee_svcProvider']
        cur_aasMarmee_svcInstance = curParsDictValue['aasMarmee_svcInstance']
        cur_aasMarmee_envRelPath = curParsDictValue['aasMarmee_envRelPath']
        def cur_examples():
            cs.examples.execInsert(execLine='bx-currents.cs')
            cs.examples.execInsert(execLine='bx-currents.cs -i usgCursParsGet')
            for each in _parNamesList:
                cs.examples.execInsert(execLine=f'bx-currents.cs -v 20 -i usgCursParsSet {each}={curParsDictValue[each]}')
####+END:

        def cpsInit(): return collections.OrderedDict()
        cmndArgs = "" ; cps=cpsInit() ;
        def menuItem(verbosity, **kwArgs): cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity=verbosity, **kwArgs)
        def execLineEx(cmndStr): cs.examples.execInsert(execLine=cmndStr)

        cs.examples.menuChapter('*Oauth Credentials And Tokens Management*')

        cs.examples.menuSection('*Credentials and Secrets --- .json*')        
        execLineEx("""# Obatining creds: https://docs.emailengine.app/setting-up-gmail-oauth2-for-imap-api/""")
        execLineEx("""ls -l ~/credentials.json""")
        execLineEx("""cat ~/credentials.json | jq""")
        
        cs.examples.menuSection('*Token File --- .pickle*')
        execLineEx("""ls -l ~/token.pickle""")
        execLineEx("""python -m pickletools ~/token.pickle # Safe""")
        execLineEx("""python -m pickle ~/token.pickle # May run byte-code""")        
        execLineEx("""rm ~/token.pickle""")

        cs.examples.menuSection('*Use Of Token For Outgoing Mail --- SSMTP*')
        execLineEx("""ls -l ~/sendpyrc""")

        cs.examples.menuSection('*Use Of Token For Incoming Mail --- IMAP*')
        execLineEx("""ls -l ~/.offlineimaprc""")

        cs.examples.menuChapter('*Refresh Token*')

        cmndArgs = ""
        cmndName = "refreshToken" ; cps=cpsInit()
        menuItem(verbosity='little', comment="# Under development in parts")
        menuItem(verbosity='none', comment="# Under development in parts")        

        return(cmndOutcome)

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "refreshTokenOrig" :cmndType "ICM-Cmnd"  :comment "" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 9999 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-ICM-Cmnd [[elisp:(outline-show-subtree+toggle)][||]] <<refreshTokenOrig>>  =verify= argsMax=9999 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class refreshTokenOrig(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 9999,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
        ####+END:
        """\
        ***** [[elisp:(org-cycle)][| *CmndDesc:* | ]] ICM examples, all on one place.
        """
        """Shows basic usage of the PostmasterTools v1beta1 API.
        Prints the visible domains on user's domain dashboard in https://postmaster.google.com/managedomains.

        Look into this:
https://stackoverflow.com/questions/51487195/how-can-i-use-python-google-api-without-getting-a-fresh-auth-code-via-browser-ea        
        
        """

        credsJsonFile = os.path.join(os.path.expanduser('~'), 'credentials.json')        
        tokenPickleFile = os.path.join(os.path.expanduser('~'), 'token.pickle')        
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists(tokenPickleFile):
            with open(tokenPickleFile, 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds:
                print(f"creds.valid={creds.valid}")
            if creds and creds.expired and creds.refresh_token:
                if creds:
                    print(f"creds.expired={creds.expired}")
                    print(f"creds.refresh_token={creds.refresh_token}")
                creds.refresh(Request())
                # 
                # if the above fails like below:
                # google.auth.exceptions.RefreshError: ('invalid_grant: Token has been expired or revoked.', {'error': 'invalid_grant', 'error_description': 'Token has been expired or revoked.'})
                # remove the token.pickle file and run again
                #
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                       credsJsonFile, SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(tokenPickleFile, 'wb') as token:
                pickle.dump(creds, token)

        # print(f"{creds}")    
        print(f"{creds.refresh_token}")
        # print(f"{creds.client_secret}")
        # print(f"{creds.client_id}")
        # print(f"{creds.scopes}")


        print(f"{credsJsonFile}")


        cmndOutcome = self.getOpOutcome()

        return(cmndOutcome)


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "refreshToken" :cmndType "ICM-Cmnd"  :comment "" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 9999 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-ICM-Cmnd [[elisp:(outline-show-subtree+toggle)][||]] <<refreshToken>>  =verify= argsMax=9999 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class refreshToken(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 9999,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
        ####+END:
        """\
        ***** [[elisp:(org-cycle)][| *CmndDesc:* | ]] ICM examples, all on one place.
        """
        """Shows basic usage of the PostmasterTools v1beta1 API.
        Prints the visible domains on user's domain dashboard in https://postmaster.google.com/managedomains.

        Look into this:
https://stackoverflow.com/questions/51487195/how-can-i-use-python-google-api-without-getting-a-fresh-auth-code-via-browser-ea        
        
        """

        credsJsonFile = os.path.join(os.path.expanduser('~'), 'credentials.json')        
        tokenPickleFile = os.path.join(os.path.expanduser('~'), 'token.pickle')        
        creds = None
        
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists(tokenPickleFile):
            with open(tokenPickleFile, 'rb') as token:
                creds = pickle.load(token)
                # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds:
                print(f"creds.valid={creds.valid}")
            if creds and creds.expired and creds.refresh_token:
                if creds:
                    print(f"creds.expired={creds.expired}")
                    print(f"creds.refresh_token={creds.refresh_token}")
                creds.refresh(Request())
                # 
                # if the above fails like below:
                # google.auth.exceptions.RefreshError: ('invalid_grant: Token has been expired or revoked.', {'error': 'invalid_grant', 'error_description': 'Token has been expired or revoked.'})
                # remove the token.pickle file and run again
                #
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                       credsJsonFile, SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(tokenPickleFile, 'wb') as token:
                pickle.dump(creds, token)

        # print(f"{creds}")    
        print(f"{creds.refresh_token}")
        # print(f"{creds.client_secret}")
        # print(f"{creds.client_id}")
        # print(f"{creds.scopes}")


        print(f"{credsJsonFile}")


        cmndOutcome = self.getOpOutcome()

        return(cmndOutcome)

    
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
