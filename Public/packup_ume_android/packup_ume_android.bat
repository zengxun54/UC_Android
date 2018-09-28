@ echo off

rd /s /q log
mkdir log

echo 正在截图
set "ymd=%date:~,4%%date:~5,2%%date:~8,2%-%time:~0,2%-%time:~3,2%-%time:~6,2%"
set "ymd=%ymd: =%"
adb.exe shell screencap -p /sdcard/%ymd%.png
adb.exe pull /sdcard/%ymd%.png log/%ymd%.png
adb.exe shell rm /sdcard/%ymd%.png
echo.


echo 正在拉取日志

adb.exe logcat -d -v time > log/android.log
adb.exe shell tar -zcvf /sdcard/yealinkume.tar.gz /sdcard/yealinkume/
adb.exe pull /sdcard/yealinkume.tar.gz log/yealinkume.tar.gz
adb.exe pull /data/anr log/trace
adb.exe shell cat /data/anr/traces.txt > log/traces.txt
adb.exe pull /data/tombstones log/tombstones
adb.exe bugreport log/
echo.
set filename=%date:~0,4%-%date:~5,2%-%date:~8,2% %time:~0,2%-%time:~3,2%-%time:~6,2%
.\tool\7z.exe a "%filename%.zip" log
MOVE /Y "%filename%.zip" F:\script\UC_1.0_Android\UC_Android\Log
echo.

pause
exit

