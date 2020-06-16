# -*- mode: python ; coding: utf-8 -*-
from kivy_deps import sdl2, glew
import pkg_resources.py2_warn

block_cipher = None


a = Analysis(['InstaLiker.py'],
             pathex=['C:\\Users\\Lenovo\\Documents\\Python\\intsaliker'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='InstaLiker',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True , icon='icon.ico')
coll = COLLECT(exe, Tree ('C:\\Users\\Lenovo\\Documents\\Python\\intsaliker'),
               a.binaries,
               a.zipfiles,
               a.datas,
	       *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],	
               strip=False,
               upx=True,
               upx_exclude=[],
               name='InstaLiker')
