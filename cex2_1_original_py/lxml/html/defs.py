# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: c:\python27\lib\site-packages\lxml-3.2.4-py2.7-win32.egg\lxml\html\defs.py
# Compiled at: 2013-12-10 09:11:58
try:
    frozenset
except NameError:
    from sets import Set as frozenset

empty_tags = frozenset([
 'area', 'base', 'basefont', 'br', 'col', 'frame', 'hr', 
 'img', 'input', 
 'isindex', 'link', 'meta', 'param'])
deprecated_tags = frozenset([
 'applet', 'basefont', 'center', 'dir', 'font', 'isindex', 
 'menu', 's', 
 'strike', 'u'])
link_attrs = frozenset([
 'action', 'archive', 'background', 'cite', 'classid', 
 'codebase', 'data', 
 'href', 'longdesc', 'profile', 'src', 
 'usemap', 
 'dynsrc', 'lowsrc'])
event_attrs = frozenset([
 'onblur', 'onchange', 'onclick', 'ondblclick', 'onerror', 
 'onfocus', 'onkeydown', 
 'onkeypress', 'onkeyup', 'onload', 
 'onmousedown', 'onmousemove', 'onmouseout', 
 'onmouseover', 
 'onmouseup', 'onreset', 'onresize', 'onselect', 'onsubmit', 
 'onunload'])
safe_attrs = frozenset([
 'abbr', 'accept', 'accept-charset', 'accesskey', 'action', 'align', 
 'alt', 
 'axis', 'border', 'cellpadding', 'cellspacing', 'char', 'charoff', 
 'charset', 
 'checked', 'cite', 'class', 'clear', 'cols', 'colspan', 
 'color', 'compact', 
 'coords', 'datetime', 'dir', 'disabled', 'enctype', 
 'for', 'frame', 
 'headers', 'height', 'href', 'hreflang', 'hspace', 'id', 
 'ismap', 'label', 
 'lang', 'longdesc', 'maxlength', 'media', 'method', 
 'multiple', 'name', 
 'nohref', 'noshade', 'nowrap', 'prompt', 'readonly', 
 'rel', 'rev', 'rows', 
 'rowspan', 'rules', 'scope', 'selected', 'shape', 
 'size', 'span', 'src', 
 'start', 'summary', 'tabindex', 'target', 'title', 
 'type', 'usemap', 
 'valign', 'value', 'vspace', 'width'])
top_level_tags = frozenset([
 'html', 'head', 'body', 'frameset'])
head_tags = frozenset([
 'base', 'isindex', 'link', 'meta', 'script', 'style', 'title'])
general_block_tags = frozenset([
 'address', 
 'blockquote', 
 'center', 
 'del', 
 'div', 
 'h1', 
 'h2', 
 'h3', 
 'h4', 
 'h5', 
 'h6', 
 'hr', 
 'ins', 
 'isindex', 
 'noscript', 
 'p', 
 'pre'])
list_tags = frozenset([
 'dir', 'dl', 'dt', 'dd', 'li', 'menu', 'ol', 'ul'])
table_tags = frozenset([
 'table', 'caption', 'colgroup', 'col', 
 'thead', 'tfoot', 'tbody', 'tr', 
 'td', 'th'])
block_tags = general_block_tags | list_tags | table_tags | frozenset([
 'fieldset', 'form', 'legend', 'optgroup', 'option'])
form_tags = frozenset([
 'form', 'button', 'fieldset', 'legend', 'input', 'label', 
 'select', 'optgroup', 
 'option', 'textarea'])
special_inline_tags = frozenset([
 'a', 'applet', 'basefont', 'bdo', 'br', 'embed', 'font', 'iframe', 
 'img', 
 'map', 'area', 'object', 'param', 'q', 'script', 
 'span', 'sub', 'sup'])
phrase_tags = frozenset([
 'abbr', 'acronym', 'cite', 'code', 'del', 'dfn', 'em', 
 'ins', 'kbd', 
 'samp', 'strong', 'var'])
font_style_tags = frozenset([
 'b', 'big', 'i', 's', 'small', 'strike', 'tt', 'u'])
frame_tags = frozenset([
 'frameset', 'frame', 'noframes'])
html5_tags = frozenset([
 'article', 'aside', 'audio', 'canvas', 'command', 'datalist', 
 'details', 
 'embed', 'figcaption', 'figure', 'footer', 'header', 
 'hgroup', 'keygen', 
 'mark', 'math', 'meter', 'nav', 'output', 
 'progress', 'rp', 'rt', 'ruby', 
 'section', 'source', 'summary', 
 'svg', 'time', 'track', 'video', 'wbr'])
nonstandard_tags = frozenset(['blink', 'marquee'])
tags = top_level_tags | head_tags | general_block_tags | list_tags | table_tags | form_tags | special_inline_tags | phrase_tags | font_style_tags | nonstandard_tags | html5_tags