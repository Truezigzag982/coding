# -*- mode: python ; coding: utf-8 -*-

import sys
import os.path as osp
sys.setrecursionlimit(5000)
 
block_cipher = None
 
 
DIR = 'M:\\OneDrive\\CentriCoding\\1-课程研发\\2B-Python二级\\3-示例源码\\21-宠物信息管理工具\\pet_manager_proj\\'


a = Analysis(['pet_manager.py', 'pet4.py', 'cat4.py', 'dog4.py', 'object_save_and_read.py'],
             pathex=[DIR],
             binaries=[],
             datas=[(DIR+'image','image'), (DIR+'data', 'data')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
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
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='pet_manager',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
