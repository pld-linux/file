Summary:	file(1) command
Summary(de):	Befehl file(1)
Summary(es):	Comando file
Summary(fr):	Commande file(1)
Summary(ja):	•’•°•§•Î§ŒºÔŒ‡§Ú»Ω Ã§π§Î•Ê°º•∆•£•Í•∆•£°º
Summary(pl):	Polecenie file(1)
Summary(pt_BR):	Um utilit·rio para determinar tipos de arquivos
Summary(ru):	ı‘…Ã…‘¡ ƒÃ— œ–“≈ƒ≈Ã≈Œ…— ‘…–œ◊ ∆¡ Ãœ◊
Summary(tr):	Dosya tipini belirleme arac˝
Summary(uk):	ı‘…Ã¶‘¡ ƒÃ— ◊…⁄Œ¡ﬁ≈ŒŒ— ‘…–¶◊ ∆¡ Ã¶◊
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
Patch5:		%{name}-palm.patch
Patch6:		%{name}-mime-elf.patch
Patch7:		%{name}-unicode.patch
Patch8:		%{name}-mng.patch
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
Sie kˆnnen dieses Paket verwenden, um zu bestimmen, welches Format
eine bestimmte Datei hat. Wird durch fsck eine Datei in lost+found
gespeichert, kˆnnen Sie 'file' ausf¸hren, um herauszufinden, ob Sie
sie mit 'more' einsehen kˆnnen, oder ob es sich um ein Bin‰rprogramm
handelt Das Programm erkennt u.a. ELF-Bin‰rprogramme,
System-Libraries, RPM-Pakete und viele Grafikformate.

%description -l es
Este paquete es ˙til para descubrir que tipo de archivo est·s buscando
en tu sistema. Por ejemplo, si fsck resulta un archivo que fue
almacenado en el "lost+found", tu puedes ejecutar file en Èl para
descubrir si es seguro leerlo con el "more" o si es un binario.
Reconoce varios tipos de archivos, incluyendo binarios ELF,
bibliotecas de sistema, paquetes RPM y varios formatos gr·ficos
diferentes.

%description -l fr
Ce paquetage sert ‡ trouver le type du fichier que vous recherchez sur
votre systËme. Par exemple, si un fsck fait qu'un fichier a ÈtÈ stockÈ
dans lost+found, vous pouvez lancer file dessus pour savoir si on peut
faire un more, ou s'il s'agit d'un binaire. Il reconnaÓt de nombreux
types de fichiers dont les binaires ELF, les bibliothËques systËmes,
les paquetages RPM et de nombreux formats graphiques diffÈrents.

%description -l ja
•’•°•§•Î•≥•ﬁ•Û•…§œ•’•°•§•Î§À¥ﬁ§ﬁ§Ï§Î•«°º•ø§ŒºÔŒ‡§À§Ë§Í∏ƒ°π§Œ•’•°•§•Î§Ú
∏´ ¨§±§Î§ø§·§Àª»§Ô§Ï§Î°£file §œ ELF •–•§• •Í°¢•∑•π•∆•‡•È•§•÷•È•Í°¢
RPM •—•√•±°º•∏°¢§Ω§∑§∆ºÔ°π§Œ•∞•È•’•£•√•Ø•’•©°º•ﬁ•√•»§Ú¥ﬁ§‡°¢¬ø§Ø§Œ∞€§ §Î
•’•°•§•Î§ŒºÔŒ‡§Ú∏´ ¨§±§Î§≥§»§¨≤ƒ«Ω§«§¢§Î°£

