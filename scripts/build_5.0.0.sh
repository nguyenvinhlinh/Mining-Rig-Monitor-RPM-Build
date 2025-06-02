#!/bin/sh

export RPM_BUILD_DIR=/home/nguyenvinhlinh/Projects/Mining-Rig-Monitor/mining_rig_monitor_rpmbuild

cd /tmp;
rm -rf /tmp/mining_rig_monitor-5.0.0;
rm -rf /tmp/mining_rig_monitor-5.0.0.tar.xz;
rm -rf $RPM_BUILD_DIR/SOURCES/mining_rig_monitor-5.0.0.tar.xz;

git clone --depth 1 --branch v5.0.0 git@github.com:nguyenvinhlinh/Mining-Rig-Monitor.git mining_rig_monitor-5.0.0;
tar -cJf mining_rig_monitor-5.0.0.tar.xz mining_rig_monitor-5.0.0;
cp /tmp/mining_rig_monitor-5.0.0.tar.xz $RPM_BUILD_DIR/SOURCES/;

cd $RPM_BUILD_DIR/SPECS;
export QA_RPATHS=$(( 0x0001|0x0002 ))
rpmbuild --define "_topdir $RPM_BUILD_DIR"  --bb mining_rig_monitor-5.0.0.spec;
