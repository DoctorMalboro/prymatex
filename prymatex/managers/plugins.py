#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
from glob import glob

try:
    import json
except ImportError:
    import simplejson as json

from prymatex.qt import QtGui, QtCore

from prymatex import resources
from prymatex.utils import osextra
from prymatex.core import PMXBaseComponent
from prymatex.utils.importlib import import_module, import_from_directory

PLUGIN_EXTENSION = 'pmxplugin'
PLUGIN_DESCRIPTOR_FILE = 'info.json'

class ResourceProvider():
    def __init__(self, resources):
        self.resources = resources

    def getImage(self, index, default = None):
        if index in self.resources:
            return QtGui.QPixmap(self.resources[index])
        return resources.getImage(index)
        
    def getIcon(self, index, default = None):
        if index in self.resources:
            return QtGui.QIcon(self.resources[index])
        return resources.getIcon(index)

class PluginDescriptor(object):
    def __init__(self, entry):
        self.__entry = entry
    
    def __getitem__(self, name):
        if name in self.__entry:
            return self.__entry[name]
        raise KeyError(name)
    
    def __getattr__(self, name):
        if name in self.__entry:
            return self.__entry[name]
        raise AttributeError(name)
        
    def getImage(self, key):
        return self.__entry["resources"].getImage(key)

    def getIcon(self, key):
        return self.__entry["resources"].getIcon(key)
        
