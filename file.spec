#
# Conditional build:
%bcond_without	python2		# don't build python-magic module for Python 2.x
%bcond_without	python3		# don't build python-magic module for Python 3.x
%bcond_without	static_libs	# don't build static libraries
%bcond_without	tests		# don't perform "make check"

Summary:	A utility for determining file types
Summary(cs.UTF-8):	Program pro zjišťování typu souborů
Summary(da.UTF-8):	Et værktøj til bestemmelse af filtyper
Summary(de.UTF-8):	Ein Befehl zur Bestimmung von Dateitypen
Summary(es.UTF-8):	Utilidad para determinar el tipo de fichero
Summary(fr.UTF-8):	Utilitaire permettant d'identifier des types de fichier
Summary(id.UTF-8):	Utility untuk menentukan tipe file
Summary(is.UTF-8):	Tól til þess að komast að tegund skráar
Summary(it.UTF-8):	Utility per determinare il tipo di file
Summary(ja.UTF-8):	ファイルの種類を判断するためのユーティリティ
Summary(ko.UTF-8):	파일 종류를 결정하는 유틸리티
Summary(nb.UTF-8):	Et verktøy for å bestemme filtyper
Summary(pl.UTF-8):	Polecenie określające rodzaj pliku
Summary(pt.UTF-8):	Um utilitário para determinar o tipo dos ficheiros
Summary(pt_BR.UTF-8):	Um utilitário para determinar tipos de arquivos
Summary(ru.UTF-8):	Утилита для определения типов файлов
Summary(sk.UTF-8):	Pomocný program pre určenie typu súboru
Summary(sl.UTF-8):	Pripomoček za ugotavljanje vrste datotek
Summary(sv.UTF-8):	Ett verktyg för att bestämma filtyper
Summary(tr.UTF-8):	Dosya türünü öğrenmek için bir araç
Summary(uk.UTF-8):	Утиліта для визначення типів файлів
Summary(zh_CN.UTF-8):	判定文件类型的工具。
Summary(zh_TW.UTF-8):	用於決定檔案類型的一個工具程式。
Name:		file
Version:	5.39
Release:	1
License:	distributable
Group:		Applications/File
Source0:	ftp://ftp.astron.com/pub/file/%{name}-%{version}.tar.gz
# Source0-md5:	1c450306053622803a25647d88f80f25
Source1:	http://ftp1.pld-linux.org/people/glen/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	6a45bcaefd19b94db36a1b2b7c5b806b
Source2:	%{name}-zisofs.magic
Source3:	%{name}-mscompress.magic
Source4:	%{name}-magic.mime-gen.awk
Patch0:		%{name}-selinux.patch
Patch1:		searchpath.patch
Patch2:		automake.patch
Patch4:		name-use-count.patch
URL:		http://www.darwinsys.com/file/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libseccomp-devel
BuildRequires:	libtool >= 2:2.0
BuildRequires:	rpmbuild(macros) >= 1.710
%if %{with python2}
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
%endif
%if %{with python3}
BuildRequires:	python3-devel
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
%endif
BuildRequires:	zlib-devel
Requires(pretrans):	coreutils
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

%description -l cs.UTF-8
Příkaz file se používá pro identifikaci zadaného souboru podle jeho
obsahu. Je schopen identifikovat množství různých typů souborů včetně
binárních souborů ELF, systémových knihoven, RPM balíčků a různých
grafických formátů.

%description -l da.UTF-8
Programmet "file" bruges til at identificere filer baseret på indhold.
"file" kan identificere mange forskellige filtyper, inkl. ELF-filer,
systembiblioteker, RPM-pakker og billedfiler i forskellige formater.

%description -l de.UTF-8
Sie können dieses Paket verwenden, um zu bestimmen, welches Format
eine bestimmte Datei hat. Wird durch fsck eine Datei in lost+found
gespeichert, können Sie 'file' ausführen, um herauszufinden, ob Sie
sie mit 'more' einsehen können, oder ob es sich um ein Binärprogramm
handelt Das Programm erkennt u.a. ELF-Binärprogramme,
System-Libraries, RPM-Pakete und viele Grafikformate.

%description -l es.UTF-8
Este paquete es útil para descubrir que tipo de archivo estás buscando
en tu sistema. Por ejemplo, si fsck resulta un archivo que fue
almacenado en el "lost+found", tu puedes ejecutar file en él para
descubrir si es seguro leerlo con el "more" o si es un binario.
Reconoce varios tipos de archivos, incluyendo binarios ELF,
bibliotecas de sistema, paquetes RPM y varios formatos gráficos
diferentes.

%description -l fr.UTF-8
Ce paquetage sert à trouver le type du fichier que vous recherchez sur
votre système. Par exemple, si un fsck fait qu'un fichier a été stocké
dans lost+found, vous pouvez lancer file dessus pour savoir si on peut
faire un more, ou s'il s'agit d'un binaire. Il reconnaît de nombreux
types de fichiers dont les binaires ELF, les bibliothèques systèmes,
les paquetages RPM et de nombreux formats graphiques différents.

