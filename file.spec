Summary:	file(1) command
Summary(de):	Befehl file(1)
Summary(es):	Comando file
Summary(fr):	Commande file(1)
Summary(ja):	¥Õ¥¡¥¤¥ë¤Î¼ïÎà¤òÈ½ÊÌ¤¹¤ë¥æ¡¼¥Æ¥£¥ê¥Æ¥£¡¼
Summary(ko):	ÆÄÀÏ Á¾·ù¸¦ ¾Ë¾Æ³»´Â µµ±¸
Summary(pl):	Polecenie file(1)
Summary(pt_BR):	Um utilitário para determinar tipos de arquivos
Summary(ru):	õÔÉÌÉÔÁ ÄÌÑ ÏĞÒÅÄÅÌÅÎÉÑ ÔÉĞÏ× ÆÁÊÌÏ×
Summary(tr):	Dosya tipini belirleme aracı
Summary(uk):	õÔÉÌ¦ÔÁ ÄÌÑ ×ÉÚÎÁŞÅÎÎÑ ÔÉĞ¦× ÆÁÊÌ¦×
Name:		file
Version:	4.00
Release:	1
License:	distributable
Group:		Applications/File
Source0:	ftp://ftp.astron.com/pub/file/%{name}-%{version}.tar.gz
Source1:	zisofs.magic
Source2:	magic.mime
Source3:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
Source4:	%{name}-magic.mscompress
Patch0:		%{name}-sparc.patch
Patch1:		%{name}-ia64.patch
Patch2:		%{name}-palm.patch
Patch3:		%{name}-mime-elf.patch
Patch4:		%{name}-unicode.patch
Patch5:		%{name}-bin-zsh-magic.patch
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

%description -l es
Este paquete es útil para descubrir que tipo de archivo estás buscando
en tu sistema. Por ejemplo, si fsck resulta un archivo que fue
almacenado en el "lost+found", tu puedes ejecutar file en él para
descubrir si es seguro leerlo con el "more" o si es un binario.
Reconoce varios tipos de archivos, incluyendo binarios ELF,
bibliotecas de sistema, paquetes RPM y varios formatos gráficos
diferentes.

%description -l fr
Ce paquetage sert à trouver le type du fichier que vous recherchez sur
votre système. Par exemple, si un fsck fait qu'un fichier a été stocké
dans lost+found, vous pouvez lancer file dessus pour savoir si on peut
faire un more, ou s'il s'agit d'un binaire. Il reconnaît de nombreux
types de fichiers dont les binaires ELF, les bibliothèques systèmes,
les paquetages RPM et de nombreux formats graphiques différents.

%description -l ja
¥Õ¥¡¥¤¥ë¥³¥Ş¥ó¥É¤Ï¥Õ¥¡¥¤¥ë¤Ë´Ş¤Ş¤ì¤ë¥Ç¡¼¥¿¤Î¼ïÎà¤Ë¤è¤ê¸Ä¡¹¤Î¥Õ¥¡¥¤¥ë¤ò
¸«Ê¬¤±¤ë¤¿¤á¤Ë»È¤ï¤ì¤ë¡£file ¤Ï ELF ¥Ğ¥¤¥Ê¥ê¡¢¥·¥¹¥Æ¥à¥é¥¤¥Ö¥é¥ê¡¢
RPM ¥Ñ¥Ã¥±¡¼¥¸¡¢¤½¤·¤Æ¼ï¡¹¤Î¥°¥é¥Õ¥£¥Ã¥¯¥Õ¥©¡¼¥Ş¥Ã¥È¤ò´Ş¤à¡¢Â¿¤¯¤Î°Û¤Ê¤ë
¥Õ¥¡¥¤¥ë¤Î¼ïÎà¤ò¸«Ê¬¤±¤ë¤³¤È¤¬²ÄÇ½¤Ç¤¢¤ë¡£

%description -l pl
Pakiet ten jest przydatny je¿eli chcesz rozpoznaæ typ plików w twoim
systemie. Na przyk³ad je¿eli fsck zdeponuje jakie¶ pliki w katalogu
lost+found, mo¿esz uruchomiæ file na zdeponowanym pliku i zobaczyæ
jaki to jest typ pliku, jest to metoda bezpieczniejsza ni¿ 'more', ze
wzglêdu na to, ¿e to mo¿e byæ plik binarny. File potrafi rozpoznaæ
wiele typów plików np. binarny ELF, biblioteki systemowe, pakiety RPM
oraz wiele ró¿nych formatów graficznych i d¼wiêkowych.

