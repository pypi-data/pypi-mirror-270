import os
import traceback
import importlib


class EntryPoint:

    def __init__(self, installer_name, session):
        self._installer_name = installer_name
        self._session = session
    
    def load(self):
        '''
        From https://packaging.python.org/en/latest/specifications/entry-points/#data-model
        '''
        modname, qualname_sep, qualname = self._installer_name.partition(':')
        try:
            obj = importlib.import_module(modname)
        except ModuleNotFoundError:
            self._session.log_error(
                f'FlowExtensions: Error while loading installer {self._installer_name}:\n'
                f'{traceback.format_exc()}')
            return
        
        if qualname_sep:
            try:
                for attr in qualname.split('.'):
                    obj = getattr(obj, attr)
            except AttributeError:
                self._session.log_error(
                    f'FlowExtensions: Error while loading installer {self._installer_name}:\n'
                    f'{traceback.format_exc()}')
                return
        return obj


def get_extension_entry_points(session):
    entry_point_names = os.environ.get(
        'KABARET_FLOW_EXT_INSTALLERS')
    entry_points = []
    if entry_point_names is not None:
        for name in entry_point_names.split(';'):
            entry_points.append(EntryPoint(name, session))
    return entry_points
