Summary:	file(1) command
Summary(de):	Befehl file(1)
Summary(fr):	Commande file(1)
Summary(pl):	komenda file(1)
Summary(tr):	Dosya tipini belirleme arac�
Name:		file
Version:	3.26
Release:	6
Copyright:	distributable
Group:		Utilities/File
Group(pl):	Narz�dzia/Pliki
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
Sie k�nnen dieses Paket verwenden, um zu bestimmen, welches Format eine
bestimmte Datei hat. Wird durch fsck eine Datei in lost+found gespeichert,
k�nnen Sie 'file' ausf�hren, um herauszufinden, ob Sie sie mit 'more'
einsehen k�nnen, oder ob es sich um ein Bin�rprogramm handelt Das Programm
erkennt u.a. ELF-Bin�rprogramme, System-Libraries, RPM-Pakete und viele
Grafikformate.

%description -l fr
Ce paquetage sert � trouver le type du fichier que vous recherchez sur votre
syst�me. Par exemple, si un fsck fait qu'un fichier a �t� stock� dans
lost+found, vous pouvez lancer file dessus pour savoir si on peut faire un
more, ou s'il s'agit d'un binaire. Il reconna�t de nombreux types de
fichiers dont les binaires ELF, les biblioth�ques syst�mes, les paquetages
RPM et de nombreux formats graphiques diff�rents.

%description -l pl
Pakiet ten jest przydatny je�eli chcesz rozpozna� typ plik�w w twoim
systemie. Na przyk�ad je�eli fsck zdeponuje jakie� pliki w katalogu
lost+found, mo�esz uruchomi� file na zdeponowanym pliku i zobaczy� jaki to
jest typ pliku, jest to metoda bezpieczniejsza ni� 'more', ze wzgl�du na to,
�e to mo�e by� plik binarny. File potrafi rozpozna� wiele typ�w plik�w np.
binarny ELF, biblioteki systemowe, pakiety RPM oraz wiele r�nych format�w
graficznych i d�wi�kowych.

%description -l tr
file, bir dosyay� inceleyerek ne t�r bir dosya oldu�u konusunda size bir
fikir verebilir. B�ylece uzant�s�ndan ve ad�ndan ne oldu�unu ��karamad���n�z
bir dosyay� hangi yaz�l�m ile kullanabilece�inize ya da ne yapaca��n�za
karar verebilisiniz. file, temel dosya tiplerini, �o�u grafik format�n�,
�al��t�r�labilir dosyalar�, sistem kitapl�klar�n� vs. tan�yabilir.

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
