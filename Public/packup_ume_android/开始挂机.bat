@ echo off

echo .
echo ����ɾ������־\r\n
echo .
adb shell rm -r sdcard/hooklog

echo ������־Ŀ¼\r\n
echo .
adb shell mkdir /sdcard/hookLog

echo ����״̬��\r\n
echo .
adb.exe shell settings put global policy_control immersive.full=*

echo ��ʼmokey����,�ȴ�2�뼴�ɹرմ���......\r\n
echo .
adb.exe shell "monkey  -p com.yealink.videophone --pct-syskeys 0 --ignore-crashes --ignore-timeouts --bugreport --monitor-native-crashes --throttle 1000 -v -v -v 1000000000"
