#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Command's module    
'''
import os
from subprocess import Popen, PIPE, STDOUT
# for run as main
if __name__ == "__main__":
    import sys
    sys.path.append(os.path.abspath('../..'))
import ponyguruma as onig
from ponyguruma.constants import OPTION_CAPTURE_GROUP
from prymatex.bundles.base import PMXBundleItem
from prymatex.bundles.utils import ensureShellScript, ensureEnvironment, makeExecutableTempFile, deleteFile

onig_compile = onig.Regexp.factory(flags = OPTION_CAPTURE_GROUP)

class PMXCommand(PMXBundleItem):
    path_patterns = ['Commands/*.tmCommand', 'Commands/*.plist']
    bundle_collection = 'commands'
    exit_codes = {
                  200: 'discard',
                  201: 'replaceSelectedText',
                  202: 'replaceDocument',
                  203: 'insertText',
                  204: 'insertAsSnippet',
                  205: 'showAsHTML',
                  206: 'showAsTooltip',
                  207: 'createNewDocument'
                  }
    def __init__(self, hash, name_space = "default", path = None):
        super(PMXCommand, self).__init__(hash, name_space, path)
        for key in [    'input', 'fallbackInput', 'standardInput', 'output', 'standardOutput',  #I/O
                        'command', 'winCommand', 'linuxCommand',                                #System based Command
                        'capturePattern', 'fileCaptureRegister',
                        'columnCaptureRegister', 'inputFormat', 'disableOutputAutoIndent',
                        'lineCaptureRegister', 'dontFollowNewOutput',
                        'beforeRunningCommand', 'autoScrollOutput', 'captureFormatString', 'beforeRunningScript' ]:
            value = hash.get(key, None)
            if value != None and key in [    'capturePattern' ]:
                value = onig_compile( value )
            setattr(self, key, value)

    @property
    def systemCommand(self):
        if self.winCommand != None and 'Window' in os.environ['OS']:
            return self.winCommand
        elif self.linuxCommand != None:
            return self.linuxCommand
        else:
            return self.command
    
    def getInputText(self, processor):
        def switch(input):
            if input == "none": return None, None
            return input, getattr(processor, input)
        input, value = switch(self.input)
        if value == None and self.fallbackInput != None:
            input, value = switch(self.fallbackInput)
        if value == None and self.standardInput != None:
            input, value = switch(self.standardInput)
        #return input, value
        return input, value

    def getOutputHandler(self, code):
        if self.output != 'showAsHTML' and code in self.exit_codes:
            return self.exit_codes[code]
        elif code != 0:
            return "commandError"
        else:
            return self.output
    
    def execute(self, processor):
        if hasattr(self, 'beforeRunningCommand') and self.beforeRunningCommand != None:
            value = getattr(processor, self.beforeRunningCommand)()
            if not value:
                return
        processor.startCommand(self)
        input_type, input_value = self.getInputText(processor)
        command = ensureShellScript(self.systemCommand)
        temp_file = makeExecutableTempFile(command)
        process = Popen([  temp_file], stdin=PIPE, stdout=PIPE, stderr=STDOUT, env = ensureEnvironment(processor.environment))
        
        if input_type != None:
            print input_type, input_value
            if input_value == None:
                input_value = processor.document
            process.stdin.write(unicode(input_value).encode("utf-8"))
        process.stdin.close()
        try:
            output_value = process.stdout.read()
        except IOError:
            pass
        process.stdout.close()
        output_type = process.wait()
        output_handler = self.getOutputHandler(output_type)
        # Remove old
        if input_type != None and output_handler in [ "insertText", "insertAsSnippet" ]:
            deleteMethod = getattr(processor, 'delete' + input_type.title(), None)
            if deleteMethod != None:
                deleteMethod()        

        args = [ output_value.decode('utf-8') ]
        function = getattr(processor, output_handler, None)
        
        if output_handler == "commandError":
            args.append(output_type)
            
        # Insert New
        function(*args)
        
        processor.endCommand(self)
        
        #Podria borrar este archivo cuando de borra el objeto
        #deleteFile(self.temp_command_file)

class PMXDragCommand(PMXCommand):
    path_patterns = ['DragCommands/*.tmCommand', 'DragCommands/*.plist']
    def __init__(self, hash, name_space = "default", path = None):
        super(PMXDragCommand, self).__init__(hash, name_space, path)
        for key in [    'draggedFileExtensions' ]:
            setattr(self, key, hash.get(key, None))

    def buildEnvironment(self, directory = "", name = ""):
        env = super(PMXDragCommand, self).buildEnvironment()
        # TM_DROPPED_FILE � relative path of the file dropped (relative to the document directory, which is also set as the current directory).
        env['TM_DROPPED_FILE'] = os.path.join(directory)
        #TM_DROPPED_FILEPATH � the absolute path of the file dropped.
        env['TM_DROPPED_FILEPATH'] = os.path.join(directory)
        #TM_MODIFIER_FLAGS � the modifier keys which were held down when the file got dropped.
        #This is a bitwise OR in the form: SHIFT|CONTROL|OPTION|COMMAND (in case all modifiers were down).
        env['TM_MODIFIER_FLAGS'] = directory
        return env
        
    def setBundle(self, bundle):
        super(PMXDragCommand, self).setBundle(bundle)
        bundle.DRAGS.append(self)