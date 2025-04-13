cd /tmp;
rm -rf mining-rig-monitor-3.0.0;
rm -rf mining-rig-monitor-3.0.0.tar.xz;
rm -rf ~/rpmbuild/SOURCES/mining-rig-monitor-3.0.0.tar.xz;

git clone --depth 1 --branch v3.0.0 git@github.com:nguyenvinhlinh/Mining-Rig-Monitor.git mining-rig-monitor-3.0.0;
tar -cJvf mining-rig-monitor-3.0.0.tar.xz mining-rig-monitor-3.0.0;
cp /tmp/mining-rig-monitor-3.0.0.tar.xz ~/rpmbuild/SOURCES/;

cd ~/rpmbuild/SPECS/
export QA_RPATHS=$(( 0x0001|0x0002 ))
rpmbuild --bb mining-rig-monitor-3.0.0.spec;
