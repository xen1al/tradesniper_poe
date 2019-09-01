#SingleInstance force

if not A_IsAdmin
	Run *RunAs "%A_AhkPath%" "%A_ScriptFullPath%"

F2::
WinActivate, ahk_class POEWindowClass
WinWaitActive, ahk_class POEWindowClass
SendInput, {Enter}^v{Enter}
SoundBeep, 250, 200
return