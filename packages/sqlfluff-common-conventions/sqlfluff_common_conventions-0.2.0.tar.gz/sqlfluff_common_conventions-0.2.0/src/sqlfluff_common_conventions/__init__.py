import os
from typing import List, Type

from sqlfluff.core.config import ConfigLoader
from sqlfluff.core.plugin import hookimpl
from sqlfluff.core.rules import BaseRule


@hookimpl
def get_rules() -> List[Type[BaseRule]]:
    """Get plugin rules."""
    from sqlfluff_common_conventions.CC01 import Rule_CC01
    from sqlfluff_common_conventions.CC02 import Rule_CC02
    from sqlfluff_common_conventions.CC03 import Rule_CC03
    from sqlfluff_common_conventions.CC04 import Rule_CC04
    from sqlfluff_common_conventions.CC05 import Rule_CC05

    return [Rule_CC01, Rule_CC02, Rule_CC03, Rule_CC04, Rule_CC05]


@hookimpl
def load_default_config() -> dict:
    """Loads the default configuration for the plugin."""
    return ConfigLoader.get_global().load_config_file(
        file_dir=os.path.dirname(__file__),
        file_name="plugin_default_config.cfg",
    )


@hookimpl
def get_configs_info() -> dict:
    """Get rule config validations and descriptions."""
    return {
        "naming_case": {
            "validation": ["snake", "dromedary", "pascal"],
            "definition": "What is the naming case?",
        },
        "allowed_strings": {"definition": "A list of strings to allow."},
        "allow_whitespace": {
            "validation": [True, False],
            "definition": "Should whitespace be allowed?",
        },
        "blocked_strings": {"definition": "A list of strings to block."},
    }
