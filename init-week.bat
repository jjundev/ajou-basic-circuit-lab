@echo off
setlocal enabledelayedexpansion

if "%~1"=="" (
    set /p "input=주차 번호를 입력하세요 (예: 13 또는 13주차): "
) else (
    set "input=%~1"
)

if "%input%"=="" (
    echo 입력이 없어 종료합니다.
    pause
    exit /b 1
)

echo %input% | findstr /C:"주차" >nul
if errorlevel 1 (
    set "week=%input%주차"
) else (
    set "week=%input%"
)

set "weekPath=%~dp0%week%"
set /a created=0
set /a skipped=0

echo.
call :make "강의노트"
call :make "실험영상"
call :make "실험사진"
call :make "STT"
call :make "책"
call :make "연습문제"
call :make "output"
call :make "보드 구조도"
call :make "측정체크리스트"

echo.
echo %week% 초기화 완료 ^(생성 %created%개, 건너뜀 %skipped%개^)
echo.
pause
exit /b 0

:make
set "p=%weekPath%\%~1"
if exist "%p%\" (
    echo   - %~1
    set /a skipped+=1
) else (
    mkdir "%p%"
    echo   + %~1
    set /a created+=1
)
exit /b