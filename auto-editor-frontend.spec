# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['auto-editor-frontend.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('C:\\Python311\\Lib\\site-packages\\tkinterdnd2\\tkdnd\\win64', 'tkdnd'),
        ('C:\\Python311\\Lib\\site-packages\\auto_editor', 'auto-editor'),
        ('C:\\Python311\\Scripts\\auto-editor.exe', '.')
        ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='auto-editor-frontend',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='auto-editor-frontend',
)
