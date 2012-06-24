Summary:	file(1) command
Summary(de):	Befehl file(1)
Summary(es):	Comando file
Summary(fr):	Commande file(1)
Summary(ja):	�ե�����μ����Ƚ�̤���桼�ƥ���ƥ���
Summary(ko):	���� ������ �˾Ƴ��� ����
Summary(pl):	Polecenie file(1)
Summary(pt_BR):	Um utilit�rio para determinar tipos de arquivos
Summary(ru):	������� ��� ����������� ����� ������
Summary(tr):	Dosya tipini belirleme arac�
Summary(uk):	���̦�� ��� ���������� ��Ц� ���̦�
Name:		file
Version:	4.02
Release:	1
License:	distributable
Group:		Applications/File
Source0:	ftp://ftp.astron.com/pub/file/%{name}-%{version}.tar.gz
# Source0-md5: 5a853ecdf3b440915bda1d1a03240a5f
Source1:	zisofs.magic
Source2:	magic.mime
Source3:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source3-md5: c157a183b64156f8baafaefd9cbf04c1
Source4:	%{name}-magic.mscompress
Patch0:		%{name}-sparc.patch
Patch1:		%{name}-ia64.patch
Patch2:		%{name}-palm.patch
Patch3:		%{name}-mime-elf.patch
Patch4:		%{name}-unicode.patch
Patch5:		%{name}-bin-zsh-magic.patch
Patch6:		%{name}-magic-path.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
Requires:	libmagic = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Conflicts:	xdelta < 1.0.0

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

%description -l ja
�ե����륳�ޥ�ɤϥե�����˴ޤޤ��ǡ����μ���ˤ��ġ��Υե������
��ʬ���뤿��˻Ȥ��롣file �� ELF �Х��ʥꡢ�����ƥ�饤�֥�ꡢ
RPM �ѥå������������Ƽ�Υ���ե��å��ե����ޥåȤ�ޤࡢ¿���ΰۤʤ�
�ե�����μ����ʬ���뤳�Ȥ���ǽ�Ǥ��롣

%description -l pl
Pakiet ten jest przydatny je�eli chcesz rozpozna� typ plik�w w twoim
systemie. Na przyk�ad je�eli fsck zdeponuje jakie� pliki w katalogu
lost+found, mo�esz uruchomi� file na zdeponowanym pliku i zobaczy�
jaki to jest typ pliku, jest to metoda bezpieczniejsza ni� 'more', ze
wzgl�du na to, �e to mo�e by� plik binarny. File potrafi rozpozna�
wiele typ�w plik�w np. binarny ELF, biblioteki systemowe, pakiety RPM
oraz wiele r�nych format�w graficznych i d�wi�kowych.

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

%package -n libmagic
Summary:	libmagic library
Summary(pl):    Biblioteka libmagic
Group:		Libraries

%description -n libmagic
Library of functions which operate on magic database file.

%description -n libmagic -l pl
Biblioteka funkcji operuj�cych na pliku bazy danych magic.

%package -n libmagic-devel
Summary:	Header files for libmagic library
Summary(pl):	Pliki nag��wkowe biblioteki libmagic
Group:		Development/Libraries
Requires:	libmagic = %{version}

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
Requires:	libmagic-devel = %{version}

%description -n libmagic-static
Library of functions which operate on magic database file.

This package contains the static libmagic.

%description -n libmagic-static -l pl
Biblioteka funkcji operuj�cych na pliku bazy danych magic.

Ten pakiet zawiera statyczn� wersj� biblioteki.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

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

cat %{SOURCE1} %{SOURCE4} >>$RPM_BUILD_ROOT%{_datadir}/file/magic
# install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}

bzip2 -dc %{SOURCE3} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

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
%attr(755,root,root) %{_bindir}/*
%{_datadir}/file
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
%{_includedir}/magic.h
%{_libdir}/lib*.la
%{_libdir}/lib*.so
%{_mandir}/man3/*

%files -n libmagic-static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
