#!/usr/bin/env python
#-*- encoding: utf-8 -*-
import os, plistlib
from copy import copy

def get_prymatex_base_path():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

def get_prymatex_user_path():
    path = os.path.join(os.path.expanduser("~"), ".prymatex")
    if not os.path.exists(path):
        os.makedirs(path)
    return path

PMX_BASE_PATH = get_prymatex_base_path()
PMX_USER_PATH = get_prymatex_user_path()
PMX_SETTINGS_FILE = os.path.join(PMX_USER_PATH , "settings.plist")

class SettingsNode(object):
    def __init__(self, hash = {}):
        self.__dict__['__wrapped_values'] = dict()
        self.__dict__['__wrapped_defaults'] = dict()
        self.__dict__['__listeners'] = []
        for key, value in hash.iteritems():
            setattr(self, key, value)
    
    def __setattr__(self, name, value):
        if isinstance(value, dict) and value.has_key('type') and value['type'] == "SettingsNode":
            value = SettingsNode(value)
        self.__dict__['__wrapped_values'][name] = value
        for listener in self.__dict__['__listeners']:
            setattr(listener, name, value)
    
    def __getattr__(self, name, default = None): 
        try:
            return self.get_value_for(name)
        except KeyError:
            if default == None:
                setattr(self, name, SettingsNode())
                return self.__dict__['__wrapped_values'][name]
        return default
    
    def __getitem__(self, name):
        return self.__dict__['__wrapped_values'][name]
    
    def __setitem__(self, name, value):
        self.__dict__['__wrapped_defaults'][name] = value
    
    def get_value_for(self, name):
        if self.__dict__['__wrapped_values'].has_key(name):
            return self.__dict__['__wrapped_values'][name]
        elif self.__dict__['__wrapped_defaults'].has_key(name):
            return self.__dict__['__wrapped_defaults'][name]
        raise KeyError()
    
    def add_listener(self, listener):
        self.__dict__['__listeners'].append(listener)
    
    def configure(self, listener):
        sets = copy(self.__dict__['__wrapped_defaults'])
        sets.update(self.__dict__['__wrapped_values'])
        for key, value in sets.iteritems():
            setattr(listener, key, value)
    
    def to_python(self):
        ret = {'type': self.__class__.__name__}
        for k, v in self.__dict__['__wrapped_values'].iteritems():
            if hasattr(v, 'to_python'):
                ret[k] = v.to_python()
            else:
                ret[k] = v
        return ret
    
class Settings(SettingsNode):
    '''
    Configuración gerarquica basada en diccionarios.
    '''
    PMX_BUNDLES_PATH = os.path.join(PMX_BASE_PATH, 'share', 'Bundles')
    PMX_THEMES_PATH = os.path.join(PMX_BASE_PATH, 'share', 'Themes')
    PMX_SUPPORT_PATH = os.path.join(PMX_BASE_PATH, 'share', 'Support')
    
    def __init__(self, parent = None, **defaults):
        if os.path.exists(PMX_SETTINGS_FILE):
            wrapped_dict = plistlib.readPlist(PMX_SETTINGS_FILE)
        else:
            wrapped_dict = {}
        super(Settings, self).__init__(wrapped_dict)
        
    def save(self):
        obj = self.to_python()
        plistlib.writePlist(obj, PMX_SETTINGS_FILE)

settings = Settings()

class Setting(object):
    def __init__(self, default = None, fset = None):
        self.__value = None
        self.__default = default
        self.__fset = fset
    
    def get_value(self):
        return self.__value or self.__default
    
    def set_value(self, value):
        self.__value = value
    
    value = property(get_value, set_value)
    
    def contribute_to_class(self, cls, name):
        self.name = name
        try:
            self.__value = cls._meta.settings[self.name]
        except KeyError:
            cls._meta.settings[self.name] = self.__default
        
        if self.__fset == None:
            #try form the class
            self.__fset = getattr(cls, "set%s" % self.name.title(), None)
        setattr(cls, self.name, self)
        
    def __get__(self, instance, instance_type = None):
        if instance != None:
            return self.value
    
    def __set__(self, instance, value):
        if instance != None:
            self.__value = value
        if self.__fset != None:
            self.__fset(instance, self.__value)