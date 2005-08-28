#
# Conditional build:
%bcond_without	python	# don't build python-magic module
%bcond_without	static_libs # don't build static libraries
#
Summary:	A utility for determining file types
Summary(cs):	Program pro zji¹»ování typu souborù
Summary(da):	Et værktøj til bestemmelse af filtyper
Summary(de):	Ein Befehl zur Bestimmung von Dateitypen
Summary(es):	Utilidad para determinar el tipo de fichero
Summary(fr):	Utilitaire permettant d'identifier des types de fichier
Summary(id):	Utility untuk menentukan tipe file
Summary(is):	Tól til þess að komast að tegund skráar
Summary(it):	Utility per determinare il tipo di file
Summary(ja):	¥Õ¥¡¥¤¥ë¤Î¼ïÎà¤òÈ½ÃÇ¤¹¤ë¤¿¤á¤Î¥æ¡¼¥Æ¥£¥ê¥Æ¥£
Summary(ko):	ÆÄÀÏ Á¾·ù¸¦ °áÁ¤ÇÏ´Â À¯Æ¿¸®Æ¼
Summary(nb):	Et verktøy for å bestemme filtyper
Summary(pl):	Polecenie okre¶laj±ce rodzaj pliku
Summary(pt):	Um utilitário para determinar o tipo dos ficheiros
Summary(pt_BR):	Um utilitário para determinar tipos de arquivos
Summary(ru):	õÔÉÌÉÔÁ ÄÌÑ ÏÐÒÅÄÅÌÅÎÉÑ ÔÉÐÏ× ÆÁÊÌÏ×
Summary(sk):	Pomocný program pre urèenie typu súboru
Summary(sl):	Pripomoèek za ugotavljanje vrste datotek
Summary(sv):	Ett verktyg för att bestämma filtyper
Summary(tr):	Dosya türünü öðrenmek için bir araç
Summary(uk):	õÔÉÌ¦ÔÁ ÄÌÑ ×ÉÚÎÁÞÅÎÎÑ ÔÉÐ¦× ÆÁÊÌ¦×
Summary(zh_CN):	ÅÐ¶¨ÎÄ¼þÀàÐÍµÄ¹¤¾ß¡£
Summary(zh_TW):	¥Î©ó¨M©wÀÉ®×Ãþ«¬ªº¤@­Ó¤u¨ãµ{¦¡¡C
Name:		file
Version:	4.15
Release:	1
License:	distributable
Group:		Applications/File
Source0:	ftp://ftp.astron.com/pub/file/%{name}-%{version}.tar.gz
# Source0-md5:	09a6603dadbe06e577e98a2547201fab
Source1:	zisofs.magic
Source2:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source2-md5:	c157a183b64156f8baafaefd9cbf04c1
Source3:	%{name}-magic.mscompress
Patch0:		%{name}-debian.patch
Patch1:		%{name}-sparc.patch
Patch2:		%{name}-unicode.patch
Patch3:		%{name}-dicom.patch
Patch4:		%{name}-lmagic.patch
Patch5:		%{name}-python2.4.patch
Patch6:		%{name}-greedy-dump.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
%if %{with python}
BuildRequires:	python-devel
BuildRequires:	python-modules
%endif
Requires:	libmagic = %{version}-%{release}
Conflicts:	rpm-build < 4.4.1-9
Conflicts:	xdelta < 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package is useful for finding out what type of file you are
looking at on your system. For example, if an fsck results in a file
being stored in lost+found, you can run file on it to find out if it's
safe to 'more' it or if it's a binary. It recognizes many file types,
including ELF binaries, system libraries, RPM packages, and many
different graphics formats.

%description -l cs
Pøíkaz file se pou¾ívá pro identifikaci zadaného souboru podle jeho
obsahu. Je schopen identifikovat mno¾ství rùzných typù souborù vèetnì
binárních souborù ELF, systémových knihoven, RPM balíèkù a rùzných
grafických formátù.

%description -l da
Programmet "file" bruges til at identificere filer baseret på indhold.
"file" kan identificere mange forskellige filtyper, inkl. ELF-filer,
systembiblioteker, RPM-pakker og billedfiler i forskellige formater.

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

%description -l it
Il comando file è utilizzato per identificare il tipo di file in base
ai tipi di dati che contiene. File può identificare molti tipi di
file, tra cui i binari ELF, le librerie di sistema, i pacchetti RPM e
vari formati grafici.

%description -l ja
¥Õ¥¡¥¤¥ë¥³¥Þ¥ó¥É¤Ï¥Õ¥¡¥¤¥ë¤Ë´Þ¤Þ¤ì¤ë¥Ç¡¼¥¿¤Î¼ïÎà¤Ë¤è¤ê¸Ä¡¹¤Î¥Õ¥¡¥¤¥ë¤ò
¸«Ê¬¤±¤ë¤¿¤á¤Ë»È¤ï¤ì¤ë¡£file ¤Ï ELF ¥Ð¥¤¥Ê¥ê¡¢¥·¥¹¥Æ¥à¥é¥¤¥Ö¥é¥ê¡¢ RPM
¥Ñ¥Ã¥±¡¼¥¸¡¢¤½¤·¤Æ¼ï¡¹¤Î¥°¥é¥Õ¥£¥Ã¥¯¥Õ¥©¡¼¥Þ¥Ã¥È¤ò´Þ¤à¡¢Â¿¤¯¤Î°Û¤Ê¤ë
¥Õ¥¡¥¤¥ë¤Î¼ïÎà¤ò¸«Ê¬¤±¤ë¤³¤È¤¬²ÄÇ½¤Ç¤¢¤ë¡£

%description -l ko
ÆÄÀÏ¿¡ ÀúÀåµÈ ÀÚ·á À¯Çü¿¡ µû¶ó ÆÄÀÏÀ» ½Äº°ÇÏ´Â file ¸í·É.
FileÀº ELF ¹ÙÀÌ³Ê¸®, ½Ã½ºÅÛ ¶óÀÌºê·¯¸®, RPM ÆÐÅ°Áö¿Í
´Ù¸¥ ±×·¡ÇÈ À¯ÇüÀ» Æ÷ÇÔÇÑ ¿©·¯ ¸¹Àº ÆÄÀÏ À¯ÇüÀ» ½Äº° °¡´ÉÇÕ´Ï´Ù.

%description -l nb
Programmet "file" brukes for å identifisere filer basert på innhold.
"file" kan identifisere mange ulike filtyper, inkl. ELF-filer,
systembibliotek, RPM-pakker og bildefiler i ulike formater.

%description -l pl
Pakiet ten jest przydatny je¿eli chcesz rozpoznaæ typ plików w twoim
systemie. Na przyk³ad je¿eli fsck zdeponuje jakie¶ pliki w katalogu
lost+found, mo¿esz uruchomiæ file na zdeponowanym pliku i zobaczyæ
jaki to jest typ pliku, jest to metoda bezpieczniejsza ni¿ 'more', ze
wzglêdu na to, ¿e to mo¿e byæ plik binarny. File potrafi rozpoznaæ
wiele typów plików np. binarny ELF, biblioteki systemowe, pakiety RPM
oraz wiele ró¿nych formatów graficznych i d¼wiêkowych.

%description -l pt
O comando file é usado para identificar um ficheiro em particular de
acordo com o tipo de dados que contém. O file pode identificar vários
formatos de ficheiros, incluindo binários ELF, bibliotecas de sistema,
pacotes RPM e vários formatos gráficos diferentes.

%description -l pt_BR
Este pacote é útil para descobrir que tipo de arquivo você está
procurando em seu sistema. Por exemplo, se um fsck resulta em um
arquivo forem armazenado no "lost+found", você pode rodar file nele
para descobrir se é seguro lê-lo com o "more" ou se ele é um binário.
Ele reconhece vários tipos de arquivos, incluindo binários ELF,
bibliotecas de sistema, pacotes RPM e vários formatos gráficos
diferentes.

%description -l ru
ëÏÍÁÎÄÁ file ÉÓÐÏÌØÚÕÅÔÓÑ ÄÌÑ ÏÐÒÅÄÅÌÅÎÉÑ ÔÉÐÁ ÆÁÊÌÁ ÐÏ ÄÁÎÎÙÍ, × ÎÅÍ
ÓÏÄÅÒÖÁÝÉÍÓÑ. ïÎÁ ÍÏÖÅÔ ÏÐÒÅÄÅÌÉÔØ ÍÎÏÖÅÓÔ×Ï ÒÁÚÎÏÏÂÒÁÚÎÙÈ ÔÉÐÏ×
ÆÁÊÌÏ×, ×ËÌÀÞÁÑ ÂÉÎÁÒÎÙÅ ÆÁÊÌÙ ÆÏÒÍÁÔÁ ELF, ÓÉÓÔÅÍÎÙÅ ÂÉÂÌÉÏÔÅËÉ,
ÐÁËÅÔÙ RPM, ÒÁÚÌÉÞÎÙÅ ÇÒÁÆÉÞÅÓËÉÅ ÆÏÒÍÁÔÙ É ÍÎÏÇÏ ÄÒÕÇÉÈ.

%description -l sv
Kommandot file används för att identifera en fil vad avser vilken typ
av data filen innehåller.  File kan identifiera många olika filtyper,
inklusive ELF-binärer, systembibliotek, RPM-paket och olika
grafikformat.

%description -l tr
file, bir dosyayý inceleyerek ne tür bir dosya olduðu konusunda size
bir fikir verebilir. Böylece uzantýsýndan ve adýndan ne olduðunu
çýkaramadýðýnýz bir dosyayý hangi yazýlým ile kullanabileceðinize ya
da ne yapacaðýnýza karar verebilisiniz. file, temel dosya tiplerini,
çoðu grafik formatýný, çalýþtýrýlabilir dosyalarý, sistem
kitaplýklarýný vs. tanýyabilir.

%description -l uk
ëÏÍÁÎÄÁ file ×ÉËÏÒÉÓÔÏ×Õ¤ÔØÓÑ ÄÌÑ ×ÉÚÎÁÞÅÎÎÑ ÔÉÐÕ ÆÁÊÌÕ ÐÏ ÄÁÎÉÈ, ÑË¦
×¦Î Í¦ÓÔÉÔØ. ÷ÏÎÁ ÍÏÖÅ ×ÉÚÎÁÞÉÔÉ ×ÅÌÉËÕ Ë¦ÌØË¦ÓÔØ Ò¦ÚÎÏÍÁÎ¦ÔÎÉÈ ÔÉÐ¦×
ÆÁÊÌ¦×, Õ ÔÏÍÕ ÞÉÓÌ¦ Â¦ÎÁÒÎ¦ ÆÁÊÌÉ ÆÏÒÍÁÔÕ ELF, ÓÉÓÔÅÍÎ¦ Â¦ÂÌ¦ÏÔÅËÉ,
ÐÁËÅÔÉ RPM, Ò¦ÚÎÏÍÁÎ¦ÔÎ¦ ÇÒÁÆ¦ÞÎ¦ ÆÏÒÍÁÔÉ ÔÁ ÂÁÇÁÔÏ ¦ÎÛÉÈ.

%description -l zh_CN
file ÃüÁîÓÃÀ´¸ù¾ÝÎÄ¼þÖÐ°üº¬µÄÊý¾ÝÀàÐÍÀ´Ê¶±ðÎÄ¼þÀàÐÍ¡£
file ¿ÉÒÔÊ¶±ðÐí¶à²»Í¬µÄÎÄ¼þÀàÐÍ£¬°üÀ¨ ELF ¶þ½øÖÆ¡¢ÏµÍ³
¿â¡¢RPM Èí¼þ°ü¡¢ºÍ²»Í¬µÄÍ¼ÐÎ¸ñÊ½¡£

%description -l zh_TW
file «ü¥O¬O®Ú¾ÚÀÉ®×¥]§tªº¸ê®ÆÃþ«¬¨Ó¿ë»{ÀÉ®×¡C
File ¥i¥H¿ë»{³\¦h¤£¦PªºÀÉ®×Ãþ«¬¡A
¥]§t ELF binaries¡A¨t²Î¨ç¦¡®w¡ARPM ®M¥ó¡A¥H¤Î¤£¦Pªº
¹Ï¹³®æ¦¡¡C

%package -n libmagic
Summary:	libmagic library
Summary(pl):	Biblioteka libmagic
Group:		Libraries

%description -n libmagic
Library of functions which operate on magic database file.

%description -n libmagic -l pl
Biblioteka funkcji operuj±cych na pliku bazy danych magic.

%package -n libmagic-devel
Summary:	Header files for libmagic library
Summary(pl):	Pliki nag³ówkowe biblioteki libmagic
Group:		Development/Libraries
Requires:	libmagic = %{version}-%{release}

%description -n libmagic-devel
Library of functions which operate on magic database file.

This package contains the header files needed to develop programs that
use these libmagic.

%description -n libmagic-devel -l pl
Biblioteka funkcji operuj±cych na pliku bazy danych magic.

Ten pakiet zawiera pliki nag³ówkowe potrzebne do tworzenia programów
u¿ywaj±cych libmagic.

%package -n libmagic-static
Summary:	Static libmagic library
Summary(pl):	Statyczna biblioteka libmagic
Group:		Development/Libraries
Requires:	libmagic-devel = %{version}-%{release}

%description -n libmagic-static
Library of functions which operate on magic database file.

This package contains the static libmagic.

%description -n libmagic-static -l pl
Biblioteka funkcji operuj±cych na pliku bazy danych magic.

Ten pakiet zawiera statyczn± wersjê biblioteki.

%package -n python-magic
Summary:	Python bindings for libmagic
Summary(pl):	Wi±zania Pythona dla libmagic
Group:		Libraries/Python
Requires:	libmagic = %{version}-%{release}
%pyrequires_eq	python-libs

%description -n python-magic
Python bindings for libmagic.

%description -n python-magic -l pl
Wi±zania Pythona dla libmagic.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--enable-fsect-man5 \
	%{!?with_static_libs:--enable-static=no}

%{__make}

%if %{with python}
cd python
python setup.py build
cd ..
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with python}
cd python
python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2
cd ..
%endif

