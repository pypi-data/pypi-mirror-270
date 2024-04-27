# incorporeal-cms

Software that makes simple Markdown content go.

## Installation and Usage

I recommend getting a release from <https://git.incorporeal.org/bss/incorporeal-cms/releases> and
installing the Python package in a virtualenv. Something like the following should suffice:

```
% cd ~/site
% virtualenv --python=python3.8 env-py3.8
% source env-py3.8/bin/activate
% pip install -U pip
% pip install ~/incorporeal_cms-1.3.0-py3-none-any.whl
% pip install -U gunicorn
% gunicorn -w 5 -t 60 -b 127.0.0.1:10000 --reload 'incorporealcms:create_app()'
```

This will get the CMS up and running, and listening on the specified port. The application is
further configured within `env-py3.8/var/incorporealcms-instance/config.py`, and content is served
out of `env-py3.8/var/incorporealcms-instance/pages/`.

## Serving a Site

Put content inside `env-py3.8/var/incorporealcms-instance/pages/` and go.

* Markdown files (ending in `.md`) are rendered via Python-Markdown if they are accessed without the
  suffix (i.e., `post.md` should be referred to as `/post` to get it to render as Markdown.
* Directory paths (e.g. `/dir/`) can be rendered with a `/dir/index.md` file.
* Symlinks to files are treated as redirects to the destination content.
* Request paths with file suffixes are not rendered and served directly, so images, etc., can be
  referenced naturally, and even the unrendered Markdown can be served as a text file via e.g.
  `/post.md`.

Care is taken to not serve content above the `pages/` dir, even via symlink.

## Configuration

I've tried to keep the software agnostic to my personal domains, logos, etc. There are some settings
you are probably interested in tweaking, by specifying new values in
`incorporealcms-instance/config.py`:

* `TITLE_SUFFIX` is appended to the title of every page, separated from other title content by a
  dash.
* `CONTACT_EMAIL` is referred to in error templates.
* `FAVICON` supplies the image used in browser tabs and that kind of thing.

If I missed anything, please let me know.

## Development and Contributing

Improvements, new plugins, and etc. are all welcome.

I'm reachable on the fediverse, over email, or on Discord, but if you're looking for an option I prefer, I maintain an
IRC channel, `#incorporeal-cms`, on [my IRC network, Randomus](https://randomus.net/) if you would like a place to hang
out and discuss issues and features and whatnot.

## Author and Licensing

Written by and copyright Brian S. Stephan (bss@incorporeal.org).

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
