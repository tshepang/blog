my current desktop setup
========================

:date: 2014-02-16
:tags: GNOME, Debian


Following is how my GUI environment is set-up on `my home machine`__
(a laptop) and work machine (a desktop). For the (libre) tools I
frequently use, see `this post`__ instead.

----

With recent Debian GNOME updates (late 2013), something got broken
enough that I could not login to my account. I saw this as a good
opportunity to finally try something other than GNOME as my primary
environment. I have before tinkered with
other GUI environments (XFCE, KDE 3, FluxBox, LXDE, and most recently,
Window Maker), but none lasted very long. But I think this time I will
actually abandon GNOME permanently, after nearly a decade of use.

I been playing with dwm__ for the past several weeks, and the experience
has convinced me to stay. I am attracted to the philosophy of
minimalism, though I find they do take things a bit far in requiring
users to tinker with C source code in order to configure it. Luckily
it's not hard, and there's examples out there. It just takes a while
since there isn't a comprehensive guide I could find.

For my login manager, I use LightDM__. I added this line to its
configuration, in ``[SeatDefaults]`` section::

  greeter-hide-users=false

It removes the need to manually enter my username each time I want to
login.

Reason I'm not using GDM? I wanted something light, which also
wouldn't pull in dozens of packages that I won't use. For example::

    $ sudo apt-get install --no-install-recommends gdm3
    Reading package lists... Done
    Building dependency tree       
    Reading state information... Done
    The following extra packages will be installed:
      bluez dconf-cli evolution-data-server evolution-data-server-common
      gir1.2-accountsservice-1.0 gir1.2-caribou-1.0 gir1.2-gck-1 gir1.2-gcr-3
      gir1.2-gdesktopenums-3.0 gir1.2-gdm3 gir1.2-gkbd-3.0 gir1.2-gmenu-3.0
      gir1.2-gnomebluetooth-1.0 gir1.2-gnomedesktop-3.0 gir1.2-ibus-1.0
      gir1.2-mutter-3.0 gir1.2-nmgtk-1.0 gir1.2-polkit-1.0 gir1.2-soup-2.4
      gir1.2-telepathyglib-0.12 gir1.2-telepathylogger-0.2 gir1.2-xkl-1.0 gjs
      gnome-bluetooth gnome-settings-daemon gnome-shell gnome-shell-common
      gnome-themes-standard gnome-themes-standard-data libbluetooth3 libcamel-1.2-43
      libcaribou-common libcaribou0 libebackend-1.2-6 libebook-1.2-14
      libebook-contacts-1.2-0 libecal-1.2-15 libedata-book-1.2-17 libedata-cal-1.2-20
      libedataserver-1.2-17 libgdata-common libgdata13 libgdm1 libgnome-menu-3-0
      libgoa-1.0-0 libgoa-1.0-common libgweather-3-3 libgweather-common libibus-1.0-5
      libical0 libmission-control-plugins0 libmutter0b liboauth0 libopenobex1
      libpackagekit-glib2-16 libpulse-mainloop-glib0 librest-0.7-0 libsoup-gnome2.4-1
      libtelepathy-glib0 libtelepathy-logger3 libwacom-common libwacom2 mutter-common
      obex-data-server obexd-client telepathy-mission-control-5
    Suggested packages:
      evolution evolution-data-server-dbg gnome-orca gnome-user-share telepathy-haze
    Recommended packages:
      zenity gvfs-backends gnome-control-center pulseaudio gkbd-capplet gnome-contacts
      gnome-user-guide gtk2-engines-pixbuf gnome-accessibility-themes packagekit
    The following NEW packages will be installed:
      bluez dconf-cli evolution-data-server evolution-data-server-common gdm3
      gir1.2-accountsservice-1.0 gir1.2-caribou-1.0 gir1.2-gck-1 gir1.2-gcr-3
      gir1.2-gdesktopenums-3.0 gir1.2-gdm3 gir1.2-gkbd-3.0 gir1.2-gmenu-3.0
      gir1.2-gnomebluetooth-1.0 gir1.2-gnomedesktop-3.0 gir1.2-ibus-1.0
      gir1.2-mutter-3.0 gir1.2-nmgtk-1.0 gir1.2-polkit-1.0 gir1.2-soup-2.4
      gir1.2-telepathyglib-0.12 gir1.2-telepathylogger-0.2 gir1.2-xkl-1.0 gjs
      gnome-bluetooth gnome-settings-daemon gnome-shell gnome-shell-common
      gnome-themes-standard gnome-themes-standard-data libbluetooth3 libcamel-1.2-43
      libcaribou-common libcaribou0 libebackend-1.2-6 libebook-1.2-14
      libebook-contacts-1.2-0 libecal-1.2-15 libedata-book-1.2-17 libedata-cal-1.2-20
      libedataserver-1.2-17 libgdata-common libgdata13 libgdm1 libgnome-menu-3-0
      libgoa-1.0-0 libgoa-1.0-common libgweather-3-3 libgweather-common libibus-1.0-5
      libical0 libmission-control-plugins0 libmutter0b liboauth0 libopenobex1
      libpackagekit-glib2-16 libpulse-mainloop-glib0 librest-0.7-0 libsoup-gnome2.4-1
      libtelepathy-glib0 libtelepathy-logger3 libwacom-common libwacom2 mutter-common
      obex-data-server obexd-client telepathy-mission-control-5
    0 upgraded, 67 newly installed, 0 to remove and 45 not upgraded.
    Need to get 0 B/31.0 MB of archives.
    After this operation, 90.8 MB of additional disk space will be used.

