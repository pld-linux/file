Summary:	file(1) command
Summary(de):	Befehl file(1)
Summary(fr):	Commande file(1)
Summary(pl):	komenda file(1)
Summary(tr):	Dosya tipini belirleme aracý
Name:		file
Version:	3.26
Release:	6
Copyright:	distributable
Group:		Utilities/File
Group(pl):	Narzêdzia/Pliki
Source0:	ftp://ftp.astron.com/pub/file/%{name}-%{version}.tar.gz
Source1:	file.gimp
Source2:	file.xdelta
Patch0:		file-fhs.patch
Patch1:		file-sparcv9.patch
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
%setup  -q
%patch0 -p1
%patch1 -p1

install %{SOURCE1} ./Magdir/gimp
install %{SOURCE2} ./Magdir/xdelta

%build
chmod +w configure && autoconf
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
    ./configure \
	--prefix=%{_prefix} \
	%{_target_platform}
	
make LDFLAGS="-s"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_prefix}/{bin,share/man/man{1,4}}

make \
    prefix=$RPM_BUILD_ROOT%{_prefix} \
    install

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man{1,4}/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/*
%{_datadir}/misc/*
%{_mandir}/man[14]/*
