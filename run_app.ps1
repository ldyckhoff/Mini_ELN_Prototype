$ErrorActionPreference = "Stop"

$AppDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $AppDir

$VenvPython = Join-Path $AppDir ".venv\Scripts\python.exe"
$DepsDir = Join-Path $AppDir ".deps"

if (Test-Path $VenvPython) {
    & $VenvPython -m streamlit run app.py
    exit $LASTEXITCODE
}

if (Test-Path $DepsDir) {
    $env:PYTHONPATH = "$DepsDir;$AppDir;$env:PYTHONPATH"
    python -m streamlit run app.py
    exit $LASTEXITCODE
}

Write-Host ""
Write-Host "Missing local Python dependencies." -ForegroundColor Yellow
Write-Host "Install them once with:"
Write-Host ""
Write-Host "  python -m pip install -r requirements.txt"
Write-Host ""
Write-Host "Then run this script again:"
Write-Host ""
Write-Host "  .\run_app.ps1"
Write-Host ""
exit 1

