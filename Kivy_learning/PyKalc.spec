# -*- mode: python -*-

"""
    First of make sure that you actually import whatever you need for your 
    app
"""

from kivy import kivy_data_dir

from kivy.tools.packaging import pyinstaller_hooks as hooks

from kivy_deps import sdl2, glew
import os
from os.path import join

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget

from Calc.functions_main import *

from kivy.clock import Clock
from kivy.factory import Factory

import math

""" 
   Next make sure you have all of kivys dependencies 
"""

block_cipher = None
kivy_deps_all = hooks.get_deps_all()
kivy_factory_modules = hooks.get_factory_modules()

"""
    Then include any files that you may need for your app
"""

# list of modules to exclude from analysis
excludes_a = ['Tkinter', '_tkinter', 'twisted', 'docutils', 'pygments']

# list of hiddenimports
hiddenimports = kivy_deps_all['hiddenimports'] + kivy_factory_modules

# binary data
sdl2_bin_tocs = [Tree(p) for p in sdl2.dep_bins]
glew_bin_tocs = [Tree(p) for p in glew.dep_bins]

bin_tocs = sdl2_bin_tocs + glew_bin_tocs

# assets
kivy_assets_toc = Tree(kivy_data_dir, prefix=join('kivy_install', 'data'))

assets_toc = [kivy_assets_toc]

tocs = bin_tocs + assets_toc

a = Analysis(['Kivy_GUI.py'],
             pathex=[os.getcwd()],
             binaries=None,
             hiddenimports=hiddenimports,
             hookspath=[],
             runtime_hooks=[],
             excludes=excludes_a,
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)


pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

"""
    Put your *tocs underneath the a.data (this would go under the collect if 
    we wanted the app to be a dir and not a onefile)
"""    

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          *tocs,
          name='PyKalc',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )