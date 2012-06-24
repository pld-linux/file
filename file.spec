Summary:	file(1) command
Summary(de):	Befehl file(1)
Summary(fr):	Commande file(1)
Summary(pl):	komenda file(1)
Summary(tr):	Dosya tipini belirleme arac�
Name:		file
Version:	3.35
Release:	3
License:	Distributable
Group:		Applications/File
Group(de):	Applikationen/Datei
Group(pl):	Aplikacje/Pliki
Source0:	ftp://ftp.astron.com/pub/file/%{name}-%{version}.tar.gz
Source1:	zisofs.magic
Source2:	magic.mime
Source3:	file.1.pl
Source4:	magic.5.pl
Patch0:		%{name}-sparc.patch
Patch1:		%{name}-tfm.patch
Patch2:		%{name}-ia64.patch
Patch3:		%{name}-magic5.patch
Patch4:		%{name}-fnovfl.patch
Patch5:		%{name}-elf.patch
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
Sie k�nnen dieses Paket verwenden, um zu bestimmen, welches Format
eine bestimmte Datei hat. Wird durch fsck eine Datei in lost+found
gespeichert, k�nnen Sie 'file' ausf�hren, um herauszufinden, ob Sie
sie mit 'more' einsehen k�nnen, oder ob es sich um ein Bin�rprogramm
handelt Das Programm erkennt u.a. ELF-Bin�rprogramme,
System-Libraries, RPM-Pakete und viele Grafikformate.

%description -l fr
Ce paquetage sert � trouver le type du fichier que vous recherchez sur
votre syst�me. Par exemple, si un fsck fait qu'un fichier a �t� stock�
dans lost+found, vous pouvez lancer file dessus pour savoir si on peut
faire un more, ou s'il s'agit d'un binaire. Il reconna�t de nombreux
types de fichiers dont les binaires ELF, les biblioth�ques syst�mes,
les paquetages RPM et de nombreux formats graphiques diff�rents.

%description -l pl
Pakiet ten jest przydatny je�eli chcesz rozpozna� typ plik�w w twoim
systemie. Na przyk�ad je�eli fsck zdeponuje jakie� pliki w katalogu
lost+found, mo�esz uruchomi� file na zdeponowanym pliku i zobaczy�
jaki to jest typ pliku, jest to metoda bezpieczniejsza ni� 'more', ze
wzgl�du na to, �e to mo�e by� plik binarny. File potrafi rozpozna�
wiele typ�w plik�w np. binarny ELF, biblioteki systemowe, pakiety RPM
oraz wiele r�nych format�w graficznych i d�wi�kowych.

%description -l tr
file, bir dosyay� inceleyerek ne t�r bir dosya oldu�u konusunda size
bir fikir verebilir. B�ylece uzant�s�ndan ve ad�ndan ne oldu�unu
��karamad���n�z bir dosyay� hangi yaz�l�m ile kullanabilece�inize ya
da ne yapaca��n�za karar verebilisiniz. file, temel dosya tiplerini,
�o�u grafik format�n�, �al��t�r�labilir dosyalar�, sistem
kitapl�klar�n� vs. tan�yabilir.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1 -R

%build
aclocal
autoconf
rm -f install-sh missing mkinstalldirs
automake --copy --add-missing
%configure \
	--disable-elf
	
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/pl/man{1,5}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

cat %{SOURCE1} >>$RPM_BUILD_ROOT%{_datadir}/magic
install %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}

install %{SOURCE3} $RPM_BUILD_ROOT%{_mandir}/pl/man1/file.1
install %{SOURCE4} $RPM_BUILD_ROOT%{_mandir}/pl/man5/magick.5

./file -m $RPM_BUILD_ROOT%{_datadir}/magic -c -C

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/*
%{_datadir}/*
%{_mandir}/man[15]/*
%lang(pl) %{_mandir}/pl/man[15]/*