%description -l it.UTF-8
Il comando file è utilizzato per identificare il tipo di file in base
ai tipi di dati che contiene. File può identificare molti tipi di
file, tra cui i binari ELF, le librerie di sistema, i pacchetti RPM e
vari formati grafici.

%description -l ja.UTF-8
ファイルコマンドはファイルに含まれるデータの種類により個々のファイルを
見分けるために使われる。file は ELF バイナリ、システムライブラリ、 RPM
パッケージ、そして種々のグラフィックフォーマットを含む、多くの異なる
ファイルの種類を見分けることが可能である。

%description -l ko.UTF-8
파일에 저장된 자료 유형에 따라 파일을 식별하는 file 명령. File은 ELF
바이너리, 시스템 라이브러리, RPM 패키지와 다른 그래픽 유형을 포함한
여러 많은 파일 유형을 식별 가능합니다.

%description -l nb.UTF-8
Programmet "file" brukes for å identifisere filer basert på innhold.
"file" kan identifisere mange ulike filtyper, inkl. ELF-filer,
systembibliotek, RPM-pakker og bildefiler i ulike formater.

%description -l pl.UTF-8
Pakiet ten jest przydatny jeżeli chcesz rozpoznać typ plików w twoim
systemie. Na przykład jeżeli fsck zdeponuje jakieś pliki w katalogu
lost+found, możesz uruchomić file na zdeponowanym pliku i zobaczyć
jaki to jest typ pliku, jest to metoda bezpieczniejsza niż 'more', ze
względu na to, że to może być plik binarny. File potrafi rozpoznać
wiele typów plików np. binarny ELF, biblioteki systemowe, pakiety RPM
oraz wiele różnych formatów graficznych i dźwiękowych.

%description -l pt.UTF-8
O comando file é usado para identificar um ficheiro em particular de
acordo com o tipo de dados que contém. O file pode identificar vários
formatos de ficheiros, incluindo binários ELF, bibliotecas de sistema,
pacotes RPM e vários formatos gráficos diferentes.

%description -l pt_BR.UTF-8
Este pacote é útil para descobrir que tipo de arquivo você está
procurando em seu sistema. Por exemplo, se um fsck resulta em um
arquivo forem armazenado no "lost+found", você pode rodar file nele
para descobrir se é seguro lê-lo com o "more" ou se ele é um binário.
Ele reconhece vários tipos de arquivos, incluindo binários ELF,
bibliotecas de sistema, pacotes RPM e vários formatos gráficos
diferentes.

%description -l ru.UTF-8
Команда file используется для определения типа файла по данным, в нем
содержащимся. Она может определить множество разнообразных типов
файлов, включая бинарные файлы формата ELF, системные библиотеки,
пакеты RPM, различные графические форматы и много других.

%description -l sv.UTF-8
Kommandot file används för att identifera en fil vad avser vilken typ
av data filen innehåller. File kan identifiera många olika filtyper,
inklusive ELF-binärer, systembibliotek, RPM-paket och olika
grafikformat.

%description -l tr.UTF-8
file, bir dosyayı inceleyerek ne tür bir dosya olduğu konusunda size
bir fikir verebilir. Böylece uzantısından ve adından ne olduğunu
çıkaramadığınız bir dosyayı hangi yazılım ile kullanabileceğinize ya
da ne yapacağınıza karar verebilisiniz. file, temel dosya tiplerini,
çoğu grafik formatını, çalıştırılabilir dosyaları, sistem
kitaplıklarını vs. tanıyabilir.

%description -l uk.UTF-8
Команда file використовується для визначення типу файлу по даних, які
він містить. Вона може визначити велику кількість різноманітних типів
файлів, у тому числі бінарні файли формату ELF, системні бібліотеки,
пакети RPM, різноманітні графічні формати та багато інших.

%description -l zh_CN.UTF-8
file 命令用来根据文件中包含的数据类型来识别文件类型。 file
可以识别许多不同的文件类型，包括 ELF 二进制、系统 库、RPM
软件包、和不同的图形格式。

%description -l zh_TW.UTF-8
file 指令是根據檔案包含的資料類型來辨認檔案。 File
可以辨認許多不同的檔案類型， 包含 ELF binaries，系統函式庫，RPM
套件，以及不同的 圖像格式。

%package -n libmagic
Summary:	libmagic library
Summary(pl.UTF-8):	Biblioteka libmagic
Group:		Libraries

%description -n libmagic
Library of functions which operate on magic database file.

%description -n libmagic -l pl.UTF-8
Biblioteka funkcji operujących na pliku bazy danych magic.

%package -n libmagic-devel
Summary:	Header files for libmagic library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libmagic
Group:		Development/Libraries
Requires:	libmagic = %{version}-%{release}
Requires:	zlib-devel

%description -n libmagic-devel
Library of functions which operate on magic database file.

This package contains the header files needed to develop programs that
use these libmagic.

%description -n libmagic-devel -l pl.UTF-8
Biblioteka funkcji operujących na pliku bazy danych magic.

