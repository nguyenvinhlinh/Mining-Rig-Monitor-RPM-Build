Name: mining-rig-monitor
Version: 3.0.0
Release: 1%{?dist}
Summary: A software helps monitor mining rig including ASICS, CPU, GPU miners

License: GNU General Public License v3.0
URL: https://github.com/nguyenvinhlinh/Mining-Rig-Monitor
Source0: mining-rig-monitor-3.0.0.tar.xz


# BuildRequires:
# Requires:

%description
A software helps monitor mining rig including ASICS, CPU, GPU miners

%prep

%autosetup

%build
mix deps.get --only prod
MIX_ENV=prod mix compile
cd assets
npm install
cd ..
mix assets.setup
mix assets.deploy
MIX_ENV=prod mix release

%install
mkdir -p %{buildroot}/opt/mining_rig_monitor
cp -r _build/prod/rel/mining_rig_monitor/* %{buildroot}/opt/mining_rig_monitor

%files





%changelog
* Sun Apr 13 2025 Nguyen Vinh Linh <nguyenvinhlinh93@gmail.com>
- CPU/GPU Miner CRUD
- Pool/Wallet Address CURD
- CPU/GPU Mining Playbook CRUD
- Allow CPU/GPU Sentry to submit log
- Allow CPU/GPU Sentry to fetch playbook


* Sat Feb 01 2025 Nguyen Vinh Linh <nguyenvinhlinh93@gmail.com>
- Login feature
- ASIC Monitoring feature
