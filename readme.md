# Mining Rig Monitor - RPM Build
This repository is all about creating rpm package for mining rig monitor software. By default, `rpmbuild` directory should be in  `$HOME`. if you want to change it to different directory, you need to use `_topdir` rpm macro. When building rpm, this process should be in `docker` or `VM`, thus, we follow rpm convention.

## Step 1. Copy source code tarball to `SOURCES`.
## Step 2. Create new `SPECS/.spec` file

```bash
cd SPECS;

rpmdev-newspec;
```

Update:

- Version
- Release
- Source0



## Step 3. Run `rpmbuild`

```bash
cd SPECS;

rpmbuild -bb mining-rig-monitor-1.0.0.spec;
```

Gonna see error:
```
ERROR   0002: file '/opt/mining_rig_monitor/lib/crypto-5.5/priv/lib/crypto.so' contains an invalid runpath '/usr/local/lib64'
```

`crypto` is an erlang module. I dont know how to modify it. this is a work around!
```
cd SPECS;
export QA_RPATHS=$(( 0x0001|0x0002 ))
rpmbuild -bb mining-rig-monitor-1.0.0.spec;
```

## Step 4. Provide `%files`
Those file would be listed after running `rpmbuild -bb mining-rig-monitor-1.0.0.spec`. Append it and re-run `rpmbuild -bb mining-rig-monitor-1.0.0.spec` to make rpm.
```
RPM build errors:
    Installed (but unpackaged) file(s) found:
   /opt/mining_rig_monitor/bin/migrate
   /opt/mining_rig_monitor/bin/migrate.bat
   /opt/mining_rig_monitor/bin/mining_rig_monitor
   /opt/mining_rig_monitor/bin/mining_rig_monitor.bat
   /opt/mining_rig_monitor/bin/server

```

Check out `RPMS` directory! RPM should be there!

```
➜ rpmbuild (master) ✗ tree -L 3
.
├── BUILD
├── BUILDROOT
├── readme.md
├── RPMS
│   └── x86_64
│       ├── mining-rig-monitor-1.0.0-1.fc40.x86_64.rpm <----------- your file here!
│       ├── mining-rig-monitor-debuginfo-1.0.0-1.fc40.x86_64.rpm
│       └── mining-rig-monitor-debugsource-1.0.0-1.fc40.x86_64.rpm
├── SOURCES
│   └── mining-rig-monitor-1.0.0.tar.xz
├── SPECS
│   ├── mining-rig-monitor-1.0.0.spec
│   └── newpackage.spec~
└── SRPMS

```
