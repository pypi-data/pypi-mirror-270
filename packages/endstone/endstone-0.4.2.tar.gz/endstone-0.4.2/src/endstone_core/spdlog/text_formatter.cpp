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

#include "endstone/detail/spdlog/text_formatter.h"

#include <spdlog/details/fmt_helper.h>

namespace endstone::detail {

void TextFormatter::format(const spdlog::details::log_msg &msg, const tm &, spdlog::memory_buf_t &dest)
{

    const auto &input = msg.payload;
    for (std::size_t i = 0; i < input.size(); i++) {
        // Check for the § character in UTF-8 (0xC2A7) and ensure there's a following character
        if (i + 2 < input.size() && static_cast<unsigned char>(input[i]) == 0xC2 &&
            static_cast<unsigned char>(input[i + 1]) == 0xA7) {
            i += 2;                  // Skip §
            if (i < input.size()) {  // if there's a color code character to after §
                if (should_do_colors_) {
                    auto format_code = static_cast<unsigned char>(input[i]);
                    auto it = ansi_codes.find(format_code);
                    if (it != ansi_codes.end()) {
                        spdlog::details::fmt_helper::append_string_view(it->second, dest);
                    }
                    else {
                        fmt::format_to(std::back_inserter(dest), "{}", input[i]);
                    }
                }
            }
        }
        else {
            // Append the current character to the result if it's not part of a color code
            fmt::format_to(std::back_inserter(dest), "{}", input[i]);
        }
    }
}

std::unique_ptr<spdlog::custom_flag_formatter> TextFormatter::clone() const
{
    return spdlog::details::make_unique<TextFormatter>(should_do_colors_);
}

}  // namespace endstone::detail
