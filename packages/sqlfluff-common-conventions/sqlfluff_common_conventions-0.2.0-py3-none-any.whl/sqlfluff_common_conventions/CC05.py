"""Implementation of Rule CC05."""

from typing import List, Optional

import regex

from sqlfluff.core.rules import BaseRule, LintResult, RuleContext
from sqlfluff.core.rules.crawlers import SegmentSeekerCrawler


class Rule_CC05(BaseRule):
    """Block a list of configurable strings from being used in identifiers.
    Think of this as the opposite of custom rule CC04 in this plugin: rather than
    whitelisting strings, it blacklists strings. Generally, you will only need
    one of the two; it is recommended to start with CC05 to quickly blacklist strings
    that one is certain they want to block early on, then switch to using CC04 to
    whitelist a set list of words after developing said list.

    This rule differs from the built-in rule CV09 in that it facilitates blocking of
    phrases or parts of words as well, collectively known as "strings". It also only
    applies to identifiers, as it makes little sense to block part of a keyword.

    This block list is case insensitive.

    **Example use cases**

    * We wish to enforce a naming convention where ```avg``` is used over ```average```
    in identifiers, e.g. ```avg_sales``` instead of ```average_sales```. We can
    add ```average``` to ```blocked_strings``` to cause a linting error to flag this.
    This use case would not be fulfilled with CV09.

    **Anti-pattern**

    If the ``blocked_strings`` config is set to ``deprecated`` then the
    following will flag:

    .. code-block:: sql

        SELECT * FROM deprecated_table WHERE 1 = 1;

    **Best practice**

    Do not used any blocked strings:

    .. code-block:: sql

        SELECT * FROM table WHERE 1 = 1;

    """

    groups = ("all", "convention")
    crawl_behaviour = SegmentSeekerCrawler({"identifier"})
    config_keywords = ["blocked_strings"]

    def _eval(self, context: RuleContext) -> Optional[LintResult]:
        # Config type hints
        self.blocked_strings: Optional[str]

        # Exit early if no block list set
        if not self.blocked_strings:
            return None

        # Get the ignore list configuration and cache it
        try:
            blocked_strings_list = self.blocked_strings_list
        except AttributeError:
            # First-time only, read the settings from configuration.
            # So we can cache them for next time for speed.
            blocked_strings_list = self._init_blocked_strings()

        blocked_strings_used = list(
            filter(lambda x: x in context.segment.raw_upper, blocked_strings_list)
        )

        if blocked_strings_used:
            return LintResult(
                anchor=context.segment,
                description=f"Use of blocked strings in '{context.segment.raw}'.",
            )

    def _init_blocked_strings(self) -> List[str]:
        """Called first time rule is evaluated to fetch & cache the blocked_strings."""
        blocked_strings_config = getattr(self, "blocked_strings")
        if blocked_strings_config:
            self.blocked_strings_list = self.split_comma_separated_string(
                blocked_strings_config.upper()
            )
        else:  # pragma: no cover
            # Shouldn't get here as we exit early if no block list
            self.blocked_strings_list = []

        return self.blocked_strings_list
