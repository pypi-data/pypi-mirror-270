# Copyright (c) 2024 Philippe Proulx <pproulx@efficios.com>
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# pyright: strict

from dataclasses import dataclass
from typing import List, Sequence, Union, Pattern, Match, Optional
import re


# Element base.
class _Elem:
    pass

# Paragraph.
@dataclass(frozen=True)
class _Para(_Elem):
    words: List[str]


# Simple list item.
@dataclass(frozen=True)
class _SimpleListItem:
    elems: List[_Elem]


# Simple list base.
@dataclass(frozen=True)
class _SimpleList(_Elem):
    items: List[_SimpleListItem]


# Unordered list.
class _Ul(_SimpleList):
    pass


# Definition list item.
@dataclass(frozen=True)
class _DlItem:
    term: str
    elems: List[_Elem]


# Definition list.
@dataclass(frozen=True)
class _Dl(_Elem):
    items: List[_DlItem]


# Unchanged block.
@dataclass(frozen=True)
class _AsIs(_Elem):
    lines: List[str]


# Heading base.
@dataclass(frozen=True)
class _Heading(_Elem):
    text: str


# Level 1 heading.
class _H1(_Heading):
    pass


# Level 2 heading.
class _H2(_Heading):
    pass


# Removes trailing empty lines from `lines`.
def _remove_trailing_empty_lines(lines: List[str]):
    assert len(lines) >= 1

    while True:
        if lines[-1] != '':
            break

        del lines[-1]


# Returns the indentation string of `count` spaces.
def _indent_str(count: int):
    return ' ' * count


