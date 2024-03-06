Summary:      Default file system
Name:         filesystem
Version:      1.1
Release:      20%{?dist}
License:      GPLv3
Group:        System Environment/Base
Vendor:       Microsoft Corporation
URL:          http://www.linuxfromscratch.org
Distribution:   Azure Linux

%description
The filesystem package is one of the basic packages that is installed
on a Linux system. Filesystem contains the basic directory
layout for a Linux operating system, including the correct permissions
for the directories. This version is for a system configured with systemd.

%prep
%build
%install
#
#	6.5.  Creating Directories
#
install -vdm 755 %{buildroot}/{dev,run/{media/{floppy,cdrom},lock}}
install -vdm 755 %{buildroot}/{etc/{opt,sysconfig},home,mnt}
install -vdm 700 %{buildroot}/boot
install -vdm 755 %{buildroot}/{var}
install -vdm 755 %{buildroot}/opt
install -vdm 755 %{buildroot}/media
install -dv -m 0750 %{buildroot}/root
install -dv -m 1777 %{buildroot}/tmp %{buildroot}/var/tmp
install -vdm 755 %{buildroot}/usr/{,local/}{bin,include,lib,sbin,src}
install -vdm 755 %{buildroot}/usr/{,local/}share/{color,dict,doc,info,locale,man}
install -vdm 755 %{buildroot}/usr/{,local/}share/{misc,terminfo,zoneinfo}
install -vdm 755 %{buildroot}/usr/libexec
install -vdm 755 %{buildroot}/usr/{,local/}share/man/man{1..8}
install -vdm 755 %{buildroot}/etc/profile.d
install -vdm 755 %{buildroot}/usr/lib/debug/{lib,bin,sbin,usr,.dwz}

ln -svfn usr/lib %{buildroot}/lib
ln -svfn usr/bin %{buildroot}/bin
ln -svfn usr/sbin %{buildroot}/sbin

ln -svfn ../bin %{buildroot}/usr/lib/debug/usr/bin
ln -svfn ../sbin %{buildroot}/usr/lib/debug/usr/sbin
ln -svfn ../lib %{buildroot}/usr/lib/debug/usr/lib

	ln -svfn usr/lib %{buildroot}/lib64
	ln -svfn lib %{buildroot}/usr/lib64
	ln -svfn lib %{buildroot}/usr/local/lib64
        ln -svfn lib %{buildroot}/usr/lib/debug/lib64
        ln -svfn ../lib %{buildroot}/usr/lib/debug/usr/lib64
        ln -svfn ../.dwz %{buildroot}/usr/lib/debug/usr/.dwz

install -vdm 755 %{buildroot}/var/{log,mail,spool,mnt,srv}

ln -svfn var/srv %{buildroot}/srv
ln -svfn ../run %{buildroot}/var/run
ln -svfn ../run/lock %{buildroot}/var/lock
install -vdm 755 %{buildroot}/var/{opt,cache,lib/{color,misc,locate},local}
install -vdm 755 %{buildroot}/mnt/cdrom
install -vdm 755 %{buildroot}/mnt/hgfs

#
#	Configuration files
#
cat > %{buildroot}/etc/passwd <<- "EOF"
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/dev/null:/bin/false
daemon:x:6:6:Daemon User:/dev/null:/bin/false
messagebus:x:18:18:D-Bus Message Daemon User:/var/run/dbus:/bin/false
systemd-bus-proxy:x:72:72:systemd Bus Proxy:/:/bin/false
systemd-journal-gateway:x:73:73:systemd Journal Gateway:/:/bin/false
systemd-journal-remote:x:74:74:systemd Journal Remote:/:/bin/false
systemd-journal-upload:x:75:75:systemd Journal Upload:/:/bin/false
systemd-network:x:76:76:systemd Network Management:/:/bin/false
systemd-resolve:x:77:77:systemd Resolver:/:/bin/false
systemd-timesync:x:78:78:systemd Time Synchronization:/:/bin/false
systemd-coredump:x:79:79:systemd Core Dumper:/:/usr/bin/false
systemd-oom:x:80:80:systemd Userspace OOM Killer:/:/usr/bin/false
nobody:x:65534:65533:Unprivileged User:/dev/null:/bin/false
EOF
cat > %{buildroot}/etc/group <<- "EOF"
root:x:0:
bin:x:1:daemon
sys:x:2:
kmem:x:3:
tape:x:4:
tty:x:5:
daemon:x:6:
floppy:x:7:
disk:x:8:
lp:x:9:
dialout:x:10:
audio:x:11:
video:x:12:
utmp:x:13:
usb:x:14:
cdrom:x:15:
adm:x:16:
messagebus:x:18:
systemd-journal:x:23:
input:x:24:
mail:x:34:
lock:x:54:
dip:x:30:
render:x:31:
kvm:x:32:
systemd-bus-proxy:x:72:
systemd-journal-gateway:x:73:
systemd-journal-remote:x:74:
systemd-journal-upload:x:75:
systemd-network:x:76:
systemd-resolve:x:77:
systemd-timesync:x:78:
systemd-coredump:x:79:
systemd-oom:x:80:
nogroup:x:65533:
users:x:100:
sudo:x:27:
wheel:x:28:
EOF
#
#	7.3. Customizing the /etc/hosts File"
#
cat > %{buildroot}/etc/hosts <<- "EOF"
127.0.0.1   localhost localhost.localdomain
::1         localhost localhost.localdomain ipv6-localhost ipv6-loopback
EOF
# host.conf file
cat > %{buildroot}/etc/host.conf <<- "EOF"
multi on
EOF
#
#	7.9. Configuring the setclock Script"
#
cat > %{buildroot}/etc/sysconfig/clock <<- "EOF"
# Begin /etc/sysconfig/clock

