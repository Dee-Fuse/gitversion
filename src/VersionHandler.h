#pragma once
#ifndef MESSMER_GITVERSION_SRC_VERSIONHANDLER_H
#define MESSMER_GITVERSION_SRC_VERSIONHANDLER_H

#include "Version.h"
#include "VersionParser.h"

namespace git_version_builder {
#include "git_version.h"
}

namespace gitversion {
    constexpr unsigned int COMMITS_SINCE_TAG = git_version_builder::version::GIT_COMMITS_SINCE_TAG;
    constexpr const char *GIT_COMMIT_ID = git_version_builder::version::GIT_COMMIT_ID;
    constexpr const Version VERSION = VersionParser::parse(git_version_builder::version::GIT_TAG_NAME,
                                                           git_version_builder::version::GIT_COMMITS_SINCE_TAG,
                                                           git_version_builder::version::GIT_COMMIT_ID);
}

#endif
