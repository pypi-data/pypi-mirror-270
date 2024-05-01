
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

#include <cstdint>

#include "bedrock/command/command_output.h"
#include "bedrock/command/command_registry.h"

class Command {
public:
    Command() = default;
    virtual ~Command() = default;
    [[nodiscard]] BEDROCK_API std::string getCommandName() const;

    virtual bool collectOptionalArguments()
    {
        return true;
    }
    virtual void execute(CommandOrigin const &, CommandOutput &) const = 0;

private:
    int version_ = 0;
    CommandRegistry *registry_ = nullptr;                                         // +16
    CommandRegistry::Symbol symbol_;                                              // +24
    CommandPermissionLevel permission_level_ = CommandPermissionLevel::Internal;  // +28
    CommandFlag flag_ = CommandFlag::None;                                        // +30
};
static_assert(sizeof(Command) == 32);
