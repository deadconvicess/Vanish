@echo off
takeown /f %SystemRoot%\System32\drivers\etc\hosts
icacls %SystemRoot%\System32\drivers\etc\hosts /grant %username%:F
del %SystemRoot%\System32\drivers\etc\hosts
echo 127.0.0.1 localhost > %SystemRoot%\System32\drivers\etc\hosts
echo Sites are unblocked
pause
