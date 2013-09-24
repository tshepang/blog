project of note: Valgrind
=========================

:date: 2013-09-25
:tags: project-of-note, non-Python



I have, since using Valgrind (and reading a bit of its documentation)
some years ago, developed much respect for it. It is quite an advanced
tool, and though its primary use is detecting memory leaks, I am here
going to explore its other functionality... calculating the cost of
each line of code in the CPU. This is useful when tuning programs for
performance.

Following is example code; it accepts 2 arguments, a filename and
content it will write to that file:

.. code-block:: c

  #include <string.h>
  #include <errno.h>
  #include <stdio.h>
  #include <fcntl.h>
  #include <unistd.h>

  int
  main (int argc, char **argv)
  {
      char path[0xFF];
      char content[0xFF];
      int fd;
      ssize_t written;

      if (argc < 3) {
          fprintf (stderr, "usage: %s <filename> <content>\n", argv[0]);
          return 1;
      }

      strcpy (path, argv[1]);
      sprintf (content, "%s\n", argv[2]);

      fd = creat (path, S_IRWXU);
      if (fd == -1) {
          fprintf (stderr, "open error: %s ('%s')\n", strerror (errno), path);
          return 1;
      }

      written = write (fd, content, strlen (content));
      if (written == -1) {
          fprintf (stderr, "write error: %s ('%s')\n", strerror (errno), path);
          return 1;
      }
      return 0;
  }

Build command (using GCC 4.8.1)::

   gcc -Wall -pedantic -g play.c -o play

System details::

  $ uname --all
  Linux thome 3.11-trunk-amd64 #1 SMP Debian 3.11-1~exp1 (2013-09-12) x86_64 GNU/Linux
  $ sudo lshw -class processor
  *-cpu
       description: CPU
       product: Intel(R) Core(TM) i5-2410M CPU @ 2.30GHz
       vendor: Intel Corp.
       physical id: 4
       bus info: cpu@0
       version: Intel(R) Core(TM) i5-2410M CPU @ 2.30GHz
       serial: To Be Filled By O.E.M.
       slot: CPU 1
       size: 2300MHz
       capacity: 4GHz
       width: 64 bits
       clock: 100MHz
       capabilities: x86-64 fpu fpu_exception wp vme de pse tsc msr
       pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts
       acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx rdtscp
       constant_tsc arch_perfmon pebs bts rep_good nopl xtopology
       nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor
       ds_cpl vmx est tm2 ssse3 cx16 xtpr pdcm pcid sse4_1 sse4_2
       x2apic popcnt tsc_deadline_timer xsave avx lahf_lm ida arat epb
       xsaveopt pln pts dtherm tpr_shadow vnmi flexpriority ept vpid
       aes cpufreq
       configuration: cores=2 enabledcores=1 threads=2

Running the resulting binary with **Callgrind**::

  $ valgrind --tool=callgrind --callgrind-out-file=out ./play filename
  filecontent
  ==5308== Callgrind, a call-graph generating cache profiler
  ==5308== Copyright (C) 2002-2012, and GNU GPL'd, by Josef Weidendorfer
  et al.
  ==5308== Using Valgrind-3.8.1 and LibVEX; rerun with -h for copyright
  info
  ==5308== Command: ./play filename filecontent
  ==5308== 
  ==5308== For interactive control, run 'callgrind_control -h'.
  ==5308== 
  ==5308== Events    : Ir
  ==5308== Collected : 107520
  ==5308== 
  ==5308== I   refs:      107,520
  $ cat filename 
  filecontent

