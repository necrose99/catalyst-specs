# stage4 specfile
# used to build a stage4
subarch: amd64
version_stamp: stage4-ceph-amd64-nomultilib-20150504
target: stage4
rel_type: container
profile: steveeJ:container/linux/amd64-native/ceph
snapshot: 2015.05.04
source_subpath: prebuilt/stage3-amd64-nomultilib-20150430
portage_confdir: confdir
pkgcache_path: pkgs
portage_overlay: /usr/local/portage/personal-portage-overlay
stage4/packages: @profile
stage4/fsscript: stage4-ceph-amd64-nomultilib.fsscript
#stage4/root_overlay: ceph_root_overlay
stage4/empty: /var/tmp /var/cache