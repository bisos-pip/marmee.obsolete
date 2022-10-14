# -*- coding: utf-8 -*-

""" #+begin_org
* ~[Summary]~ :: A =CS-Lib= for Managing MARMEE AAS (Abstracted Accessible Service) Control File Parameters
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
* *[[elisp:(org-cycle)][| Proclamations |]]* :: Libre-Halaal Software --- Part Of Blee ---  Poly-COMEEGA Format.
** This is Libre-Halaal Software. © Libre-Halaal Foundation. Subject to AGPL.
** It is not part of Emacs. It is part of Blee.
** Best read and edited  with Poly-COMEEGA (Polymode Colaborative Org-Mode Enhance Emacs Generalized Authorship)
#+end_org """
####+END:

####+BEGIN: b:prog:file/particulars :authors ("./inserts/authors-mb.org")
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars |]]* :: Authors, version
** This File: NOTYET
** Authors: Mohsen BANAN, http://mohsen.banan.1.byname.net/contact
#+end_org """
####+END:

####+BEGIN: b:python:file/particulars-csInfo :status "inUse"
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars-csInfo |]]*
#+end_org """
import typing
csInfo: typing.Dict[str, typing.Any] = { 'moduleName': ['ro'], }
csInfo['version'] = '202209130210'
csInfo['status']  = 'inUse'
csInfo['panel'] = 'ro-Panel.org'
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
** Imports Based On Classification=cs-u
#+end_org """
from bisos import b
from bisos.b import cs
from bisos.b import b_io

import collections
####+END:

from bisos.bpo import bpoRunBases

from bisos.currents import currentsConfig
from bisos.marmee import aasMailFps


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


####+BEGIN: bx:cs:py3:section :title "Service Specification"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    [[elisp:(outline-show-subtree+toggle)][||]] *Service Specification*  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :sep nil :title "CSU" :anchor ""  :extraInfo "Command Services Section"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _CSU_: |]]  Command Services Section  [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:

####+BEGIN: b:py3:cs:func/typing :funcName "examples_csu" :funcType "eType" :retType "" :deco "default" :argsList ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-eType  [[elisp:(outline-show-subtree+toggle)][||]] /examples_csu/ deco=default  deco=default   [[elisp:(org-cycle)][| ]]
#+end_org """
@cs.track(fnLoc=True, fnEntry=True, fnExit=True)
def examples_csu(
####+END:
        bpoId: str,
        envRelPath: str,
        sectionTitle: typing.AnyStr = '',
) -> None:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr* | ] Examples of Service Access Instance Commands.
    #+end_org """

    def cpsInit(): return collections.OrderedDict()
    def menuItem(verbosity, **kwArgs): cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity=verbosity, **kwArgs)
    def execLineEx(cmndStr): cs.examples.execInsert(execLine=cmndStr)

    cs.examples.menuChapter('*Oauth Credentials And Tokens Management*')

    icmWrapper = ""
    cmndName = "marmeeAasIn_fps"
    cps = cpsInit() ; cps['bpoId'] = bpoId ; cps['envRelPath'] = envRelPath
    cmndArgs = "list" ;
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='none', icmWrapper=icmWrapper)

    icmWrapper = ""
    cmndName = "marmeeAasIn_fps"
    cps = cpsInit() ; cps['bpoId'] = bpoId ; cps['envRelPath'] = envRelPath
    cmndArgs = "menu" ;
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='none', icmWrapper=icmWrapper)



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
    cmndName = "refreshToken" ; cps=cpsInit() ; cps['bpoId'] = bpoId ; cps['envRelPath'] = envRelPath
    menuItem(verbosity='little', comment="# Under development in parts")
    menuItem(verbosity='none', comment="# Under development in parts")



####+BEGIN: b:py3:cs:func/args :funcName "commonParamsSpecify" :comment "" :funcType "FmWrk" :retType "Void" :deco "" :argsList "csParams"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-A-FmWrk  [[elisp:(outline-show-subtree+toggle)][||]] /commonParamsSpecify/ deco=  [[elisp:(org-cycle)][| ]]  [[elisp:(org-cycle)][| ]]
#+end_org """
def commonParamsSpecify(
    csParams,
):
####+END:
    """
** Based on class's static method.
    """

    pass


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


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "refreshToken" :cmndType "ICM-Cmnd"  :comment "" :parsMand "bpoId envRelPath" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-ICM-Cmnd [[elisp:(outline-show-subtree+toggle)][||]] <<refreshToken>>  =verify= parsMand=bpoId envRelPath ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class refreshToken(cs.Cmnd):
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
        """\
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]] ICM examples, all on one place.
        """
        """Shows basic usage of the PostmasterTools v1beta1 API.
        Prints the visible domains on user's domain dashboard in https://postmaster.google.com/managedomains.

        Look into this:
https://stackoverflow.com/questions/51487195/how-can-i-use-python-google-api-without-getting-a-fresh-auth-code-via-browser-ea

        """

        refreshTokenObtain(bpoId, envRelPath)

        cmndOutcome = self.getOpOutcome()

        return(cmndOutcome)


####+BEGIN: b:py3:cs:func/typing :funcName "refreshTokenObtain" :funcType "eType" :deco "default"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-eType  [[elisp:(outline-show-subtree+toggle)][||]] /refreshTokenObtain/  deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
@cs.track(fnLoc=True, fnEntry=True, fnExit=True)
def refreshTokenObtain(
####+END:
        bpoId: str,
        envRelPath: str,
) -> str:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr* | ] Returns a token
    #+end_org """

    runEnvBases = b.pattern.sameInstance(bpoRunBases.BpoRunEnvBases, bpoId, envRelPath)
    controlBase = runEnvBases.controlBasePath_obtain()

    credsJsonFile = controlBase.joinpath('credentials.json')
    tokenPickleFile = controlBase.joinpath('token.pickle')
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

    return creds.refresh_token



####+BEGIN: b:py3:cs:framework/endOfFile :basedOn "classification"
""" #+begin_org
* *[[elisp:(org-cycle)][| ~End-Of-Editable-Text~ |]]* :: emacs and org variables and control parameters
#+end_org """

#+STARTUP: showall

### local variables:
### no-byte-compile: t
### end:
####+END:
