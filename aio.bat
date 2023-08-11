@echo off
title %~n0
set back=popd
set go1=pushd program2
set go3=pushd program4
set go4=pushd program5
%go1% 
python -m main 
%back%  
%go3% 
python -m main 
%back% 
%go4% 
python -m main 
%back%
pause>nul
