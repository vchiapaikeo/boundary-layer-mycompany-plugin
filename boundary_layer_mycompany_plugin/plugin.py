import os
from boundary_layer.plugins import BasePlugin, PluginPriority
from boundary_layer_mycompany_plugin.schema import MyCompanyPluginConfigSchema


class MyCompanyPlugin(BasePlugin):
    name = 'mycompany'

    priority = PluginPriority.FINAL

    configs_path = os.path.join(os.path.dirname(__file__), 'config')

    config_schema_cls = MyCompanyPluginConfigSchema

    # Add additional property processors here
    property_preprocessors = []

    def insert_imports(self, config):
        pass

    def insert_before(self, config):
        pass

    def insert_operators(self, config):
        pass

    def insert_dag_args(self, config):
        pass

    def insert_default_task_args(self, config):
        pass
