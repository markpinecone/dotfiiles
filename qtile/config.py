import os
import json
import subprocess
import unicodes as uc
from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration
from libqtile import bar, layout, qtile, hook, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from theme import colors
from keybindings import mod, keys

# #PyWal Colors
# pycolors = os.path.expanduser('~/.cache/wal/colors.json')
# colordict = json.load(open(pycolors))

main_color = "#ff4d4d"
main_bg = "#0F0F0F"
main_fg = "#f3f2ed"
term = "kitty"

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )

groups = [
    Group("1", label=""),
    Group("2", label="󰨞", matches=[Match(wm_class="code")]),
    Group("3", label="󰈹", matches=[Match(wm_class="firefox")]),
    Group("4", label=""),
    Group("5", label="󰿎", matches=[Match(wm_class="Stremio")], layout="max"),
    Group("6", label="", matches=[Match(wm_class="telegram-desktop"), Match(wm_class="discord")]),
    Group(
        "7",
        label="󰝚",
        matches=[Match(wm_class="tidal-hifi"), Match(wm_class="spotify")],
        layout="max",
    ),
    Group(
        "8",
        label="󱚤",
        matches=[Match(wm_class="anythingllm-desktop"), Match(wm_class="lm studio")],
        layout="columns",
    ),
    Group("9", label="", matches=[Match(wm_class="thunderbird")]),
]


for i in groups:
    # mod1 + letter of group = switch to group
    keys.append(Key([mod], i.name, lazy.group[i.name].toscreen()))

    # mod1 + shift + letter of group = switch to & move focused window to group
    keys.append(Key([mod, "shift"], i.name, lazy.window.togroup(i.name)))


layout_theme = {
    "border_width": 3,
    "margin": 8,
    "border_focus": main_color,
    "border_normal": main_bg,
}

layouts = [
    layout.MonadTall(**layout_theme, name=""),
    layout.Columns(**layout_theme, name="󰕭"),
    layout.Max(name=""),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="JetBrainsMono Nerd Font Bold",
    fontsize=14,
    padding=6,
)

color_scheme = dict(
    background=main_bg,
    foreground=main_color,
)

