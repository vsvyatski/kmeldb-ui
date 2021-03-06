"""
Copyright (C) 2019  Vladimir Svyatski

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import glob
import os
import subprocess

subprocess.run(['pyuic5', '-o', '../ui_mainwindow.py', '../forms/mainwindow.ui'])
subprocess.run(['pyuic5', '-o', '../ui_aboutdialog.py', '../forms/aboutdialog.ui'])
subprocess.run(['pyuic5', '-o', '../ui_preferencesdialog.py', '../forms/preferencesdialog.ui'])

subprocess.run(['pyrcc5', '-o', '../appresources_rc.py', '../appresources.qrc'])

# translations
for tsfile in glob.glob('../translations/*.ts'):
    basename = os.path.basename(tsfile)
    subprocess.run(['lrelease', tsfile, '-qm', '../translations/' + os.path.splitext(basename)[0] + '.qm'])
