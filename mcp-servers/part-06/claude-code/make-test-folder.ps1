# Block 1. Run the first line, download a Microsoft sample .pbix (such as Store Sales) into model-test, then run the rest.
New-Item -ItemType Directory -Force "$HOME\model-test\.claude" | Out-Null
Set-Location "$HOME\model-test"
Copy-Item -Path "Store Sales.pbix" -Destination "Store Sales - copy.pbix"
