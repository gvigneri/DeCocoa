param([int]$Port = 4173)
$ErrorActionPreference = 'Stop'
$bundledPython = Join-Path $env:USERPROFILE '.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
$pythonCommand = if (Test-Path -LiteralPath $bundledPython) { $bundledPython } else { 'python' }
& $pythonCommand (Join-Path $PSScriptRoot 'scripts\build_homepage.py')
if ($LASTEXITCODE -ne 0) { throw 'The local site build failed.' }
& $pythonCommand (Join-Path $PSScriptRoot 'scripts\preview_server.py') --port $Port