install -D magic/magic.local $RPM_BUILD_ROOT%{_sysconfdir}/magic

cat %{SOURCE1} %{SOURCE3} >>$RPM_BUILD_ROOT%{_datadir}/file/magic

bzip2 -dc %{SOURCE2} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

# somebody forgot about patching in tarball
mv -f $RPM_BUILD_ROOT%{_mandir}/pt_BR/man{4,5}
sed -e 's/MAGIC 4/MAGIC 5/' $RPM_BUILD_ROOT%{_mandir}/pt_BR/man5/magic.4 \
	> $RPM_BUILD_ROOT%{_mandir}/pt_BR/man5/magic.5
rm -f $RPM_BUILD_ROOT%{_mandir}/pt_BR/man5/magic.4

./src/file -m $RPM_BUILD_ROOT%{_datadir}/file/magic -c -C

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n libmagic -p /sbin/ldconfig
%postun	-n libmagic -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog LEGAL.NOTICE README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/file
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/magic
%{_mandir}/man[15]/*
%lang(de) %{_mandir}/de/man[15]/*
%lang(es) %{_mandir}/es/man[15]/*
%lang(fr) %{_mandir}/fr/man[15]/*
%lang(hu) %{_mandir}/hu/man[15]/*
%lang(it) %{_mandir}/it/man[15]/*
%lang(ja) %{_mandir}/ja/man[15]/*
%lang(nl) %{_mandir}/nl/man[15]/*
%lang(pl) %{_mandir}/pl/man[15]/*
%lang(pt_BR) %{_mandir}/pt_BR/man[15]/*

%files -n libmagic
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files -n libmagic-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/magic.h
%{_mandir}/man3/*

%if %{with static_libs}
%files -n libmagic-static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif

%if %{with python}
%files -n python-magic
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/*.so
%endif
