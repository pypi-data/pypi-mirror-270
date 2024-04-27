from kabaret import flow
from kabaret.flow_extensions.flow import DynamicTreeManager
from dev_studio.flow.unittest_project import UnittestProject


class CustomMapItem(flow.Object):
    pass


class CustomMap(flow.DynamicMap):
    @classmethod
    def mapped_type(cls):
        return CustomMapItem

    def mapped_names(self, page_num=0, page_size=None):
        return ['item_000', 'item_001', 'item_002']


class ExtendableObject(flow.Object):
    _MANAGER_TYPE = DynamicTreeManager

    child_object = flow.Child(flow.Object)
    child_map    = flow.Child(CustomMap)


class ExtendableObjectAndChildren(ExtendableObject):
    _PROPAGATE_MANAGER_TYPE = True


class DynamicRelationTypes(flow.Object):
    _MANAGER_TYPE = DynamicTreeManager


class FlowExtensionsGroup(flow.Object):    
    extendable_object = flow.Child(ExtendableObject)
    extendable_object_and_children = flow.Child(ExtendableObjectAndChildren)
    all_relation_types = flow.Child(DynamicRelationTypes)


class FlowExtensionsProject(UnittestProject):

    flow_extensions = flow.Child(FlowExtensionsGroup)
