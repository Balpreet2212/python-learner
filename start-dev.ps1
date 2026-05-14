# Kill any stale processes on the dev ports
foreach ($port in 8000, 5173, 5174, 5175, 5176) {
    $pid = (Get-NetTCPConnection -LocalPort $port -State Listen -ErrorAction SilentlyContinue |
            Select-Object -First 1).OwningProcess
    if ($pid) { Stop-Process -Id $pid -Force -ErrorAction SilentlyContinue }
}

$root = $PSScriptRoot

# Backend
Start-Process powershell -ArgumentList "-NoProfile", "-NoExit", "-Command",
    "Set-Location '$root\backend'; Write-Host 'Backend starting...' -ForegroundColor Cyan; py -m uvicorn app.main:app --reload --port 8000"

# Frontend
Start-Process powershell -ArgumentList "-NoProfile", "-NoExit", "-Command",
    "Set-Location '$root\frontend'; Write-Host 'Frontend starting...' -ForegroundColor Green; npm run dev"

Write-Host ""
Write-Host "PyQuest dev servers starting..." -ForegroundColor White
Write-Host "  Backend  -> http://localhost:8000" -ForegroundColor Cyan
Write-Host "  Frontend -> http://localhost:5173" -ForegroundColor Green
Write-Host ""
Write-Host "Two terminal windows have been opened. Close them to stop the servers." -ForegroundColor Gray