color_scheme_inverted = dict(
    background=main_color,
    foreground=main_bg,
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.TextBox(
                    "󰣇",
                    padding=20,
                    background=main_color,
                    foreground=main_bg,
                    fontsize=20,
                    mouse_callbacks={
                        "Button1": lazy.spawn("rofi -show drun -show-icons")
                    },
                ),
                widget.GroupBox(
                    fmt='{}',
                    center_aligned=True,
                    fontsize=20,
                    padding_x=18,
                    scroll="false",
                    background=main_bg,
                    active=main_color,
                    use_mouse_wheel=False,
                    this_current_screen_border=main_color,
                    highlight_method='block',
                    block_highlight_text_color=main_bg,
                    disable_drag=True,
                ),
                widget.TextBox(
                    " ",  # As Spacer
                    background=main_bg,
                ),
                widget.CurrentLayout(
                    background=main_bg,
                    foreground=main_color,
                    fontsize=20,
                ),
                widget.TextBox(
                    " ",  # As Spacer
                    background=main_bg,
                ),
                widget.Prompt(),
                widget.GlobalMenu(
                    background=main_bg,
                    foreground=main_fg,
                ),
                widget.Spacer(length=16),
                widget.WindowName(
                 foreground = main_color,
                 max_chars = 40
                 ),
                # widget.Chord(
                #     chords_colors={
                #         "launch": (colors["Red"], colors["Rosewater"]),
                #     },
                #     name_transform=lambda name: name.upper(),
                #     background=Color_bg,
                # ),
                widget.Systray(padding = 3),
                widget.Spacer(length=16),
                widget.UnitStatus(
                    label='FW',
                    unitname='ufw.service',
                    colour_inactive=main_color,  
                    foreground=main_color,
                    decorations=[
                        BorderDecoration(
                            colour=main_color,
                            border_width=[0, 0, 2, 0],
                        )
                    ],
                ),
                widget.Spacer(length=8),
                widget.UnitStatus(
                    label='Docker',
                    unitname='docker.service',
                    colour_inactive=main_color,
                    foreground=main_color,
                    decorations=[
                        BorderDecoration(
                            colour=main_color,
                            border_width=[0, 0, 2, 0],
                        )
                    ],  
                ),
                widget.Spacer(length=8),
                widget.PulseVolume(
                    fmt='{} ',
                    emoji=True,
                    emoji_list=['', '', '', ''], 
                    volume_app="pavucontrol",
                    limit_max_volume=True,
                    margin_x=10,
                    scroll=True,
                    foreground=main_color,
                    decorations=[
                        BorderDecoration(
                            colour=main_color,
                            border_width=[0, 0, 2, 0],
                        )
                    ],
                ),
                widget.Spacer(length=8),
                widget.ThermalSensor(
                    fmt='CPU: {}',
                    foreground=main_color,
                    tag_sensor='Tctl',
                    decorations=[
                        BorderDecoration(
                            colour=main_color,
                            border_width=[0, 0, 2, 0],
                        )
                    ],    
                ),
                widget.Spacer(length=8),
                widget.NvidiaSensors(
                    format="GPU {temp}󰔄",
                    background=main_bg,
                    foreground=main_color,
                    decorations=[
                        BorderDecoration(
                            colour=main_color,
                            border_width=[0, 0, 2, 0],
                        )
                    ],
                ),
                widget.Spacer(length=8),
                widget.CPU(
                    format="▓ {load_percent:04}%",
                    background=main_bg,
                    foreground=main_color,
                    decorations=[
                        BorderDecoration(
                            colour=main_color,
                            border_width=[0, 0, 2, 0],
                        )
                    ],
                ),
                widget.Spacer(length=8),
                widget.Memory(
                    format="󰍛 {MemPercent}%",
                    background=main_bg,
                    foreground=main_color,
                    measure_mem="G",
                    decorations=[
                        BorderDecoration(
                            colour=main_color,
                            border_width=[0, 0, 2, 0],
                        )
                    ],
                ),
                widget.Spacer(length=8),
                # widget.DF(
                #     update_interval=60,
                #     foreground=main_color,
                #     mouse_callbacks={
                #         "Button1": lambda: qtile.cmd_spawn(term + " -e df")
                #     },
                #     partition="/",
                #     # format = '[{p}] {uf}{m} ({r:.0f}%)',
                #     format="{uf}{m} free",
                #     fmt="🖴  Disk: {}",
                #     visible_on_warn=False,
                #     decorations=[
                #         BorderDecoration(
                #             colour=main_color,
                #             border_width=[0, 0, 2, 0],
                #         )
                #     ],
                # ),
                # widget.Spacer(length=8),
                widget.KeyboardLayout(
                    foreground=main_color,
                    fmt="⌨ {}",
                    configured_keyboards=['lv', 'us'],
                    decorations=[
                        BorderDecoration(
                            colour=main_color,
                            border_width=[0, 0, 2, 0],
                        )
                    ],
                ),
                widget.Spacer(length=8),
                widget.Clock(
                    format=" %d.%m.%Y 󰥔 %H:%M %p",
                    background=main_bg,
                    foreground=main_color,
                    decorations=[
                        BorderDecoration(
                            colour=main_color,
                            border_width=[0, 0, 2, 0],
                        )
                    ],
                ),
                widget.Spacer(length=8),
                widget.QuickExit(
                    default_text=" 󰩈 ",
                    countdown_format=" {} ",
                    background=main_bg,
                    foreground=main_color,
                    fontsize=20,
                    decorations=[
                        BorderDecoration(
                            colour=main_color,
                            border_width=[0, 0, 2, 0],
                        )
                    ],
                ),
            ],
            28,
            background=main_bg,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.Popen([home])
