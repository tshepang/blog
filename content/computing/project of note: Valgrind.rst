project of note: Valgrind
=========================

:date: 2013-09-24
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

  8,820  *  /build/eglibc-TepTGA/eglibc-2.17/string/../sysdeps/x86_64/multiarch/../strcmp.S:strcmp'2 [/lib/x86_64-linux-gnu/ld-2.17.so]
  46,923  >   /build/eglibc-TepTGA/eglibc-2.17/string/../sysdeps/x86_64/multiarch/../strcmp.S:strcmp'2 (1107x) [/lib/x86_64-linux-gnu/ld-2.17.so]

  8,329  *  /build/eglibc-TepTGA/eglibc-2.17/elf/do-rel.h:_dl_relocate_object

  4,510  *  /build/eglibc-TepTGA/eglibc-2.17/elf/dl-lookup.c:check_match.9345 [/lib/x86_64-linux-gnu/ld-2.17.so]
  8,913  >   /build/eglibc-TepTGA/eglibc-2.17/string/../sysdeps/x86_64/multiarch/../strcmp.S:strcmp (106x) [/lib/x86_64-linux-gnu/ld-2.17.so]

  1,820  *  /build/eglibc-TepTGA/eglibc-2.17/stdlib/bsearch.c:bsearch [/lib/x86_64-linux-gnu/libc-2.17.so]
  648  >   /build/eglibc-TepTGA/eglibc-2.17/string/../sysdeps/x86_64/multiarch/../cacheinfo.c:intel_02_known_compare (108x) [/lib/x86_64-linux-gnu/libc-2.17.so]

  1,358  *  /build/eglibc-TepTGA/eglibc-2.17/string/../sysdeps/x86_64/multiarch/../strcmp.S:strcmp [/lib/x86_64-linux-gnu/ld-2.17.so]
  8,820  >   /build/eglibc-TepTGA/eglibc-2.17/string/../sysdeps/x86_64/multiarch/../strcmp.S:strcmp'2 (121x) [/lib/x86_64-linux-gnu/ld-2.17.so]

  1,201  *  /build/eglibc-TepTGA/eglibc-2.17/elf/dl-minimal.c:strsep [/lib/x86_64-linux-gnu/ld-2.17.so]

  1,149  *  /build/eglibc-TepTGA/eglibc-2.17/elf/dl-load.c:_dl_map_object_from_fd [/lib/x86_64-linux-gnu/ld-2.17.so]
  84  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-object.c:_dl_add_to_namespace_list (2x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  8  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-tls.c:_dl_next_tls_modid (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  16  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-debug.c:_dl_debug_initialize (2x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  10  >   /build/eglibc-TepTGA/eglibc-2.17/misc/../sysdeps/unix/syscall-template.S:mprotect (2x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  50  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-lookup.c:_dl_setup_hash (2x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  30  >   /build/eglibc-TepTGA/eglibc-2.17/misc/../sysdeps/unix/syscall-template.S:mmap (5x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  20  >   /build/eglibc-TepTGA/eglibc-2.17/io/../sysdeps/unix/sysv/linux/wordsize-64/fxstat.c:_fxstat (2x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  10  >   /build/eglibc-TepTGA/eglibc-2.17/io/../sysdeps/unix/syscall-template.S:close (2x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  383  >   /build/eglibc-TepTGA/eglibc-2.17/string/../sysdeps/x86_64/multiarch/../memset.S:memset (2x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  983  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-object.c:_dl_new_object (2x) [/lib/x86_64-linux-gnu/ld-2.17.so]

  1,139  *  /build/eglibc-TepTGA/eglibc-2.17/elf/dl-version.c:_dl_check_map_versions [/lib/x86_64-linux-gnu/ld-2.17.so]
  443  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-version.c:match_symbol (3x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  138  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-minimal.c:calloc (3x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  510  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-misc.c:_dl_name_match_p (7x) [/lib/x86_64-linux-gnu/ld-2.17.so]

  1,076  *  /build/eglibc-TepTGA/eglibc-2.17/elf/dl-misc.c:_dl_name_match_p [/lib/x86_64-linux-gnu/ld-2.17.so]
  979  >   /build/eglibc-TepTGA/eglibc-2.17/string/../sysdeps/x86_64/multiarch/../strcmp.S:strcmp (82x) [/lib/x86_64-linux-gnu/ld-2.17.so]

  1,057  *  /build/eglibc-TepTGA/eglibc-2.17/elf/dl-deps.c:_dl_map_object_deps [/lib/x86_64-linux-gnu/ld-2.17.so]
  110  >   /build/eglibc-TepTGA/eglibc-2.17/string/../sysdeps/x86_64/multiarch/../memcpy.S:memcpy (5x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  5,758  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-error.c:_dl_catch_error (2x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  68  >   /build/eglibc-TepTGA/eglibc-2.17/string/../sysdeps/x86_64/multiarch/../strchr.S:index (2x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  87  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-minimal.c:malloc (3x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  51  >   /build/eglibc-TepTGA/eglibc-2.17/string/../sysdeps/x86_64/multiarch/../memset.S:memset (3x) [/lib/x86_64-linux-gnu/ld-2.17.so]

  1,008  *  /build/eglibc-TepTGA/eglibc-2.17/string/../string/memcmp.c:bcmp [/lib/x86_64-linux-gnu/ld-2.17.so]

  922  *  /build/eglibc-TepTGA/eglibc-2.17/elf/rtld.c:dl_main [/lib/x86_64-linux-gnu/ld-2.17.so]
  238  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-object.c:_dl_new_object (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  81  >   /build/eglibc-TepTGA/eglibc-2.17/string/../sysdeps/x86_64/multiarch/../rtld-strlen.S:strlen (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  76,461  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-reloc.c:_dl_relocate_object (4x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  7,131  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-deps.c:_dl_map_object_deps (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  2  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-debug.c:_dl_debug_state (2x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  226  >   /build/eglibc-TepTGA/eglibc-2.17/string/../string/memcmp.c:bcmp (3x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  2,345  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-error.c:_dl_receive_error (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  7  >   /build/eglibc-TepTGA/eglibc-2.17/string/../sysdeps/x86_64/multiarch/../strcmp.S:strcmp (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  132  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-tls.c:_dl_allocate_tls_init (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  9  >   /build/eglibc-TepTGA/eglibc-2.17/io/../sysdeps/unix/syscall-template.S:access (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  25  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-debug.c:_dl_debug_initialize (2x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  1,431  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-load.c:_dl_init_paths (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  2,532  >   /build/eglibc-TepTGA/eglibc-2.17/elf/rtld.c:do_preload (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  15  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-cache.c:_dl_unload_cache (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  914  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-minimal.c:strsep (2x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  34  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-object.c:_dl_add_to_namespace_list (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  610  >   /build/eglibc-TepTGA/eglibc-2.17/elf/rtld.c:init_tls (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  21  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-tls.c:_dl_add_to_slotinfo (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  353  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-environ.c:_dl_next_ld_env_entry (3x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  25  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-lookup.c:_dl_setup_hash (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  79  >   /build/eglibc-TepTGA/eglibc-2.17/elf/../sysdeps/unix/sysv/linux/dl-sysdep.c:_dl_discover_osversion (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  1  >   /build/eglibc-TepTGA/eglibc-2.17/elf/../elf/dl-sysdep.c:_dl_sysdep_start_cleanup (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  47  >   /build/eglibc-TepTGA/eglibc-2.17/string/../sysdeps/x86_64/multiarch/../memcpy.S:memcpy (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]

  896  *  /build/eglibc-TepTGA/eglibc-2.17/string/../sysdeps/x86_64/multiarch/../cacheinfo.c:intel_check_word [/lib/x86_64-linux-gnu/libc-2.17.so]
  2,468  >   /build/eglibc-TepTGA/eglibc-2.17/stdlib/bsearch.c:bsearch (16x) [/lib/x86_64-linux-gnu/libc-2.17.so]

  849  *  /build/eglibc-TepTGA/eglibc-2.17/elf/dl-cache.c:_dl_cache_libcmp [/lib/x86_64-linux-gnu/ld-2.17.so]
  6  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-cache.c:_dl_cache_libcmp'2 (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]

  730  *  /build/eglibc-TepTGA/eglibc-2.17/string/../sysdeps/x86_64/multiarch/../rtld-strlen.S:strlen [/lib/x86_64-linux-gnu/ld-2.17.so]

  648  *  /build/eglibc-TepTGA/eglibc-2.17/string/../sysdeps/x86_64/multiarch/../cacheinfo.c:intel_02_known_compare [/lib/x86_64-linux-gnu/libc-2.17.so]

  648  *  /build/eglibc-TepTGA/eglibc-2.17/elf/../elf/dl-runtime.c:_dl_fixup [/lib/x86_64-linux-gnu/ld-2.17.so]
  5,352  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-lookup.c:_dl_lookup_symbol_x (8x) [/lib/x86_64-linux-gnu/ld-2.17.so]

  606  *  /build/eglibc-TepTGA/eglibc-2.17/elf/dl-minimal.c:__libc_memalign [/lib/x86_64-linux-gnu/ld-2.17.so]
  18  >   /build/eglibc-TepTGA/eglibc-2.17/misc/../sysdeps/unix/syscall-template.S:mmap (3x) [/lib/x86_64-linux-gnu/ld-2.17.so]

  586  *  /build/eglibc-TepTGA/eglibc-2.17/elf/dl-object.c:_dl_new_object [/lib/x86_64-linux-gnu/ld-2.17.so]
  71  >   /build/eglibc-TepTGA/eglibc-2.17/string/../sysdeps/x86_64/memcpy.S:mempcpy (2x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  120  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-minimal.c:calloc (3x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  58  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-minimal.c:malloc (2x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  298  >   /build/eglibc-TepTGA/eglibc-2.17/string/../sysdeps/x86_64/multiarch/../rtld-strlen.S:strlen (5x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  88  >   /build/eglibc-TepTGA/eglibc-2.17/string/../sysdeps/x86_64/multiarch/../memcpy.S:memcpy (3x) [/lib/x86_64-linux-gnu/ld-2.17.so]

  549  *  /build/eglibc-TepTGA/eglibc-2.17/elf/get-dynamic-info.h:_dl_map_object_from_fd

  520  *  /build/eglibc-TepTGA/eglibc-2.17/elf/dl-load.c:open_verify [/lib/x86_64-linux-gnu/ld-2.17.so]
  562  >   /build/eglibc-TepTGA/eglibc-2.17/string/../string/memcmp.c:bcmp (7x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  10  >   /build/eglibc-TepTGA/eglibc-2.17/io/../sysdeps/unix/syscall-template.S:read (2x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  46  >   /build/eglibc-TepTGA/eglibc-2.17/io/../sysdeps/unix/syscall-template.S:open (6x) [/lib/x86_64-linux-gnu/ld-2.17.so]

  512  *  /build/eglibc-TepTGA/eglibc-2.17/string/../sysdeps/x86_64/multiarch/../memset.S:memset [/lib/x86_64-linux-gnu/ld-2.17.so]

  458  *  /build/eglibc-TepTGA/eglibc-2.17/elf/dl-reloc.c:_dl_relocate_object [/lib/x86_64-linux-gnu/ld-2.17.so]
  72  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-reloc.c:_dl_protect_relro (3x) [/lib/x86_64-linux-gnu/ld-2.17.so]

  450  *  /build/eglibc-TepTGA/eglibc-2.17/elf/dl-load.c:_dl_map_object [/lib/x86_64-linux-gnu/ld-2.17.so]
  18  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-load.c:cache_rpath (3x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  3,292  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-load.c:_dl_map_object_from_fd (2x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  63  >   /build/eglibc-TepTGA/eglibc-2.17/string/../sysdeps/x86_64/multiarch/../rtld-strlen.S:strlen (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  1,514  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-cache.c:_dl_load_cache_lookup (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  492  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-misc.c:_dl_name_match_p (7x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  21  >   /build/eglibc-TepTGA/eglibc-2.17/string/../sysdeps/x86_64/multiarch/../strcmp.S:strcmp (2x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  732  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-load.c:open_path (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  62  >   /build/eglibc-TepTGA/eglibc-2.17/string/../sysdeps/x86_64/multiarch/../strchr.S:index (2x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  974  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-load.c:open_verify (2x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  239  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-load.c:expand_dynamic_string_token (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  186  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-load.c:local_strdup (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]

  411  *  /build/eglibc-TepTGA/eglibc-2.17/elf/../elf/dl-sysdep.c:_dl_sysdep_start [/lib/x86_64-linux-gnu/ld-2.17.so]
  17  >   /build/eglibc-TepTGA/eglibc-2.17/elf/../misc/sbrk.c:sbrk (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  39  >   /build/eglibc-TepTGA/eglibc-2.17/string/../sysdeps/x86_64/multiarch/../rtld-strlen.S:strlen (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  93,880  >   /build/eglibc-TepTGA/eglibc-2.17/elf/rtld.c:dl_main (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]

  405  *  /build/eglibc-TepTGA/eglibc-2.17/string/../sysdeps/x86_64/multiarch/../memcpy.S:memcpy [/lib/x86_64-linux-gnu/ld-2.17.so]

  377  *  /build/eglibc-TepTGA/eglibc-2.17/string/../sysdeps/x86_64/memcpy.S:mempcpy [/lib/x86_64-linux-gnu/ld-2.17.so]

  363  *  /build/eglibc-TepTGA/eglibc-2.17/elf/dl-cache.c:_dl_load_cache_lookup [/lib/x86_64-linux-gnu/ld-2.17.so]
  67  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-misc.c:_dl_sysdep_read_whole_file (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  9  >   /build/eglibc-TepTGA/eglibc-2.17/io/../sysdeps/unix/syscall-template.S:access (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  855  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-cache.c:_dl_cache_libcmp (12x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  220  >   /build/eglibc-TepTGA/eglibc-2.17/string/../string/memcmp.c:bcmp (2x) [/lib/x86_64-linux-gnu/ld-2.17.so]

  353  *  /build/eglibc-TepTGA/eglibc-2.17/elf/dl-environ.c:_dl_next_ld_env_entry [/lib/x86_64-linux-gnu/ld-2.17.so]

  349  *  /build/eglibc-TepTGA/eglibc-2.17/elf/dl-load.c:_dl_init_paths [/lib/x86_64-linux-gnu/ld-2.17.so]
  48  >   /build/eglibc-TepTGA/eglibc-2.17/string/../sysdeps/x86_64/multiarch/../rtld-strlen.S:strlen (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  25  >   /build/eglibc-TepTGA/eglibc-2.17/string/../sysdeps/x86_64/multiarch/../strchr.S:index (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  111  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-minimal.c:malloc (3x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  339  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-hwcaps.c:_dl_important_hwcaps (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  31  >   /build/eglibc-TepTGA/eglibc-2.17/string/../sysdeps/x86_64/multiarch/../memcpy.S:memcpy (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  528  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-load.c:fillin_rpath (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]

  325  *  /build/eglibc-TepTGA/eglibc-2.17/elf/dl-tls.c:_dl_allocate_tls_storage [/lib/x86_64-linux-gnu/ld-2.17.so]
  50  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-minimal.c:__libc_memalign (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  57  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-tls.c:allocate_dtv (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]

  311  *  /build/eglibc-TepTGA/eglibc-2.17/elf/dl-load.c:open_path [/lib/x86_64-linux-gnu/ld-2.17.so]
  164  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-load.c:open_verify (4x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  49  >   /build/eglibc-TepTGA/eglibc-2.17/io/../sysdeps/unix/sysv/linux/wordsize-64/xstat.c:_xstat (4x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  208  >   /build/eglibc-TepTGA/eglibc-2.17/string/../sysdeps/x86_64/memcpy.S:mempcpy (9x) [/lib/x86_64-linux-gnu/ld-2.17.so]

  287  *  /build/eglibc-TepTGA/eglibc-2.17/string/../sysdeps/x86_64/multiarch/../cacheinfo.c:init_cacheinfo [/lib/x86_64-linux-gnu/libc-2.17.so]
  3,544  >   /build/eglibc-TepTGA/eglibc-2.17/string/../sysdeps/x86_64/multiarch/../cacheinfo.c:handle_intel (4x) [/lib/x86_64-linux-gnu/libc-2.17.so]
  74  >   /build/eglibc-TepTGA/eglibc-2.17/csu/../sysdeps/x86_64/multiarch/init-arch.c:__init_cpu_features (1x) [/lib/x86_64-linux-gnu/libc-2.17.so]

  270  *  /build/eglibc-TepTGA/eglibc-2.17/elf/dl-fini.c:_dl_fini [/lib/x86_64-linux-gnu/ld-2.17.so]
  774  >   ???:0x0000000000000630 (1x) [/usr/lib/valgrind/vgpreload_core-amd64-linux.so]
  3  >   ???:0x0000000004a247e8 (1x) [???]
  16  >   ???:0x0000000000400700 (1x) [/tmp/play]
  2  >   /build/eglibc-TepTGA/eglibc-2.17/elf/rtld.c:rtld_lock_default_lock_recursive (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  3  >   ???:0x0000000000400944 (1x) [???]
  2  >   /build/eglibc-TepTGA/eglibc-2.17/elf/rtld.c:rtld_lock_default_unlock_recursive (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  232  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-fini.c:_dl_sort_fini (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]

  266  *  /build/eglibc-TepTGA/eglibc-2.17/elf/get-dynamic-info.h:_dl_start

  257  *  /build/eglibc-TepTGA/eglibc-2.17/elf/dl-hwcaps.c:_dl_important_hwcaps [/lib/x86_64-linux-gnu/ld-2.17.so]
  44  >   /build/eglibc-TepTGA/eglibc-2.17/string/../sysdeps/x86_64/memcpy.S:mempcpy (2x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  29  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-minimal.c:malloc (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  9  >   /build/eglibc-TepTGA/eglibc-2.17/io/../sysdeps/unix/syscall-template.S:access (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]

  234  *  /build/eglibc-TepTGA/eglibc-2.17/elf/get-dynamic-info.h:dl_main

  232  *  /build/eglibc-TepTGA/eglibc-2.17/elf/dl-init.c:call_init [/lib/x86_64-linux-gnu/ld-2.17.so]
  4  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-altinit.c:dlinit_alt (1x) [/lib/x86_64-linux-gnu/libc-2.17.so]
  6  >   ???:0x0000000004a24560 (1x) [???]
  16  >   ???:0x0000000000000670 (1x) [/usr/lib/valgrind/vgpreload_core-amd64-linux.so]
  3,905  >   /build/eglibc-TepTGA/eglibc-2.17/string/../sysdeps/x86_64/multiarch/../cacheinfo.c:init_cacheinfo (2x) [/lib/x86_64-linux-gnu/libc-2.17.so]
  188  >   /build/eglibc-TepTGA/eglibc-2.17/csu/../csu/init-first.c:_init (1x) [/lib/x86_64-linux-gnu/libc-2.17.so]

  211  *  /build/eglibc-TepTGA/eglibc-2.17/elf/../sysdeps/x86_64/dl-machine.h:_dl_start

  206  *  /build/eglibc-TepTGA/eglibc-2.17/stdio-common/vfprintf.c:vfprintf [/lib/x86_64-linux-gnu/libc-2.17.so]
  14  >   /build/eglibc-TepTGA/eglibc-2.17/malloc/malloc.c:free (2x) [/lib/x86_64-linux-gnu/libc-2.17.so]
  613  >   /build/eglibc-TepTGA/eglibc-2.17/elf/../sysdeps/x86_64/dl-trampoline.S:_dl_runtime_resolve (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  155  >   /build/eglibc-TepTGA/eglibc-2.17/libio/genops.c:_IO_default_xsputn (3x) [/lib/x86_64-linux-gnu/libc-2.17.so]

  198  *  /build/eglibc-TepTGA/eglibc-2.17/string/../sysdeps/x86_64/multiarch/../strchr.S:index [/lib/x86_64-linux-gnu/ld-2.17.so]

  185  *  /build/eglibc-TepTGA/eglibc-2.17/elf/dl-version.c:match_symbol [/lib/x86_64-linux-gnu/ld-2.17.so]
  258  >   /build/eglibc-TepTGA/eglibc-2.17/string/../sysdeps/x86_64/multiarch/../strcmp.S:strcmp (3x) [/lib/x86_64-linux-gnu/ld-2.17.so]

  181  *  /build/eglibc-TepTGA/eglibc-2.17/elf/dl-fini.c:_dl_sort_fini [/lib/x86_64-linux-gnu/ld-2.17.so]
  51  >   /build/eglibc-TepTGA/eglibc-2.17/string/../sysdeps/x86_64/multiarch/../memset.S:memset (3x) [/lib/x86_64-linux-gnu/ld-2.17.so]

  180  *  /build/eglibc-TepTGA/eglibc-2.17/string/../sysdeps/x86_64/multiarch/../cacheinfo.c:handle_intel [/lib/x86_64-linux-gnu/libc-2.17.so]
  3,364  >   /build/eglibc-TepTGA/eglibc-2.17/string/../sysdeps/x86_64/multiarch/../cacheinfo.c:intel_check_word (8x) [/lib/x86_64-linux-gnu/libc-2.17.so]

  175  *  /build/eglibc-TepTGA/eglibc-2.17/elf/rtld.c:_dl_start [/lib/x86_64-linux-gnu/ld-2.17.so]
  25  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-lookup.c:_dl_setup_hash (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  94,365  >   /build/eglibc-TepTGA/eglibc-2.17/elf/../elf/dl-sysdep.c:_dl_sysdep_start (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]

  168  *  /build/eglibc-TepTGA/eglibc-2.17/elf/../sysdeps/x86_64/dl-trampoline.S:_dl_runtime_resolve [/lib/x86_64-linux-gnu/ld-2.17.so]
  6,028  >   /build/eglibc-TepTGA/eglibc-2.17/elf/../elf/dl-runtime.c:_dl_fixup (8x) [/lib/x86_64-linux-gnu/ld-2.17.so]

  155  *  /build/eglibc-TepTGA/eglibc-2.17/libio/genops.c:_IO_default_xsputn [/lib/x86_64-linux-gnu/libc-2.17.so]

  148  *  /build/eglibc-TepTGA/eglibc-2.17/csu/../sysdeps/x86_64/multiarch/init-arch.c:__init_cpu_features [/lib/x86_64-linux-gnu/libc-2.17.so]

  146  *  /build/eglibc-TepTGA/eglibc-2.17/elf/do-rel.h:_dl_start

  137  *  /build/eglibc-TepTGA/eglibc-2.17/elf/dl-load.c:fillin_rpath [/lib/x86_64-linux-gnu/ld-2.17.so]
  44  >   /build/eglibc-TepTGA/eglibc-2.17/string/../sysdeps/x86_64/multiarch/../rtld-strlen.S:strlen (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  31  >   /build/eglibc-TepTGA/eglibc-2.17/string/../sysdeps/x86_64/memcpy.S:mempcpy (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  29  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-minimal.c:malloc (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  287  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-minimal.c:strsep (2x) [/lib/x86_64-linux-gnu/ld-2.17.so]

  111  *  /build/eglibc-TepTGA/eglibc-2.17/elf/dl-error.c:_dl_catch_error [/lib/x86_64-linux-gnu/ld-2.17.so]
  2,447  >   /build/eglibc-TepTGA/eglibc-2.17/elf/rtld.c:map_doit (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  57  >   /build/eglibc-TepTGA/eglibc-2.17/setjmp/../sysdeps/x86_64/setjmp.S:__sigsetjmp (3x) [/lib/x86_64-linux-gnu/libc-2.17.so]
  6  >   /build/eglibc-TepTGA/eglibc-2.17/elf/rtld.c:_dl_initial_error_catch_tsd (3x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  5,642  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-deps.c:openaux (2x) [/lib/x86_64-linux-gnu/ld-2.17.so]

  106  *  /build/eglibc-TepTGA/eglibc-2.17/elf/dl-object.c:_dl_add_to_namespace_list [/lib/x86_64-linux-gnu/ld-2.17.so]
  6  >   /build/eglibc-TepTGA/eglibc-2.17/elf/rtld.c:rtld_lock_default_lock_recursive (3x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  6  >   /build/eglibc-TepTGA/eglibc-2.17/elf/rtld.c:rtld_lock_default_unlock_recursive (3x) [/lib/x86_64-linux-gnu/ld-2.17.so]

  100  *  /build/eglibc-TepTGA/eglibc-2.17/elf/dl-lookup.c:_dl_setup_hash [/lib/x86_64-linux-gnu/ld-2.17.so]

  88  *  /build/eglibc-TepTGA/eglibc-2.17/libio/genops.c:_IO_flush_all_lockp [/lib/x86_64-linux-gnu/libc-2.17.so]

  82  *  /build/eglibc-TepTGA/eglibc-2.17/elf/dl-tls.c:_dl_allocate_tls_init [/lib/x86_64-linux-gnu/ld-2.17.so]
  23  >   /build/eglibc-TepTGA/eglibc-2.17/string/../sysdeps/x86_64/memcpy.S:mempcpy (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  27  >   /build/eglibc-TepTGA/eglibc-2.17/string/../sysdeps/x86_64/multiarch/../memset.S:memset (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]

  78  *  /build/eglibc-TepTGA/eglibc-2.17/elf/dl-init.c:_dl_init [/lib/x86_64-linux-gnu/ld-2.17.so]
  4,351  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-init.c:call_init (5x) [/lib/x86_64-linux-gnu/ld-2.17.so]

  75  *  /build/eglibc-TepTGA/eglibc-2.17/elf/dl-version.c:_dl_check_all_versions [/lib/x86_64-linux-gnu/ld-2.17.so]
  2,230  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-version.c:_dl_check_map_versions (4x) [/lib/x86_64-linux-gnu/ld-2.17.so]

  75  *  /build/eglibc-TepTGA/eglibc-2.17/setjmp/../sysdeps/x86_64/setjmp.S:__sigsetjmp [/lib/x86_64-linux-gnu/libc-2.17.so]
  9  >   /build/eglibc-TepTGA/eglibc-2.17/setjmp/sigjmp.c:__sigjmp_save (1x) [/lib/x86_64-linux-gnu/libc-2.17.so]

  74  *  /build/eglibc-TepTGA/eglibc-2.17/elf/../sysdeps/unix/sysv/linux/dl-sysdep.c:_dl_discover_osversion [/lib/x86_64-linux-gnu/ld-2.17.so]
  5  >   /build/eglibc-TepTGA/eglibc-2.17/posix/../sysdeps/unix/syscall-template.S:uname (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]

  73  *  /build/eglibc-TepTGA/eglibc-2.17/elf/dl-tls.c:_dl_determine_tlsoffset [/lib/x86_64-linux-gnu/ld-2.17.so]

  72  *  /build/eglibc-TepTGA/eglibc-2.17/elf/dl-minimal.c:calloc [/lib/x86_64-linux-gnu/ld-2.17.so]
  262  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-minimal.c:malloc (8x) [/lib/x86_64-linux-gnu/ld-2.17.so]

  67  *  /build/eglibc-TepTGA/eglibc-2.17/elf/rtld.c:init_tls [/lib/x86_64-linux-gnu/ld-2.17.so]
  38  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-minimal.c:calloc (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  432  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-tls.c:_dl_allocate_tls_storage (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  73  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-tls.c:_dl_determine_tlsoffset (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]

  60  *  /build/eglibc-TepTGA/eglibc-2.17/csu/libc-start.c:(below main) [/lib/x86_64-linux-gnu/libc-2.17.so]
  5,218  >   /tmp/play.c:main (1x)
  55  >   ???:__libc_csu_init (1x) [/tmp/play]
  64  >   /build/eglibc-TepTGA/eglibc-2.17/stdlib/cxa_atexit.c:__cxa_atexit (1x) [/lib/x86_64-linux-gnu/libc-2.17.so]
  29  >   /build/eglibc-TepTGA/eglibc-2.17/setjmp/../sysdeps/x86_64/bsd-_setjmp.S:_setjmp (1x) [/lib/x86_64-linux-gnu/libc-2.17.so]
  1,500  >   /build/eglibc-TepTGA/eglibc-2.17/stdlib/exit.c:exit (1x) [/lib/x86_64-linux-gnu/libc-2.17.so]

  60  *  /build/eglibc-TepTGA/eglibc-2.17/elf/dl-minimal.c:malloc [/lib/x86_64-linux-gnu/ld-2.17.so]
  574  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-minimal.c:__libc_memalign (20x) [/lib/x86_64-linux-gnu/ld-2.17.so]

  57  *  /build/eglibc-TepTGA/eglibc-2.17/elf/dl-reloc.c:_dl_protect_relro [/lib/x86_64-linux-gnu/ld-2.17.so]
  15  >   /build/eglibc-TepTGA/eglibc-2.17/misc/../sysdeps/unix/syscall-template.S:mprotect (3x) [/lib/x86_64-linux-gnu/ld-2.17.so]

  54  *  /build/eglibc-TepTGA/eglibc-2.17/misc/../sysdeps/unix/syscall-template.S:mmap [/lib/x86_64-linux-gnu/ld-2.17.so]

  51  *  /build/eglibc-TepTGA/eglibc-2.17/stdlib/exit.c:__run_exit_handlers [/lib/x86_64-linux-gnu/libc-2.17.so]
  1,302  >   /build/eglibc-TepTGA/eglibc-2.17/elf/dl-fini.c:_dl_fini (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  138  >   /build/eglibc-TepTGA/eglibc-2.17/libio/genops.c:_IO_cleanup (1x) [/lib/x86_64-linux-gnu/libc-2.17.so]
  5  >   /build/eglibc-TepTGA/eglibc-2.17/posix/../sysdeps/unix/sysv/linux/_exit.c:_Exit (1x) [/lib/x86_64-linux-gnu/libc-2.17.so]

  51  *  /build/eglibc-TepTGA/eglibc-2.17/io/../sysdeps/unix/syscall-template.S:open [/lib/x86_64-linux-gnu/ld-2.17.so]

  50  *  /build/eglibc-TepTGA/eglibc-2.17/libio/genops.c:_IO_cleanup [/lib/x86_64-linux-gnu/libc-2.17.so]
  88  >   /build/eglibc-TepTGA/eglibc-2.17/libio/genops.c:_IO_flush_all_lockp (1x) [/lib/x86_64-linux-gnu/libc-2.17.so]

  49  *  /build/eglibc-TepTGA/eglibc-2.17/io/../sysdeps/unix/sysv/linux/wordsize-64/xstat.c:_xstat [/lib/x86_64-linux-gnu/ld-2.17.so]

  47  *  /build/eglibc-TepTGA/eglibc-2.17/stdlib/cxa_finalize.c:__cxa_finalize [/lib/x86_64-linux-gnu/libc-2.17.so]
  7  >   /build/eglibc-TepTGA/eglibc-2.17/nptl/../nptl/sysdeps/unix/sysv/linux/unregister-atfork.c:__unregister_atfork (1x) [/lib/x86_64-linux-gnu/libc-2.17.so]

  46  *  /build/eglibc-TepTGA/eglibc-2.17/string/../sysdeps/x86_64/strchrnul.S:strchrnul [/lib/x86_64-linux-gnu/libc-2.17.so]

  44  *  /build/eglibc-TepTGA/eglibc-2.17/csu/../sysdeps/generic/dl-hash.h:_init

  44  *  /build/eglibc-TepTGA/eglibc-2.17/time/../sysdeps/generic/dl-hash.h:gettimeofday

  44  *  /build/eglibc-TepTGA/eglibc-2.17/time/../sysdeps/generic/dl-hash.h:time

  44  *  play.c:main [/tmp/play]
  14  >   /build/eglibc-TepTGA/eglibc-2.17/string/../sysdeps/x86_64/multiarch/strlen-sse2-pminub.S:__strlen_sse2_pminub (1x) [/lib/x86_64-linux-gnu/libc-2.17.so]
  21  >   /build/eglibc-TepTGA/eglibc-2.17/string/../sysdeps/x86_64/multiarch/strcpy-sse2-unaligned.S:__strcpy_sse2_unaligned (1x) [/lib/x86_64-linux-gnu/libc-2.17.so]
  7  >   /build/eglibc-TepTGA/eglibc-2.17/io/../sysdeps/unix/syscall-template.S:write (1x) [/lib/x86_64-linux-gnu/libc-2.17.so]
  1,188  >   /build/eglibc-TepTGA/eglibc-2.17/stdio-common/sprintf.c:sprintf (1x) [/lib/x86_64-linux-gnu/libc-2.17.so]
  3,937  >   /build/eglibc-TepTGA/eglibc-2.17/elf/../sysdeps/x86_64/dl-trampoline.S:_dl_runtime_resolve (5x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  7  >   /build/eglibc-TepTGA/eglibc-2.17/io/../sysdeps/unix/syscall-template.S:creat (1x) [/lib/x86_64-linux-gnu/libc-2.17.so]

  41  *  /build/eglibc-TepTGA/eglibc-2.17/elf/dl-misc.c:_dl_sysdep_read_whole_file [/lib/x86_64-linux-gnu/ld-2.17.so]
  5  >   /build/eglibc-TepTGA/eglibc-2.17/io/../sysdeps/unix/syscall-template.S:close (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  10  >   /build/eglibc-TepTGA/eglibc-2.17/io/../sysdeps/unix/sysv/linux/wordsize-64/fxstat.c:_fxstat (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  6  >   /build/eglibc-TepTGA/eglibc-2.17/misc/../sysdeps/unix/syscall-template.S:mmap (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]
  5  >   /build/eglibc-TepTGA/eglibc-2.17/io/../sysdeps/unix/syscall-template.S:open (1x) [/lib/x86_64-linux-gnu/ld-2.17.so]

  41  *  /build/eglibc-TepTGA/eglibc-2.17/elf/dl-debug.c:_dl_debug_initialize [/lib/x86_64-linux-gnu/ld-2.17.so]

  38  *  /build/eglibc-TepTGA/eglibc-2.17/stdlib/cxa_atexit.c:__new_exitfn [/lib/x86_64-linux-gnu/libc-2.17.so]

  36  *  /build/eglibc-TepTGA/eglibc-2.17/libio/iovsprintf.c:vsprintf [/lib/x86_64-linux-gnu/libc-2.17.so]
  52  >   /build/eglibc-TepTGA/eglibc-2.17/libio/strops.c:_IO_str_init_static_internal (1x) [/lib/x86_64-linux-gnu/libc-2.17.so]
  41  >   /build/eglibc-TepTGA/eglibc-2.17/libio/genops.c:_IO_no_init (1x) [/lib/x86_64-linux-gnu/libc-2.17.so]
  1,042  >   /build/eglibc-TepTGA/eglibc-2.17/stdio-common/vfprintf.c:vfprintf (1x) [/lib/x86_64-linux-gnu/libc-2.17.so]

  35  *  /build/eglibc-TepTGA/eglibc-2.17/libio/strops.c:_IO_str_init_static_internal [/lib/x86_64-linux-gnu/libc-2.17.so]
  17  >   /build/eglibc-TepTGA/eglibc-2.17/libio/genops.c:_IO_setb (1x) [/lib/x86_64-linux-gnu/libc-2.17.so]
  [to be continued]

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
