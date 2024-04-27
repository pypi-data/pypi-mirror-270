from kabaret import flow


def create_child(parent):
    if parent.oid().endswith('/flow_extensions/all_relation_types'):
        label = flow.Label('<h3>Child</h3>')
        label.name = 'label_child'
        r = flow.Child(flow.Object)
        r.name = 'dynamic_child'
        return [label, r]

def create_param(parent):
    if parent.oid().endswith('/flow_extensions/all_relation_types'):
        label = flow.Label('<h3>Param</h3>')
        label.name = 'label_param'
        r = flow.Param('')
        r.name = 'dynamic_param'
        return [label, r]

def create_computed(parent):
    if parent.oid().endswith('/flow_extensions/all_relation_types'):
        label = flow.Label('<h3>Computed</h3>')
        label.name = 'label_computed'
        r = flow.Computed()
        r.name = 'dynamic_computed'
        return [label, r]

def create_parent(parent):
    if parent.oid().endswith('/flow_extensions/all_relation_types'):
        label = flow.Label('<h3>Parent</h3>')
        label.name = 'label_parent'
        r = flow.Parent()
        r.name = 'dynamic_parent'
        return [label, r]

def create_relative(parent):
    if parent.oid().endswith('/flow_extensions/all_relation_types'):
        label = flow.Label('<h3>Relative</h3>')
        label.name = 'label_relative'
        r = flow.Relative('../extendable_object/child_map')
        r.name = 'dynamic_relative'
        return [label, r]

def create_separator(parent):
    if parent.oid().endswith('/flow_extensions/all_relation_types'):
        label = flow.Label('<h3>Separator</h3>')
        label.name = 'label_separator'
        r = flow.Separator()
        r.name = 'dynamic_separator'
        return [label, r]

def create_label(parent):
    if parent.oid().endswith('/flow_extensions/all_relation_types'):
        r = flow.Label('<h3>Label</h3>')
        r.name = 'dynamic_label'
        return r

def create_connection(parent):
    if parent.oid().endswith('/flow_extensions/all_relation_types'):
        label = flow.Label('<h3>Connection</h3>')
        label.name = 'label_connection'
        r = flow.Connection(flow.Object)
        r.name = 'dynamic_connection'
        return [label, r]


def install_extensions(session):
    return {
        'unittest': [
            create_child,
            create_param,
            create_computed,
            create_parent,
            create_relative,
            create_separator,
            create_label,
            create_connection,
        ]
    }
