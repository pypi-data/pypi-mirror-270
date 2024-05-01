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

#include "bedrock/bedrock.h"
#include "bedrock/network/protocol/connection.h"
#include "bedrock/server/level/server_player.h"
#include "bedrock/world/actor/player/player.h"
#include "bedrock/world/level/event/server_event.h"

class ServerNetworkHandler {
public:
    BEDROCK_API void disconnectClient(NetworkIdentifier const &, SubClientId,
                                                            Connection::DisconnectFailReason, std::string const &,
                                                            bool);

private:
    BEDROCK_API bool _loadNewPlayer(ServerPlayer &, bool);              // NOLINT(*-identifier-naming)
    BEDROCK_API void _displayGameMessage(Player const &, ChatEvent &);  // NOLINT(*-identifier-naming)
};