# Parses the raw lines of a comment on construction; the `elems`
# property is then the resulting list of elements.
class _Parser:
    def __init__(self, lines: Sequence[str]):
        self._lines = lines
        self._at = 0
        self._last_line_index = len(lines) - 1
        self._elems : List[_Elem] = []
        self._parse()

    # Resulting list of elements.
    @property
    def elems(self):
        return self._elems

    def _add_elem(self, elem: _Elem):
        self._elems.append(elem)

    @property
    def _cur_line(self):
        return self._lines[self._at]

    @property
    def _at_last_line(self):
        return self._at == self._last_line_index

    @property
    def _prev_line(self):
        if len(self._lines) == 1:
            return ''

        return '' if self._at == 0 else self._lines[self._at - 1]

    @property
    def _next_line(self):
        if len(self._lines) == 1:
            return ''

        return '' if self._at >= self._last_line_index else self._lines[self._at + 1]

    def _match_cur_line(self, pat: Union[str, Pattern[str]]) -> Optional[Match[str]]:
        return re.match(pat, self._cur_line)

    def _match_next_line(self, pat: Union[str, Pattern[str]]) -> Optional[Match[str]]:
        return re.match(pat, self._next_line)

    def _skip_empty_lines(self):
        while not self._is_done:
            if self._cur_line != '':
                break

            self._at += 1

    @property
    def _is_done(self):
        return self._at >= len(self._lines)

    # Tries to parse a level 1 heading.
    def _try_parse_h1(self):
        if self._next_line == '===' or self._match_next_line(r'^═+$'):
            elem = _H1(self._cur_line)
            self._at += 2
            return elem

    # Tries to parse a level 2 heading.
    def _try_parse_h2(self):
        if self._next_line == '---' or self._match_next_line(r'^─+$'):
            elem = _H2(self._cur_line)
            self._at += 2
            return elem

    # Unindents the lines by `count` spaces when possible, keeping
    # unindentable lines as is.
    @staticmethod
    def _unindent_lines(lines: List[str], count: int = 4):
        def unindent_line(line: str):
            if line.startswith(_indent_str(count)):
                # enough initial spaces to unindent
                return line[count:]
            else:
                # keep as is
                return line

        return list(map(unindent_line, lines))

    _indented_content_pat = re.compile(r'^    .+')

    # Tries to parse a definition list item.
    def _try_parse_dl_item(self):
        # term?
        dt_m = self._match_cur_line(r'^(\S.*):$')

        if not dt_m:
            # no term
            return

        if not self._match_next_line(self._indented_content_pat):
            # no definition
            return

        # skip term line
        self._at += 1

        # parse definition lines
        def_lines: List[str] = []
        at = self._at

        while at <= self._last_line_index:
            if self._lines[at] == '':
                # keep empty line
                def_lines.append('')
                at += 1
                continue

            if self._indented_content_pat.match(self._lines[at]):
                # indented content line
                def_lines.append(self._lines[at])
                at += 1
                continue

            # end of definition
            break

        # remove trailing empty definition lines
        _remove_trailing_empty_lines(def_lines)

        # update current position
        self._at = at

        # create item from unintended definition lines
        return _DlItem(dt_m.group(1),
                       _Parser(self._unindent_lines(def_lines)).elems)

    # Tries to parse a definition list.
    def _try_parse_dl(self):
        items: List[_DlItem] = []

        while True:
            self._skip_empty_lines()

            if self._is_done:
                break

            item = self._try_parse_dl_item()

            if item is None:
                break

            items.append(item)

        if len(items) > 0:
            return _Dl(items)

    # Tries to parse an unchanged block.
    def _try_parse_as_is(self):
        if not self._match_cur_line(self._indented_content_pat):
            return

        lines: List[str] = []
        at = self._at

        while at <= self._last_line_index:
            if self._lines[at] == '':
                # keep empty line
                lines.append('')
                at += 1
                continue

            if re.match(self._indented_content_pat, self._lines[at]):
                # content line
                lines.append(self._lines[at])
                at += 1
                continue

            # end of block
            break

        # remove trailing empty lines
        _remove_trailing_empty_lines(lines)

        # update current position
        self._at = at

        # create element from unindented lines
        return _AsIs(self._unindent_lines(lines))

    _bullet_line_pat = re.compile(r'^(?:\*|•|‣) (.+)')

    # Tries to parse an unordered list item.
    def _try_parse_ul_item(self):
        # item start?
        bullet_m = self._match_cur_line(self._bullet_line_pat)

        if not bullet_m:
            # no item
            return

        # skip first line
        self._at += 1

        # parse content lines
        lines: List[str] = [bullet_m.group(1)]
        at = self._at

        while at <= self._last_line_index:
            if self._lines[at] == '':
                # keep empty line
                lines.append('')
                at += 1
                continue

            if re.match(r'^  .+$', self._lines[at]):
                # indented content line
                lines.append(self._lines[at])
                at += 1
                continue

            # end of item
            break

        # remove trailing empty lines
        _remove_trailing_empty_lines(lines)

        # update current position
        self._at = at

        # create item from unintended content lines
        return _SimpleListItem(_Parser(self._unindent_lines(lines, 2)).elems)

    # Tries to parse an unordered list.
    def _try_parse_ul(self):
        items: List[_SimpleListItem] = []

        while True:
            self._skip_empty_lines()

            if self._is_done:
                break

            item = self._try_parse_ul_item()

            if item is None:
                break

            items.append(item)

        if len(items) > 0:
            return _Ul(items)

    _literal_pat = re.compile(r'`[^`]*`')
    _word_pat = re.compile(r'(.+?)(?=`| |$)')

    # Converts a paragraph string to a paragraph element containing
    # individual words.
    @staticmethod
    def _para_elem_from_text(text: str):
        elems: List[str] = []
        i = 0

        # scan each character
        while i < len(text):
            # literal?
            m = _Parser._literal_pat.match(text, i)

            if m:
                # literal
                elems.append(m.group(0))
            else:
                # word?
                m = _Parser._word_pat.match(text, i)

                if m:
                    # word
                    word = m.group(1).strip()

                    if len(word) > 0:
                        elems.append(word)

            if m:
                i += len(m.group(0))

        return _Para(elems)

    # Tries to parse a paragraph.
    def _try_parse_para(self):
        lines: List[str] = []

        while not self._is_done:
            if self._cur_line == '' or self._match_cur_line(self._bullet_line_pat):
                # empty line: end of paragraph
                break

            lines.append(self._cur_line)
            self._at += 1

        if len(lines) > 0:
            return self._para_elem_from_text(' '.join(lines))

    def _parse(self):
        while not self._is_done:
            self._skip_empty_lines()

            if self._is_done:
                break

            # level 1 heading?
            elem = self._try_parse_h1()

            if elem is not None:
                self._add_elem(elem)
                continue

            # level 2 heading?
            elem = self._try_parse_h2()

            if elem is not None:
                self._add_elem(elem)
                continue

            # unordered list?
            elem = self._try_parse_ul()

            if elem is not None:
                self._add_elem(elem)
                continue

            # definition list?
            elem = self._try_parse_dl()

            if elem is not None:
                self._add_elem(elem)
                continue

            # block as is?
            elem = self._try_parse_as_is()

            if elem is not None:
                self._add_elem(elem)
                continue

            # fall back to paragraph
            elem = self._try_parse_para()

            if elem is not None:
                self._add_elem(elem)


