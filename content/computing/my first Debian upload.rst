my first Debian upload
======================

:date: 2013-10-13
:tags: Debian, wajig


Output of my first ever upload to Debian (using dput__)::

    Trying to upload package to ftp-master (ftp.upload.debian.org)
    Checking signature on .changes
    gpg: Signature made Sun 13 Oct 2013 09:21:35 SAST using RSA key ID 500BF4A2
    gpg: Good signature from "Tshepang Lekhonkhobe <tshepang@gmail.com>"
    Good signature on ../wajig_2.10_amd64.changes.
    Checking signature on .dsc
    gpg: Signature made Sun 13 Oct 2013 09:21:31 SAST using RSA key ID 500BF4A2
    gpg: Good signature from "Tshepang Lekhonkhobe <tshepang@gmail.com>"
    Good signature on ../wajig_2.10.dsc.
    Uploading to ftp-master (via ftp to ftp.upload.debian.org):
      Uploading wajig_2.10.dsc: done.
      Uploading wajig_2.10.tar.gz: done.
      Uploading wajig_2.10_all.deb: done.
      Uploading wajig_2.10_amd64.changes: done.
    Successfully uploaded packages.

(`the package was accepted within 30 minutes`__)

----

And, yeah, that means `I am now Debian Maintainer`__. Other than
giving me more freedom, this helps reduce the workload on `Dirk
Eddelbuettel`__, who has been uploading wajig for several years now. He
even `became an Advocate`__ for `my application`__.  This process
started several weeks ago when a Debian Developer named `Tristan
Seligmann`__ signed my key [#]_.


__ http://packages.debian.org/dput
__ http://packages.qa.debian.org/w/wajig/news/20131013T074831Z.html
__ http://bugs.debian.org/cgi-bin/bugreport.cgi?msg=12;bug=723802
__ http://dirk.eddelbuettel.com
__ http://lists.debian.org/debian-newmaint/2013/09/msg00029.html
__ http://lists.debian.org/debian-newmaint/2013/09/msg00028.html
__ http://mithrandi.net/blog

.. [#] before applying to be a Maintainer, a Debian Developer needs to
       sign your key as a way of verifying your identity
