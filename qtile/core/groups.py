from libqtile.config import Group, Key, Match
from libqtile.lazy import lazy
from core.keybindings import mod, keys

groups = [
    Group("1", label=""),
    Group("2", label="󰨞", matches=[Match(wm_class="code")]),
    Group("3", label="󰈹", matches=[Match(wm_class="firefox")]),
    Group("4", label=""),
    Group("5", label="󰿎", matches=[Match(wm_class="Stremio")]),
    Group("6", label="", matches=[Match(wm_class="telegram-desktop"), Match(wm_class="discord")]),
    Group(
        "7",
        label="󰝚",
        matches=[Match(wm_class="tidal-hifi"), Match(wm_class="spotify")],
    ),
    Group(
        "8",
        label="󱚤",
        matches=[Match(wm_class="anythingllm-desktop"), Match(wm_class="lm studio")],
    ),
    Group("9", label="", matches=[Match(wm_class="thunderbird")]),
]


for i in groups:
    # mod1 + letter of group = switch to group
    keys.append(Key([mod], i.name, lazy.group[i.name].toscreen()))

    # mod1 + shift + letter of group = switch to & move focused window to group
    keys.append(Key([mod, "shift"], i.name, lazy.window.togroup(i.name)))
