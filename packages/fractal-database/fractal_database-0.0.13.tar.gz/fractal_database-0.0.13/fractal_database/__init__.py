import importlib.metadata as metadata
from typing import List


def autodiscover_apps() -> List[str]:
    """
    Autodiscovers all installed django apps that
    specify a `fractal.database.app` plugin.
    """
    entry_points = metadata.entry_points()
    plugins = entry_points.select(group="fractal.database.app")
    apps = [plugin.value for plugin in plugins]
    apps.extend(["fractal_database_matrix", "fractal_database"])
    return apps
