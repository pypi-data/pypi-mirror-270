"""
Adapted from https://github.com/noahmorrison/chevron
MIT License
"""

import logging
from typing import (
    Any,
    Dict,
    Iterator,
    List,
    Literal,
    Optional,
    Sequence,
    Tuple,
    Union,
    cast,
)

from typing_extensions import TypeAlias

logger = logging.getLogger(__name__)


Scopes: TypeAlias = List[Union[Literal[False, 0], Dict[str, Any]]]


# Globals
_CURRENT_LINE = 1
_LAST_TAG_LINE = None


class ChevronError(SyntaxError):
    pass


#
# Helper functions
#


def grab_literal(template: str, l_del: str) -> Tuple[str, str]:
    """Parse a literal from the template"""

    global _CURRENT_LINE

    try:
        # Look for the next tag and move the template to it
        literal, template = template.split(l_del, 1)
        _CURRENT_LINE += literal.count("\n")
        return (literal, template)

    # There are no more tags in the template?
    except ValueError:
        # Then the rest of the template is a literal
        return (template, "")


def l_sa_check(template: str, literal: str, is_standalone: bool) -> bool:
    """Do a preliminary check to see if a tag could be a standalone"""

    # If there is a newline, or the previous tag was a standalone
    if literal.find("\n") != -1 or is_standalone:
        padding = literal.split("\n")[-1]

        # If all the characters since the last newline are spaces
        if padding.isspace() or padding == "":
            # Then the next tag could be a standalone
            return True
        else:
            # Otherwise it can't be
            return False
    else:
        return False


def r_sa_check(template: str, tag_type: str, is_standalone: bool) -> bool:
    """Do a final checkto see if a tag could be a standalone"""

    # Check right side if we might be a standalone
    if is_standalone and tag_type not in ["variable", "no escape"]:
        on_newline = template.split("\n", 1)

        # If the stuff to the right of us are spaces we're a standalone
        if on_newline[0].isspace() or not on_newline[0]:
            return True
        else:
            return False

    # If we're a tag can't be a standalone
    else:
        return False


def parse_tag(template: str, l_del: str, r_del: str) -> Tuple[Tuple[str, str], str]:
    """Parse a tag from a template"""
    global _CURRENT_LINE
    global _LAST_TAG_LINE

    tag_types = {
        "!": "comment",
        "#": "section",
        "^": "inverted section",
        "/": "end",
        ">": "partial",
        "=": "set delimiter?",
        "{": "no escape?",
        "&": "no escape",
    }

    # Get the tag
    try:
        tag, template = template.split(r_del, 1)
    except ValueError:
        raise ChevronError("unclosed tag " "at line {0}".format(_CURRENT_LINE))

    # Find the type meaning of the first character
    tag_type = tag_types.get(tag[0], "variable")

    # If the type is not a variable
    if tag_type != "variable":
        # Then that first character is not needed
        tag = tag[1:]

    # If we might be a set delimiter tag
    if tag_type == "set delimiter?":
        # Double check to make sure we are
        if tag.endswith("="):
            tag_type = "set delimiter"
            # Remove the equal sign
            tag = tag[:-1]

        # Otherwise we should complain
        else:
            raise ChevronError(
                "unclosed set delimiter tag\n" "at line {0}".format(_CURRENT_LINE)
            )

    # If we might be a no html escape tag
    elif tag_type == "no escape?":
        # And we have a third curly brace
        # (And are using curly braces as delimiters)
        if l_del == "{{" and r_del == "}}" and template.startswith("}"):
            # Then we are a no html escape tag
            template = template[1:]
            tag_type = "no escape"

    # Strip the whitespace off the key and return
    return ((tag_type, tag.strip()), template)


#
# The main tokenizing function
#


