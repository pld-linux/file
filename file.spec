Summary:	file(1) command
Summary(de):	Befehl file(1)
Summary(fr):	Commande file(1)
Summary(pl):	komenda file(1)
Summary(tr):	Dosya tipini belirleme aracý
Name:		file
Version:	3.26
Release:	4
Copyright:	distributable
Group:		Utilities/File
Source0:	ftp://ftp.astron.com/pub/file/%{name}-%{version}.tar.gz
Source1:	file.gimp
Source2:	file.xdelta
Patch1:		file-glibc.patch
Buildroot:	/tmp/%{name}-%{version}-root
Conflicts:	xdelta < 1.0.0

%description
This package is useful for finding out what type of file you are looking at
on your system. For example, if an fsck results in a file being stored in
lost+found, you can run file on it to find out if it's safe to 'more' it or
if it's a binary. It recognizes many file types, including ELF binaries,
system libraries, RPM packages, and many different graphics formats.

%description -l de
Sie können dieses Paket verwenden, um zu bestimmen, welches Format eine
bestimmte Datei hat. Wird durch fsck eine Datei in lost+found gespeichert,
können Sie 'file' ausführen, um herauszufinden, ob Sie sie mit 'more'
einsehen können, oder ob es sich um ein Binärprogramm handelt Das Programm
erkennt u.a. ELF-Binärprogramme, System-Libraries, RPM-Pakete und viele
Grafikformate.

%description -l fr
Ce paquetage sert à trouver le type du fichier que vous recherchez sur votre
système. Par exemple, si un fsck fait qu'un fichier a été stocké dans
lost+found, vous pouvez lancer file dessus pour savoir si on peut faire un
more, ou s'il s'agit d'un binaire. Il reconnaît de nombreux types de
fichiers dont les binaires ELF, les bibliothèques systèmes, les paquetages
RPM et de nombreux formats graphiques différents.

%description -l pl
Pakiet ten jest przydatny je¿eli chcesz rozpoznaæ typ plików w twoim
systemie. Na przyk³ad je¿eli fsck zdeponuje jakie¶ pliki w katalogu
lost+found, mo¿esz uruchomiæ file na zdeponowanym pliku i zobaczyæ jaki to
jest typ pliku, jest to metoda bezpieczniejsza ni¿ 'more', ze wzglêdu na to,
¿e to mo¿e byæ plik binarny. File potrafi rozpoznaæ wiele typów plików np.
binarny ELF, biblioteki systemowe, pakiety RPM oraz wiele ró¿nych formatów
graficznych i d¼wiêkowych.

%description -l tr
file, bir dosyayý inceleyerek ne tür bir dosya olduðu konusunda size bir
fikir verebilir. Böylece uzantýsýndan ve adýndan ne olduðunu çýkaramadýðýnýz
bir dosyayý hangi yazýlým ile kullanabileceðinize ya da ne yapacaðýnýza
karar verebilisiniz. file, temel dosya tiplerini, çoðu grafik formatýný,
çalýþtýrýlabilir dosyalarý, sistem kitaplýklarýný vs. tanýyabilir.

%prep
%setup -q
%patch1 -p1 -b .glibc

install %{SOURCE1} ./Magdir/gimp
install %{SOURCE2} ./Magdir/xdelta

%build
CFLAGS="$RPM_OPT_FLAGS" \
./configure \
	--prefix=/usr
make LDFLAGS="-s"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/man
make prefix=$RPM_BUILD_ROOT/usr install

gzip -9nf $RPM_BUILD_ROOT/usr/man/man{1,4}/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(755, root, root) /usr/bin/file
%attr(644, root, root) /usr/share/magic
/usr/man/man[14]/*

%changelog
* Thu Mar 11 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [3.26-4]
- removed man group from man pages.

* Wed Dec 23 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [3.26-3]
- added gzipping man pages,
- added LDFLAGS="-s" make parameter.

* Thu Nov 26 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [3.26-2]
- updated file.xdelta from xdelta-1.0.0 and added
  "Conflicts: xdelta < 1.0.0".

* Fri Sep 18 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [3.26-1]
- added -q %setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- corrected group on man pages,
- updated base Source Url to ftp://ftp.astron.com/pub/file/,
- added xdelta magic,
- added stripping /usr/bin/file,
- removed %defattr,
- added using %%{name} and %%{version} in Source.

* Mon Aug 24 1998 Jeff Johnson <jbj@redhat.com>
  [3.25-1]
- update to 3.25.
- detect gimp XCF versions.

* Thu Jul 23 1998 Wojtek Slusarczyk <wojtek@shadow.eu.org>
  [3.24-2]
- build against glibc-2.1,
- added pl translation,
- moved %changelog at the end of spec.

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 08 1998 Erik Troan <ewt@redhat.com>
- updated to 3.24
- buildrooted

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Mon Mar 31 1997 Erik Troan <ewt@redhat.com>
  Fixed problems caused by 64 bit time_t.

* Thu Mar 06 1997 Michael K. Johnson <johnsonm@redhat.com>
  Improved recognition of Linux kernel images.
