_cpp_format = """
#pragma once
#ifndef __GITVERSIONBUILDER__VERSION_H__
#define __GITVERSIONBUILDER__VERSION_H__

namespace version {
  constexpr const char *versionString = "%s";
  constexpr const char *tagName = "%s";
  constexpr const unsigned int commitsSinceTag = %d;
  constexpr const char *gitCommitId = "%s";
}

#endif
"""

_python_format = """
VERSION_STRING = "%s"
TAG_NAME = "%s"
COMMITS_SINCE_TAG = %d
GIT_COMMIT_ID = "%s"
"""


def _output(version_info, format):
    return format % (
        version_info.version_string, version_info.tag_name, version_info.commits_since_tag, version_info.commit_id)


def to_cpp(version_info):
    return _output(version_info, _cpp_format)


def to_python(version_info):
    return _output(version_info, _python_format)