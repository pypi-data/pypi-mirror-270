import traceback
from collections import OrderedDict
from kabaret.flow.object import _Manager, Object, _Relation
from .utils import get_extension_entry_points


class DynamicTreeManager(_Manager):
    '''
    This manager allows to add third-party relations (called dynamic
    relations) to its managed object.

    A dynamic relation is defined in a function (factory) taking the
    target parent object as a parameter, and returning the relation
    instance: `callable(object -> Object) -> _Relation`.

    Factories are grouped by extension and provided by another type
    of function called "installers". An installer takes the current
    session as an argument and returns a dict of factory lists:
        
        {
            <extension_name>: [relation_factory, ...],
            ...
        }

    To be available to the manager, installers must be identified in
    the `KABARET_FLOW_EXT_INSTALLERS` environment variable with the
    following syntax:
        
        `<module_qualified_name>:<installer_name>[;<module_qualified_name>:<installer_name>...]`
    '''
    _EXT_INSTALLERS = None

    def get_extension_installers(self):
        installers = []
        for entry_point in get_extension_entry_points(self.root().session()):
            installer = entry_point.load()
            installers.append(installer)
        
        return installers
    
    def __init__(self, object, parent, name, value_store):
        super(DynamicTreeManager, self).__init__(object, parent, name, value_store)
        self._ext_relations = OrderedDict()
        # Store only the names of base relations which are not overriden
        self._base_relation_indices = {r.name: i for i, r in enumerate(self.object._relations)}
        self._next_index = max([r.index for r in self.object._relations], default=-1) + 1
    
    def has_related(self, relation_name):
        return relation_name in [r.name for r in self.relations()]
    
    def get_relation(self, name):
        index = self._base_relation_indices.get(name, -1)
        if index < 0:
            if name not in self._ext_relations:
                raise AttributeError("Could not find relation '%s' under '%s'" %
                                    (name, self.oid()))
            
            r = self._ext_relations[name][0]
        else:
            r = self.object._relations[index]
        return r
    
    def relations(self):
        relations = (
              [self.object._relations[i] for i in sorted(self._base_relation_indices.values())]
            + [r for r, _ in self._ext_relations.values()]
        )
        return sorted(relations, key=lambda r: r.index)
    
    def on_object_init(self):
        self._register_dynamic_relations()
    
    def _register_dynamic_relations(self):
        '''
        From https://gitlab.com/dee909/somepipeline/-/blob/main/src/somepipeline/plugins/__init__.py#L208
        '''
        for installer in self.get_extension_installers():
            self._run_installer(installer)
        
        for name, (rel, priority) in self._ext_relations.items():
            # Check if a base relation exists and can be overriden
            if name in self._base_relation_indices:
                if priority < 0: # Negative weight disables override
                    continue
                else:
                    self._base_relation_indices.pop(name)
            
            related = rel.__get__(self.object)
            setattr(self.object, name, related)
    
    def _run_installer(self, installer):
        if installer is None:
            return
        
        try:
            extensions = installer(self.root().session())
        except Exception:
            self.root().session().log_error(
                f'FlowExtensions :: Could not execute installer {installer}:\n'
                f'{traceback.format_exc()}')
        else:
            for ext_name, factories in extensions.items():
                for factory in factories:
                    self._run_factory(factory, ext_name)
    
    def _run_factory(self, factory, extension_name):
        '''
        Evaluates the given relation factory, checks the returned relations
        and adds them to the list of dynamic relations of this manager.
        '''
        try:
            relations = factory(self.object)
        except Exception as err:
            self.root().session().log_error(
                f'FlowExtensions :: Failed to execute factory {factory} ({extension_name})'
                f' on object \'{self.oid()}\'\n'
                f'{traceback.format_exc()}')
        else:
            if relations is None:
                return
            elif not isinstance(relations, list):
                relations = [relations]

            for rel in relations:
                priority = 0
                if isinstance(rel, tuple):
                    rel, priority = rel
                    if not isinstance(priority, int):
                        priority = 0
                
                try:
                    self._register_dynamic_relation(rel, priority)
                except:
                    self.root().session().log_error(
                        f"FlowExtensions :: Failed to add relation to object '{self.oid()}' "
                        f"(factory <{extension_name}:{factory.__name__}>)\n"
                        f'{traceback.format_exc()}')
    
    def _register_dynamic_relation(self, relation, priority):
        '''
        Adds a relation as a class attribute to this manager's object
        class with the name `name`. This relation will be of type
        `relation_type` and relate an object of type `related_type`.
        '''
        # Check relation type and name
        if not isinstance(relation, _Relation):
            raise Exception('Invalid relation type %r (must be one of the %r subclasses)' % (
                relation.__class__, _Relation))
        elif relation.related_type is not None and not issubclass(relation.related_type, Object):
            raise Exception('Invalid related object type %r (must be %r or a subclass)' % (
                relation.related_type, Object))
        
        name = relation.name
        if not name:
            raise TypeError('Cannot create a dynamic relation without name.')
        elif name == 'oid':
            raise ValueError(
                'Cannot create a dynamic relation %r named "oid" (reserved name)' % (
                    relation))
        elif name == 'name':
            raise ValueError('Cannot create a dynamic relation %r named "name" (reserved name)' % (
                relation))

        if '.' in name:
            raise TypeError(
                f'Invalid dynamic relation name \'{name}\' (it must be a valid attribute name).')
        try:
            exec(name + '=None') in {}
        except Exception:
            raise TypeError(
                f'Invalid dynamic relation name \'{name}\' (it must be a valid attribute name).')
        
        rel = next((r for r in self.object._relations if r.name == name), None)

        # Raise if an attribute exists with the same name
        if rel is None and hasattr(self.object, name):
            raise AttributeError(
                f"An attribute named '{name}' already exists.")
        # Return if a base relation exists but override is disabled
        if rel is not None and priority < 0:
            self.root().session().log_warning(
                f"FlowExtensions :: base relation '{name}' ({rel}) was not overriden since "
                 "override has been disabled for the candidate relation.")
            return

        if not isinstance(relation.index, int):
            relation.index = self._next_index
            self._next_index += 1
        elif relation.index >= self._next_index:
            self._next_index = relation.index + 1

        # Override relation according to weight
        if name not in self._ext_relations or self._ext_relations[name][1] <= priority:
            self._ext_relations[name] = (relation, priority)


class DynamicTreeObject(Object):
    
    _MANAGER_TYPE = DynamicTreeManager
    _PROPAGATE_MANAGER_TYPE = False
