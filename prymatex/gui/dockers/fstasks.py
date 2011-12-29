from prymatex.gui.dockers.base import PMXBaseDock
from PyQt4 import QtGui, QtCore
import os
from prymatex.utils.i18n import ugettext as _
from prymatex.core.exceptions import PrymatexFileExistsException
from prymatex.gui.dialogs.newfromtemplate import PMXNewFromTemplateDialog

class PMXFileSystemTasks(PMXBaseDock):
    '''
    Groups FileSystem and Project actions, it's a facade of the PMXFileManager
    that displays dialogs and handle common exceptions.
    
    Slots Mixin
    '''
    
    @QtCore.pyqtSlot()
    def on_actionNewFolder_triggered(self):
        self.createDirectory()

    @QtCore.pyqtSlot()
    def on_actionNewFile_triggered(self):
        self.createFile()

    
    @QtCore.pyqtSlot()
    def on_actionDelete_triggered(self):
        self.deletePath(self.currentPath())
        
    
    @QtCore.pyqtSlot()
    def on_actionNewFromTemplate_triggered(self):
        path = self.currentPath()
        fileDirectory = self.application.fileManager.getDirectory(path)
        path = PMXNewFromTemplateDialog.newFileFromTemplate(fileDirectory = fileDirectory,  parent = self)

    
    def createDirectory(self, basePath = None):
        
        basePath = basePath or self.currentPath()
        while True:
            newDirName, accepted = QtGui.QInputDialog.getText(self, _("Create Directory"), 
                                                        _("Please specify the new directory name"), 
                                                        text = _("New Folder"))
            if accepted:
                absNewDirName = os.path.join(basePath, newDirName)
                try:
                    rslt = self.application.fileManager.createDirectory(absNewDirName)
                except PrymatexFileExistsException as e:
                    QtGui.QMessageBox.warning(self, _("Error creating directory"), 
                                              _("%s already exists") % newDirName)
                    continue
                # Permissions? Bad Disk? 
                except Exception as e:
                    # TODO: Show some info about the reason
                    QtGui.QMessageBox.warning(self, _("Error creating directory"), 
                                              _("An error occured while creating %s") % newDirName)
                    
                else:
                    print("Created", rslt)
                    break
            else:
                return
    
    def createFile(self, basePath = None):
        basePath = basePath or self.currentPath()
        while True:
            newFileName, accepted = QtGui.QInputDialog.getText(self, _("Create file"), 
                                                        _("Please specify the file name"), 
                                                        text = _("NewFile"))
            if accepted:
                absNewFileName = os.path.join(basePath, newFileName)
                try:
                    rslt = self.application.fileManager.createFile(absNewFileName)
                except PrymatexFileExistsException as e:
                    QtGui.QMessageBox.warning(self, _("Error creating file"), 
                                              _("%s already exists") % newFileName)
                    continue
                # Permissions? Bad Disk? 
                except Exception as e:
                    # TODO: Show some info about the reason
                    QtGui.QMessageBox.warning(self, _("Error creating file"), 
                                              _("An error occured while creating %s") % absNewFileName)
                    
                else:
                    print("Created", rslt)
                    break
            else:
                return
    
    def createFileFromTemplate(self):
        pass
    
    def deletePath(self, path):
        basePath, pathTail = os.path.split(path)
        result = QtGui.QMessageBox.question(self, _("Are you sure?"), 
                                        _("Are you sure you want to delete %s<br>"
                                          "This action can not be undone.") % pathTail,
                                            buttons = QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel,
                                            defaultButton = QtGui.QMessageBox.Cancel)
        if result == QtGui.QMessageBox.Ok:
            self.application.fileManager.deletePath(path)