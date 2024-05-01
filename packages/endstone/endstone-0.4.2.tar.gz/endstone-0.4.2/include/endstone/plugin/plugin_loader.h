// Copyright (c) 2023, The Endstone Project. (https://endstone.dev) All Rights Reserved.
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

#include <memory>
#include <string>
#include <vector>

#include "endstone/event/server/plugin_disable_event.h"
#include "endstone/event/server/plugin_enable_event.h"
#include "endstone/logger.h"
#include "endstone/plugin/plugin.h"
#include "endstone/server.h"

namespace endstone {

/**
 * @brief Represents a plugin loader, which handles direct access to specific types of plugins
 */
class PluginLoader {
public:
    explicit PluginLoader(Server &server) : server_(server) {}
    PluginLoader(const PluginLoader &) = delete;
    PluginLoader &operator=(const PluginLoader &) = delete;

    virtual ~PluginLoader() = default;

    /**
     * Loads the plugin contained within the specified directory
     *
     * @param directory Directory to check for plugins
     * @return A list of all plugins loaded
     */
    [[nodiscard]] virtual std::vector<Plugin *> loadPlugins(const std::string &directory) = 0;

    /**
     * Enables the specified plugin
     * Attempting to enable a plugin that is already enabled will have no effect
     *
     * @param plugin Plugin to enable
     */
    virtual void enablePlugin(Plugin &plugin) const
    {
        if (!plugin.isEnabled()) {
            plugin.getLogger().info("Enabling {}", plugin.getDescription().getFullName());
            plugin.setEnabled(true);
            PluginEnableEvent event(plugin);
            server_.getPluginManager().callEvent(event);
        }
    }

    /**
     * Disables the specified plugin
     * Attempting to disable a plugin that is not enabled will have no effect
     *
     * @param plugin Plugin to disable
     */
    virtual void disablePlugin(Plugin &plugin) const
    {
        if (plugin.isEnabled()) {
            plugin.getLogger().info("Disabling {}", plugin.getDescription().getFullName());
            plugin.setEnabled(false);
            PluginDisableEvent event(plugin);
            server_.getPluginManager().callEvent(event);
        }
    }

    /**
     * @brief Retrieves the Server object associated with the PluginLoader.
     *
     * This function returns a reference to the Server object that the PluginLoader is associated with.
     *
     * @return The Server reference.
     */
    [[nodiscard]] Server &getServer() const
    {
        return server_;
    }

protected:
    void initPlugin(Plugin &plugin, Logger &logger)
    {
        plugin.loader_ = this;
        plugin.server_ = &server_;
        plugin.logger_ = &logger;
    }

    Server &server_;
};

}  // namespace endstone
