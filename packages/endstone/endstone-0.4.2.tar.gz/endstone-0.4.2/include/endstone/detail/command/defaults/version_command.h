// Copyright (c) 2024, The Endstone Project. (https://endstone.dev) All Rights Reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#pragma once

#include "endstone/detail/command/endstone_command.h"
#include "endstone/plugin/plugin.h"

namespace endstone::detail {

class VersionCommand : public EndstoneCommand {
public:
    VersionCommand();
    bool execute(CommandSender &sender, const std::vector<std::string> &args) const override;

private:
    void describeToSender(Plugin &plugin, CommandSender &sender) const;
    [[nodiscard]] std::string getNameList(const std::vector<std::string> &names) const;
};

}  // namespace endstone::detail