def tokenize(
    template: str, def_ldel: str = "{{", def_rdel: str = "}}"
) -> Iterator[Tuple[str, str]]:
    """Tokenize a mustache template

    Tokenizes a mustache template in a generator fashion,
    using file-like objects. It also accepts a string containing
    the template.


    Arguments:

    template -- a file-like object, or a string of a mustache template

    def_ldel -- The default left delimiter
                ("{{" by default, as in spec compliant mustache)

    def_rdel -- The default right delimiter
                ("}}" by default, as in spec compliant mustache)


    Returns:

    A generator of mustache tags in the form of a tuple

    -- (tag_type, tag_key)

    Where tag_type is one of:
     * literal
     * section
     * inverted section
     * end
     * partial
     * no escape

    And tag_key is either the key or in the case of a literal tag,
    the literal itself.
    """

    global _CURRENT_LINE, _LAST_TAG_LINE
    _CURRENT_LINE = 1
    _LAST_TAG_LINE = None

    is_standalone = True
    open_sections = []
    l_del = def_ldel
    r_del = def_rdel

    while template:
        literal, template = grab_literal(template, l_del)

        # If the template is completed
        if not template:
            # Then yield the literal and leave
            yield ("literal", literal)
            break

        # Do the first check to see if we could be a standalone
        is_standalone = l_sa_check(template, literal, is_standalone)

        # Parse the tag
        tag, template = parse_tag(template, l_del, r_del)
        tag_type, tag_key = tag

        # Special tag logic

        # If we are a set delimiter tag
        if tag_type == "set delimiter":
            # Then get and set the delimiters
            dels = tag_key.strip().split(" ")
            l_del, r_del = dels[0], dels[-1]

        # If we are a section tag
        elif tag_type in ["section", "inverted section"]:
            # Then open a new section
            open_sections.append(tag_key)
            _LAST_TAG_LINE = _CURRENT_LINE

        # If we are an end tag
        elif tag_type == "end":
            # Then check to see if the last opened section
            # is the same as us
            try:
                last_section = open_sections.pop()
            except IndexError:
                raise ChevronError(
                    'Trying to close tag "{0}"\n'
                    "Looks like it was not opened.\n"
                    "line {1}".format(tag_key, _CURRENT_LINE + 1)
                )
            if tag_key != last_section:
                # Otherwise we need to complain
                raise ChevronError(
                    'Trying to close tag "{0}"\n'
                    'last open tag is "{1}"\n'
                    "line {2}".format(tag_key, last_section, _CURRENT_LINE + 1)
                )

        # Do the second check to see if we're a standalone
        is_standalone = r_sa_check(template, tag_type, is_standalone)

        # Which if we are
        if is_standalone:
            # Remove the stuff before the newline
            template = template.split("\n", 1)[-1]

            # Partials need to keep the spaces on their left
            if tag_type != "partial":
                # But other tags don't
                literal = literal.rstrip(" ")

        # Start yielding
        # Ignore literals that are empty
        if literal != "":
            yield ("literal", literal)

        # Ignore comments and set delimiters
        if tag_type not in ["comment", "set delimiter?"]:
            yield (tag_type, tag_key)

    # If there are any open sections when we're done
    if open_sections:
        # Then we need to complain
        raise ChevronError(
            "Unexpected EOF\n"
            'the tag "{0}" was never closed\n'
            "was opened at line {1}".format(open_sections[-1], _LAST_TAG_LINE)
        )


#
# Helper functions
#


def _html_escape(string: str) -> str:
    """HTML escape all of these " & < >"""

    html_codes = {
        '"': "&quot;",
        "<": "&lt;",
        ">": "&gt;",
    }

    # & must be handled first
    string = string.replace("&", "&amp;")
    for char in html_codes:
        string = string.replace(char, html_codes[char])
    return string


