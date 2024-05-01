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

#include <thread>
#include <vector>

#include "bedrock/bedrock.h"
#include "bedrock/forward.h"
#include "bedrock/server/server_instance.h"
#include "bedrock/world/level/event/actor_event.h"
#include "bedrock/world/level/event/block_event.h"
#include "bedrock/world/level/event/coordinator_result.h"
#include "bedrock/world/level/event/event_ref.h"
#include "bedrock/world/level/event/gameplay_handler.h"
#include "bedrock/world/level/event/item_event.h"
#include "bedrock/world/level/event/level_event.h"
#include "bedrock/world/level/event/player_event.h"
#include "bedrock/world/level/event/server_event.h"

template <typename ListenerType>
class EventCoordinatorPimpl : public Bedrock::EnableNonOwnerReferences {
public:
    ~EventCoordinatorPimpl() override = 0;

private:
    std::vector<ListenerType *> unk1_;                              // +24
    std::vector<std::function<EventResult(ListenerType &)>> unk2_;  // +48
    std::vector<ListenerType *> unk3_;                              // +72
    bool unk4_;                                                     // +96
    std::thread::id unk5_;                                          // +100 (+104)
    bool unk6_;                                                     // +104 (+112)
    std::int32_t unk7_;                                             // +112 (+116)
};

class ActorEventCoordinator {
public:
    void sendEvent(EventRef<ActorGameplayEvent<void>> const &ref);
    CoordinatorResult sendEvent(EventRef<ActorGameplayEvent<CoordinatorResult>> const &ref);
};

class BlockEventCoordinator {
public:
    void sendEvent(EventRef<BlockGameplayEvent<void>> const &ref);
    CoordinatorResult sendEvent(EventRef<BlockGameplayEvent<CoordinatorResult>> const &ref);
};
class ItemEventCoordinator;

class LevelEventCoordinator : public EventCoordinatorPimpl<LevelEventListener> {
public:
    void sendEvent(EventRef<LevelGameplayEvent<void>> const &ref);
    LevelGameplayHandler &getLevelGameplayHandler();

private:
    std::unique_ptr<LevelGameplayHandler> level_gameplay_handler_;     // +112
    std::shared_ptr<Bedrock::PubSub::SubscriptionBase> subscription_;  // +120
};

class PlayerEventCoordinator {
public:
    void sendEvent(EventRef<PlayerGameplayEvent<void>> const &ref);
    CoordinatorResult sendEvent(EventRef<PlayerGameplayEvent<CoordinatorResult>> const &ref);
};
class ServerPlayerEventCoordinator : public PlayerEventCoordinator {};
class ClientPlayerEventCoordinator : public PlayerEventCoordinator {};

class ServerInstanceEventCoordinator {
public:
    BEDROCK_API void sendServerInitializeStart(ServerInstance &instance);
    BEDROCK_API void sendServerThreadStarted(ServerInstance &instance);
    BEDROCK_API void sendServerThreadStopped(ServerInstance &instance);
    BEDROCK_API void sendServerLevelInitialized(ServerInstance &instance, Level &level);
};

class ServerNetworkEventCoordinator;
class ScriptingEventCoordinator;
class ScriptDeferredEventCoordinator;