UTC=1

# Set this to any options you might need to give to hwclock,
# such as machine hardware clock type for Alphas.
CLOCKPARAMS=

# End /etc/sysconfig/clock
EOF
#
#	7.10. Configuring the Linux Console"
#
cat > %{buildroot}/etc/sysconfig/console <<- "EOF"
# Begin /etc/sysconfig/console
#       Begin /etc/sysconfig/console
#       KEYMAP="us"
#       FONT="lat1-16 -m utf8"
#       FONT="lat1-16 -m 8859-1"
#       KEYMAP_CORRECTIONS="euro2"
#       UNICODE="1"
#       LEGACY_CHARSET="iso-8859-1"
# End /etc/sysconfig/console
EOF
#
#	7.13. The Bash Shell Startup Files
#
cat > %{buildroot}/etc/profile <<- "EOF"
# Begin /etc/profile
# Written for Beyond Linux From Scratch
# by James Robertson <jameswrobertson@earthlink.net>
# modifications by Dagmar d'Surreal <rivyqntzne@pbzpnfg.arg>

# System wide environment variables and startup programs.

# System wide aliases and functions should go in /etc/bashrc.  Personal
# environment variables and startup programs should go into
# ~/.bash_profile.  Personal aliases and functions should go into
# ~/.bashrc.

# Functions to help us manage paths.  Second argument is the name of the
# path variable to be modified (default: PATH)
pathremove () {
        local IFS=':'
        local NEWPATH
        local DIR
        local PATHVARIABLE=${2:-PATH}
        for DIR in ${!PATHVARIABLE} ; do
                if [ "$DIR" != "$1" ] ; then
                  NEWPATH=${NEWPATH:+$NEWPATH:}$DIR
                fi
        done
        export $PATHVARIABLE="$NEWPATH"
}

pathprepend () {
        pathremove $1 $2
        local PATHVARIABLE=${2:-PATH}
        export $PATHVARIABLE="$1${!PATHVARIABLE:+:${!PATHVARIABLE}}"
}

pathappend () {
        pathremove $1 $2
        local PATHVARIABLE=${2:-PATH}
        export $PATHVARIABLE="${!PATHVARIABLE:+${!PATHVARIABLE}:}$1"
}

export -f pathremove pathprepend pathappend

# Set the initial path
# Block unnessary as this is set elsewhere.
# export PATH=$PATH:/bin:/usr/bin

# if [ $EUID -eq 0 ] ; then
#         pathappend /sbin:/usr/sbin
#         unset HISTFILE
# fi

# Setup some environment variables.
export HISTSIZE=1000
export HISTIGNORE="&:[bf]g:exit"

# Set some defaults for graphical systems
export XDG_DATA_DIRS=/usr/share/
export XDG_CONFIG_DIRS=/etc/xdg/

# Setup a red prompt for root and a green one for users.
NORMAL="\[\e[0m\]"
RED="\[\e[1;31m\]"
GREEN="\[\e[1;32m\]"
if [[ $EUID == 0 ]] ; then
  PS1="$RED\u@\h [ $NORMAL\w$RED ]# $NORMAL"
else
  PS1="$GREEN\u@\h [ $NORMAL\w$GREEN ]\$ $NORMAL"
fi

