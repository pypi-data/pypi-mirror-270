"""Implementation of Rule CC04."""

import re
from typing import List, Set

from sqlfluff.core.rules import BaseRule, LintResult, RuleContext
from sqlfluff.core.rules.crawlers import SegmentSeekerCrawler

# TODO: Ignore project and dataset names, i.e. given abc.def.ghi, only look at ghi.
# This is harder to implement, though, so this rule currently checks all identifiers.


class Rule_CC04(BaseRule):
    """Only allow a list of configurable strings to be used in identifiers.
    Think of this as the opposite of custom rule CC05 in this plugin: rather than
    blacklisting strings (words, phrases, and parts of words), it whitelists strings.
    Generally, you will only need one of the two; it is recommended to start with CC05
    to quickly blacklist strings that one is certain they want to block early on, then
    switch to using CC04 to whitelist a set list of words after developing said list.

    This whitelist is case insensitive.

    **Anti-pattern**

    If the ``allowed_strings`` config is set to ``user,profile,id,_`` and
    ``allow_whitespace`` is set to False, then the following will flag:

    .. code-block:: sql

        select * from profile_of_user;
        select * from `user id`;

    **Best practice**

    Only use allowed strings:

    .. code-block:: sql

        select * from user_profile;
        select * from user_id;

    """

    groups = ("all", "convention")

    crawl_behaviour = SegmentSeekerCrawler({"identifier"})
    config_keywords = ["allowed_strings", "allow_whitespace"]
    is_fix_compatible = False

    def _eval(self, context: RuleContext):
        """Find rule violations and provide fixes."""

        self.allowed_strings: Optional[str]
        self.allow_whitespace: bool

        # Exit early if allowed_strings is not set
        if not self.allowed_strings:
            return None

        # Get the allowed list configuration and cache it
        try:
            allowed_strings_set = self.allowed_strings_set
        except AttributeError:
            # First-time only, read the settings from configuration.
            # So we can cache them for next time for speed.
            allowed_strings_set = set(self._init_allowed_strings())

        # Account for presence of backticks in e.g. `proj-name.dataset.table`.
        identifier = context.segment.raw.replace("`", "")

        allowed_strings_regex = "|".join(allowed_strings_set)
        if self.allow_whitespace:
            allowed_strings_regex += "| "

        match = re.findall(
            rf"^(?:{allowed_strings_regex}|\.)+$",  # . allowed because of e.g. `proj-name.dataset.table`.
            identifier,
            re.IGNORECASE,
        )

        if not match:
            return LintResult(
                anchor=context.segment,
                description=f"Use of unallowed strings in '{identifier}'.",
            )

    def _init_allowed_strings(self) -> List[str]:
        """Called first time rule is evaluated to fetch & cache the allowed_strings."""
        allowed_strings = getattr(self, "allowed_strings")
        if allowed_strings:
            self.allowed_strings_list = self.split_comma_separated_string(
                allowed_strings.upper()
            )
        else:  # pragma: no cover
            # Shouldn't get here as we exit early if no allow list
            self.allowed_strings_list = []

        return self.allowed_strings_list