GNOME philosophy tends towards tight integration, leading to things
being not as modular as I would like: how could a display manager end
up depending on a Contacts tool, or the Bluetooth stack. It may
be just how it was built in Debian, but that also means there
were build options that allowed such tight coupling in the first
place. GDM has served me well for years, but I'm not interested in all
those tools it brings with.

Anyways, enough with that. I added a custom ``.desktop`` file which will
become selectable on LightDM UI::

    $ cat /usr/share/xsessions/custom.desktop
    [Desktop Entry]
    Name=Custom
    Exec=/etc/X11/Xsession
    Type=XSession

On selecting the entry labeled **Custom** that appears on LightDM,
and logging in, the following will get executed (`~/.xsession`__):


.. code-block:: sh

   # apps
   xfce4-terminal --hide-menubar --tab --tab --tab &
   firefox &
   nautilus --no-desktop &
   nm-applet &
   trayer --edge top --align right --widthtype request --distance 15 &
   quodlibet &
   if [ $HOSTNAME == 'twork' ]; then
      icedove &
   fi

   # settings
   xset b off
   xmodmap -e "clear Lock"
   xmodmap -e "keycode 66 = Super_L"

   # host-specific settings
   if [ $HOSTNAME == 'twork' ]; then
       xrandr --output VGA-0 --output DVI-0 --right-of VGA-0
   else
       synclient TapButton1=1
       synclient ClickFinger2=2
       syndaemon -dti 1
   fi

   # clock
   while true; do
       datetime=$( date +"%F %R" )
       if acpi -a | grep off-line > /dev/null; then
           battery=$( python -c
           "print(\"$(acpi)\".split(',')[1].strip())" )
           xsetroot -name "$battery"" | ""$datetime"
       else
           xsetroot -name "$datetime"
       fi
       sleep 1m
   done &

   exec dwm


Finally, this is what my dwm config changes look like (`config.def.h`__)::

    diff --git a/config.def.h b/config.def.h
    index 77ff358..78af5d6 100644
    --- a/config.def.h
    +++ b/config.def.h
    @@ -14,12 +14,15 @@ static const Bool showbar           = True;     /*
    False means no bar */
     static const Bool topbar            = True;     /* False means bottom
     bar */

     /* tagging */
    -static const char *tags[] = { "1", "2", "3", "4", "5", "6", "7", "8",
    "9" };
    +static const char *tags[] = { "web", "files", "terminal", "misc" };

     static const Rule rules[] = {
    -       /* class      instance    title       tags mask     isfloating
            monitor */
    -       { "Gimp",     NULL,       NULL,       0,
            True,        -1 },
    -       { "Firefox",  NULL,       NULL,       1 << 8,
            False,       -1 },
    +  /* class             instance  title  tags mask  isfloating
       monitor */
    +  { "Iceweasel",       NULL,     NULL,  1 << 0,    False,       -1 },
    +  { "trayer",          NULL,     NULL,  1 << 0,    False,       -1 },
    +  { "Nautilus",        NULL,     NULL,  1 << 1,    False,       -1 },
    +  { "Xfce4-terminal",  NULL,     NULL,  1 << 2,    False,       -1 },
    +  { "Quodlibet",       NULL,     NULL,  1 << 3,    False,       -1 },
     };

     /* layout(s) */
    @@ -35,7 +38,7 @@ static const Layout layouts[] = {
     };

     /* key definitions */
    -#define MODKEY Mod1Mask
    +#define MODKEY Mod4Mask
     #define TAGKEYS(KEY,TAG) \
            { MODKEY,                       KEY,      view,           {.ui
            = 1 << TAG} }, \
            { MODKEY|ControlMask,           KEY,      toggleview,     {.ui
            = 1 << TAG} }, \
    @@ -47,7 +50,7 @@ static const Layout layouts[] = {

     /* commands */
     static const char *dmenucmd[] = { "dmenu_run", "-fn", font, "-nb",
     normbgcolor, "-nf", normfgcolor, "-sb", selbgcolor, "-sf",
     selfgcolor, NULL };
    -static const char *termcmd[]  = { "uxterm", NULL };
    +static const char *termcmd[]  = { "xfce4-terminal", "--hide-menubar"
    };

     static Key keys[] = {
            /* modifier                     key        function
            argument */


Note that this diff is against the Debian package (version **6.0-6**). I
could not change the modifier key with the upstream version of dwm.

You will notice that I'm still using one major GNOME package,
Nautilus, the file browser. It remains `my favorite`__.



__ http://tshepang.net/sony-vaio-pro-13-svp13212sgbi
__ http://tshepang.net/floss-i-use-a-lot
__ http://dwm.suckless.org
__ http://www.freedesktop.org/wiki/Software/LightDM
__ https://bitbucket.org/tshepang/custom/src/tip/xsession
__ https://bitbucket.org/tshepang/custom/src/tip/config.def.h
__ http://tshepang.net/favorite-floss
