# kabaret.flow_extensions

Flow extensions is a Kabaret extension which allows to extend flow objects with standalone relations (i.e. defined outside of the flow object classes). These relations are named *dynamic relations*.

### Dependencies

This module relies on versions `2.3.0` and later of Kabaret, which provide the feature to override the object manager type needed to enable extensions on objects.

## Enabling extensions

The ability of an object to accept extensions relies on its manager, which must be of type `DynamicTreeManager`. We can then control extensions using the mecanism provided in Kabaret to override the object manager type (`Object._MANAGER_TYPE`) and specify whether it must be used in the object sub-tree (`Object._PROPAGATE_MANAGER_TYPE`).

To enable extensions on an object, simply set the manager type of its class to `DynamicTreeManager`.

```python
from kabaret.flow import Object
from kabaret.flow_extensions.flow import DynamicTreeManager

class MyExtendableObject(Object):
    _MANAGER_TYPE = DynamicTreeManager
```

In the above example, only `MyExtendableObject` instances can be extended. To enable extensions for all children existing in the sub-trees of these instances as well, set the value of the class attribute `_PROPAGATE_MANAGER_TYPE` to `True`.

```python
class MyExtendableProject(Object):
    _MANAGER_TYPE = DynamicTreeManager
    _PROPAGATE_MANAGER_TYPE = True
```

In case the use of extensions must be disabled on an object which exists in a part of the flow where extensions are enabled by default, one can reset its `_MANAGER_TYPE` to the default type `_Manager`.

```python
class MyRegularObject(Object):
    _MANAGER_TYPE = _Manager

class MyExtendableObject(Object):
    _MANAGER_TYPE = DynamicTreeManager
    _PROPAGATE_MANAGER_TYPE = True

    regular_object = flow.Child(MyRegularObject)
    ...
```
In the above example, all but the `MyRegularObject` child under the `MyExtendableObject` will be able to register extensions.

## Definition

### Factories

Dynamic relations must be defined in *factories*. A factory is a function which takes an `Object` instance as an argument representing an extendable object, and returns either a single relation (`_Relation` instance), a list of relations, or `None` if no relation has to be registered by the target object.

```python
def relation_factory(parent -> Object) -> [None, _Relation, list]: 
    ...
```

Declaring a dynamic relation is done similarly as for a regular relation, except that its name must be set explicitly.

```python
def create_dynamic_param(parent): 
    if parent.oid() == '/my/target/oid':
        relation = flow.Param('').ui(label='My dynamic param')
        relation.name = 'my_dynamic_param'
        return relation
```

### Ordering

Optionally, one might set the relation's index to control its position among the existing ones. The default index of a dynamic relation is `0`, which makes it appear first in the UI. When set to `None`, the index is automatically computed so that the relation appears last.

```python
relation.index = 5
```

### Overrides

When multiple relation candidates have the same name, only the one with the highest priority weight is retained. This weight is optional and can be provided by the factory:

```python
def create_relation(parent):
    ...
    return relation, 10
```

The default value of a relation weight is `0`. When not provided, only the last found relation candidate will be available.

It is also possible to provide a negative weight to prevent a dynamic relation from overriding an existing base relation.

### Installers

Installers are functions called by the manager of an object to retrieve its dynamic relations. An installer takes the current session as an argument, and returns a dictionary which maps a list of relation factories with the name of the extension.

Example:

```python
def install_extensions(session): 
    if session.session_uid().split(':', 1)[0] = 'my_user_name':
        return {
            "my_extension": [
                create_dynamic_param,
                ...
            ],
            ...
        }
```

In order for installers to be accessible to the manager, they must be provided in the environment variable `KABARET_FLOW_EXT_INSTALLERS` following the pattern: `<module_qualified_name>:<installer_name>[;<module_qualified_name>:<installer_name>...]`.

## Known issues

Instanciation of objects referenced by native relations obeys to the principle of *lazy evaluation*: objects are not instanciated until the relations are accessed.
The extension system currently drops this mecanism, in two points:
- child objects referenced by dynamic relations are instanciated as soon as their parent is instanciated.
- child objects themselves are set as attributes of their parent (instead of the generating relations).

The issues listed below stem from this change of behaviour. We propose a workaround for each whenever possible.

- **Infinite extension branch.** Given an extendable flow object, all objects in its sub-tree, including children generated by dynamic relations, will also accept extensions unless their manager type is set back to Kabaret's default manager type `_Manager`. It means that as long as factories return relations, an extension object can itself registers dynamic relations, leading to an infinite creation of dynamic relations.
  
  Workaround: explicitly set the manager type of the dynamic relation's related types to `_Manager`.

  ```python
  class MyExtensionObject(flow.Object):
      _MANAGER_TYPE = _Manager # prevent extension from registering extensions itself
  ```

- **Invalid calls to `ProjectRoot.project()`.** When the `parent` object is the project instance, any call to `Object.root().project()` currently raises an `AttributeError`. This is because the project is not instanciated yet at the time the factory is called, hence it is not available as an attribute of the `ProjectRoot` instance.

  Workarounds:
  - get the project instance (from an object): use an explicit `Parent` relation pointing to the project
  - check if the `parent` extension target is the project instance (in a factory): exploit the fact that the project *oid* equals to its name preceded by `/`.
  ```python
  if parent.oid() == '/'+parent.name():
      ...
  ```

As a consequence of the second point, nothing prevents from overwriting a child object since it is a regular Python attribute.