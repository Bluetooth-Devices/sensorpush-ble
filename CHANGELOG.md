# CHANGELOG



## v1.7.1 (2024-11-01)

### Chore

* chore(pre-commit.ci): pre-commit autoupdate (#35)

Co-authored-by: pre-commit-ci[bot] &lt;66853113+pre-commit-ci[bot]@users.noreply.github.com&gt; ([`d65b5ab`](https://github.com/Bluetooth-Devices/sensorpush-ble/commit/d65b5ab9ffa8a91d7f6bb5a5df73bff07b3aa4ab))

### Fix

* fix: model TC.x being detected as HT.w with active scans (#37) ([`a04e13c`](https://github.com/Bluetooth-Devices/sensorpush-ble/commit/a04e13cec97a0c905c6cd2a0f2f38e462af17974))

### Unknown

* Remove FUNDING.yml (#34) ([`abf474e`](https://github.com/Bluetooth-Devices/sensorpush-ble/commit/abf474eb3d8df60bac5fe59b5f40cdc089bd6ee7))


## v1.7.0 (2024-10-22)

### Chore

* chore(pre-commit.ci): pre-commit autoupdate (#31) ([`37b7c3e`](https://github.com/Bluetooth-Devices/sensorpush-ble/commit/37b7c3eac03ec38842794132c5f67c7c01362514))

* chore(pre-commit.ci): pre-commit autoupdate (#30)

Co-authored-by: pre-commit-ci[bot] &lt;66853113+pre-commit-ci[bot]@users.noreply.github.com&gt; ([`9a9af04`](https://github.com/Bluetooth-Devices/sensorpush-ble/commit/9a9af049cdc92723775553da9aebcedf52106d60))

* chore(pre-commit.ci): pre-commit autoupdate (#29)

Co-authored-by: pre-commit-ci[bot] &lt;66853113+pre-commit-ci[bot]@users.noreply.github.com&gt; ([`cb073f5`](https://github.com/Bluetooth-Devices/sensorpush-ble/commit/cb073f5c7f2c99bdaca46f9b7387c9c425845627))

* chore(pre-commit.ci): pre-commit autoupdate (#27)

Co-authored-by: pre-commit-ci[bot] &lt;66853113+pre-commit-ci[bot]@users.noreply.github.com&gt; ([`8e207f7`](https://github.com/Bluetooth-Devices/sensorpush-ble/commit/8e207f724026e471b597e41a747ece4d9f86a09e))

* chore(pre-commit.ci): pre-commit autoupdate (#26)

Co-authored-by: pre-commit-ci[bot] &lt;66853113+pre-commit-ci[bot]@users.noreply.github.com&gt; ([`4c035f5`](https://github.com/Bluetooth-Devices/sensorpush-ble/commit/4c035f5b61c7f7e9564ec72017397c0946a96c78))

* chore(pre-commit.ci): pre-commit autoupdate (#25)

Co-authored-by: pre-commit-ci[bot] &lt;66853113+pre-commit-ci[bot]@users.noreply.github.com&gt; ([`a307e01`](https://github.com/Bluetooth-Devices/sensorpush-ble/commit/a307e011684400dfbf07a082d35b3863b10edf07))

* chore(pre-commit.ci): pre-commit autoupdate (#24)

Co-authored-by: pre-commit-ci[bot] &lt;66853113+pre-commit-ci[bot]@users.noreply.github.com&gt; ([`b1d79b0`](https://github.com/Bluetooth-Devices/sensorpush-ble/commit/b1d79b0bec58d00ef839dbdd1d04978217516fa3))

### Feature

* feat: add support for TC.x (#33)

Co-authored-by: James Nick Sears &lt;nick@cousins-sears.com&gt;
Co-authored-by: pre-commit-ci[bot] &lt;66853113+pre-commit-ci[bot]@users.noreply.github.com&gt; ([`3279892`](https://github.com/Bluetooth-Devices/sensorpush-ble/commit/3279892b051558341776b4b11a535ad038b352c4))


## v1.6.2 (2024-01-06)

### Fix

* fix: missing name (#23) ([`c532926`](https://github.com/Bluetooth-Devices/sensorpush-ble/commit/c5329265e3d753efb27f92e65da6d94148b817d4))


## v1.6.1 (2023-12-29)

### Fix

* fix: release permissions (#22) ([`98b27d0`](https://github.com/Bluetooth-Devices/sensorpush-ble/commit/98b27d0c2b0104ed36d47d3ad59e81911429c5e6))


## v1.6.0 (2023-12-29)

### Chore

* chore: fix release process (#21) ([`d45532b`](https://github.com/Bluetooth-Devices/sensorpush-ble/commit/d45532bead20ce34e93c6a0ddc9586ff71594d48))

### Feature

* feat: add support for HT1 (#20)

Co-authored-by: J. Nick Koston &lt;nick@koston.org&gt; ([`7b76e6d`](https://github.com/Bluetooth-Devices/sensorpush-ble/commit/7b76e6dbe4287561afa8d9f152616af113a9fdce))


## v1.5.5 (2023-02-07)

### Fix

* fix: parsing with passive scans (#19) ([`adcafc8`](https://github.com/Bluetooth-Devices/sensorpush-ble/commit/adcafc8fb63ff6f7d04041f73aa9274d8bbc6a4c))


## v1.5.4 (2023-02-07)

### Fix

* fix: account for switching adapter when finding changed_manufacturer_data (#18) ([`dcccd49`](https://github.com/Bluetooth-Devices/sensorpush-ble/commit/dcccd497987e0dea164fc2fbd196cd77fa9fe62e))


## v1.5.3 (2023-02-07)

### Fix

* fix: update isort to fix CI (#17) ([`12bf0ac`](https://github.com/Bluetooth-Devices/sensorpush-ble/commit/12bf0acf35565c81d92852be512fde529ce99ce4))


## v1.5.2 (2022-08-14)

### Fix

* fix: use new changed_manufacturer_data helper from bluetooth-sensor-state-data (#16) ([`574210f`](https://github.com/Bluetooth-Devices/sensorpush-ble/commit/574210f800ca664121078cbf6f6dd63f3ee29747))


## v1.5.1 (2022-07-26)

### Fix

* fix: latest data was not always found if page0 was not last (#15) ([`a0e78c8`](https://github.com/Bluetooth-Devices/sensorpush-ble/commit/a0e78c814e877810e481fc4ff3fc850d10a0162b))


## v1.5.0 (2022-07-26)

### Feature

* feat: Add parser tests (#13) ([`90701be`](https://github.com/Bluetooth-Devices/sensorpush-ble/commit/90701be63e077ebc043868d35dfa596bef0a7042))

### Fix

* fix: ci fix (#14) ([`3bb525e`](https://github.com/Bluetooth-Devices/sensorpush-ble/commit/3bb525e2bd8420a6a30e8e0b0d18e43959f7a99d))


## v1.4.2 (2022-07-21)

### Fix

* fix: fix refactoring error in pressure (#12) ([`2db9381`](https://github.com/Bluetooth-Devices/sensorpush-ble/commit/2db93812d50b7af795dfb924a9d4d610f2488c2b))


## v1.4.1 (2022-07-21)

### Fix

* fix: bump sensor-state-data (#11) ([`af06b0b`](https://github.com/Bluetooth-Devices/sensorpush-ble/commit/af06b0b7679a090ec2648dae2ecfaed58e6c5c06))


## v1.4.0 (2022-07-21)

### Feature

* feat: refactor for sensor-state-data 2 (#10) ([`a723449`](https://github.com/Bluetooth-Devices/sensorpush-ble/commit/a723449519d3a18aa0ac859570683c573ba1b371))


## v1.3.0 (2022-07-20)

### Feature

* feat: export SensorDescription and SensorValue (#9) ([`ced7098`](https://github.com/Bluetooth-Devices/sensorpush-ble/commit/ced7098af4d6744c2edcc182bfe0f36fac250c5a))


## v1.2.2 (2022-07-20)

### Fix

* fix: bump deps (#8) ([`5b86419`](https://github.com/Bluetooth-Devices/sensorpush-ble/commit/5b86419ad62eb1d86c76cd0b4479adf866fa100d))


## v1.2.1 (2022-07-19)

### Fix

* fix: guard against invalid devices (#7)

fix: guard aginst invalid devices ([`4badaa0`](https://github.com/Bluetooth-Devices/sensorpush-ble/commit/4badaa0da1f782fc9ffd24eb608d085b0e6b9dd7))


## v1.2.0 (2022-07-19)

### Feature

* feat: set manufacturer (#6) ([`0b823c2`](https://github.com/Bluetooth-Devices/sensorpush-ble/commit/0b823c28e391f5e89fa86b20822a822f2a67c5f7))


## v1.1.2 (2022-07-19)

### Fix

* fix: add guard for missing manufacturer_data (#5) ([`a705260`](https://github.com/Bluetooth-Devices/sensorpush-ble/commit/a70526016a43a6347bb1ac40b8aeb3b77e981fe3))


## v1.1.1 (2022-07-19)

### Fix

* fix: bump libs (#4) ([`d1760e4`](https://github.com/Bluetooth-Devices/sensorpush-ble/commit/d1760e49ab671e50d8616576726abe7c82c8ba0c))


## v1.1.0 (2022-07-19)

### Feature

* feat: export all needed objects (#3) ([`f46bb89`](https://github.com/Bluetooth-Devices/sensorpush-ble/commit/f46bb8942b7578246348794af210d33b2f8981c4))


## v1.0.0 (2022-07-19)

### Chore

* chore: initial commit ([`fafd308`](https://github.com/Bluetooth-Devices/sensorpush-ble/commit/fafd308051d2cfa3d0a47ffc5e5c10e79c8873d8))

### Feature

* feat: init publish (#2) ([`e60b59f`](https://github.com/Bluetooth-Devices/sensorpush-ble/commit/e60b59fd209095b0e24c6874f3bf0811a510ce7c))

* feat: init repo (#1) ([`08f9867`](https://github.com/Bluetooth-Devices/sensorpush-ble/commit/08f9867e1ef5aa66bb6b0584754f0da34dca65ca))
