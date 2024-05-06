from qtile_extras import widget
from libqtile import bar
from libqtile.config import Screen
from qtile_extras.widget.decorations import BorderDecoration
from libqtile.lazy import lazy
from core.defaults import *

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
