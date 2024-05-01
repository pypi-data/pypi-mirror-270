# Shortcut Functions for Web Operations

## Install

```bash
# Install without extras
pip install invisibleroads-macros-web
# Install with extras
pip install invisibleroads-macros-web[jinja,markdown,starlette]
```

## Use

```python
# Open browser
from invisibleroads_macros_web.browser import (
    open_browser)

# Escape characters
from invisibleroads_macros_web.escape import (
    escape_quotes_html,
    escape_quotes_js)

# Check ports
from invisibleroads_macros_web.port import (
    find_open_port,
    is_port_in_use)

# Render markdown
from invisibleroads_macros_web.markdown import (
    get_html_from_markdown,
    remove_single_paragraph,
    remove_parent_paragraphs,
    remove_line_break_after_div)

# Configure templates
from invisibleroads_macros_web.jinja import (
    AssetStorage,
    RelativeTemplateEnvironment,
    PathTemplateLoader)
from invisibleroads_macros_web.starlette import (
    ExtraResponseHeadersMiddleware,
    TemplateResponseFactory)
```

## Test

```bash
git clone https://github.com/invisibleroads/invisibleroads-macros-web
cd invisibleroads-macros-web
pip install -e .[jinja,markdown,starlette,test]
pytest --cov=invisibleroads_macros_web --cov-report term-missing tests
```
