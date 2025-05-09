# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device z3s
%define vendor samsung

%define vendor_pretty Samsung
%define device_pretty Galaxy S20 Ultra 5G

%define installable_zip 1

%define droid_target_aarch64 1

%define straggler_files \
	/bugreports \
	/d \
	/sdcard \
   	/dsp \
   	/firmware \
   	/persist \
   	/product \
   	/system_ext \
%{nil}

%define makefstab_skip_entries / /product /system /system_ext /vendor

%include rpm/dhd/droid-hal-device.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