def _get_key(
    key: str,
    scopes: Scopes,
    warn: bool,
    keep: bool,
    def_ldel: str,
    def_rdel: str,
) -> Any:
    """Get a key from the current scope"""

    # If the key is a dot
    if key == ".":
        # Then just return the current scope
        return scopes[0]

    # Loop through the scopes
    for scope in scopes:
        try:
            # Return an empty string if falsy, with two exceptions
            # 0 should return 0, and False should return False
            if scope in (0, False):
                return scope

            # For every dot separated key
            for child in key.split("."):
                # Return an empty string if falsy, with two exceptions
                # 0 should return 0, and False should return False
                if scope in (0, False):
                    return scope
                # Move into the scope
                try:
                    # Try subscripting (Normal dictionaries)
                    scope = cast(Dict[str, Any], scope)[child]
                except (TypeError, AttributeError):
                    try:
                        scope = getattr(scope, child)
                    except (TypeError, AttributeError):
                        # Try as a list
                        scope = scope[int(child)]  # type: ignore

            try:
                # This allows for custom falsy data types
                # https://github.com/noahmorrison/chevron/issues/35
                if scope._CHEVRON_return_scope_when_falsy:  # type: ignore
                    return scope
            except AttributeError:
                return scope or ""
        except (AttributeError, KeyError, IndexError, ValueError):
            # We couldn't find the key in the current scope
            # We'll try again on the next pass
            pass

    # We couldn't find the key in any of the scopes

    if warn:
        logger.warn("Could not find key '%s'" % (key))

    if keep:
        return "%s %s %s" % (def_ldel, key, def_rdel)

    return ""


def _get_partial(name: str, partials_dict: Dict[str, str]) -> str:
    """Load a partial"""
    try:
        # Maybe the partial is in the dictionary
        return partials_dict[name]
    except KeyError:
        return ""


#
# The main rendering function
#
g_token_cache: Dict[str, List[Tuple[str, str]]] = {}


