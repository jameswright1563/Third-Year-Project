@CD %~dp0
@MKDIR C:\texlive\texmf-local\tex\base\cmpreport > nul
@MOVE cmpreport.cls  C:\texlive\texmf-local\tex\base\cmpreport > nul
@MOVE *.tex C:\texlive\texmf-local\tex\base\cmpreport > nul
@MOVE *.png C:\texlive\texmf-local\tex\base\cmpreport > nul
@texhash > nul
@CD .. > nul
@(RMDIR InstallCMPreport /s/q
(echo.Installation completed)
pause
exit)