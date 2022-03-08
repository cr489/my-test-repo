@ECHO OFF

pushd %~dp0

REM Command file for Sphinx documentation

if "%SPHINXBUILD%" == "" (
	set SPHINXBUILD=sphinx-build
)
<<<<<<< HEAD
<<<<<<< HEAD
set SOURCEDIR=.
set BUILDDIR=_build
=======
set SOURCEDIR=source
set BUILDDIR=build
>>>>>>> daa0d62985a9f82016bbffaa83ba490a9fe7ace1
=======
set SOURCEDIR=source
set BUILDDIR=build
<<<<<<< HEAD
=======

>>>>>>> master
>>>>>>> ca41bd288d29f90fb402282eecd70aec7fe862b7

if "%1" == "" goto help

%SPHINXBUILD% >NUL 2>NUL
if errorlevel 9009 (
	echo.
	echo.The 'sphinx-build' command was not found. Make sure you have Sphinx
	echo.installed, then set the SPHINXBUILD environment variable to point
	echo.to the full path of the 'sphinx-build' executable. Alternatively you
	echo.may add the Sphinx directory to PATH.
	echo.
	echo.If you don't have Sphinx installed, grab it from
	echo.https://www.sphinx-doc.org/
	exit /b 1
)

%SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
goto end

:help
%SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%

:end
popd
