Summary:	file(1) command
Summary(de):	Befehl file(1)
Summary(fr):	Commande file(1)
Summary(pl):	Komenda file(1)
Summary(tr):	Dosya tipini belirleme aracý
Name:		file
Version:	3.37
Release:	4
License:	distributable
Group:		Applications/File
Source0:	ftp://ftp.astron.com/pub/file/%{name}-%{version}.tar.gz
Source1:	zisofs.magic
Source2:	magic.mime
Source3:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
Source4:	%{name}-magic.mscompress
Patch0:		%{name}-sparc.patch
Patch1:		%{name}-tfm.patch
Patch2:		%{name}-ia64.patch
Patch3:		%{name}-elf.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Conflicts:	xdelta < 1.0.0

%define		_datadir	%{_prefix}/share/misc

%description
This package is useful for finding out what type of file you are
looking at on your system. For example, if an fsck results in a file
being stored in lost+found, you can run file on it to find out if it's
safe to 'more' it or if it's a binary. It recognizes many file types,
including ELF binaries, system libraries, RPM packages, and many
different graphics formats.

%description -l de
Sie können dieses Paket verwenden, um zu bestimmen, welches Format
eine bestimmte Datei hat. Wird durch fsck eine Datei in lost+found
gespeichert, können Sie 'file' ausführen, um herauszufinden, ob Sie
sie mit 'more' einsehen können, oder ob es sich um ein Binärprogramm
handelt Das Programm erkennt u.a. ELF-Binärprogramme,
System-Libraries, RPM-Pakete und viele Grafikformate.

%description -l fr
Ce paquetage sert à trouver le type du fichier que vous recherchez sur
votre système. Par exemple, si un fsck fait qu'un fichier a été stocké
dans lost+found, vous pouvez lancer file dessus pour savoir si on peut
faire un more, ou s'il s'agit d'un binaire. Il reconnaît de nombreux
types de fichiers dont les binaires ELF, les bibliothèques systèmes,
les paquetages RPM et de nombreux formats graphiques différents.

%description -l pl
Pakiet ten jest przydatny je¿eli chcesz rozpoznaæ typ plików w twoim
systemie. Na przyk³ad je¿eli fsck zdeponuje jakie¶ pliki w katalogu
lost+found, mo¿esz uruchomiæ file na zdeponowanym pliku i zobaczyæ
jaki to jest typ pliku, jest to metoda bezpieczniejsza ni¿ 'more', ze
wzglêdu na to, ¿e to mo¿e byæ plik binarny. File potrafi rozpoznaæ
wiele typów plików np. binarny ELF, biblioteki systemowe, pakiety RPM
oraz wiele ró¿nych formatów graficznych i d¼wiêkowych.

%description -l tr
file, bir dosyayý inceleyerek ne tür bir dosya olduðu konusunda size
bir fikir verebilir. Böylece uzantýsýndan ve adýndan ne olduðunu
çýkaramadýðýnýz bir dosyayý hangi yazýlým ile kullanabileceðinize ya
da ne yapacaðýnýza karar verebilisiniz. file, temel dosya tiplerini,
çoðu grafik formatýný, çalýþtýrýlabilir dosyalarý, sistem
kitaplýklarýný vs. tanýyabilir.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
aclocal
autoconf
rm -f install-sh missing mkinstalldirs
automake -a -c
%configure \
	--enable-fsect-man5
	
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

cat %{SOURCE1} %{SOURCE4} >>$RPM_BUILD_ROOT%{_datadir}/magic
# install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}

bzip2 -dc %{SOURCE3} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

./file -m $RPM_BUILD_ROOT%{_datadir}/magic -c -C

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/*
%{_datadir}/*
%{_mandir}/man[15]/*
%lang(de) %{_mandir}/de/man[15]/*
%lang(es) %{_mandir}/es/man[15]/*
%lang(fr) %{_mandir}/fr/man[15]/*
%lang(hu) %{_mandir}/hu/man[15]/*
%lang(it) %{_mandir}/it/man[15]/*
%lang(ja) %{_mandir}/ja/man[15]/*
%lang(nl) %{_mandir}/nl/man[15]/*
%lang(pl) %{_mandir}/pl/man[15]/*
