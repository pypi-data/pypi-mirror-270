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

#include "endstone/actor/actor.h"

#include <pybind11/pybind11.h>

#include "endstone/actor/human.h"

namespace py = pybind11;

namespace endstone::detail {

void init_actor(py::module &m)
{
    py::class_<Actor, CommandSender>(m, "Actor")
        .def_property_readonly("runtime_id", &Actor::getRuntimeId, "Returns the runtime id for this actor.");

    py::class_<HumanActor, Actor>(m, "HumanActor");
}

}  // namespace endstone::detail
