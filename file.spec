Summary:	file(1) command
Summary(de):	Befehl file(1)
Summary(es):	Comando file
Summary(fr):	Commande file(1)
Summary(ja):	ファイルの種類を判別するユーティリティー
Summary(pl):	Polecenie file(1)
Summary(pt_BR):	Um utilit�rio para determinar tipos de arquivos
Summary(ru):	�塢棉堊 通� 椀凖津姪良� 塢佻� 徳別��
Summary(tr):	Dosya tipini belirleme arac�
Summary(uk):	�塢巳堊 通� 徂變挿杜倫 塢丶� 徳別ψ
Name:		file
Version:	3.39
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
Patch2:		%{name}-man.patch
Patch3:		%{name}-palm.patch
Patch4:		%{name}-mime-elf.patch
Patch5:		%{name}-unicode.patch
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
ファイルコマンドはファイルに含まれるデータの種類により個々のファイルを
見分けるために使われる。file は ELF バイナリ、システムライブラリ、
RPM パッケージ、そして種々のグラフィックフォーマットを含む、多くの異なる
ファイルの種類を見分けることが可能である。

%description -l pl
Pakiet ten jest przydatny je�eli chcesz rozpozna� typ plik�w w twoim
systemie. Na przyk�ad je�eli fsck zdeponuje jakie� pliki w katalogu
lost+found, mo�esz uruchomi� file na zdeponowanym pliku i zobaczy�
jaki to jest typ pliku, jest to metoda bezpieczniejsza ni� 'more', ze
wzgl�du na to, �e to mo�e by� plik binarny. File potrafi rozpozna�
wiele typ�w plik�w np. binarny ELF, biblioteki systemowe, pakiety RPM
oraz wiele r鷽nych format�w graficznych i d�wi�kowych.

%description -l pt_BR
Este pacote � �til para descobrir que tipo de arquivo voc� est�
procurando em seu sistema. Por exemplo, se um fsck resulta em um
arquivo forem armazenado no "lost+found", voc� pode rodar file nele
para descobrir se � seguro l�-lo com o "more" ou se ele � um bin�rio.
Ele reconhece v�rios tipos de arquivos, incluindo bin�rios ELF,
bibliotecas de sistema, pacotes RPM e v�rios formatos gr�ficos
diferentes.

%description -l ru
誅輿猟� file 瓶佻蒙旁都嗔 通� 椀凖津姪良� 塢仭 徳別� 佻 珍領挈, � 療�
嗜津雙掃浜嗔. 鑪� 溶崚� 椀凖津棉墮 洋�崚嘖從 卅變蕨岱惣隣� 塢佻�
徳別��, 徊明涸� 舵料厠拇 徳別� 届厖壮� ELF, 喇嘖斗隣� 舵駄貧堙防,
仭謀壅 RPM, 卅斂扶隣� 拝粗扶途防� 届厖壮� � 洋惑� 漬嫻蛭.

%description -l tr
file, bir dosyay� inceleyerek ne t�r bir dosya oldu�u konusunda size
bir fikir verebilir. B�ylece uzant�s�ndan ve ad�ndan ne oldu�unu
茉karamad�顯n�z bir dosyay� hangi yaz�l�m ile kullanabilece�inize ya
da ne yapaca顯n�za karar verebilisiniz. file, temel dosya tiplerini,
�o�u grafik format�n�, �al��t�r�labilir dosyalar�, sistem
kitapl�klar�n� vs. tan�yabilir.

%description -l uk
誅輿猟� file 徂墨夘嘖�徼ぴ慯� 通� 徂變挿杜倫 塢侖 徳別� 佻 珍良�, 冕�
廢� 勇嘖不�. �藁� 溶崚 徂變挿不� 彭棉釦 胞蒙胞嘖� 勁變詫僧υ良� 塢丶�
徳別ψ, � 塹葉 淺嗅� 側料厠� 徳別� 届厖壮� ELF, 喇嘖斗陸 側駄ο堙防,
仭謀塢 RPM, 勁變詫僧υ陸 拝粗�淮� 届厖壮� 堊 汰覗塹 ξ柯�.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p0
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
rm -f install-sh missing mkinstalldirs
aclocal
autoheader
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
