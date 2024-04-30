import contextlib
import pathlib
import re

import pytest
import docutils.core
from jaraco.packaging import metadata


project_files = 'setup.py', 'setup.cfg', 'pyproject.toml'


def pytest_collect_file(file_path: pathlib.Path, parent):
    if file_path.name not in project_files:
        return
    return CheckdocsItem.from_parent(parent, name='project')


class Description(str):
    @classmethod
    def from_md(cls, md):
        desc = cls(md.get('Description'))
        desc.content_type = md.get('Description-Content-Type', 'text/x-rst')
        return desc


class CheckdocsItem(pytest.Item):
    def runtest(self):
        desc = self.get_long_description()
        method_name = f"run_{re.sub('[-/]', '_', desc.content_type)}"
        getattr(self, method_name)(desc)

    def run_text_markdown(self, desc):
        "stubbed"

    def run_text_x_rst(self, desc):
        with self.monkey_patch_system_message() as reports:
            self.rst2html(desc)
        assert not reports

    @contextlib.contextmanager
    def monkey_patch_system_message(self):
        reports = []
        orig = docutils.utils.Reporter.system_message

        def system_message(reporter, level, message, *children, **kwargs):
            result = orig(reporter, level, message, *children, **kwargs)
            if level >= reporter.WARNING_LEVEL:
                # All reST failures preventing doc publishing go to reports
                # and thus will result to failed checkdocs run
                reports.append(message)

            return result

        docutils.utils.Reporter.system_message = system_message
        yield reports
        docutils.utils.Reporter.system_message = orig

    def get_long_description(self):
        return Description.from_md(metadata.load('.'))

    @staticmethod
    def rst2html(value):
        docutils_settings = {}
        parts = docutils.core.publish_parts(
            source=value, writer_name="html4css1", settings_overrides=docutils_settings
        )
        return parts['whole']
