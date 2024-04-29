"""Implementation of Rule CC04."""

import re
from typing import List, Set

from sqlfluff.core.rules import BaseRule, LintResult, RuleContext
from sqlfluff.core.rules.crawlers import SegmentSeekerCrawler

# TODO: Ignore project and dataset names, i.e. given abc.def.ghi, only look at ghi.
# This is harder to implement, though, so this rule currently checks all identifiers.


class Rule_CC04(BaseRule):
    """Only allows a list of configurable words to be used in identifiers.
    Think of this as the opposite of the build-in rule CV09: rather than
    blacklisting words, it whitelists words.

    This whitelist is case insensitive.

    **Anti-pattern**

    If the ``allowed_words`` config is set to ``user,profile,id,_`` and
    ``allow_whitespace`` is set to False, then the following will flag:

    .. code-block:: sql

        select * from profile_of_user;
        select * from `user id`;

    **Best practice**

    Only use allowed words:

    .. code-block:: sql

        select * from user_profile;
        select * from user_id;

    """

    groups = ("all",)

    crawl_behaviour = SegmentSeekerCrawler({"identifier"})
    config_keywords = ["allowed_words", "allow_whitespace"]
    is_fix_compatible = False

    def _eval(self, context: RuleContext):
        """Find rule violations and provide fixes."""

        self.allowed_words: Optional[str]
        self.allow_whitespace: bool

        # Exit early if allowed_words is not set
        if not self.allowed_words:
            return None

        # Get the allowed list configuration and cache it
        try:
            allowed_words_set = self.allowed_words_set
        except AttributeError:
            # First-time only, read the settings from configuration.
            # So we can cache them for next time for speed.
            allowed_words_set = set(self._init_allowed_words())

        # Account for presence of backticks in e.g. `proj-name.dataset.table`.
        identifier = context.segment.raw.replace("`", "")

        allowed_words_regex = "|".join(allowed_words_set)
        if self.allow_whitespace:
            allowed_words_regex += "| "

        match = re.findall(
            rf"^(?:{allowed_words_regex}|\.)+$",  # . allowed because of e.g. `proj-name.dataset.table`.
            identifier,
            re.IGNORECASE,
        )

        if not match:
            return LintResult(
                anchor=context.segment,
                description=f"Use of unallowed words in '{identifier}'.",
            )

    def _init_allowed_words(self) -> List[str]:
        """Called first time rule is evaluated to fetch & cache the allowed_words."""
        allowed_words_config = getattr(self, "allowed_words")
        if allowed_words_config:
            self.allowed_words_list = self.split_comma_separated_string(
                allowed_words_config.upper()
            )
        else:  # pragma: no cover
            # Shouldn't get here as we exit early if no allow list
            self.allowed_words_list = []

        return self.allowed_words_list
