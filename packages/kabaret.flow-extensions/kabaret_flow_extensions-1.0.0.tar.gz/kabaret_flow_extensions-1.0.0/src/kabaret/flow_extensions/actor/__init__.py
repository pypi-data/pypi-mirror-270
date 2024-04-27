import os
import re
import pkgutil
import importlib
import traceback

from kabaret.app._actor import Actor, Cmd, Cmds
from kabaret.flow.exceptions import MissingChildError, MissingRelationError


class FlowExtensionsCmds(Cmds):
    pass


@FlowExtensionsCmds.cmd
class List_Enabled_Extensions(Cmd):
    """
    Returns a list of all the extensions enabled for the given oid
    as a dict mapping an extension's list of relations to its name:
        {
            extension_name:
            [
                (
                    relation_name,
                    relation
                ),
                ...
            ]
        }
    """

    def _decode(self, oid):
        self._oid = oid

    def _execute(self):
        return self.actor().get_enabled_extensions(self._oid)


class FlowExtensions(Actor):
    '''
    This actor manages a set of extensions. 

    Each extension has a name and a list of relations which
    can be enabled depending on the oid of a given object.
    '''
    
    def __init__(self, session):
        super(FlowExtensions, self).__init__(session)
        self._extensions = None
        self._init_extensions()
    
    def _create_cmds(self):
        return FlowExtensionsCmds(self)
    
    def get_enabled_extensions(self, oid):
        extensions = {}

        def validate_object(validate_func, oid, ext_name, rel_name):
            try:
                o = self.session().get_actor('Flow').get_object(oid)
            except (MissingChildError, MissingRelationError):
                return False
            
            try:
                return validate_func is None or validate_func(o)
            except:
                self.session().log_error(
                     'FlowExtensions: invalid validation function for '
                    f'extension {ext_name}:{rel_name} (see traceback below)')
                self.session().log_error(traceback.format_exc())
                return False

        for ext_name, relations in self._extensions.items():
            enabled_relations = []

            for validate_func, rel_name, relation in relations:
                if validate_object(validate_func, oid, ext_name, rel_name):
                    enabled_relations.append((rel_name, relation))
            
            extensions[ext_name] = enabled_relations
        
        return extensions
    
    def _init_extensions(self):
        ext_modules = os.environ.get('KABARET_FLOW_EXT_MODULES', 'kabaret.flow_extensions_root')
        ext_modules = ext_modules.split(os.pathsep)
        self._extensions = {}

        for m_name in ext_modules:
            self._extensions.update(self._get_extensions(m_name))
    
    def _get_extensions(self, module_name):
        
        def import_module(module_name):
            m = None
            try:
                m = importlib.import_module(module_name)
            except ModuleNotFoundError as err:
                self.session().log_warning(f'FlowExtensions: Could not import module {module_name}')
                self.session().log_warning(f'FlowExtensions: {err}')
            return m
        
        def get_module_extensions(module):
            if module is None:
                return {}
            
            exts = {}
            try:
                module.get_flow_extensions
            except AttributeError:
                pass
            else:
                exts = module.get_flow_extensions()

                if not isinstance(exts, dict):
                    self.session().log_error(
                        f'FlowExtensions: {module}.get_flow_extensions() has invalid return type'
                    )
                    exts = {}
                else:
                    self.session().log_info(
                        f'FlowExtensions: load extensions from \'{module.__name__}\' ({module.__file__})'
                    )
            return exts

        m = import_module(module_name)
        extensions = get_module_extensions(m)

        if hasattr(m, '__path__'):
            for sm_info in pkgutil.iter_modules(m.__path__):
                sm = import_module(module_name+'.'+sm_info.name)
                extensions.update(get_module_extensions(sm))

        return extensions