def render(
    template: Union[str, List[Tuple[str, str]]] = "",
    data: Dict[str, Any] = {},
    partials_dict: Dict[str, str] = {},
    padding: str = "",
    def_ldel: str = "{{",
    def_rdel: str = "}}",
    scopes: Optional[Scopes] = None,
    warn: bool = False,
    keep: bool = False,
) -> str:
    """Render a mustache template.

    Renders a mustache template with a data scope and inline partial capability.

    Arguments:

    template      -- A file-like object or a string containing the template

    data          -- A python dictionary with your data scope

    partials_path -- The path to where your partials are stored
                     If set to None, then partials won't be loaded from the file system
                     (defaults to '.')

    partials_ext  -- The extension that you want the parser to look for
                     (defaults to 'mustache')

    partials_dict -- A python dictionary which will be search for partials
                     before the filesystem is. {'include': 'foo'} is the same
                     as a file called include.mustache
                     (defaults to {})

    padding       -- This is for padding partials, and shouldn't be used
                     (but can be if you really want to)

    def_ldel      -- The default left delimiter
                     ("{{" by default, as in spec compliant mustache)

    def_rdel      -- The default right delimiter
                     ("}}" by default, as in spec compliant mustache)

    scopes        -- The list of scopes that get_key will look through

    warn          -- Log a warning when a template substitution isn't found in the data

    keep          -- Keep unreplaced tags when a substitution isn't found in the data


    Returns:

    A string containing the rendered template.
    """

    # If the template is a sequence but not derived from a string
    if isinstance(template, Sequence) and not isinstance(template, str):
        # Then we don't need to tokenize it
        # But it does need to be a generator
        tokens: Iterator[Tuple[str, str]] = (token for token in template)
    else:
        if template in g_token_cache:
            tokens = (token for token in g_token_cache[template])
        else:
            # Otherwise make a generator
            tokens = tokenize(template, def_ldel, def_rdel)

    output = ""

    if scopes is None:
        scopes = [data]

    # Run through the tokens
    for tag, key in tokens:
        # Set the current scope
        current_scope = scopes[0]

        # If we're an end tag
        if tag == "end":
            # Pop out of the latest scope
            del scopes[0]

        # If the current scope is falsy and not the only scope
        elif not current_scope and len(scopes) != 1:
            if tag in ["section", "inverted section"]:
                # Set the most recent scope to a falsy value
                scopes.insert(0, False)

        # If we're a literal tag
        elif tag == "literal":
            # Add padding to the key and add it to the output
            output += key.replace("\n", "\n" + padding)

        # If we're a variable tag
        elif tag == "variable":
            # Add the html escaped key to the output
            thing = _get_key(
                key, scopes, warn=warn, keep=keep, def_ldel=def_ldel, def_rdel=def_rdel
            )
            if thing is True and key == ".":
                # if we've coerced into a boolean by accident
                # (inverted tags do this)
                # then get the un-coerced object (next in the stack)
                thing = scopes[1]
            if not isinstance(thing, str):
                thing = str(thing)
            output += _html_escape(thing)

        # If we're a no html escape tag
        elif tag == "no escape":
            # Just lookup the key and add it
            thing = _get_key(
                key, scopes, warn=warn, keep=keep, def_ldel=def_ldel, def_rdel=def_rdel
            )
            if not isinstance(thing, str):
                thing = str(thing)
            output += thing

        # If we're a section tag
        elif tag == "section":
            # Get the sections scope
            scope = _get_key(
                key, scopes, warn=warn, keep=keep, def_ldel=def_ldel, def_rdel=def_rdel
            )

            # If the scope is a callable (as described in
            # https://mustache.github.io/mustache.5.html)
            if callable(scope):
                # Generate template text from tags
                text = ""
                tags: List[Tuple[str, str]] = []
                for token in tokens:
                    if token == ("end", key):
                        break

                    tags.append(token)
                    tag_type, tag_key = token
                    if tag_type == "literal":
                        text += tag_key
                    elif tag_type == "no escape":
                        text += "%s& %s %s" % (def_ldel, tag_key, def_rdel)
                    else:
                        text += "%s%s %s%s" % (
                            def_ldel,
                            {
                                "comment": "!",
                                "section": "#",
                                "inverted section": "^",
                                "end": "/",
                                "partial": ">",
                                "set delimiter": "=",
                                "no escape": "&",
                                "variable": "",
                            }[tag_type],
                            tag_key,
                            def_rdel,
                        )

                g_token_cache[text] = tags

                rend = scope(
                    text,
                    lambda template, data=None: render(
                        template,
                        data={},
                        partials_dict=partials_dict,
                        padding=padding,
                        def_ldel=def_ldel,
                        def_rdel=def_rdel,
                        scopes=data and [data] + scopes or scopes,
                        warn=warn,
                        keep=keep,
                    ),
                )

                output += rend

            # If the scope is a sequence, an iterator or generator but not
            # derived from a string
            elif isinstance(scope, (Sequence, Iterator)) and not isinstance(scope, str):
                # Then we need to do some looping

                # Gather up all the tags inside the section
                # (And don't be tricked by nested end tags with the same key)
                # TODO: This feels like it still has edge cases, no?
                tags = []
                tags_with_same_key = 0
                for token in tokens:
                    if token == ("section", key):
                        tags_with_same_key += 1
                    if token == ("end", key):
                        tags_with_same_key -= 1
                        if tags_with_same_key < 0:
                            break
                    tags.append(token)

                # For every item in the scope
                for thing in scope:
                    # Append it as the most recent scope and render
                    new_scope = [thing] + scopes
                    rend = render(
                        template=tags,
                        scopes=new_scope,
                        padding=padding,
                        partials_dict=partials_dict,
                        def_ldel=def_ldel,
                        def_rdel=def_rdel,
                        warn=warn,
                        keep=keep,
                    )

                    output += rend

            else:
                # Otherwise we're just a scope section
                scopes.insert(0, scope)

        # If we're an inverted section
        elif tag == "inverted section":
            # Add the flipped scope to the scopes
            scope = _get_key(
                key, scopes, warn=warn, keep=keep, def_ldel=def_ldel, def_rdel=def_rdel
            )
            scopes.insert(0, cast(Literal[False], not scope))

        # If we're a partial
        elif tag == "partial":
            # Load the partial
            partial = _get_partial(key, partials_dict)

            # Find what to pad the partial with
            left = output.rpartition("\n")[2]
            part_padding = padding
            if left.isspace():
                part_padding += left

            # Render the partial
            part_out = render(
                template=partial,
                partials_dict=partials_dict,
                def_ldel=def_ldel,
                def_rdel=def_rdel,
                padding=part_padding,
                scopes=scopes,
                warn=warn,
                keep=keep,
            )

            # If the partial was indented
            if left.isspace():
                # then remove the spaces from the end
                part_out = part_out.rstrip(" \t")

            # Add the partials output to the output
            output += part_out

    return output
