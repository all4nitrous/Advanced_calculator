import importlib
import pkgutil

def load_plugins():
    plugins = {}
    for _, plugin_name, _ in pkgutil.iter_modules(__path__):
        module = importlib.import_module(f"app.plugins.{plugin_name}")
        if hasattr(module, "execute"):
            plugins[plugin_name] = module.execute
    return plugins