And finally, seeing closely the cost of each function call, where
**Ir** stands for **Instruction cache reads**, which you can read as
*number of CPU instructions*. I have used ``tree=calling`` option so
that I can see the cost of all operations called by a parent (marked
with a ``*``) ::

  $ callgrind_annotate --tree=calling out play.c
  --------------------------------------------------------------------------------
  Profile data file 'out' (creator: callgrind-3.8.1)
  --------------------------------------------------------------------------------
  I1 cache: 
  D1 cache: 
  LL cache: 
  Timerange: Basic block 0 - 22326
  Trigger: Program termination
  Profiled target:  ./play filename filecontent (PID 5308, part 1)
  Events recorded:  Ir
  Events shown:     Ir
  Event sort order: Ir
  Thresholds:       99
  Include dirs:     
  User annotated:   play.c
  Auto-annotation:  off

  --------------------------------------------------------------------------------
  Ir 
  --------------------------------------------------------------------------------
  107,520  PROGRAM TOTALS

  --------------------------------------------------------------------------------
  Ir  file:function
  --------------------------------------------------------------------------------

  24,113  *  /build/eglibc-TepTGA/eglibc-2.17/elf/dl-lookup.c:do_lookup_x [/lib/x86_64-linux-gnu/ld-2.17.so]
  1,053  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-misc.c:_dl_name_match_p (25x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  13,423  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-lookup.c:check_match.9345 (88x) [/lib/x86_64-linux-gnu/ld-2.17.so]

  18,264  *  /build/eglibc-TepTGA/eglibc-2.17/elf/dl-lookup.c:_dl_lookup_symbol_x [/lib/x86_64-linux-gnu/ld-2.17.so]
  38,589  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-lookup.c:do_lookup_x (94x) [/lib/x86_64-linux-gnu/ld-2.17.so]

  15,836  *  /build/eglibc-TepTGA/eglibc-2.17/elf/../sysdeps/x86_64/dl-machine.h:_dl_relocate_object
  13  >   /build/eglibc-TepTGA/eglibc-2.17/string/../sysdeps/x86_64/multiarch/memmove.c:memcpy@GLIBC_2.2.5 (1x) [/lib/x86_64-linux-gnu/libc-2.17.so]
  81  >   /build/eglibc-TepTGA/eglibc-2.17/string/../sysdeps/x86_64/multiarch/strcmp.S:strcasecmp (1x) [/lib/x86_64-linux-gnu/libc-2.17.so]
  6  >   /build/eglibc-TepTGA/eglibc-2.17/string/../sysdeps/x86_64/multiarch/strcmp.S:strncasecmp (1x) [/lib/x86_64-linux-gnu/libc-2.17.so]
  7  >   /build/eglibc-TepTGA/eglibc-2.17/string/../sysdeps/x86_64/multiarch/memset.S:memset (1x) [/lib/x86_64-linux-gnu/libc-2.17.so]
  51,501  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-lookup.c:_dl_lookup_symbol_x (86x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  18  >   /build/eglibc-TepTGA/eglibc-2.17/string/../sysdeps/x86_64/multiarch/../memcpy.S:memcpy (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  67  >   /build/eglibc-TepTGA/eglibc-2.17/time/../sysdeps/unix/sysv/linux/x86_64/time.c:time (1x) [/lib/x86_64-linux-gnu/libc-2.17.so]
  67  >   /build/eglibc-TepTGA/eglibc-2.17/time/../sysdeps/unix/sysv/linux/x86_64/gettimeofday.c:gettimeofday (1x) [/lib/x86_64-linux-gnu/libc-2.17.so]
  6  >   /build/eglibc-TepTGA/eglibc-2.17/string/../sysdeps/x86_64/multiarch/strnlen.S:strnlen (1x) [/lib/x86_64-linux-gnu/libc-2.17.so]
  [snip; to be continued]

I have trimmed the output to bring focus to the most interesting
output of all, which is the total cost for each line of my code::

  [continued]
  --------------------------------------------------------------------------------
  -- User-annotated source: play.c
  --------------------------------------------------------------------------------
  Ir 

  .  #include <string.h>
  .  #include <errno.h>
  .  #include <stdio.h>
  .  #include <fcntl.h>
  .  #include <unistd.h>
  .  
  .  int
  .  main (int argc, char **argv)
  5  {
  .      char path[0xFF];
  .      char content[0xFF];
  .      int fd;
  .      ssize_t written;
  .  
  2      if (argc < 3) {
  .  	fprintf (stderr, "usage: %s <filename> <content>\n", argv[0]);
  .  	return 1;
  .      }
  .  
  7      strcpy (path, argv[1]);
  21  => /build/eglibc-TepTGA/eglibc-2.17/string/../sysdeps/x86_64/multiarch/strcpy-sse2-unaligned.S:__strcpy_sse2_unaligned (1x)
  799  => /build/eglibc-TepTGA/eglibc-2.17/elf/../sysdeps/x86_64/dl-trampoline.S:_dl_runtime_resolve (1x)
  8      sprintf (content, "%s\n", argv[2]);
  1,188  => /build/eglibc-TepTGA/eglibc-2.17/stdio-common/sprintf.c:sprintf (1x)
  805  => /build/eglibc-TepTGA/eglibc-2.17/elf/../sysdeps/x86_64/dl-trampoline.S:_dl_runtime_resolve (1x)
  .  
  5      fd = creat (path, S_IRWXU);
  766  => /build/eglibc-TepTGA/eglibc-2.17/elf/../sysdeps/x86_64/dl-trampoline.S:_dl_runtime_resolve (1x)
  7  => /build/eglibc-TepTGA/eglibc-2.17/io/../sysdeps/unix/syscall-template.S:creat (1x)
  2      if (fd == -1) {
  .  	fprintf (stderr, "open error: %s ('%s')\n", strerror (errno), path);
  .  	return 1;
  .      }
  .  
  10      written = write (fd, content, strlen (content));
  7  => /build/eglibc-TepTGA/eglibc-2.17/io/../sysdeps/unix/syscall-template.S:write (1x)
  14  => /build/eglibc-TepTGA/eglibc-2.17/string/../sysdeps/x86_64/multiarch/strlen-sse2-pminub.S:__strlen_sse2_pminub (1x)
  1,567  => /build/eglibc-TepTGA/eglibc-2.17/elf/../sysdeps/x86_64/dl-trampoline.S:_dl_runtime_resolve (2x)
  2      if (written == -1) {
  .  	fprintf (stderr, "write error: %s ('%s')\n", strerror (errno), path);
  .  	return 1;
  .      }
  1      return 0;
  2  }

  --------------------------------------------------------------------------------
  Ir 
  --------------------------------------------------------------------------------
  0  percentage of events annotated

As an aside, note that the indentation is messed up a bit.

---

Since I normally work at too high a level to care about CPU
instructions cycles at this detail, I found the exercise eye-opening.