%description -l pt_BR
Este pacote é útil para descobrir que tipo de arquivo você está
procurando em seu sistema. Por exemplo, se um fsck resulta em um
arquivo forem armazenado no "lost+found", você pode rodar file nele
para descobrir se é seguro lê-lo com o "more" ou se ele é um binário.
Ele reconhece vários tipos de arquivos, incluindo binários ELF,
bibliotecas de sistema, pacotes RPM e vários formatos gráficos
diferentes.

%description -l ru
ëÏÍÁÎÄÁ file ÉÓĞÏÌØÚÕÅÔÓÑ ÄÌÑ ÏĞÒÅÄÅÌÅÎÉÑ ÔÉĞÁ ÆÁÊÌÁ ĞÏ ÄÁÎÎÙÍ, × ÎÅÍ
ÓÏÄÅÒÖÁİÉÍÓÑ. ïÎÁ ÍÏÖÅÔ ÏĞÒÅÄÅÌÉÔØ ÍÎÏÖÅÓÔ×Ï ÒÁÚÎÏÏÂÒÁÚÎÙÈ ÔÉĞÏ×
ÆÁÊÌÏ×, ×ËÌÀŞÁÑ ÂÉÎÁÒÎÙÅ ÆÁÊÌÙ ÆÏÒÍÁÔÁ ELF, ÓÉÓÔÅÍÎÙÅ ÂÉÂÌÉÏÔÅËÉ,
ĞÁËÅÔÙ RPM, ÒÁÚÌÉŞÎÙÅ ÇÒÁÆÉŞÅÓËÉÅ ÆÏÒÍÁÔÙ É ÍÎÏÇÏ ÄÒÕÇÉÈ.

%description -l tr
file, bir dosyayı inceleyerek ne tür bir dosya olduğu konusunda size
bir fikir verebilir. Böylece uzantısından ve adından ne olduğunu
çıkaramadığınız bir dosyayı hangi yazılım ile kullanabileceğinize ya
da ne yapacağınıza karar verebilisiniz. file, temel dosya tiplerini,
çoğu grafik formatını, çalıştırılabilir dosyaları, sistem
kitaplıklarını vs. tanıyabilir.

%description -l uk
ëÏÍÁÎÄÁ file ×ÉËÏÒÉÓÔÏ×Õ¤ÔØÓÑ ÄÌÑ ×ÉÚÎÁŞÅÎÎÑ ÔÉĞÕ ÆÁÊÌÕ ĞÏ ÄÁÎÉÈ, ÑË¦
×¦Î Í¦ÓÔÉÔØ. ÷ÏÎÁ ÍÏÖÅ ×ÉÚÎÁŞÉÔÉ ×ÅÌÉËÕ Ë¦ÌØË¦ÓÔØ Ò¦ÚÎÏÍÁÎ¦ÔÎÉÈ ÔÉĞ¦×
ÆÁÊÌ¦×, Õ ÔÏÍÕ ŞÉÓÌ¦ Â¦ÎÁÒÎ¦ ÆÁÊÌÉ ÆÏÒÍÁÔÕ ELF, ÓÉÓÔÅÍÎ¦ Â¦ÂÌ¦ÏÔÅËÉ,
ĞÁËÅÔÉ RPM, Ò¦ÚÎÏÍÁÎ¦ÔÎ¦ ÇÒÁÆ¦ŞÎ¦ ÆÏÒÍÁÔÉ ÔÁ ÂÁÇÁÔÏ ¦ÎÛÉÈ.

%package -n libmagic
Summary:	libmagic library
Summary(pl):    Biblioteka libmagic
Group:		Libraries

%description -n libmagic
Library of functions which operate on magic database file.

%package -n libmagic-devel
Summary:	libmagic library
Summary(pl):	Biblioteka libmagic
Group:		Development/Libraries
Requires:	libmagic = %{version}

%description -n libmagic-devel
Library of functions which operate on magic database file.

This package contains the header files needed to develop programs that
use these libmagic.

%package -n libmagic-static
Summary:	libmagic library
Summary(pl):	Biblioteka libmagic
Group:		Development/Libraries
Requires:	libmagic-devel = %{version}

%description -n libmagic-static
Library of functions which operate on magic database file.

This package contains the static libmagic.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
rm -f install-sh ltmain.sh missing mkinstalldirs
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--enable-fsect-man5

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

cat %{SOURCE1} %{SOURCE4} >>$RPM_BUILD_ROOT%{_datadir}/magic
# install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}

bzip2 -dc %{SOURCE3} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

./src/file -m $RPM_BUILD_ROOT%{_datadir}/magic -c -C

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n libmagic -p /sbin/ldconfig
%postun	-n libmagic -p /sbin/ldconfig

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

%files -n libmagic
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files -n libmagic-devel
%defattr(644,root,root,755}
%{_includedir}/magic.h
%{_libdir}/lib*.la
%{_libdir}/lib*.so
%{_mandir}/man3/*

%files -n libmagic-static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
