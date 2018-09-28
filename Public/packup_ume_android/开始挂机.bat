@ echo off

echo .
echo 正在删除旧日志\r\n
echo .
adb shell rm -r sdcard/hooklog

echo 创建日志目录\r\n
echo .
adb shell mkdir /sdcard/hookLog

echo 隐藏状态栏\r\n
echo .
adb.exe shell settings put global policy_control immersive.full=*

echo 开始mokey测试,等待2秒即可关闭窗口......\r\n
echo .
adb.exe shell "monkey  -p com.yealink.videophone --pct-syskeys 0 --ignore-crashes --ignore-timeouts --bugreport --monitor-native-crashes --throttle 1000 -v -v -v 1000000000"