%description -l pl
Pakiet ten jest przydatny jeøeli chcesz rozpoznaÊ typ plikÛw w twoim
systemie. Na przyk≥ad jeøeli fsck zdeponuje jakie∂ pliki w katalogu
lost+found, moøesz uruchomiÊ file na zdeponowanym pliku i zobaczyÊ
jaki to jest typ pliku, jest to metoda bezpieczniejsza niø 'more', ze
wzglÍdu na to, øe to moøe byÊ plik binarny. File potrafi rozpoznaÊ
wiele typÛw plikÛw np. binarny ELF, biblioteki systemowe, pakiety RPM
oraz wiele rÛønych formatÛw graficznych i dºwiÍkowych.

%description -l pt_BR
Este pacote È ˙til para descobrir que tipo de arquivo vocÍ est·
procurando em seu sistema. Por exemplo, se um fsck resulta em um
arquivo forem armazenado no "lost+found", vocÍ pode rodar file nele
para descobrir se È seguro lÍ-lo com o "more" ou se ele È um bin·rio.
Ele reconhece v·rios tipos de arquivos, incluindo bin·rios ELF,
bibliotecas de sistema, pacotes RPM e v·rios formatos gr·ficos
diferentes.

%description -l ru
ÎœÕ¡Œƒ¡ file …”–œÃÿ⁄’≈‘”— ƒÃ— œ–“≈ƒ≈Ã≈Œ…— ‘…–¡ ∆¡ Ã¡ –œ ƒ¡ŒŒŸÕ, ◊ Œ≈Õ
”œƒ≈“÷¡›…Õ”—. ÔŒ¡ Õœ÷≈‘ œ–“≈ƒ≈Ã…‘ÿ ÕŒœ÷≈”‘◊œ “¡⁄Œœœ¬“¡⁄ŒŸ» ‘…–œ◊
∆¡ Ãœ◊, ◊ÀÃ¿ﬁ¡— ¬…Œ¡“ŒŸ≈ ∆¡ ÃŸ ∆œ“Õ¡‘¡ ELF, ”…”‘≈ÕŒŸ≈ ¬…¬Ã…œ‘≈À…,
–¡À≈‘Ÿ RPM, “¡⁄Ã…ﬁŒŸ≈ «“¡∆…ﬁ≈”À…≈ ∆œ“Õ¡‘Ÿ … ÕŒœ«œ ƒ“’«…».

%description -l tr
file, bir dosyay˝ inceleyerek ne t¸r bir dosya olduu konusunda size
bir fikir verebilir. Bˆylece uzant˝s˝ndan ve ad˝ndan ne olduunu
Á˝karamad˝˝n˝z bir dosyay˝ hangi yaz˝l˝m ile kullanabileceinize ya
da ne yapaca˝n˝za karar verebilisiniz. file, temel dosya tiplerini,
Áou grafik format˝n˝, Áal˝˛t˝r˝labilir dosyalar˝, sistem
kitapl˝klar˝n˝ vs. tan˝yabilir.

%description -l uk
ÎœÕ¡Œƒ¡ file ◊…Àœ“…”‘œ◊’§‘ÿ”— ƒÃ— ◊…⁄Œ¡ﬁ≈ŒŒ— ‘…–’ ∆¡ Ã’ –œ ƒ¡Œ…», —À¶
◊¶Œ Õ¶”‘…‘ÿ. ˜œŒ¡ Õœ÷≈ ◊…⁄Œ¡ﬁ…‘… ◊≈Ã…À’ À¶ÃÿÀ¶”‘ÿ “¶⁄ŒœÕ¡Œ¶‘Œ…» ‘…–¶◊
∆¡ Ã¶◊, ’ ‘œÕ’ ﬁ…”Ã¶ ¬¶Œ¡“Œ¶ ∆¡ Ã… ∆œ“Õ¡‘’ ELF, ”…”‘≈ÕŒ¶ ¬¶¬Ã¶œ‘≈À…,
–¡À≈‘… RPM, “¶⁄ŒœÕ¡Œ¶‘Œ¶ «“¡∆¶ﬁŒ¶ ∆œ“Õ¡‘… ‘¡ ¬¡«¡‘œ ¶Œ€…».

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p0
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

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
