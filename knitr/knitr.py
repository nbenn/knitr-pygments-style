# -*- coding: utf-8 -*-
"""
    pygments.styles.knitr
    ~~~~~~~~~~~~~~~~~~~

    A highlighting style for Pygments, inspired by knitr.

    :copyright: Copyright 2006-2014 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic, Whitespace, Token


class KnitrStyle(Style):
    background_color = ""
    highlight_color  = ""
    default_style    = ""
    styles = {

        Comment:                "italic #ad95af",
        Comment.Preproc:        "",
        Comment.Special:        "",
        Comment.Single:         "",

        Keyword:                "",
        Keyword.Pseudo:         "#b05a65",
        Keyword.Reserved:       "bold #295f94",
        Keyword.Type:           "#b05a65",
        Keyword.Namespace:      "#b05a65",
        Keyword.Declaration:     "",
        Keyword.Constant:       "#55aa55",

        Name:                   "",
        Name.Builtin.Pseudo:    "#55aa55",
        Name.Class:             "",
        Name.Builtin:           "",
        Name.Exception:         "",
        Name.Variable:          "",
        Name.Function:          "",

        Operator:               "#3399cc",
        Operator.Word:          "",

        Number:                 "#af0f91",
        Number.Hex:             "",
        String:                 "#317ecc",
        String.Backtick:        ""
    }