for script in /etc/profile.d/*.sh ; do
        if [ -r $script ] ; then
                . $script
        fi
done

unset script RED GREEN NORMAL
# End /etc/profile
EOF
#
#	7.14. Creating the /etc/inputrc File
#
cat > %{buildroot}/etc/inputrc <<- "EOF"
# Begin /etc/inputrc
# Modified by Chris Lynn <roryo@roryo.dynup.net>

# Allow the command prompt to wrap to the next line
set horizontal-scroll-mode Off

# Enable 8bit input
set meta-flag On
set input-meta On

# Turns off 8th bit stripping
set convert-meta Off

# Keep the 8th bit for display
set output-meta On

# none, visible or audible
set bell-style none

# All of the following map the escape sequence of the value
# contained in the 1st argument to the readline specific functions
"\eOd": backward-word
"\eOc": forward-word

# for linux console
"\e[1~": beginning-of-line
"\e[4~": end-of-line
# page up - history search backward
"\e[5~": history-search-backward
# page down - history search forward
"\e[6~": history-search-forward
"\e[3~": delete-char
"\e[2~": quoted-insert

# for xterm
"\eOH": beginning-of-line
"\eOF": end-of-line

# for Konsole
"\e[H": beginning-of-line
"\e[F": end-of-line

# ctrl + left/right arrow to jump words
"\e[1;5C": forward-word
"\e[1;5D": backward-word

# End /etc/inputrc
EOF
#
#	8.2. Creating the /etc/fstab File
#
touch %{buildroot}/etc/fstab

#
#		chapter 9.1. The End
#

# Since these following symlinks are ghosted entries, create them manually upon
# package installation.

# Use Lua to achieve this since when filesystem installs, there may not be any
# other packages installed if this is a new environment.
%post -p <lua>
posix.symlink("lib", "/usr/lib/debug/lib64")
posix.symlink("../bin", "/usr/lib/debug/usr/bin")
posix.symlink("../sbin", "/usr/lib/debug/usr/sbin")
posix.symlink("../lib", "/usr/lib/debug/usr/lib")
posix.symlink("../lib", "/usr/lib/debug/usr/lib64")
posix.symlink("../.dwz", "/usr/lib/debug/usr/.dwz")
return 0

%pretrans -p <lua>
posix.mkdir("/proc")
posix.mkdir("/sys")
posix.chmod("/proc", 0555)
posix.chmod("/sys", 0555)
return 0

%files
%defattr(-,root,root)
#	Root filesystem
/bin
%dir /boot
%dir /dev
%dir /etc
%dir /home
/lib
%dir /opt

/media
%dir /mnt
%ghost %attr(555,root,root) /proc
%dir /root
%dir /run
/sbin
/srv
%ghost %attr(555,root,root) /sys
%dir /tmp
%dir /usr
%dir /var
#	etc fileystem
%dir /etc/opt
%config(noreplace) /etc/fstab
%config(noreplace) /etc/group
%config(noreplace) /etc/host.conf
%config(noreplace) /etc/hosts
%config(noreplace) /etc/inputrc
%config(noreplace) /etc/passwd
%config(noreplace) /etc/profile
%dir /etc/sysconfig
%config(noreplace) /etc/sysconfig/clock
%config(noreplace) /etc/sysconfig/console
%dir /etc/profile.d
#	media filesystem
%dir /run/media/cdrom
%dir /run/media/floppy
#	run filesystem
%dir /run/lock
#	usr filesystem
%dir /mnt/cdrom
%dir /mnt/hgfs
%dir /usr/bin
%dir /usr/include
%dir /usr/lib
%dir /usr/lib/debug
%dir /usr/lib/debug/bin
%dir /usr/lib/debug/lib
%dir /usr/lib/debug/sbin
%dir /usr/lib/debug/usr
%dir /usr/lib/debug/.dwz
%dir /usr/libexec
%dir /usr/local
%dir /usr/local/bin
%dir /usr/local/include
%dir /usr/local/lib
%dir /usr/local/sbin
%dir /usr/local/share
%dir /usr/local/share/color
%dir /usr/local/share/dict
%dir /usr/local/share/doc
%dir /usr/local/share/info
%dir /usr/local/share/locale
%dir /usr/local/share/man
%dir /usr/local/share/man/man1
%dir /usr/local/share/man/man2
%dir /usr/local/share/man/man3
%dir /usr/local/share/man/man4
%dir /usr/local/share/man/man5
%dir /usr/local/share/man/man6
%dir /usr/local/share/man/man7
%dir /usr/local/share/man/man8
%dir /usr/local/share/misc
%dir /usr/local/share/terminfo
%dir /usr/local/share/zoneinfo
%dir /usr/local/src
%dir /usr/sbin
%dir /usr/share
%dir /usr/share/color
%dir /usr/share/dict
%dir /usr/share/doc
%dir /usr/share/info
%dir /usr/share/locale
%dir /usr/share/man
%dir /usr/share/man/man1
%dir /usr/share/man/man2
%dir /usr/share/man/man3
%dir /usr/share/man/man4
%dir /usr/share/man/man5
%dir /usr/share/man/man6
%dir /usr/share/man/man7
%dir /usr/share/man/man8
%dir /usr/share/misc
%dir /usr/share/terminfo
%dir /usr/share/zoneinfo
%dir /usr/src

# 	ghosted /usr/lib/debug symlinks.
#
#   Ghost them to allow others packages to create/provide files
#   inside the symlinks without conflicting with this package. 
%ghost /usr/lib/debug/lib64
%ghost /usr/lib/debug/usr/bin
%ghost /usr/lib/debug/usr/lib
%ghost /usr/lib/debug/usr/lib64
%ghost /usr/lib/debug/usr/sbin
%ghost /usr/lib/debug/usr/.dwz

#	var filesystem
%dir /var/cache
%dir /var/lib
%dir /var/lib/color
%dir /var/lib/locate
%dir /var/lib/misc
%dir /var/local
%dir /var/log
%dir /var/mail
%dir /var/mnt
%dir /var/srv
%dir /var/opt
%dir /var/spool
%dir /var/tmp
/var/lock
/var/run

/lib64
/usr/lib64
/usr/local/lib64

%changelog
* Mon Mar 04 2024 Dan Streetman <ddstreet@microsoft.com> - 1.1-20
- move filesystem-asc stuff into asc
- move /etc/modprobe.d into kmod package
- move /etc/mtab from filesystem to util-linux package
- move /var/log/* files from filesystem to systemd package
- remove opensuse-style 'proxy' config file

* Wed Feb 28 2024 Dan Streetman <ddstreet@microsoft.com> - 1.1-19
- fix /etc/hosts
- add /etc/host.conf to enable multi

* Thu Nov 30 2023 Dan Streetman <ddstreet@ieee.org> - 1.1-18
- Remove umask 027

* Thu Oct 12 2023 Chris PeBenito <chpebeni@microsoft.com> - 1.1-17
- Restore the /opt directory.

* Mon Oct 09 2023 Chris Co <chrco@microsoft.com> - 1.1-16
- Make /media a proper directory

* Thu Jun 29 2023 Tobias Brick <tobiasb@microsoft.com> - 1.1-15
- Revert: Remove setting umask from /etc/profile and add it to a separate file in /etc/profile.d

* Tue Jun 13 2023 Andy Zaugg <azaugg@linkedin.com> - 1.1-14
- Adding /usr/local/sbin as per FHS

* Thu May 18 2023 Tobias Brick <tobiasb@microsoft.com> - 1.1-13
- Remove setting umask from /etc/profile and add it to a separate file in /etc/profile.d

* Thu Sep 14 2022 Thara Gopinath <tgopinath@microsoft.com> - 1.1-12
- Add the 'systemd-coredump' and 'systemd-oom' user and group accounts.

* Mon Jul 18 2022 Minghe Ren <mingheren@microsoft.com> - 1.1-11
- Update etc/modprobe.d/ folder to include new multiple config files and improve security
- Add subpackage asc to include all the new config files

* Thu Jun 16 2022 Olivia Crain <oliviacrain@microsoft.com> - 1.1-10
- Mark /proc and /sys as %%ghost
- Create /proc and /sys as a pretransaction step

*   Wed May 18 2022 Brendan Kerrigan <bkerrigan@microsoft.com> 1.1-9
-   Update /etc/inputrc to enable Ctrl+LeftArrow and Ctrl+RightArrow word jumping binds.
-   License Verified.
*   Mon Sep 28 2020 Ruying Chen <v-ruyche@microsoft.com> 1.1-8
-   Add folders and symlinks for .dwz files.
*   Mon Jun 15 2020 Joe Schmitt <joschmit@microsoft.com> 1.1-7
-   Use ghost directive for /usr/lib/debug/* symlinks to avoid conflicting with debuginfo packages.
*   Wed May 20 2020 Emre Girgin <mrgirgin@microsoft.com> 1.1-6
-   Change /boot directory permissions to 600.
*   Wed May 20 2020 Joe Schmitt <joschmit@microsoft.com> 1.1-5
-   Add render and kvm group by default.
*   Tue Sep 03 2019 Mateusz Malisz <mamalisz@microsoft.com> 1.1-4
-   Initial CBL-Mariner import from Photon (license: Apache2).
*   Wed May 8 2019 Alexey Makhalov <amakhalov@vmware.com> 1.1-3
-   Set 'x' as a root password placeholder
*   Tue Nov 14 2017 Alexey Makhalov <amakhalov@vmware.com> 1.1-2
-   Aarch64 support
*   Fri Sep 15 2017 Anish Swaminathan <anishs@vmware.com>  1.1-1
-   Move network file from filesystem package
*   Fri Apr 21 2017 Alexey Makhalov <amakhalov@vmware.com> 1.0-13
-   make /var/run symlink to /run and keep it in rpm
*   Thu Apr 20 2017 Bo Gan <ganb@vmware.com> 1.0-12
-   Fix /usr/local/lib64 symlink
*   Wed Mar 08 2017 Vinay Kulkarni <kulkarniv@vmware.com> 1.0-11
-   Create default DHCP net config in 99-dhcp-en.network instead of 10-dhcp-en.network
*   Wed Aug 24 2016 Alexey Makhalov <amakhalov@vmware.com> 1.0-10
-   /etc/inputrc PgUp/PgDown for history search
*   Tue Jul 12 2016 Divya Thaluru <dthaluru@vmware.com> 1.0-9
-   Added filesystem for debug libraries and binaries
*   Fri Jul 8 2016 Divya Thaluru <dthaluru@vmware.com> 1.0-8
-   Removing multiple entries of localhost in /etc/hosts file
*   Fri May 27 2016 Divya Thaluru <dthaluru@vmware.com> 1.0-7
-   Fixed nobody user uid and group gid
*   Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.0-6
-   GA - Bump release of all rpms
*   Wed May 4 2016 Divya Thaluru <dthaluru@vmware.com> 1.0-5
-   Removing non-existent users from /etc/group file
*   Fri Apr 29 2016 Mahmoud Bassiouny <mbassiouny@vmware.com> 1.0-4
-   Updating the /etc/hosts file
*   Fri Apr 22 2016 Divya Thaluru <dthaluru@vmware.com> 1.0-3
-   Setting default umask value to 027
*   Thu Apr 21 2016 Anish Swaminathan <anishs@vmware.com> 1.0-2
-   Version update for network file change
*   Mon Jan 18 2016 Anish Swaminathan <anishs@vmware.com> 1.0-1
-   Reset version to match with Photon version
*   Wed Jan 13 2016 Mahmoud Bassiouny <mbassiouny@vmware.com> 7.5-13
-   Support to set proxy configuration file - SLES proxy configuration implementation.
*   Thu Jan 7 2016 Mahmoud Bassiouny <mbassiouny@vmware.com> 7.5-12
-   Removing /etc/sysconfig/network file.
*   Mon Nov 16 2015 Mahmoud Bassiouny <mbassiouny@vmware.com> 7.5-11
-   Removing /etc/fstab mount entries.
*   Mon Nov 16 2015 Sharath George <sharathg@vmware.com> 7.5-10
-   Removint /opt from filesystem.
*   Fri Oct 02 2015 Vinay Kulkarni <kulkarniv@vmware.com> 7.5-9
-   Dump build-number and release version from macros.
*   Fri Aug 14 2015 Sharath George <sharathg@vmware.com> 7.5-8
-   upgrading release to TP2
*   Tue Jun 30 2015 Alexey Makhalov <amakhalov@vmware.com> 7.5-7
-   /etc/profile.d permission fix
*   Tue Jun 23 2015 Divya Thaluru <dthaluru@vmware.com> 7.5-6
-   Adding group dip
*   Mon Jun 22 2015 Divya Thaluru <dthaluru@vmware.com> 7.5-5
-   Fixing lsb-release file
*   Tue Jun 16 2015 Alexey Makhalov <amakhalov@vmware.com> 7.5-4
-   Change users group id to 100.
-   Add audio group to users group.
*   Mon Jun 15 2015 Sharath George <sharathg@vmware.com> 7.5-3
-   Change the network match for dhcp.
*   Mon May 18 2015 Touseef Liaqat <tliaqat@vmware.com> 7.5-2
-   Update according to UsrMove.
*   Wed Nov 5 2014 Divya Thaluru <dthaluru@vmware.com> 7.5-1
-   Initial build. First version
