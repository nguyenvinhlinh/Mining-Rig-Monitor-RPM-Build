Name: mining_rig_monitor
Version: 5.0.0
Release: 1%{?dist}
Summary: A software helps monitor mining rig including ASICS, CPU, GPU miners

License: GNU General Public License v3.0
URL: https://github.com/nguyenvinhlinh/Mining-Rig-Monitor
Source0: mining_rig_monitor-5.0.0.tar.xz

%description
A software helps monitor mining rig including ASICS, CPU, GPU miners

%global debug_package %{nil}
%define _build_id_links none

%prep

%autosetup

%build
mix deps.get --only prod
MIX_ENV=prod mix compile
cd assets
npm install
cd ..
MIX_ENV=prod mix assets.deploy
MIX_ENV=prod mix release

%install
mkdir -p %{buildroot}/opt/mining_rig_monitor
cp -r _build/prod/rel/mining_rig_monitor/* %{buildroot}/opt/mining_rig_monitor

%files
%dir /opt/mining_rig_monitor
/opt/mining_rig_monitor/*




%changelog
* Mon Jun 2 2025 Nguyen Vinh Linh <nguyenvinhlinh93@gmail.com>
- add remote relay controller UI to turn on/off ASIC Miner

* Wed Apr 30 2025 Nguyen Vinh Linh <nguyenvinhlinh93@gmail.com>
- revamp css

* Sun Apr 13 2025 Nguyen Vinh Linh <nguyenvinhlinh93@gmail.com>
- CPU/GPU Miner CRUD
- Pool/Wallet Address CURD
- CPU/GPU Mining Playbook CRUD
- Allow CPU/GPU Sentry to submit log
- Allow CPU/GPU Sentry to fetch playbook


* Sat Feb 01 2025 Nguyen Vinh Linh <nguyenvinhlinh93@gmail.com>
- Login feature
- ASIC Monitoring feature