class _Formatter:
    def __init__(self, elems: List[_Elem], max_width: int):
        self._max_width = max_width
        self._cur_indent = 0
        self._cur_list_level = -1
        self._lines = self._elems_lines(elems)

    @property
    def lines(self):
        return self._lines

    @property
    def _cur_max_width(self):
        return max([self._max_width - self._cur_indent, 0])

    @property
    def _indent_str(self):
        return _indent_str(self._cur_indent)

    # Returns the lines of the paragraph `para`.
    def _para_lines(self, para: _Para):
        lines: List[str] = [self._indent_str]

        # append each word, wrapping when necessary
        for word in para.words:
            to_append = f'{word} '

            if len(lines[-1]) + len(word) >= self._cur_max_width:
                # append to current line
                lines.append(self._indent_str + to_append)
            else:
                # new line
                lines[-1] += to_append

        # remove trailing empty lines
        _remove_trailing_empty_lines(lines)

        # append final empty line and return lines
        lines.append('')
        return lines

    # Returns the lines of the unordered list item `item`.
    def _ul_item_lines(self, item: _SimpleListItem):
        # get indented element lines
        self._cur_indent += 2
        lines: List[str] = []

        for elem in item.elems:
            lines += self._elem_lines(elem)

        self._cur_indent -= 2

        # insert bullet point
        bullet = ['•', '‣', '⁃'][self._cur_list_level % 3]
        lines[0] = f'{self._indent_str}{bullet} {lines[0][self._cur_indent + 2:]}'

        # remove trailing empty lines
        _remove_trailing_empty_lines(lines)

        # append final empty line and return lines
        lines.append('')
        return lines

    # Returns the lines of the unordered list `ul`.
    def _ul_lines(self, ul: _Ul):
        lines: List[str] = []
        self._cur_list_level += 1

        for item in ul.items:
            lines += self._ul_item_lines(item)

        self._cur_list_level -= 1

        # special case to make the list compact if there are only
        # single-line items
        if len(lines) == 2 * len(ul.items):
            lines = list(filter(lambda line: len(line.strip()) > 0, lines))

            # reappend final empty line
            lines.append('')

        return lines

    # Returns the lines of the definition list item `item`.
    def _dl_item_lines(self, item: _DlItem):
        # start with term line
        lines = [f'{item.term}:']

        # get indented element lines
        self._cur_indent += 4

        for elem in item.elems:
            lines += self._elem_lines(elem)

        self._cur_indent -= 4

        # remove trailing empty lines
        _remove_trailing_empty_lines(lines)

        # append final empty line and return lines
        lines.append('')
        return lines

    # Returns the lines of the definition list `dl`.
    def _dl_lines(self, dl: _Dl):
        lines: List[str] = []

        for item in dl.items:
            lines += self._dl_item_lines(item)

        return lines

    # Returns the lines of the unchanged block `as_is`.
    def _as_is_lines(self, as_is: _AsIs):
        return list(map(lambda line: f'{self._indent_str}    {line}',
                        as_is.lines)) + ['']

    # Returns the lines of the level 1 heading `h1`.
    def _h1_lines(self, h1: _H1):
        return [
            h1.text.upper(),
            '═' * len(h1.text),
        ]

    # Returns the lines of the level 2 heading `h2`.
    def _h2_lines(self, h2: _H2):
        return [
            h2.text,
            '─' * len(h2.text),
        ]

    # Returns the lines of the element `elem`.
    def _elem_lines(self, elem: _Elem) -> List[str]:
        if type(elem) is _Para:
            return self._para_lines(elem)
        elif type(elem) is _Ul:
            return self._ul_lines(elem)
        elif type(elem) is _Dl:
            return self._dl_lines(elem)
        elif type(elem) is _H1:
            return self._h1_lines(elem)
        elif type(elem) is _H2:
            return self._h2_lines(elem)
        elif type(elem) is _AsIs:
            return self._as_is_lines(elem)
        else:
            return []

    # Returns the lines of the elements `elems`.
    def _elems_lines(self, elems: List[_Elem]):
        lines: List[str] = []

        for elem in elems:
            lines += self._elem_lines(elem)

        # right-strip all lines
        lines = list(map(lambda line: line.rstrip(), lines))

        # remove trailing empty lines and return them
        _remove_trailing_empty_lines(lines)
        return lines


# Returns the beautified raw comment text `text` to fit on `max_width`
# columns.
#
# `text` is raw in that it must not contain special block comment
# characters, raw text.
#
# Use format_block_comment() to format a complete C/C++ block comment.
def format(text: str, max_width: int = 72):
    return '\n'.join(_Formatter(_Parser(text.splitlines()).elems, max_width).lines)


# Returns the beautified version of the C/C++ block comment text `text`
# to fit on `max_width` columns.
#
# The comment text is everything between `/*` and `*/`, where the column
# of `/*` within its original document is `start_col`.
#
# The whole `comment` string must have a format such as this:
#
#     /*
#      * Hello world.
#      * ===
#      *
#      * * Cupidatat in elit irure.
#      * * Qui sint.
#      *
#      * Sunt tempor cillum ut sint.
#      */
#
# The leading ` * ` strings are important.
def format_block_comment(comment: str, start_col: int = 0, max_width: int = 72):
    # extract content lines from comment string
    comment_lines = comment.splitlines()
    content_lines: List[str] = []

    for comment_line in comment_lines:
        comment_line = comment_line.strip()

        if comment_line in ('/*', '*/'):
            continue

        if comment_line == '*':
            content_lines.append('')
            continue

        m = re.match(r'\s*\* (.+)$', comment_line)

        if not m:
            raise ValueError(m)

        content_lines.append(m.group(1))

    # format contents of comment
    new_content_lines = _Formatter(_Parser(content_lines).elems, max_width).lines

    # create and return final comment
    new_comment_lines = ['/*']
    indent_str = _indent_str(start_col)
    new_comment_lines += list(map(lambda rline: f'{indent_str} * {rline}',
                                  new_content_lines))
    new_comment_lines.append(f'{indent_str} */')
    return '\n'.join(new_comment_lines)
