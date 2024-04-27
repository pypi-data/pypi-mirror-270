import sys

from kabaret.app.ui.gui import KabaretStandaloneGUISession

from dev_studio.icons import gui as _  # register our icons.gui resourses
from dev_studio.icons import flow as _  # register our icons.flow resourses
from dev_studio.gui import MyStudioGUISession

# To test the custom home:
CUSTOM_HOME = False
if CUSTOM_HOME:
    from kabaret.app.actors.flow import Flow
    from dev_studio.flow.custom_home import MyHomeRoot

# In case you have kabaret.script_view installed:
SCRIPT_VIEW = True
try:
    from kabaret.script_view import ScriptView
except ImportError:
    SCRIPT_VIEW = False


class MyExtensionsGUISession(MyStudioGUISession):

    def register_view_types(self):
        KabaretStandaloneGUISession.register_view_types(self)

        if SCRIPT_VIEW:
            type_name = self.register_view_type(ScriptView)
            self.add_view(type_name, hidden=True)

    def _create_actors(self):
        if CUSTOM_HOME:
            Flow(self, CustomHomeRootType=MyHomeRoot)
        else:
            return super(MyStudioGUISession, self)._create_actors()


if __name__ == '__main__':
    argv = sys.argv[1:]  # get rid of first args which is script filename
    (
        session_name,
        host, port, cluster_name,
        db_index, password, debug,
        remaining_args
    ) = MyExtensionsGUISession.parse_command_line_args(argv)
    session = MyExtensionsGUISession(session_name=session_name)
    session.cmds.Cluster.connect(host, port, cluster_name, db_index, password)

    session.start()
    session.close()
