+++
date = 2011-03-19
title = "my JHBuild setup"

[taxonomies]
tags = ['GNOME']
+++

JHBuild is a [powerful] and [flexible] build tool for GNOME. It does
takes some getting used to in terms of set-up, but this [wiki page] is
quite gentle, and it details how to get the code running on your
machine.

If you use Debian (or Ubuntu), you can use run this command:

``` {.sourceCode .sh}
wajig --norecommends install build-essential docbook-xsl flex \
bison cvs gperf cmake  {uuid,ppp}-dev \
libx{composite,randr,damage,ft2,i,t}-dev \
libxcb-{event1,aux0,atom1}-dev \
lib{pam0g,iw,db,gdbm,png12,ffi,tiff,vorbis,gl1-mesa,unistring} \
lib{quvi,icu,neon27,usb-1.0-0,asound2,ncurses5,udev,usb,acl1} \
lib{boost-signals,ldap2,sasl2}-dev
```

It\'s installs the development packages that will be needed by the build
process. The `--no-recommends` option means I want to limit the
installation to packages I really need, avoiding the extra stuff deemed
by the packager to be useful for me.

My \"\~/.jhbuilrc\" contains the following:

``` {.sourceCode .python}
# build directory
checkoutroot = os.path.expanduser("~/src/gnome")

# don't spew lots of distracting status messages
notrayicon = True

# attempt to build modules even if their dependencies weren't successfully built
nopoison = True

# don't build these since they have issues; this implies that I must install my distro's development versions
skip = ['nss', 'nspr']

# dont fetch moduleset xml files from the web; use ones that are installed locally
use_local_modulesets = True

# where html-formatted logs are kept
tinderbox_outputdir = os.path.expanduser("~/temp/tinderbox")
```

See [Configuration File Reference][flexible] for a detailed explanation
of these options.

After this, I run `jhbuild bootstrap --ignore-system`. This downloads,
builds, and installs the basic tools for building packages (here\'s [the
xml file] it uses to determine what these tools are, and where it
downloads them from). To avoid issues with some incompatibility with my
OS, I use `--ignore-system`, which ensures that the bootstrap command
will use the blessed versions of these tools.

When the bootstrap process is complete, I run the not-so-descriptive
command `jhbuild tinderbox` (See Command Reference for a detailed
explanation of this and the other options). This is the same as build,
except that the output is stored in html files, in a directory specified
by **tinderbox\_outputdir** in the config file.

Ideally, some hours later, the process should be complete. Reaching for
\"\~/temp/tinderbox\" will present you with a whole bunch of html files,
one for each module. The file \"index.html\" will give a decent page
that acts like a summary of the entire build process, showing which
modules failed, and on what build stages. Gorgeous!

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

**sidenotes**:

-   This process is rather simplified, for the sake of clarity.
-   I run Debian 6, codenamed Squeeze.
-   There is [a more thorough tutorial] elsewhere.

  [powerful]: http://library.gnome.org/devel/jhbuild/unstable/command-reference.html.en
  [flexible]: http://library.gnome.org/devel/jhbuild/unstable/config-reference.html.en
  [wiki page]: http://live.gnome.org/Jhbuild
  [the xml file]: http://git.gnome.org/browse/jhbuild/tree/modulesets/bootstrap.modules
  [a more thorough tutorial]: http://www.vuntz.net/journal/post/2010/09/23/My-love-for-jhbuild
