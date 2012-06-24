#
# Conditional build:
%bcond_without	python	# don't build python-magic module
%bcond_without	static_libs # don't build static libraries
#
Summary:	A utility for determining file types
Summary(cs):	Program pro zji��ov�n� typu soubor�
Summary(da):	Et v�rkt�j til bestemmelse af filtyper
Summary(de):	Ein Befehl zur Bestimmung von Dateitypen
Summary(es):	Utilidad para determinar el tipo de fichero
Summary(fr):	Utilitaire permettant d'identifier des types de fichier
Summary(id):	Utility untuk menentukan tipe file
Summary(is):	T�l til �ess a� komast a� tegund skr�ar
Summary(it):	Utility per determinare il tipo di file
Summary(ja):	�ե�����μ����Ƚ�Ǥ��뤿��Υ桼�ƥ���ƥ�
Summary(ko):	���� ������ �����ϴ� ��ƿ��Ƽ
Summary(nb):	Et verkt�y for � bestemme filtyper
Summary(pl):	Polecenie okre�laj�ce rodzaj pliku
Summary(pt):	Um utilit�rio para determinar o tipo dos ficheiros
Summary(pt_BR):	Um utilit�rio para determinar tipos de arquivos
Summary(ru):	������� ��� ����������� ����� ������
Summary(sk):	Pomocn� program pre ur�enie typu s�boru
Summary(sl):	Pripomo�ek za ugotavljanje vrste datotek
Summary(sv):	Ett verktyg f�r att best�mma filtyper
Summary(tr):	Dosya t�r�n� ��renmek i�in bir ara�
Summary(uk):	���̦�� ��� ���������� ��Ц� ���̦�
Summary(zh_CN):	�ж��ļ����͵Ĺ��ߡ�
Summary(zh_TW):	�Ω�M�w�ɮ��������@�Ӥu��{���C
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
P��kaz file se pou��v� pro identifikaci zadan�ho souboru podle jeho
obsahu. Je schopen identifikovat mno�stv� r�zn�ch typ� soubor� v�etn�
bin�rn�ch soubor� ELF, syst�mov�ch knihoven, RPM bal��k� a r�zn�ch
grafick�ch form�t�.

%description -l da
Programmet "file" bruges til at identificere filer baseret p� indhold.
"file" kan identificere mange forskellige filtyper, inkl. ELF-filer,
systembiblioteker, RPM-pakker og billedfiler i forskellige formater.

%description -l de
Sie k�nnen dieses Paket verwenden, um zu bestimmen, welches Format
eine bestimmte Datei hat. Wird durch fsck eine Datei in lost+found
gespeichert, k�nnen Sie 'file' ausf�hren, um herauszufinden, ob Sie
sie mit 'more' einsehen k�nnen, oder ob es sich um ein Bin�rprogramm
handelt Das Programm erkennt u.a. ELF-Bin�rprogramme,
System-Libraries, RPM-Pakete und viele Grafikformate.

%description -l es
Este paquete es �til para descubrir que tipo de archivo est�s buscando
en tu sistema. Por ejemplo, si fsck resulta un archivo que fue
almacenado en el "lost+found", tu puedes ejecutar file en �l para
descubrir si es seguro leerlo con el "more" o si es un binario.
Reconoce varios tipos de archivos, incluyendo binarios ELF,
bibliotecas de sistema, paquetes RPM y varios formatos gr�ficos
diferentes.

%description -l fr
Ce paquetage sert � trouver le type du fichier que vous recherchez sur
votre syst�me. Par exemple, si un fsck fait qu'un fichier a �t� stock�
dans lost+found, vous pouvez lancer file dessus pour savoir si on peut
faire un more, ou s'il s'agit d'un binaire. Il reconna�t de nombreux
types de fichiers dont les binaires ELF, les biblioth�ques syst�mes,
les paquetages RPM et de nombreux formats graphiques diff�rents.

%description -l it
Il comando file � utilizzato per identificare il tipo di file in base
ai tipi di dati che contiene. File pu� identificare molti tipi di
file, tra cui i binari ELF, le librerie di sistema, i pacchetti RPM e
vari formati grafici.

%description -l ja
�ե����륳�ޥ�ɤϥե�����˴ޤޤ��ǡ����μ���ˤ��ġ��Υե������
��ʬ���뤿��˻Ȥ��롣file �� ELF �Х��ʥꡢ�����ƥ�饤�֥�ꡢ RPM
�ѥå������������Ƽ�Υ���ե��å��ե����ޥåȤ�ޤࡢ¿���ΰۤʤ�
�ե�����μ����ʬ���뤳�Ȥ���ǽ�Ǥ��롣

%description -l ko
���Ͽ� ����� �ڷ� ������ ���� ������ �ĺ��ϴ� file ���.
File�� ELF ���̳ʸ�, �ý��� ���̺귯��, RPM ��Ű����
�ٸ� �׷��� ������ ������ ���� ���� ���� ������ �ĺ� �����մϴ�.

%description -l nb
Programmet "file" brukes for � identifisere filer basert p� innhold.
"file" kan identifisere mange ulike filtyper, inkl. ELF-filer,
systembibliotek, RPM-pakker og bildefiler i ulike formater.

%description -l pl
Pakiet ten jest przydatny je�eli chcesz rozpozna� typ plik�w w twoim
systemie. Na przyk�ad je�eli fsck zdeponuje jakie� pliki w katalogu
lost+found, mo�esz uruchomi� file na zdeponowanym pliku i zobaczy�
jaki to jest typ pliku, jest to metoda bezpieczniejsza ni� 'more', ze
wzgl�du na to, �e to mo�e by� plik binarny. File potrafi rozpozna�
wiele typ�w plik�w np. binarny ELF, biblioteki systemowe, pakiety RPM
oraz wiele r�nych format�w graficznych i d�wi�kowych.

%description -l pt
O comando file � usado para identificar um ficheiro em particular de
acordo com o tipo de dados que cont�m. O file pode identificar v�rios
formatos de ficheiros, incluindo bin�rios ELF, bibliotecas de sistema,
pacotes RPM e v�rios formatos gr�ficos diferentes.

%description -l pt_BR
Este pacote � �til para descobrir que tipo de arquivo voc� est�
procurando em seu sistema. Por exemplo, se um fsck resulta em um
arquivo forem armazenado no "lost+found", voc� pode rodar file nele
para descobrir se � seguro l�-lo com o "more" ou se ele � um bin�rio.
Ele reconhece v�rios tipos de arquivos, incluindo bin�rios ELF,
bibliotecas de sistema, pacotes RPM e v�rios formatos gr�ficos
diferentes.

%description -l ru
������� file ������������ ��� ����������� ���� ����� �� ������, � ���
������������. ��� ����� ���������� ��������� ������������� �����
������, ������� �������� ����� ������� ELF, ��������� ����������,
������ RPM, ��������� ����������� ������� � ����� ������.

%description -l sv
Kommandot file anv�nds f�r att identifera en fil vad avser vilken typ
av data filen inneh�ller.  File kan identifiera m�nga olika filtyper,
inklusive ELF-bin�rer, systembibliotek, RPM-paket och olika
grafikformat.

%description -l tr
file, bir dosyay� inceleyerek ne t�r bir dosya oldu�u konusunda size
bir fikir verebilir. B�ylece uzant�s�ndan ve ad�ndan ne oldu�unu
��karamad���n�z bir dosyay� hangi yaz�l�m ile kullanabilece�inize ya
da ne yapaca��n�za karar verebilisiniz. file, temel dosya tiplerini,
�o�u grafik format�n�, �al��t�r�labilir dosyalar�, sistem
kitapl�klar�n� vs. tan�yabilir.

%description -l uk
������� file ����������դ���� ��� ���������� ���� ����� �� �����, �˦
צ� ͦ�����. ���� ���� ��������� ������ ˦��˦��� Ҧ�����Φ���� ��Ц�
���̦�, � ���� ���̦ ¦���Φ ����� ������� ELF, ������Φ ¦�̦�����,
������ RPM, Ҧ�����Φ�Φ ���Ʀ�Φ ������� �� ������ �����.

%description -l zh_CN
file �������������ļ��а���������������ʶ���ļ����͡�
file ����ʶ����಻ͬ���ļ����ͣ����� ELF �����ơ�ϵͳ
�⡢RPM ��������Ͳ�ͬ��ͼ�θ�ʽ��

%description -l zh_TW
file ���O�O�ھ��ɮץ]�t����������ӿ�{�ɮסC
File �i�H��{�\�h���P���ɮ������A
�]�t ELF binaries�A�t�Ψ禡�w�ARPM �M��A�H�Τ��P��
�Ϲ��榡�C

%package -n libmagic
Summary:	libmagic library
Summary(pl):	Biblioteka libmagic
Group:		Libraries

%description -n libmagic
Library of functions which operate on magic database file.

%description -n libmagic -l pl
Biblioteka funkcji operuj�cych na pliku bazy danych magic.

%package -n libmagic-devel
Summary:	Header files for libmagic library
Summary(pl):	Pliki nag��wkowe biblioteki libmagic
Group:		Development/Libraries
Requires:	libmagic = %{version}-%{release}

%description -n libmagic-devel
Library of functions which operate on magic database file.

This package contains the header files needed to develop programs that
use these libmagic.

%description -n libmagic-devel -l pl
Biblioteka funkcji operuj�cych na pliku bazy danych magic.

Ten pakiet zawiera pliki nag��wkowe potrzebne do tworzenia program�w
u�ywaj�cych libmagic.

%package -n libmagic-static
Summary:	Static libmagic library
Summary(pl):	Statyczna biblioteka libmagic
Group:		Development/Libraries
Requires:	libmagic-devel = %{version}-%{release}

%description -n libmagic-static
Library of functions which operate on magic database file.

This package contains the static libmagic.

%description -n libmagic-static -l pl
Biblioteka funkcji operuj�cych na pliku bazy danych magic.

Ten pakiet zawiera statyczn� wersj� biblioteki.

%package -n python-magic
Summary:	Python bindings for libmagic
Summary(pl):	Wi�zania Pythona dla libmagic
Group:		Libraries/Python
Requires:	libmagic = %{version}-%{release}
%pyrequires_eq	python-libs

%description -n python-magic
Python bindings for libmagic.

%description -n python-magic -l pl
Wi�zania Pythona dla libmagic.

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