Ten pakiet zawiera pliki nagłówkowe potrzebne do tworzenia programów
używających libmagic.

%package -n libmagic-static
Summary:	Static libmagic library
Summary(pl.UTF-8):	Statyczna biblioteka libmagic
Group:		Development/Libraries
Requires:	libmagic-devel = %{version}-%{release}

%description -n libmagic-static
Library of functions which operate on magic database file.

This package contains the static libmagic.

%description -n libmagic-static -l pl.UTF-8
Biblioteka funkcji operujących na pliku bazy danych magic.

Ten pakiet zawiera statyczną wersję biblioteki.

%package -n python-magic
Summary:	Python 2 bindings for libmagic
Summary(pl.UTF-8):	Wiązania Pythona 2 do biblioteki libmagic
Group:		Libraries/Python
Requires:	libmagic = %{version}-%{release}
Requires:	python-libs

%description -n python-magic
Python 2 bindings for libmagic.

%description -n python-magic -l pl.UTF-8
Wiązania Pythona 2 do biblioteki libmagic.

%package -n python3-magic
Summary:	Python 3 bindings for libmagic
Summary(pl.UTF-8):	Wiązania Pythona 3 do biblioteki libmagic
Group:		Libraries/Python
Requires:	libmagic = %{version}-%{release}
Requires:	python-libs

%description -n python3-magic
Python 3 bindings for libmagic.

%description -n python3-magic -l pl.UTF-8
Wiązania Pythona 3 do biblioteki libmagic.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch4 -p1

%if "%{cc_version}" < "3.4"
%{__sed} -i -e 's,-Wextra,,' configure.ac
%endif

cp -p %{SOURCE3} magic/Magdir/mscompress
cp -p %{SOURCE2} magic/Magdir/zisofs

rm -f magic/Magdir/{*.orig,*~}

%if %{with python3}
cp -a python py3
%endif

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
%ifnarch %{x8664}
	--disable-libseccomp \
%endif
	--disable-silent-rules \
	--enable-fsect-man5 \
	%{?with_static_libs:--enable-static}

%{__make}

%if %{with python2}
cd python
%py_build
cd ..
%endif
%if %{with python3}
cd py3
%py3_build
cd ..
%endif

%if %{with tests}
%{__make} check
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_lib}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_libdir}/libmagic.so.* $RPM_BUILD_ROOT/%{_lib}
ln -sf /%{_lib}/$(basename $RPM_BUILD_ROOT/%{_lib}/libmagic.so.*.*.*) \
        $RPM_BUILD_ROOT%{_libdir}/libmagic.so

%if %{with python2}
cd python
%py_install
cd ..
%py_postclean
%endif

%if %{with python3}
cd py3
%py3_install
cd ..
%endif

awk -f %{SOURCE4} < $RPM_BUILD_ROOT%{_datadir}/misc/magic > $RPM_BUILD_ROOT%{_datadir}/misc/magic.mime
ln -s misc $RPM_BUILD_ROOT%{_datadir}/file

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}
%{__rm} $RPM_BUILD_ROOT%{_mandir}/README.file-non-english-man-pages
%{__rm} $RPM_BUILD_ROOT%{_mandir}/file-magic4.diff

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n libmagic -p /sbin/ldconfig
%postun	-n libmagic -p /sbin/ldconfig

%pretrans
# it used to be directory
if [ -d %{_datadir}/file -a ! -L %{_datadir}/file ]; then
	mv -b %{_datadir}/file{,.dir}
	ln -sn misc %{_datadir}/file
%banner -e %{name} <<EOF
Check %{_datadir}/file.dir for your own files and remove it when done.
EOF
fi

%files
%defattr(644,root,root,755)
%doc ChangeLog COPYING README
%attr(755,root,root) %{_bindir}/file
%{_datadir}/file
%{_datadir}/misc/magic
%{_datadir}/misc/magic.mgc
%{_datadir}/misc/magic.mime
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/magic
%{_mandir}/man1/file.1*
%{_mandir}/man5/magic.5*
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
%attr(755,root,root) /%{_lib}/libmagic.so.*.*.*
%attr(755,root,root) %ghost /%{_lib}/libmagic.so.1

%files -n libmagic-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmagic.so
%{_libdir}/libmagic.la
%{_includedir}/magic.h
%{_pkgconfigdir}/libmagic.pc
%{_mandir}/man3/libmagic.3*

%if %{with static_libs}
%files -n libmagic-static
%defattr(644,root,root,755)
%{_libdir}/libmagic.a
%endif

%if %{with python3}
%files -n python-magic
%defattr(644,root,root,755)
%doc python/README.md python/example.py
%{py_sitescriptdir}/magic.py[co]
%{py_sitescriptdir}/file_magic-*-py*.egg-info
%endif

%if %{with_python3}
%files -n python3-magic
%defattr(644,root,root,755)
%doc python/README.md python/example.py
%{py3_sitescriptdir}/magic.py
%{py3_sitescriptdir}/__pycache__/magic.*.py[co]
%{py3_sitescriptdir}/file_magic-*-py*.egg-info
%endif
