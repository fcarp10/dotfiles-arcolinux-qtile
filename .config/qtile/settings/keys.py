# Qtile keybindings

from libqtile.config import Key
from libqtile.command import lazy


mod = "mod4"

keys = [
    # ------------ Window Configs ------------
    # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.down()),
    Key([mod], "j", lazy.layout.up()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    # Change window sizes (MonadTall)
    Key([mod, "shift"], "h", lazy.layout.grow()),
    Key([mod, "shift"], "j", lazy.layout.shrink()),
    # Toggle floating
    Key([mod, "shift"], "f", lazy.window.toggle_floating()),
    # Move windows up or down in current stack
    Key([mod, "shift"], "k", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_up()),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod, "shift"], "Tab", lazy.prev_layout()),
    # Kill window
    Key([mod], "w", lazy.window.kill()),
    # Switch focus of monitors
    Key([mod], "period", lazy.next_screen()),
    Key([mod], "comma", lazy.prev_screen()),
    # Restart Qtile
    Key([mod, "shift"], "r", lazy.restart()),
    Key([mod, "shift"], "q", lazy.shutdown()),
    # ------------ App Configs ------------
    # Menu
    Key([mod, "shift"], "Return", lazy.spawn("dmenu_run -p 'Run: '")),
    # Browser
    Key([mod], "b", lazy.spawn("firefox")),
    # File Explorer
    Key([mod], "f", lazy.spawn("thunar")),
    # Terminal
    Key([mod], "Return", lazy.spawn("alacritty")),
    Key([mod], "t", lazy.spawn("alacritty")),
    # editor gui
    Key([mod], "e", lazy.spawn("vscodium")),
    # mail
    Key([mod], "a", lazy.spawn("thunderbird")),
    # chat
    Key([mod], "c", lazy.spawn("slack")),
    # arcolinux-logout
    Key([mod], "x", lazy.spawn("arcolinux-logout")),
    # pamac-manager
    Key([mod], "p", lazy.spawn("pamac-manager")),
    # Screenshot
    Key([mod], "Print", lazy.spawn("gnome-screenshot -i")),
    # ------------ Hardware Configs ------------
    # Volume
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%"),
    ),
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%"),
    ),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]