class PluginManager(QtCore.QObject, PMXBaseComponent):
    
    #=========================================================
    # Settings
    #=========================================================
    SETTINGS_GROUP = 'PluginManager'
    
    def __init__(self, application):
        self.application = application
        self.directories = []
        
        self.currentPluginDescriptor = None
        self.modules = {}
        
        self.editors = []
        self.dockers = []
        self.statusBars = []
        self.keyHelpers = {}
        self.addons = {}
        self.instances = {}
    
    def addPluginDirectory(self, directory):
        self.directories.append(directory)

    #==================================================
    # Cargando clases
    #==================================================
    def registerEditor(self, editorClass):
        self.application.populateComponent(editorClass)
        editorClass.plugin = self.currentPluginDescriptor
        self.editors.append(editorClass)
 
    def registerDocker(self, dockerClass):
        self.application.populateComponent(dockerClass)
        dockerClass.plugin = self.currentPluginDescriptor
        self.dockers.append(dockerClass)
        
    def registerStatusBar(self, statusBarClass):
        self.application.populateComponent(statusBarClass)
        statusBarClass.plugin = self.currentPluginDescriptor
        self.statusBars.append(statusBarClass)
    
    def registerKeyHelper(self, widgetClass, helperClass):
        self.application.extendComponent(helperClass)
        helperClass.plugin = self.currentPluginDescriptor
        keyHelperClasses = self.keyHelpers.setdefault(widgetClass, [])
        keyHelperClasses.append(helperClass)
    
    def registerAddon(self, widgetClass, addonClass):
        self.application.populateComponent(addonClass)
        addonClass.plugin = self.currentPluginDescriptor
        addonClasses = self.addons.setdefault(widgetClass, [])
        addonClasses.append(addonClass)
           
    #==================================================
    # Creando instancias
    #==================================================     
    def createWidgetInstance(self, widgetClass, mainWindow):
        instance = widgetClass(mainWindow)
        
        for addonClass in self.addons.get(widgetClass, []):
            addon = addonClass(instance)
            instance.addAddon(addon)
        
        for keyHelperClass in self.keyHelpers.get(widgetClass, []):
            keyHelper = keyHelperClass(instance)
            instance.addKeyHelper(keyHelper)
            
        self.application.profile.configure(instance)
        instance.initialize(mainWindow)
        
        instances = self.instances.setdefault(widgetClass, [])
        instances.append(instance)
        return instance
    
    def createCustomActions(self, mainWindow):
        for editorClass in self.editors:
            addonClasses = self.addons.get(editorClass, [])
            menus = editorClass.contributeToMainMenu(addonClasses)
            if menus is not None:
                customEditorActions = []
                for name, settings in menus.iteritems():
                    actions = mainWindow.contributeToMainMenu(name, settings)
                    customEditorActions.extend(actions)
            mainWindow.registerEditorClassActions(editorClass, customEditorActions)
        
        for dockClass in self.dockers:
            addonClasses = self.addons.get(dockClass, [])
            menus = dockClass.contributeToMainMenu(addonClasses)
            if menus is not None:
                customDockActions = []
                for name, settings in menus.iteritems():
                    actions = mainWindow.contributeToMainMenu(name, settings)
                    customDockActions.extend(actions)
            mainWindow.registerDockClassActions(dockClass, customDockActions)
        
        for statusClass in self.statusBars:
            addonClasses = self.addons.get(statusClass, [])
            menus = statusClass.contributeToMainMenu(addonClasses)
            if menus is not None:
                customStatusActions = []
                for name, settings in menus.iteritems():
                    actions = mainWindow.contributeToMainMenu(name, settings)
                    customStatusActions.extend(actions)
            mainWindow.registerStatusClassActions(statusClass, customStatusActions)
            
    def populateMainWindow(self, mainWindow):
        self.createCustomActions(mainWindow)
            
        mainWindow.setDockOptions(QtGui.QMainWindow.AllowTabbedDocks | QtGui.QMainWindow.AllowNestedDocks | QtGui.QMainWindow.AnimatedDocks)
        
        for dockClass in self.dockers:
            dock = self.createWidgetInstance(dockClass, mainWindow)
            mainWindow.addDock(dock, dock.PREFERED_AREA)

        for statusBarClass in self.statusBars:
            status = self.createWidgetInstance(statusBarClass, mainWindow)
            mainWindow.addStatusBar(status)
    
    #==================================================
    # Handle editor classes
    #==================================================
    def findEditorClassForFile(self, filePath):
        mimetype = self.application.fileManager.mimeType(filePath)
        for Klass in self.editors:
            if Klass.acceptFile(filePath, mimetype):
                return Klass
    
    def defaultEditor(self):
        return self.editors[0]

    #==================================================
    # Load plugins
    #==================================================
    def beginRegisterPlugin(self, pluginId, pluginEntry):
        self.modules[pluginId] = pluginEntry
        self.currentPluginDescriptor = PluginDescriptor(pluginEntry)
        
    def endRegisterPlugin(self, success):
        if not success:
            del self.modules[self.currentPluginDescriptor["id"]]
        self.currentPluginDescriptor = None
        
    def loadResources(self, pluginDirectory, pluginEntry):
        if "resources" in pluginEntry:
            resourcesDirectory = os.path.join(pluginDirectory, pluginEntry["resources"])
            res = resources.loadResources(resourcesDirectory)
            pluginEntry["resources"] = ResourceProvider(res)
        else:
            # Global resources
            pluginEntry["resources"] = resources
        
    def loadPlugin(self, pluginEntry):
        pluginId = pluginEntry.get("id")
        packageName = pluginEntry.get("package")
        registerFunction = pluginEntry.get("register", "registerPlugin")
        pluginDirectory = pluginEntry.get("path")    
        self.loadResources(pluginDirectory, pluginEntry)
        self.beginRegisterPlugin(pluginId, pluginEntry)
        try:
            pluginEntry["module"] = import_from_directory(pluginDirectory, packageName)
            registerPluginFunction = getattr(pluginEntry["module"], registerFunction)
            registerPluginFunction(self)
            self.endRegisterPlugin(True)
        except (ImportError, AttributeError), reason:
            import traceback
            traceback.print_exc()
            self.endRegisterPlugin(False)
            raise reason
    
    def loadCoreModule(self, moduleName, pluginId):
        pluginEntry = {"id": pluginId,
                       "resources": resources}
        self.beginRegisterPlugin(pluginId, pluginEntry)
        try:
            pluginEntry["module"] = import_module(moduleName)
            registerPluginFunction = getattr(pluginEntry["module"], "registerPlugin")
            registerPluginFunction(self)
            self.endRegisterPlugin(True)
        except (ImportError, AttributeError), reason:
            import traceback
            traceback.print_exc()
            self.endRegisterPlugin(False)
            raise reason
    
    def hasDependenciesResolved(self, pluginEntry):
        return all(map(lambda dep: dep in self.modules, pluginEntry.get("depends", [])))
    
    def loadPlugins(self):
        self.loadCoreModule('prymatex.gui.codeeditor', 'org.prymatex.codeeditor')
        self.loadCoreModule('prymatex.gui.dockers', 'org.prymatex.dockers')
        loadLaterEntries = []
        for directory in self.directories:
            if not os.path.isdir(directory):
                continue
            for pluginPath in glob(os.path.join(directory, '*.%s' % PLUGIN_EXTENSION)):
                pluginDescriptorPath = os.path.join(pluginPath, PLUGIN_DESCRIPTOR_FILE)
                if os.path.isdir(pluginPath) and os.path.isfile(pluginDescriptorPath):
                    descriptorFile = open(pluginDescriptorPath, 'r')
                    pluginEntry = json.load(descriptorFile)
                    descriptorFile.close()
                    pluginEntry["path"] = pluginPath
                    if self.hasDependenciesResolved(pluginEntry):
                        self.loadPlugin(pluginEntry)
                    else:
                        loadLaterEntries.append(pluginEntry)
        #Cargar las que quedaron bloqueadas por dependencias hasta consumirlas
        # dependencias circulares? son ridiculas pero por lo menos detectarlas
        unsolvedCount = len(loadLaterEntries)
        while True:
            loadLater = []
            for pluginEntry in loadLaterEntries:
                if self.hasDependenciesResolved(pluginEntry):
                    self.loadPlugin(pluginEntry)
                else:
                    loadLater.append(pluginEntry)
            if not loadLater or unsolvedCount == len(loadLater):
                break
            else:
                loadLaterEntries = loadLater
                unsolvedCount = len(loadLaterEntries)
        #Si me quedan plugins tendira que avisar o mostrar algo es que no se cumplieron todas las dependencias