Summary:	file(1) command
Summary(de):	Befehl file(1)
Summary(es):	Comando file
Summary(fr):	Commande file(1)
Summary(pl):	Polecenie file(1)
Summary(pt_BR):	Um utilitАrio para determinar tipos de arquivos
Summary(tr):	Dosya tipini belirleme aracЩ
Summary(ru):	Утилита для определения типов файлов
Summary(uk):	Утил╕та для визначення тип╕в файл╕в
Name:		file
Version:	3.38
Release:	1
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
Patch4:		%{name}-man.patch
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
Sie kЖnnen dieses Paket verwenden, um zu bestimmen, welches Format
eine bestimmte Datei hat. Wird durch fsck eine Datei in lost+found
gespeichert, kЖnnen Sie 'file' ausfЭhren, um herauszufinden, ob Sie
sie mit 'more' einsehen kЖnnen, oder ob es sich um ein BinДrprogramm
handelt Das Programm erkennt u.a. ELF-BinДrprogramme,
System-Libraries, RPM-Pakete und viele Grafikformate.

%description -l es
Este paquete es Зtil para descubrir que tipo de archivo estАs buscando
en tu sistema. Por ejemplo, si fsck resulta un archivo que fue
almacenado en el "lost+found", tu puedes ejecutar file en Иl para
descubrir si es seguro leerlo con el "more" o si es un binario.
Reconoce varios tipos de archivos, incluyendo binarios ELF,
bibliotecas de sistema, paquetes RPM y varios formatos grАficos
diferentes.

%description -l fr
Ce paquetage sert Ю trouver le type du fichier que vous recherchez sur
votre systХme. Par exemple, si un fsck fait qu'un fichier a ИtИ stockИ
dans lost+found, vous pouvez lancer file dessus pour savoir si on peut
faire un more, ou s'il s'agit d'un binaire. Il reconnaНt de nombreux
types de fichiers dont les binaires ELF, les bibliothХques systХmes,
les paquetages RPM et de nombreux formats graphiques diffИrents.

%description -l pl
Pakiet ten jest przydatny je©eli chcesz rozpoznaФ typ plikСw w twoim
systemie. Na przykЁad je©eli fsck zdeponuje jakie╤ pliki w katalogu
lost+found, mo©esz uruchomiФ file na zdeponowanym pliku i zobaczyФ
jaki to jest typ pliku, jest to metoda bezpieczniejsza ni© 'more', ze
wzglЙdu na to, ©e to mo©e byФ plik binarny. File potrafi rozpoznaФ
wiele typСw plikСw np. binarny ELF, biblioteki systemowe, pakiety RPM
oraz wiele rС©nych formatСw graficznych i d╪wiЙkowych.

%description -l pt_BR
Este pacote И Зtil para descobrir que tipo de arquivo vocЙ estА
procurando em seu sistema. Por exemplo, se um fsck resulta em um
arquivo forem armazenado no "lost+found", vocЙ pode rodar file nele
para descobrir se И seguro lЙ-lo com o "more" ou se ele И um binАrio.
Ele reconhece vАrios tipos de arquivos, incluindo binАrios ELF,
bibliotecas de sistema, pacotes RPM e vАrios formatos grАficos
diferentes.

%description -l tr
file, bir dosyayЩ inceleyerek ne tЭr bir dosya olduПu konusunda size
bir fikir verebilir. BЖylece uzantЩsЩndan ve adЩndan ne olduПunu
ГЩkaramadЩПЩnЩz bir dosyayЩ hangi yazЩlЩm ile kullanabileceПinize ya
da ne yapacaПЩnЩza karar verebilisiniz. file, temel dosya tiplerini,
ГoПu grafik formatЩnЩ, ГalЩЧtЩrЩlabilir dosyalarЩ, sistem
kitaplЩklarЩnЩ vs. tanЩyabilir.

%description -l ru
Команда file используется для определения типа файла по данным, в нем
содержащимся. Она может определить множество разнообразных типов
файлов, включая бинарные файлы формата ELF, системные библиотеки,
пакеты RPM, различные графические форматы и много других.

%description -l uk
Команда file використову╓ться для визначення типу файлу по даних, як╕
в╕н м╕стить. Вона може визначити велику к╕льк╕сть р╕зноман╕тних тип╕в
файл╕в, у тому числ╕ б╕нарн╕ файли формату ELF, системн╕ б╕бл╕отеки,
пакети RPM, р╕зноман╕тн╕ граф╕чн╕ формати та багато ╕нших.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p0

%build
rm -f install-sh missing mkinstalldirs
aclocal
autoheader
autoconf
automake -a -c -f
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
